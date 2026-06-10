#!/usr/bin/env python3
"""Fazy C->D+: HLA proxy, DAT1 VNTR, CNV depth, NSUN6 fix — bez Dockera/WSL."""

from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FASTQ = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER")
MISSING_CSV = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
OUT_JSON = ROOT / "scripts" / "data" / "advanced_mini_results.json"

os.environ["PATH"] = (
    f"{FASTQ / 'tools' / 'bin'};C:\\msys64\\mingw64\\bin;" + os.environ.get("PATH", "")
)
sys.path.insert(0, str(FASTQ / "scripts"))
from bam_genotype_core import genotype_rsids, samtools_depth  # noqa: E402
from vntr_read_utils import fetch_ref, max_tandem_repeat, merge_vntr_marker, region_depth, read_sequences  # noqa: E402

SKIP = frozenset({"", "NOT_FOUND", "NO_CALL", "BRAK", "--", "NOT_IN_DBSNP"})

# Faza C: proxy tag-SNP MHC (bez OptiType)
HLA_PROXY = {
    "HLA-B": ["rs1050502", "rs3135388", "rs2844633"],
    "HLA-DQB1": ["rs2187668", "rs7775228", "rs7454108"],
    "HLA-DRB1": ["rs660895", "rs9268839", "rs2395182"],
}

# Faza D+: tag-SNP w genach LoF/CNV (literatura + GWAS)
GENE_PROXY = {
    "DYRK1A": ["rs8025580", "rs11701976", "rs11733587"],
    "CHD8": ["rs60333600", "rs10122956"],
    "PTEN": ["rs701848", "rs2735340"],
    "KMT2D": ["rs772057441", "rs189469207"],
    "KCNN2": ["rs6480535", "rs6480536"],
    "GRIA2": ["rs13182811", "rs13182812"],
    "GRIN2B": ["rs7301328", "rs1806201"],
    "HCN1": ["rs789088", "rs789089"],
    "SLC12A5": ["rs2885267", "rs2885268"],
    "UBE3A": ["rs1807588", "rs2367715"],
    "MICA": ["rs2596542", "rs2596541"],
    "DHFR": ["rs1650699", "rs1650722"],
    "ANK2": ["rs1939197", "rs10948382"],
    "AKAP11": ["rs10936545", "rs10936546"],
}

DAT1_REGION = ("chr5", 1393390, 1393600)


def ensembl_gene_region(gene: str) -> tuple[str, int, int] | None:
    url = (
        f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene}"
        f"?content-type=application/json"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "genmarker"})
        data = json.loads(urllib.request.urlopen(req, timeout=30).read())
        return f"chr{data['seq_region_name']}", int(data["start"]), int(data["end"])
    except Exception:
        return None


def ensembl_common_snps(chrom: str, start: int, end: int, limit: int = 5) -> list[str]:
    c = chrom.replace("chr", "")
    url = (
        f"https://rest.ensembl.org/overlap/region/human/{c}:{start}-{end}"
        f"?feature=variation;content-type=application/json"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "genmarker"})
        data = json.loads(urllib.request.urlopen(req, timeout=60).read())
        hits: list[tuple[float, str]] = []
        for v in data:
            if v.get("var_class") != "SNV":
                continue
            rsid = v.get("id", "")
            if not rsid.startswith("rs"):
                continue
            maf = v.get("minor_allele_freq") or 0
            if maf >= 0.05:
                hits.append((maf, rsid))
        hits.sort(reverse=True)
        return [rs for _, rs in hits[:limit]]
    except Exception:
        return []


def pick_best(gene: str, rsids: list[str], rows: list[dict]) -> dict | None:
    by = {r["RSID"].lower(): r for r in rows}
    for rs in rsids:
        hit = by.get(rs.lower())
        if hit and hit["RESULT"] not in SKIP:
            return {
                "gene": gene,
                "rsid": hit["RSID"],
                "genotype": hit["RESULT"],
                "notes": hit.get("NOTES", ""),
                "confidence": hit.get("CONFIDENCE", ""),
            }
    return None


def infer_dat1_vntr() -> dict:
    chrom, start, end = DAT1_REGION
    cov = region_depth(chrom, start, end)
    ref = fetch_ref(chrom, start, end)
    unit = "TTCAT"  # 40bp VNTR ~ 8x 5mer (uproszczenie)
    seqs = read_sequences(chrom, start, end)
    counts = [max_tandem_repeat(s, unit) for s in seqs if len(s) > 20]
    median_rep = sorted(counts)[len(counts) // 2] if counts else 0

    tags = genotype_rsids(["rs27072", "rs40184"], min_mapq=0, min_baseq=0, prefer_dbsnp=True)
    by = {r["RSID"].lower(): r["RESULT"] for r in tags}
    r72, r184 = by.get("rs27072", ""), by.get("rs40184", "")

    # CC/CC tag-SNP -> 9R/9R (literatura DAT1)
    if r72 == "CC" and r184 == "CC":
        genotype = "9R/9R"
        conf = "medium"
        method = "proxy tag-SNP (rs27072=CC, rs40184=CC)"
    elif "NO_CALL" in (r72, r184):
        genotype = "NO_CALL"
        conf = "low"
        method = "brak tag-SNP"
    else:
        genotype = f"9R/10R (proxy rs27072={r72}, rs40184={r184})"
        conf = "medium-low"
        method = "proxy tag-SNP"

    notes = (
        f"region {chrom}:{start}-{end}; reads={len(seqs)}; "
        f"median_repeat~{median_rep}; {method}; cov={cov.get('mean_depth')}x"
    )
    merge_vntr_marker("DAT1-9R10R", "SLC6A3", genotype, conf, method, notes, coverage=cov)
    return {"gene": "SLC6A3", "genotype": genotype, "confidence": conf, "method": method, "notes": notes}


def cnv_depth_scan(gene: str) -> dict | None:
    region = ensembl_gene_region(gene)
    if not region:
        return None
    chrom, start, end = region
    mid = (start + end) // 2
    d, avg = samtools_depth(chrom, mid)
    status = "diploid_ok" if avg >= 8 else "low_coverage"
    if avg < 4:
        status = "possible_deletion"
    elif avg > 45:
        status = "possible_duplication"
    return {
        "gene": gene,
        "region": f"{chrom}:{start}-{end}",
        "depth": d,
        "avg_depth": round(avg, 1),
        "cnv_hint": status,
    }


def nsun6_fix() -> dict | None:
    """rs2241604 mapuje na chr5 (bledny); szukaj SNP w prawdziwym locus chr10."""
    region = ensembl_gene_region("NSUN6")
    if not region:
        return None
    chrom, start, end = region
    rsids = ensembl_common_snps(chrom, start, end, limit=8)
    if not rsids:
        return None
    rows = genotype_rsids(rsids, min_mapq=0, min_baseq=0, prefer_dbsnp=True, threads=4)
    hit = pick_best("NSUN6", rsids, rows)
    if hit:
        hit["notes"] = (
            f"rs2241604=chr5:1056998 bledny locus; proxy {hit['rsid']} w NSUN6 chr10; "
            + hit.get("notes", "")
        )
    return hit


def update_missing_csv(hits: dict[str, dict]) -> None:
    if not MISSING_CSV.exists():
        return
    rows = list(csv.DictReader(MISSING_CSV.open(encoding="utf-8")))
    for row in rows:
        gene = row["GENE"].upper()
        if gene not in hits:
            continue
        hit = hits[gene]
        gt = hit.get("genotype", "")
        if gt in SKIP:
            continue
        row["PRIMARY_RSID"] = hit.get("rsid", row.get("PRIMARY_RSID", ""))
        row["GENOTYPE"] = gt
        row["SOURCE"] = hit.get("source", "bam+advanced")
        row["NOTES"] = hit.get("notes", "")
    with MISSING_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["GENE", "PRIMARY_RSID", "ALL_RSIDS", "GENOTYPE", "SOURCE", "NOTES"],
        )
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    hits: dict[str, dict] = {}
    payload: dict = {"hla": {}, "vntr": {}, "cnv": {}, "proxy": {}, "nsun6": None}

    # --- Faza C: HLA proxy ---
    hla_rsids = [rs for rslist in HLA_PROXY.values() for rs in rslist]
    hla_rows = genotype_rsids(sorted(set(hla_rsids), key=lambda x: int(x[2:])), min_mapq=0, min_baseq=0, prefer_dbsnp=True)
    print(f"[C] HLA proxy: {len(hla_rows)} rsID", flush=True)
    for gene, rsids in HLA_PROXY.items():
        best = pick_best(gene, rsids, hla_rows)
        if best:
            best["source"] = "bam+hla_proxy"
            best["notes"] = f"proxy (OptiType niedostepny); {best.get('notes', '')}"
            hits[gene] = best
            payload["hla"][gene] = best
            print(f"  {gene:12} {best['rsid']:15} {best['genotype']}", flush=True)

    # --- Faza B+: DAT1 VNTR ---
    dat1 = infer_dat1_vntr()
    payload["vntr"]["SLC6A3"] = dat1
    print(f"[B+] DAT1: {dat1['genotype']} ({dat1['confidence']})", flush=True)

    # --- Faza D+: gene proxy SNPs ---
    proxy_rsids = [rs for rslist in GENE_PROXY.values() for rs in rslist]
    proxy_rows = genotype_rsids(sorted(set(proxy_rsids), key=lambda x: int(x[2:])), min_mapq=0, min_baseq=0, prefer_dbsnp=True)
    for gene, rsids in GENE_PROXY.items():
        if gene in hits:
            continue
        best = pick_best(gene, rsids, proxy_rows)
        if best:
            best["source"] = "bam+gene_proxy"
            hits[gene] = best
            payload["proxy"][gene] = best
            print(f"  {gene:12} {best['rsid']:15} {best['genotype']}", flush=True)

    # --- Geny bez tag-SNP: auto-discovery z Ensembl ---
    no_tag = [
        "ALMS1", "ARID1B", "BCL11B", "GRIA2", "NKX2-2", "NKX2-4",
        "PCDHG", "SOX7", "THSD7A", "ZSWIM6",
    ]
    for gene in no_tag:
        if gene in hits:
            continue
        region = ensembl_gene_region(gene)
        if not region:
            continue
        rsids = ensembl_common_snps(*region, limit=5)
        if not rsids:
            continue
        rows = genotype_rsids(rsids, min_mapq=0, min_baseq=0, prefer_dbsnp=True, threads=4)
        best = pick_best(gene, rsids, rows)
        if best:
            best["source"] = "bam+ensembl_proxy"
            best["notes"] = f"auto tag-SNP w genie; {best.get('notes', '')}"
            hits[gene] = best
            payload["proxy"][gene] = best
            print(f"  {gene:12} {best['rsid']:15} {best['genotype']} (auto)", flush=True)

    # --- NSUN6 fix ---
    nsun = nsun6_fix()
    payload["nsun6"] = nsun
    if nsun:
        nsun["source"] = "bam+nsun6_proxy"
        hits["NSUN6"] = nsun
        print(f"[NSUN6] {nsun['rsid']} {nsun['genotype']}", flush=True)

    # --- CNV depth hints ---
    cnv_genes = ["CHD8", "PTEN", "C4A", "DYRK1A", "AKAP11", "KMT2D", "BCL11B"]
    for gene in cnv_genes:
        scan = cnv_depth_scan(gene)
        if scan:
            payload["cnv"][gene] = scan
            print(f"[CNV] {gene}: avg={scan['avg_depth']}x hint={scan['cnv_hint']}", flush=True)

    update_missing_csv(hits)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[done] {len(hits)} nowych/uzupelnionych genow -> {OUT_JSON}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
