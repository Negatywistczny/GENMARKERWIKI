#!/usr/bin/env python3
"""Fazy A–D: genotypowanie brakujących minikart bezpośrednio z BAM."""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FASTQ = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER")
OUT_CSV = ROOT / "scripts" / "data" / "phased_bam_genotypes.csv"
OUT_JSON = ROOT / "scripts" / "data" / "phased_bam_results.json"

os.environ["PATH"] = (
    f"{FASTQ / 'tools' / 'bin'};C:\\msys64\\mingw64\\bin;" + os.environ.get("PATH", "")
)
sys.path.insert(0, str(FASTQ / "scripts"))
from bam_genotype_core import genotype_rsids, samtools_depth  # noqa: E402

SKIP = frozenset({"", "NOT_FOUND", "NO_CALL", "BRAK", "--", "NOT_IN_DBSNP"})

# Faza A: oryginalne + proxy MAPT + alternatywy dla usuniętych rsID
PHASE_A = {
    "NSUN6": ["rs2241604"],
    "MAPT": ["rs1800547", "rs9468", "rs8070723", "rs242557"],
    "AKT3": ["rs4599042", "rs17015062", "rs17036101", "rs3730356"],
    "C1R": ["rs1806698", "rs4925659", "rs6689930"],
    "SHISA9": ["rs7192086", "rs4553616", "rs10492782", "rs4548843"],
}

# Faza B: SLC6A3 DAT1 proxy + DRD4
PHASE_B = {
    "SLC6A3": ["rs27072", "rs40184", "rs6347"],
    "DRD4": ["rs1800955", "rs3758653"],
}

# Faza D: CNV proxy SNP (copy-number tag SNPs where known)
PHASE_D = {
    "C4A": ["rs1137101", "rs3129057"],
    "PTEN": ["rs701848", "rs2735340"],
    "UBE3A": ["rs1807588", "rs2367715"],
    "DYRK1A": ["rs28357468", "rs28357470"],
}


def ncbi_chrpos(rsid: str) -> str | None:
    num = rsid.lower().replace("rs", "")
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        f"?db=snp&id={num}&retmode=json"
    )
    try:
        time.sleep(0.4)
        data = json.loads(urllib.request.urlopen(url, timeout=25).read())
        return (data.get("result", {}).get(num, {}) or {}).get("chrpos") or None
    except Exception:
        return None


def query_rsids(rsids: list[str], *, label: str) -> list[dict]:
    unique = sorted(set(rsids), key=lambda x: int(x[2:]))
    print(f"[{label}] {len(unique)} rsID...", flush=True)
    rows = genotype_rsids(unique, min_mapq=0, min_baseq=0, prefer_dbsnp=True, threads=8)
    ok = [r for r in rows if r["RESULT"] not in SKIP]
    print(f"[{label}] OK: {len(ok)}/{len(rows)}", flush=True)
    for r in ok:
        print(f"  {r['RSID']:15} {r['RESULT']:6} {r['NOTES'][:65]}", flush=True)
    return rows


def pick_best(gene: str, rsids: list[str], rows: list[dict]) -> dict | None:
    by_rsid = {r["RSID"].lower(): r for r in rows}
    for rs in rsids:
        hit = by_rsid.get(rs.lower())
        if hit and hit["RESULT"] not in SKIP:
            return {
                "gene": gene,
                "rsid": hit["RSID"],
                "genotype": hit["RESULT"],
                "notes": hit.get("NOTES", ""),
                "confidence": hit.get("CONFIDENCE", ""),
            }
    return None


def check_depth(gene: str, rsid: str) -> str:
    cp = ncbi_chrpos(rsid)
    if not cp or ":" not in cp:
        return f"no_coords for {rsid}"
    chrom, pos_s = cp.split(":", 1)
    if not chrom.lower().startswith("chr"):
        chrom = f"chr{chrom}"
    d, avg = samtools_depth(chrom, int(pos_s))
    return f"{rsid} depth={d} avg={avg:.1f}"


def run_hla_phase() -> dict:
    """Faza C: sprawdź czy OptiType / arcasHLA dostępne."""
    result: dict = {"status": "skipped", "tools": {}}
    for tool, cmd in [
        ("optitype", ["optitype", "-h"]),
        ("arcasHLA", ["arcasHLA", "version"]),
        ("samtools", ["samtools", "--version"]),
    ]:
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            result["tools"][tool] = p.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            result["tools"][tool] = False
    if not any(result["tools"].get(t) for t in ("optitype", "arcasHLA")):
        result["status"] = "no_hla_tool"
        result["note"] = (
            "Zainstaluj OptiType (pip) lub arcasHLA; wymaga BAM + hg38 + ~8GB RAM"
        )
        return result
    result["status"] = "tool_available_not_run"
    return result


def run_expansion_hunter_phase() -> dict:
    """Faza B extended: ExpansionHunter dla DAT1 VNTR."""
    result: dict = {"status": "skipped"}
    for name in ("ExpansionHunter", "expansionhunter"):
        try:
            p = subprocess.run([name, "--version"], capture_output=True, timeout=10)
            if p.returncode == 0:
                result["status"] = "available_not_run"
                result["tool"] = name
                return result
        except FileNotFoundError:
            continue
    result["note"] = "ExpansionHunter niedostępny; użyto proxy SNP (Faza B)"
    return result


def main() -> int:
    all_rows: list[dict] = []
    gene_hits: dict[str, dict] = {}

    for phase_name, phase_map in [
        ("A", PHASE_A),
        ("B", PHASE_B),
        ("D", PHASE_D),
    ]:
        rsids = [rs for rslist in phase_map.values() for rs in rslist]
        rows = query_rsids(rsids, label=f"Faza {phase_name}")
        all_rows.extend(rows)
        for gene, gene_rsids in phase_map.items():
            best = pick_best(gene, gene_rsids, rows)
            if best:
                gene_hits[gene] = {**best, "phase": phase_name}

    # NSUN6 depth diagnostic
    if "NSUN6" not in gene_hits:
        print(f"[diag] NSUN6: {check_depth('NSUN6', 'rs2241604')}", flush=True)

    hla = run_hla_phase()
    eh = run_expansion_hunter_phase()

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["RSID", "RESULT", "SOURCE", "CONFIDENCE", "NOTES"])
        w.writeheader()
        seen: set[str] = set()
        for r in all_rows:
            key = r["RSID"].lower()
            if key not in seen:
                w.writerow(r)
                seen.add(key)

    payload = {
        "gene_hits": gene_hits,
        "hla": hla,
        "expansion_hunter": eh,
        "total_rsids_queried": len(seen),
        "genes_resolved": len(gene_hits),
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # Merge into missing_mini_wgs_from_bam.csv format for apply script
    missing_csv = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
    if missing_csv.exists():
        rows = list(csv.DictReader(missing_csv.open(encoding="utf-8")))
        for row in rows:
            gene = row["GENE"].upper()
            if gene in gene_hits:
                hit = gene_hits[gene]
                row["PRIMARY_RSID"] = hit["rsid"]
                row["GENOTYPE"] = hit["genotype"]
                row["SOURCE"] = f"bam+{hit.get('phase', 'phased')}"
                row["NOTES"] = hit.get("notes", "")
        with missing_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(
                f,
                fieldnames=["GENE", "PRIMARY_RSID", "ALL_RSIDS", "GENOTYPE", "SOURCE", "NOTES"],
            )
            w.writeheader()
            w.writerows(rows)

    print(f"\n[done] {len(gene_hits)} genow z genotypem -> {OUT_JSON}", flush=True)
    for gene, hit in sorted(gene_hits.items()):
        print(f"  {gene:14} {hit['rsid']:15} {hit['genotype']:6} (faza {hit['phase']})", flush=True)
    print(f"[hla] {hla['status']}: {hla.get('note', hla.get('tools', {}))}", flush=True)
    print(f"[vntr] {eh['status']}: {eh.get('note', '')}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
