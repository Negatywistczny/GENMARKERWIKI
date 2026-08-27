#!/usr/bin/env python3
"""Audyt personal-gene-profiles.js: doklejone zalecenia sekcji 6, LoF na SNP, itp."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "public" / "html" / "personal-gene-profiles.js"
MD = ROOT / "docs" / "genes"
MD_MINI = ROOT / "docs" / "genes-mini"

SECTION6_MARKERS = (
    "sport:",
    "suplementacja:",
    "diagnostyka:",
    "farmakologia:",
    "rehabilitacja:",
    "nutrigenom",
    "terapia psychodiet",
    "rygor zegara",
    "dziedziczenie allelu ryzyka",
    "ostrzeżenie kliniczne",
    "genetyka rodzinna",
)

SYNDROME_WORDS = (
    "cowden",
    "angelman",
    "dup15q",
    "heterozygota lof",
    "zespół łamliwego",
    "pełna mutacja",
)


def parse_profiles_js(text: str) -> list[dict]:
    genes: list[dict] = []
    # split na wpisy genów (płaskie parsowanie)
    for m in re.finditer(
        r"(\w[\w-]*): \{ headline: \"((?:\\.|[^\"])*)\""
        r", impact: \"((?:\\.|[^\"])*)\""
        r".*?byTopic: (\{.*?\})\s*\}\s*,?\s*\n",
        text,
        re.S,
    ):
        gene = m.group(1)
        headline = m.group(2).encode().decode("unicode_escape")
        impact = m.group(3).encode().decode("unicode_escape")
        by_topic_raw = m.group(4)
        topics: dict[str, list[dict]] = {}
        for tm in re.finditer(
            r"(\w[\w-]*): \{ variants: \[\{ headline: \"((?:\\.|[^\"])*)\""
            r", text: \"((?:\\.|[^\"])*)\"",
            by_topic_raw,
        ):
            tid = tm.group(1)
            th = tm.group(2).encode().decode("unicode_escape")
            tt = tm.group(3).encode().decode("unicode_escape")
            topics.setdefault(tid, []).append({"headline": th, "text": tt})
        genes.append(
            {"gene": gene, "headline": headline, "impact": impact, "byTopic": topics}
        )
    return genes


def audit_profile(g: dict) -> list[tuple[str, str, str]]:
    issues: list[tuple[str, str, str]] = []
    gene = g["gene"]
    for topic, variants in g.get("byTopic", {}).items():
        for v in variants:
            blob = f"{v['headline']} {v['text']}".lower()
            if any(m in blob for m in SECTION6_MARKERS):
                issues.append((gene, topic, f"section6_leak: {v['text'][:90]}"))
            if any(w in blob for w in SYNDROME_WORDS) and "nie oznacza" not in blob:
                issues.append((gene, topic, f"syndrome/advice: {v['headline'][:60]}"))
            if len(v["text"].strip()) < 12:
                issues.append((gene, topic, f"trivial_text: {v['text']!r}"))
            # headline vs impact mismatch: topic text != variant meaning
            if v["text"] != g["impact"][: len(v["text"])] and topic in {
                "sport",
                "nutrition",
                "mdd",
            }:
                if "rola biologiczna" in blob and "genu/białka" in blob:
                    issues.append((gene, topic, "mechanism_only_not_phenotype"))
    return issues


def audit_mini_stars() -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    for md in sorted(MD_MINI.glob("*.md")):
        body = md.read_text(encoding="utf-8")
        in_table = False
        for ln in body.splitlines():
            if "| Genotyp | Opis krótki |" in ln:
                in_table = True
                continue
            if not in_table or not ln.startswith("|") or ":---" in ln:
                continue
            parts = [p.strip() for p in ln.strip("|").split("|")]
            if len(parts) < 4:
                continue
            gt, short, _tone, long = parts
            if "\u2605" not in gt:
                continue
            blob = (short + " " + long).lower()
            gt_clean = re.sub(r"[*`\s\u2605]", "", gt)
            if gt_clean in ("-", "") and "ochron" not in blob and "referenc" not in blob:
                issues.append((md.stem, f"star_on_dash: {short[:50]}"))
            if "lof" in short.lower() and "nie oznacza" not in blob:
                issues.append((md.stem, f"lof_label: {gt_clean} {short[:40]}"))
    return issues


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    text = PROFILES.read_text(encoding="utf-8")
    genes = parse_profiles_js(text)
    profile_issues: list[tuple[str, str, str]] = []
    for g in genes:
        profile_issues.extend(audit_profile(g))

    mini_issues = audit_mini_stars()

    print(f"Geny w profiles.js: {len(genes)}")
    print(f"Problemy byTopic: {len(profile_issues)}")
    for gene, topic, msg in sorted(profile_issues):
        print(f"  {gene}/{topic}: {msg}")

    print(f"Problemy minikart (★): {len(mini_issues)}")
    for gene, msg in mini_issues:
        print(f"  {gene}: {msg}")

    return 1 if profile_issues or mini_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
