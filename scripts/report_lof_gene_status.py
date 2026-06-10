#!/usr/bin/env python3
"""Podsumowanie genów LoF/CNV bez calla SNP — wymagają sekwencjonowania strukturalnego."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSING = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
MD_MINI = ROOT / "md-mini"

LOF_GENES = [
    "ALMS1",
    "ARID1B",
    "BCL11B",
    "NKX2-2",
    "NKX2-4",
    "NSUN6",
    "PCDHG",
    "SOX7",
    "THSD7A",
    "ZSWIM6",
]


def has_star(gene: str) -> bool:
    md = MD_MINI / f"{gene}.md"
    if not md.exists():
        return False
    return any(
        "\u2605" in ln and ln.startswith("|") and "Genotyp" not in ln
        for ln in md.read_text(encoding="utf-8").splitlines()
    )


def main() -> int:
    csv_rows = {}
    if MISSING.exists():
        with MISSING.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                csv_rows[row["GENE"].upper()] = row

    print("Geny LoF/CNV bez tag-SNP (wymagają CNV caller + kohorta lub lab kliniczny):\n")
    for gene in LOF_GENES:
        row = csv_rows.get(gene, {})
        gt = row.get("GENOTYPE", "—")
        notes = row.get("NOTES", "")
        star = "★" if has_star(gene) else "—"
        print(f"  {gene:10}  WGS={gt:12}  minikarta={star}  {notes[:60]}")

    print("\nCNVkit: wymaga `-n` (próbki referencyjne). Depth-scan to heurystyka, nie call kliniczny.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
