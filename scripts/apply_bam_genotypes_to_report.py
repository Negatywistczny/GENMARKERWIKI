#!/usr/bin/env python3
"""Wstrzyknij genotypy z BAM do raportu markerów i przebuduj md-mini/."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from enrich_marker_report_genotypes import (  # noqa: E402
    REPORT,
    SKIP_GT,
    canonical_gene,
    dedupe_headers,
    enrich_section,
    load_gene_variants,
    parse_sections,
)

BAM_CSV = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
WSL_CSV = ROOT / "scripts" / "data" / "wsl_deep_genotypes.csv"
WORK_CSV = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\missing_mini_bam_genotypes.csv")
BUILD = ROOT / "scripts" / "build_mini_gene_cards.py"

STRUCTURAL_GT = frozenset({"diploid", "duplication", "deletion"})


def confidence(notes: str) -> str:
    m = re.search(r"depth=(\d+)", notes or "")
    depth = int(m.group(1)) if m else 0
    if depth >= 20:
        return "high"
    if depth >= 8:
        return "medium"
    return "low"


def load_bam_hits() -> dict[str, dict]:
    hits: dict[str, dict] = {}

    def ingest(path: Path) -> None:
        if not path.exists():
            return
        with path.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                gt = row["GENOTYPE"].strip().upper()
                if gt in SKIP_GT or gt.lower() in STRUCTURAL_GT:
                    continue
                hits[canonical_gene(row["GENE"])] = row

    ingest(BAM_CSV)
    # WSL: tylko allele HLA / VNTR (nie depth-scan CNV)
    if WSL_CSV.exists():
        with WSL_CSV.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                gt = row.get("GENOTYPE", "").strip()
                src = row.get("SOURCE", "")
                if gt.lower() in STRUCTURAL_GT or src == "wsl+depth":
                    continue
                gene = canonical_gene(row["GENE"])
                if gt and gt.upper() not in SKIP_GT:
                    hits[gene] = row
    return hits


def write_work_csv(hits: dict[str, dict]) -> None:
    WORK_CSV.parent.mkdir(parents=True, exist_ok=True)
    with WORK_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["RSID", "RESULT", "SOURCE", "CONFIDENCE", "NOTES"])
        for row in hits.values():
            rsid = row["PRIMARY_RSID"] or row["ALL_RSIDS"].split(";")[0]
            w.writerow(
                [
                    rsid,
                    row["GENOTYPE"],
                    "ensembl+bam",
                    confidence(row.get("NOTES", "")),
                    row.get("NOTES", ""),
                ]
            )


def build_rsid_gt(hits: dict[str, dict]) -> dict[str, dict]:
    rsid_gt: dict[str, dict] = {}
    for row in hits.values():
        rsid = (row["PRIMARY_RSID"] or row["ALL_RSIDS"].split(";")[0]).strip().lower()
        if not rsid.startswith("rs"):
            continue
        notes = row.get("NOTES", "")
        rsid_gt[rsid] = {
            "genotype": row["GENOTYPE"].strip().upper(),
            "source": "ensembl+bam",
            "confidence": confidence(notes),
            "notes": notes,
        }
        for alt in row["ALL_RSIDS"].split(";"):
            alt = alt.strip().lower()
            if alt.startswith("rs") and alt not in rsid_gt:
                rsid_gt[alt] = {
                    "genotype": "NOT_IN_DBSNP",
                    "source": "marker_report",
                    "confidence": "none",
                    "notes": "",
                }
    return rsid_gt


def main() -> int:
    hits = load_bam_hits()
    if not hits:
        print("[warn] Brak genotypow do dodania.", file=sys.stderr)
        return 1

    write_work_csv(hits)
    rsid_gt = build_rsid_gt(hits)
    gene_vars = load_gene_variants()
    text = REPORT.read_text(encoding="utf-8")
    sections = parse_sections(text)
    hit_genes = set(hits.keys())
    updated = 0
    parts: list[str] = []
    cursor = 0

    for gene_raw, body, start, end in sections:
        parts.append(text[cursor:start])
        gene = canonical_gene(gene_raw.split()[0])
        if gene in hit_genes:
            new_body = enrich_section(
                gene, body, rsid_gt, gene_vars, force=True, bam_hit=hits.get(gene)
            )
            if new_body != body:
                updated += 1
            parts.append(new_body)
        else:
            parts.append(body)
        cursor = end

    parts.append(text[cursor:])
    REPORT.write_text(dedupe_headers("".join(parts)), encoding="utf-8")
    print(f"[done] Zaktualizowano WGS dla {updated} sekcji ({len(hits)} genow).")

    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT)
    if proc.returncode != 0:
        return proc.returncode

    print("[done] Przebudowano md-mini/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
