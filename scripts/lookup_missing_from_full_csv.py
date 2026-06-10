#!/usr/bin/env python3
"""Dopasuj brakujące rsID do ULCEDCBF2693.full.csv (chr,pos,GT)."""

from __future__ import annotations

import csv
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSING = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
FULL_CSV = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\BAM\ULCEDCBF2693.full.csv")
OUT = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"


def fetch_site(rsid: str) -> tuple[str, tuple[str, int] | None]:
    url = f"https://rest.ensembl.org/variation/human/{rsid}?content-type=application/json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except Exception:
        return rsid, None
    mappings = [m for m in data.get("mappings", []) if m.get("assembly_name") == "GRCh38"]
    if not mappings:
        mappings = data.get("mappings", [])
    if not mappings:
        return rsid, None
    m = mappings[0]
    chrom = str(m["seq_region_name"])
    return rsid, (chrom, int(m["start"]))


def main() -> int:
    rows = list(csv.DictReader(MISSING.open(encoding="utf-8")))
    rsids: set[str] = set()
    rs_to_genes: dict[str, list[str]] = {}
    for row in rows:
        for rs in row["ALL_RSIDS"].split(";"):
            rs = rs.strip().lower()
            if rs.startswith("rs"):
                rsids.add(rs)
                rs_to_genes.setdefault(rs, []).append(row["GENE"])

    sites: dict[str, tuple[str, int]] = {}
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(fetch_site, rs): rs for rs in sorted(rsids)}
        for future in as_completed(futures):
            rsid, site = future.result()
            if site:
                sites[rsid] = site
    print(f"[info] Ensembl: {len(sites)}/{len(rsids)}", flush=True)

    wanted = {(chrom, pos): rs for rs, (chrom, pos) in sites.items()}
    found: dict[str, str] = {}
    print(f"[info] Skan {FULL_CSV.name}...", flush=True)
    with FULL_CSV.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            chrom, pos_s, gt = parts
            try:
                pos = int(pos_s)
            except ValueError:
                continue
            key = (chrom, pos)
            if key in wanted:
                found[wanted[key]] = gt.upper()
                if len(found) == len(wanted):
                    break

    print(f"[info] full.csv: {len(found)}/{len(wanted)}", flush=True)

    for row in rows:
        best_rs = row["PRIMARY_RSID"].strip().lower()
        best_gt = row["GENOTYPE"]
        best_src = row["SOURCE"]
        for rs in row["ALL_RSIDS"].split(";"):
            rs = rs.strip().lower()
            gt = found.get(rs, "")
            if gt and (not best_gt or best_gt in {"NO_CALL", "NOT_IN_DBSNP", ""}):
                best_rs, best_gt, best_src = rs, gt, "ULCEDCBF2693.full.csv"
        row["GENOTYPE"] = best_gt
        row["SOURCE"] = best_src
        if best_rs:
            row["PRIMARY_RSID"] = best_rs

    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["GENE", "PRIMARY_RSID", "ALL_RSIDS", "GENOTYPE", "SOURCE", "NOTES"],
        )
        w.writeheader()
        w.writerows(rows)

    hits = sum(1 for r in rows if r["GENOTYPE"] not in {"", "NO_CALL", "NOT_IN_DBSNP"})
    print(f"[done] {hits}/{len(rows)} genow z genotypem -> {OUT}", flush=True)
    for row in rows:
        if row["GENOTYPE"] not in {"", "NO_CALL", "NOT_IN_DBSNP"}:
            print(f"  {row['GENE']:12} {row['PRIMARY_RSID']:15} {row['GENOTYPE']:6} ({row['SOURCE']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
