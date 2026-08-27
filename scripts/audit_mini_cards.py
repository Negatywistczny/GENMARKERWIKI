#!/usr/bin/env python3
"""Sprawdź układ minikart: genotyp → opis krótki → szczegóły + opcjonalna ★."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_MINI = ROOT / "docs" / "genes-mini"

TABLE_HEADER = re.compile(r"^\| Genotyp \| Opis krótki \| Ton \| Wpływ fenotypowy \|")
ROW = re.compile(r"^\| (.+?) \| (.+?) \| (\w+) \| (.+?) \|$")

# Geny z wierszem patogennym „—” (CNV/LoF) — dozwolone ≠ 3 wiersze SNP
STRUCTURAL_EXCEPTIONS = frozenset(
    {
        "ALMS1",
        "ARID1B",
        "ASTN2",
        "AKT3",
        "BCL11B",
        "CHRNA7",
        "DYRK1A",
        "MACROD2",
        "NKX2-2",
        "NKX2-4",
        "PCDHG",
        "SOX7",
        "THSD7A",
        "TYW5",
        "ZSWIM6",
    }
)


def norm_genotype_cell(cell: str) -> str:
    g = re.sub(r"\s+", "", cell.upper().strip("`*★ "))
    if g in {"—", "-", ""}:
        return "—"
    return g


def parse_table_rows(body: str) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    in_table = False
    for ln in body.splitlines():
        if TABLE_HEADER.match(ln.strip()):
            in_table = True
            continue
        if in_table:
            if ln.startswith("| :"):
                continue
            m = ROW.match(ln.strip())
            if not m:
                if ln.strip() == "":
                    break
                continue
            rows.append(m.groups())
    return rows


def audit_file(path: Path) -> list[str]:
    issues: list[str] = []
    body = path.read_text(encoding="utf-8")
    gene = path.stem.upper()
    if "### 4. Tabela Wariantów" not in body:
        issues.append("brak sekcji tabeli wariantów")
        return issues

    rows = parse_table_rows(body)
    if not rows:
        issues.append("pusta tabela wariantów")
        return issues

    if len(rows) != 3 and gene not in STRUCTURAL_EXCEPTIONS:
        issues.append(f"oczekiwano 3 wiersze, jest {len(rows)}")

    seen_genotypes: dict[str, int] = {}
    for i, (genotype, short, tone, long) in enumerate(rows, start=1):
        if tone not in {"positive", "neutral", "negative"}:
            issues.append(f"wiersz {i}: nieznany ton '{tone}'")
        if not long.strip():
            issues.append(f"wiersz {i}: brak opisu szczegółowego")
        if not short.strip():
            issues.append(f"wiersz {i}: brak opisu krótkiego")
        if short.strip() and len(short) > len(long):
            issues.append(f"wiersz {i}: opis krótki dłuższy niż szczegóły")
        gkey = norm_genotype_cell(genotype)
        if gkey in seen_genotypes and gkey != "—":
            issues.append(
                f"wiersz {i}: zduplikowany genotyp '{gkey}' (wcześniej wiersz {seen_genotypes[gkey]})"
            )
        else:
            seen_genotypes[gkey] = i

    return issues


def main() -> int:
    bad: list[tuple[str, list[str]]] = []
    for md in sorted(MD_MINI.glob("*.md")):
        issues = audit_file(md)
        if issues:
            bad.append((md.stem, issues))
    print(f"Minikart: {len(list(MD_MINI.glob('*.md')))}")
    print(f"Problemy: {len(bad)}")
    for gene, issues in bad:
        for i in issues:
            print(f"  {gene}: {i}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
