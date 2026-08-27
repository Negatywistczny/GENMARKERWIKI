#!/usr/bin/env python3
"""Ręczny audyt rozszerzony: byTopic vs impact, ton GWAS, LoF bez disclaimeru."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_topic_profiles import parse_profiles_js, audit_mini_stars  # noqa: E402

PROFILES = ROOT / "public" / "html" / "personal-gene-profiles.js"
MD_MINI = ROOT / "docs" / "genes-mini"

GWAS_ALARM = (
    "schizofren",
    "autyzm",
    "patolog",
    "drastyczn",
    "heterozygota lof",
    "pełna mutacja",
    "zespół",
    "niepełnosprawno",
)

NO_STAR_EXPECTED = {
    "ALMS1", "ARID1B", "BCL11B", "NKX2-2", "NKX2-4",
    "NSUN6", "PCDHG", "SOX7", "THSD7A", "ZSWIM6",
}


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    text = PROFILES.read_text(encoding="utf-8")
    genes = parse_profiles_js(text)

    # 1. byTopic text != main impact (truncated compare)
    mismatch: list[tuple[str, str, str]] = []
    for g in genes:
        imp = g["impact"][:200]
        for topic, vars_ in g.get("byTopic", {}).items():
            for v in vars_:
                vt = v["text"][:200]
                if vt != imp[: len(vt)] and vt not in g["impact"]:
                    mismatch.append((g["gene"], topic, v["headline"][:50]))

    # 2. Negative tone + GWAS alarm without disclaimer
    gwas_issues: list[tuple[str, str]] = []
    for g in genes:
        blob = (g["headline"] + " " + g["impact"]).lower()
        if "gwas" in blob or "sygnał gwas" in blob:
            if any(w in blob for w in GWAS_ALARM) and "nie oznacza" not in blob:
                gwas_issues.append((g["gene"], g["headline"][:60]))

    # 3. Stars count per mini
    no_star: list[str] = []
    wrong_star: list[str] = []
    for md in sorted(MD_MINI.glob("*.md")):
        body = md.read_text(encoding="utf-8")
        has_star = "\u2605" in body or "★" in body
        gene = md.stem
        if gene in NO_STAR_EXPECTED:
            if has_star:
                wrong_star.append(f"{gene}: ma ★ (oczekiwano brak)")
        elif not has_star:
            no_star.append(gene)

    # 4. Mini negative + clinical without disclaimer
    mini_clinical: list[tuple[str, str]] = []
    for md in sorted(MD_MINI.glob("*.md")):
        body = md.read_text(encoding="utf-8")
        in_table = False
        for ln in body.splitlines():
            if "| Genotyp | Opis krótki |" in ln:
                in_table = True
                continue
            if not in_table or not ln.startswith("|"):
                continue
            if "\u2605" not in ln and "★" not in ln:
                continue
            parts = [p.strip() for p in ln.strip("|").split("|")]
            if len(parts) < 4:
                continue
            short, tone, long = parts[1], parts[2], parts[3]
            blob = (short + " " + long).lower()
            if tone == "negative" and any(w in blob for w in GWAS_ALARM):
                if "gwas" in blob and "nie oznacza" not in blob:
                    mini_clinical.append((md.stem, short[:50]))

    print("=== byTopic text != impact (podejrzane) ===")
    print(len(mismatch))
    for row in sorted(mismatch)[:30]:
        print(f"  {row[0]}/{row[1]}: {row[2]}")

    print("\n=== Profile GWAS + alarm bez disclaimer ===")
    print(len(gwas_issues))
    for gene, hl in sorted(gwas_issues):
        print(f"  {gene}: {hl}")

    print("\n=== Minikarty ★ + GWAS alarm bez disclaimer ===")
    print(len(mini_clinical))
    for gene, short in sorted(mini_clinical):
        print(f"  {gene}: {short}")

    print("\n=== Brak ★ (poza oczekiwanymi 10) ===")
    print(no_star or "(brak)")

    print("\n=== Nieoczekiwane ★ na LoF genach ===")
    print(wrong_star or "(brak)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
