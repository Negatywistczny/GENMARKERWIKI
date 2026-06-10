#!/usr/bin/env python3
"""Scal wyniki wsl_deep_genotypes.csv do missing_mini_wgs_from_bam.csv."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSING = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
SKIP = frozenset({"", "NOT_FOUND", "NO_CALL", "BRAK", "--", "NOT_IN_DBSNP"})


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "scripts" / "data" / "wsl_deep_genotypes.csv"
    if not src.exists():
        print(f"[skip] Brak {src}")
        return 0

    hits: dict[str, dict] = {}
    with src.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            gt = row.get("GENOTYPE", "").strip()
            if gt in SKIP or gt.lower() in {"diploid", "duplication", "deletion"}:
                continue
            hits[row["GENE"].upper()] = row

    if not hits:
        return 0

    rows = list(csv.DictReader(MISSING.open(encoding="utf-8")))
    for row in rows:
        gene = row["GENE"].upper()
        if gene not in hits:
            continue
        cur = row.get("GENOTYPE", "").strip().upper()
        if len(cur) == 2 and cur.isalpha():
            continue
        hit = hits[gene]
        row["PRIMARY_RSID"] = hit.get("PRIMARY_RSID", "")
        row["GENOTYPE"] = hit["GENOTYPE"]
        row["SOURCE"] = hit.get("SOURCE", "wsl")
        row["NOTES"] = hit.get("NOTES", "")

    with MISSING.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["GENE", "PRIMARY_RSID", "ALL_RSIDS", "GENOTYPE", "SOURCE", "NOTES"],
        )
        w.writeheader()
        w.writerows(rows)

    print(f"[done] Scalono {len(hits)} genow z {src.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
