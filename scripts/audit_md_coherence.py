#!/usr/bin/env python3
"""Spójność md/, md-mini/, raportu źródłowego i plików JS."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "md"
MD_MINI = ROOT / "md-mini"
REPORT = ROOT / "raporty" / "markery" / "Zbiorowe badanie markerów.md"
GENES_WITH_MD = ROOT / "html" / "genes-with-md.js"
GENES_WITH_MINI = ROOT / "html" / "genes-with-mini.js"
SKIP_MD = frozenset({"UNIWERSALNY_SZABLON_MARKERA.md", "index.md"})

MINI_TABLE_HEADER = re.compile(r"^\| Genotyp \| Opis krótki \| Ton \| Wpływ fenotypowy \|")
MINI_ROW = re.compile(r"^\| (.+?) \| (.+?) \| (\w+) \| (.+?) \|$")


def genes_from_js(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r'"([A-Z0-9-]+)"', text))


def parse_report_genes(text: str) -> set[str]:
    return {
        m.group(1).upper()
        for m in re.finditer(r"^### ([A-Z0-9-]+)\s*$", text, re.M)
    }


def extract_primary_rsid(text: str) -> str | None:
    m = re.search(r"\*\*Główny rsID[^:]*:\*\*\s*(.+)", text, re.I)
    if not m:
        m = re.search(r"\*\*Główny wariant:\*\*\s*(.+)", text, re.I)
    if not m:
        return None
    hits = re.findall(r"rs\d+", m.group(1), re.I)
    return hits[0].lower() if hits else None


def md_spacing_issues() -> list[str]:
    issues: list[str] = []
    for path in sorted(MD.glob("*.md")):
        if path.name in SKIP_MD:
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"\|[^\n]*\n### 5\.", text):
            issues.append(f"{path.stem}: brak pustej linii przed §5")
    return issues


def mini_content_issues() -> list[str]:
    issues: list[str] = []
    for path in sorted(MD_MINI.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        in_table = False
        rows = 0
        seen: set[str] = set()
        for ln in body.splitlines():
            if MINI_TABLE_HEADER.match(ln.strip()):
                in_table = True
                continue
            if not in_table:
                continue
            if ln.startswith("| :"):
                continue
            m = MINI_ROW.match(ln.strip())
            if not m:
                if ln.strip() == "":
                    break
                continue
            rows += 1
            genotype, short, _tone, long = m.groups()
            if not short.strip():
                issues.append(f"{path.stem}: wiersz {rows} — pusty opis krótki")
            g = re.sub(r"\s+", "", genotype.upper().strip("`*★ "))
            if g and g not in {"—", "-"} and g in seen:
                issues.append(f"{path.stem}: zduplikowany genotyp {g}")
            if g:
                seen.add(g)
    return issues


def rsid_report_vs_mini(report: str, report_genes: set[str]) -> list[str]:
    issues: list[str] = []
    md_genes = {p.stem.upper() for p in MD.glob("*.md") if p.name not in SKIP_MD}
    parts = re.split(r"^### ", report, flags=re.M)[1:]
    report_bodies: dict[str, str] = {}
    for part in parts:
        gene = part.split("\n", 1)[0].strip().upper()
        body = part.split("\n", 1)[1] if "\n" in part else ""
        report_bodies[gene] = body

    for gene in sorted(report_genes - md_genes):
        mini_path = MD_MINI / f"{gene}.md"
        if not mini_path.exists():
            issues.append(f"{gene}: brak minikarty dla genu z raportu")
            continue
        body = report_bodies.get(gene, "")
        mini_text = mini_path.read_text(encoding="utf-8")
        c_rs = extract_primary_rsid(mini_text)
        if not c_rs:
            continue
        if c_rs.lower() in body.lower():
            continue
        r_rs = extract_primary_rsid(body)
        if r_rs and r_rs != c_rs.split("/")[0].strip().lower():
            if r_rs not in (c_rs or "") and (c_rs or "") not in (r_rs or ""):
                issues.append(f"{gene}: rsID raport={r_rs} mini={c_rs}")
    return issues


def main() -> int:
    issues: list[str] = []

    md_genes = {p.stem.upper() for p in MD.glob("*.md") if p.name not in SKIP_MD}
    mini_genes = {p.stem.upper() for p in MD_MINI.glob("*.md")}
    overlap = md_genes & mini_genes
    if overlap:
        issues.append(f"overlap md/md-mini: {sorted(overlap)}")

    js_md = genes_from_js(GENES_WITH_MD)
    js_mini = genes_from_js(GENES_WITH_MINI)
    if js_md != md_genes:
        issues.append(f"genes-with-md.js ≠ md/: +{sorted(js_md - md_genes)} -{sorted(md_genes - js_md)}")
    if js_mini != mini_genes:
        issues.append(
            f"genes-with-mini.js ≠ md-mini/: +{sorted(js_mini - mini_genes)} -{sorted(mini_genes - js_mini)}"
        )

    report_text = REPORT.read_text(encoding="utf-8")
    report_genes = parse_report_genes(report_text)
    expected_mini = report_genes - md_genes
    if expected_mini != mini_genes:
        issues.append(
            f"raport−md ({len(expected_mini)}) ≠ md-mini ({len(mini_genes)}): "
            f"brak={sorted(expected_mini - mini_genes)[:5]} "
            f"extra={sorted(mini_genes - expected_mini)[:5]}"
        )

    issues.extend(md_spacing_issues())
    issues.extend(mini_content_issues())
    issues.extend(rsid_report_vs_mini(report_text, report_genes))

    print(f"md/: {len(md_genes)}, md-mini/: {len(mini_genes)}, raport: {len(report_genes)}")
    print(f"Problemy spójności: {len(issues)}")
    for item in issues:
        print(f"  {item}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
