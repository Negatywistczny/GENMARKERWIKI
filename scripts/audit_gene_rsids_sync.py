#!/usr/bin/env python3
"""Audyt synchronizacji gene-rsids.js z rsID w md/ (sekcje 2 i 4)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "docs" / "genes"
GENE_RSIDS = ROOT / "public" / "html" / "gene-rsids.js"

GENE_RE = re.compile(r"^\s+([A-Z0-9]+):\s*\[", re.M)
RS_RE = re.compile(r"rs\d+", re.I)
SKIP = {"UNIWERSALNY_SZABLON_MARKERA", "index"}


def parse_gene_rsids() -> dict[str, list[str]]:
    text = GENE_RSIDS.read_text(encoding="utf-8")
    out: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        gm = GENE_RE.match(line)
        if gm:
            current = gm.group(1)
            out[current] = []
        if current:
            for rs in re.findall(r'"(rs\d+)"', line, re.I):
                if rs.lower() not in out[current]:
                    out[current].append(rs.lower())
    return out


def parse_sections(text: str) -> dict[int, str]:
    parts: dict[int, list[str]] = {0: []}
    current = 0
    for line in text.splitlines():
        m = re.match(r"^###\s+(\d+)\.\s+", line)
        if m:
            current = int(m.group(1))
            parts.setdefault(current, [])
        parts.setdefault(current, []).append(line)
    return {n: "\n".join(lines).strip() for n, lines in parts.items()}


def rsids_from_md(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    sections = parse_sections(text)
    rsids: set[str] = set()
    sec2 = sections.get(2, "")
    for line in sec2.splitlines():
        if re.search(r"główny rsid", line, re.I):
            for rs in re.findall(r"rs\d+", line):
                rsids.add(rs.lower())
            continue
        if re.search(r"powiązane", line, re.I):
            if re.search(r"opcjonalnie", line, re.I):
                continue
            for rs in re.findall(r"rs\d+", line):
                rsids.add(rs.lower())
    sec4 = sections.get(4, "")
    for m in re.finditer(r"^\*\*(.+?)\*\*", sec4, re.M):
        for rs in re.findall(r"rs\d+", m.group(1)):
            rsids.add(rs.lower())
    return rsids


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    js_map = parse_gene_rsids()
    md_genes: dict[str, set[str]] = {}
    for md in sorted(MD_DIR.glob("*.md")):
        if md.stem in SKIP:
            continue
        md_genes[md.stem.upper()] = rsids_from_md(md)

    js_only_genes = sorted(set(js_map) - set(md_genes))
    md_only_genes = sorted(set(md_genes) - set(js_map))
    in_js_not_md: list[tuple[str, str]] = []
    in_md_not_js: list[tuple[str, str]] = []

    for gene in sorted(set(js_map) & set(md_genes)):
        js_set = set(js_map[gene])
        md_set = md_genes[gene]
        for rs in sorted(js_set - md_set):
            in_js_not_md.append((gene, rs))
        for rs in sorted(md_set - js_set):
            in_md_not_js.append((gene, rs))

    print(f"Geny w gene-rsids.js: {len(js_map)}")
    print(f"Geny w md/ (bez szablonu): {len(md_genes)}")
    print(f"W JS bez pliku md/: {len(js_only_genes)}")
    print(f"W md/ bez wpisu w JS: {len(md_only_genes)}")
    print(f"rsID w JS brak w md: {len(in_js_not_md)}")
    print(f"rsID w md brak w JS: {len(in_md_not_js)}\n")

    if js_only_genes:
        print("=== GEN W JS BEZ PLIKU MD ===")
        for g in js_only_genes:
            print(f"  {g}")
        print()

    if md_only_genes:
        print("=== GEN W MD BEZ WPISU W GENE-RSIDS.JS ===")
        for g in md_only_genes:
            print(f"  {g}")
        print()

    if in_js_not_md:
        print("=== RSID W JS, BRAK W MD (§2/§4) ===")
        for gene, rs in in_js_not_md:
            print(f"  {gene:10} {rs}")
        print()

    if in_md_not_js:
        print("=== RSID W MD (§2/§4), BRAK W JS ===")
        for gene, rs in in_md_not_js:
            print(f"  {gene:10} {rs}")
        print()

    issues = (
        len(js_only_genes)
        + len(in_js_not_md)
        + len(in_md_not_js)
    )
    if issues:
        print(f"[FAIL] {issues} nieścisłości synchronizacji")
        return 1
    print("[OK] gene-rsids.js zsynchronizowany z md/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
