#!/usr/bin/env python3
"""Genotypuj brakujące minikarty bezpośrednio z pliku BAM (bcftools + samtools)."""

from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FASTQ = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER")
MISSING_GENES_CSV = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
OUT = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"

# bcftools/samtools wymagają DLL z MSYS2 (jak w run_bam_to_genotype_csv.ps1)
msys_bin = Path(r"C:\msys64\mingw64\bin")
tools_bin = FASTQ / "tools" / "bin"
os.environ["PATH"] = f"{tools_bin};{msys_bin};" + os.environ.get("PATH", "")

sys.path.insert(0, str(FASTQ / "scripts"))
from bam_genotype_core import genotype_rsids  # noqa: E402

SKIP = frozenset({"", "NOT_FOUND", "NO_CALL", "BRAK", "--", "NOT_IN_DBSNP"})


def load_genes() -> list[dict]:
    return list(csv.DictReader(MISSING_GENES_CSV.open(encoding="utf-8")))


def main() -> int:
    rows = load_genes()
    rsids: list[str] = []
    for row in rows:
        for rs in row["ALL_RSIDS"].split(";"):
            rs = rs.strip()
            if rs.lower().startswith("rs"):
                rsids.append(rs)
    rsids = sorted(set(rsids), key=lambda x: int(x[2:]))

    print(f"[info] BAM: {FASTQ / 'BAM' / 'F25A910000190-04_HOMnzpvR_ULCEDCBF2693_ULCEDCBF2693.bam'}")
    print(f"[info] Genotypowanie {len(rsids)} rsID...", flush=True)

    gt_rows = genotype_rsids(rsids, threads=8)
    retry = [r["RSID"] for r in gt_rows if r["RESULT"] in SKIP]
    if retry:
        print(f"[info] Retry q0/Q0 dla {len(retry)} rsID...", flush=True)
        retry_rows = genotype_rsids(retry, min_mapq=0, min_baseq=0, prefer_dbsnp=True, threads=8)
        by_rsid = {r["RSID"]: r for r in gt_rows}
        for r in retry_rows:
            if r["RESULT"] not in SKIP:
                by_rsid[r["RSID"]] = r
            elif r["RSID"] not in by_rsid:
                by_rsid[r["RSID"]] = r
        gt_rows = list(by_rsid.values())

    by_rsid = {r["RSID"].lower(): r for r in gt_rows}

    for row in rows:
        best_rs = ""
        best_gt = ""
        best_src = ""
        best_notes = ""
        candidates = [row["PRIMARY_RSID"].strip().lower()] if row["PRIMARY_RSID"].strip() else []
        candidates += [rs.strip().lower() for rs in row["ALL_RSIDS"].split(";") if rs.strip()]
        seen: set[str] = set()
        for rs in candidates:
            if not rs or rs in seen:
                continue
            seen.add(rs)
            hit = by_rsid.get(rs)
            if not hit or hit["RESULT"] in SKIP:
                continue
            best_rs, best_gt = rs, hit["RESULT"]
            best_src = f"bam+{hit.get('SOURCE', 'bcftools')}"
            best_notes = hit.get("NOTES", "")
            break
        if best_gt:
            row["PRIMARY_RSID"] = best_rs
            row["GENOTYPE"] = best_gt
            row["SOURCE"] = best_src
            row["NOTES"] = best_notes
        else:
            row["GENOTYPE"] = row.get("GENOTYPE") or "NO_CALL"
            row["SOURCE"] = row.get("SOURCE") or "bam_no_call"

    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["GENE", "PRIMARY_RSID", "ALL_RSIDS", "GENOTYPE", "SOURCE", "NOTES"],
        )
        w.writeheader()
        w.writerows(rows)

    hits = sum(1 for r in rows if r["GENOTYPE"] not in SKIP)
    print(f"[done] {hits}/{len(rows)} genow z genotypem z BAM -> {OUT}", flush=True)
    for row in rows:
        if row["GENOTYPE"] not in SKIP:
            print(f"  {row['GENE']:14} {row['PRIMARY_RSID']:15} {row['GENOTYPE']:6}  {row['NOTES'][:70]}")
    no_call = [r["GENE"] for r in rows if r["GENOTYPE"] in SKIP]
    if no_call:
        print(f"[warn] Bez calla ({len(no_call)}): {', '.join(no_call)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
