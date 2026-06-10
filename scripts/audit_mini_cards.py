#!/usr/bin/env python3
"""Sprawdź układ minikart: genotyp → opis krótki → szczegóły + opcjonalna ★."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_MINI = ROOT / "md-mini"

TABLE_HEADER = re.compile(r"^\| Genotyp \| Opis krótki \| Ton \| Wpływ fenotypowy \|")
ROW = re.compile(r"^\| (.+?) \| (.+?) \| (\w+) \| (.+?) \|$")


def audit_file(path: Path) -> list[str]:
    issues: list[str] = []
    body = path.read_text(encoding="utf-8")
    if "### 4. Tabela Wariantów" not in body:
        issues.append("brak sekcji tabeli wariantów")
        return issues
    in_table = False
    rows = 0
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
            rows += 1
            genotype, short, tone, long = m.groups()
            if tone not in {"positive", "neutral", "negative"}:
                issues.append(f"wiersz {rows}: nieznany ton '{tone}'")
            if not long.strip():
                issues.append(f"wiersz {rows}: brak opisu szczegółowego")
            if short.strip() and len(short) > len(long):
                issues.append(f"wiersz {rows}: opis krótki dłuższy niż szczegóły")
    if rows == 0:
        issues.append("pusta tabela wariantów")
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
