#!/usr/bin/env python3
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts/data/missing_mini_wgs_from_bam.csv"
rows = list(csv.DictReader(path.open(encoding="utf-8")))
no_rs = [r["GENE"] for r in rows if not r["ALL_RSIDS"].strip()]
found = [r for r in rows if r["GENOTYPE"] not in {"", "NO_CALL", "NOT_IN_DBSNP"}]
missing_rs = [r for r in rows if r["ALL_RSIDS"].strip() and r["GENOTYPE"] in {"", "NO_CALL", "NOT_IN_DBSNP"}]

print(f"Razem bez calla WGS w minikarcie: {len(rows)}")
print(f"  bez tag-SNP w raporcie: {len(no_rs)}")
print(f"  z tag-SNP, znalezione w BAM: {len(found)}")
print(f"  z tag-SNP, brak w eksporcie BAM: {len(missing_rs)}")
print()
print("BEZ tag-SNP (CNV / LoF / HLA):")
for g in no_rs:
    print(f"  {g}")
print()
print("ZNALEZIONE w ULCEDCBF2693:")
for r in found:
    print(f"  {r['GENE']:12} {r['PRIMARY_RSID']:15} {r['GENOTYPE']:6} ({r['SOURCE']})")
print()
print("TAG-SNP bez calla w eksporcie:")
for r in missing_rs:
    print(f"  {r['GENE']:12} {r['ALL_RSIDS']}")
