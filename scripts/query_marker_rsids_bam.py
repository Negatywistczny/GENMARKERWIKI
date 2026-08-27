#!/usr/bin/env python3
"""Szybkie genotypowanie rsID z raportu markerów (Ensembl + jeden mpileup BAM)."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "data" / "reports" / "markery" / "Zbiorowe badanie markerów.md"
FASTQ = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER")
WORK = FASTQ / ".work"
OUT = WORK / "marker_report_genotypes.csv"

BCF = str(FASTQ / "tools/bin/bcftools.exe")
BAM = str(FASTQ / "BAM/F25A910000190-04_HOMnzpvR_ULCEDCBF2693_ULCEDCBF2693.bam")
REF = str(WORK / "hg38.fa")
SKIP = {"", "NOT_FOUND", "NO_CALL", "BRAK", "--", "NOT_IN_DBSNP"}


def load_existing() -> dict[str, str]:
    found: dict[str, str] = {}
    for path in sorted(WORK.glob("query_rsid*.csv")):
        with path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                rs = row.get("RSID", "").strip().lower()
                gt = row.get("RESULT", "").strip()
                if rs.startswith("rs") and gt not in SKIP:
                    found[rs] = gt
    for name in (
        "bam_genotypes_final.csv",
        "pharmaco_genotypes.csv",
        "neurodev_wiki_genotypes.csv",
        "missing_sec4_genotypes.csv",
        "vntr_genotypes.csv",
    ):
        path = WORK / name
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                rs = row.get("RSID", "").strip().lower()
                gt = row.get("RESULT", "").strip()
                if rs.startswith("rs") and gt not in SKIP:
                    found.setdefault(rs, gt)
    return found


def fetch_ensembl(rsid: str) -> tuple[str, dict | None, str | None]:
    url = f"https://rest.ensembl.org/variation/human/{rsid}?content-type=application/json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except Exception as exc:
        return rsid, None, str(exc)
    mappings = [m for m in data.get("mappings", []) if m.get("assembly_name") == "GRCh38"]
    if not mappings:
        mappings = data.get("mappings", [])
    if not mappings:
        return rsid, None, "no mapping"
    m = mappings[0]
    chrom = str(m["seq_region_name"])
    if not chrom.lower().startswith("chr"):
        chrom = f"chr{chrom}"
    return rsid, {"chrom": chrom, "pos": int(m["start"])}, None


def parse_gt(gt_raw: str) -> list[str] | None:
    if gt_raw in {"", ".", "./.", ".|."}:
        return None
    tokens = re.split(r"[/|]", gt_raw)
    if not tokens or any(t in {"", "."} for t in tokens):
        return None
    return tokens


def gt_to_bases(gt_tokens: list[str], ref: str, alt: str) -> str | None:
    alts = alt.split(",") if alt and alt != "." else []
    alleles = [ref] + alts
    bases: list[str] = []
    try:
        for token in gt_tokens:
            idx = int(token)
            if idx < 0 or idx >= len(alleles):
                return None
            bases.append(alleles[idx])
    except ValueError:
        return None
    if len(bases) == 1:
        return f"{bases[0]}{bases[0]}"
    return "".join(bases)


def main() -> int:
    found = load_existing()
    text = REPORT.read_text(encoding="utf-8")
    rsids = sorted(set(re.findall(r"rs\d+", text, re.I)), key=lambda x: int(x[2:]))
    missing = [r for r in rsids if r.lower() not in found]
    print(f"[info] Brakujących rsID: {len(missing)}", flush=True)
    if not missing:
        return 0

    sites: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=16) as pool:
        futures = {pool.submit(fetch_ensembl, rsid): rsid for rsid in missing}
        for future in as_completed(futures):
            rsid, info, _err = future.result()
            if info:
                sites[rsid] = info
    print(f"[info] Ensembl: {len(sites)}/{len(missing)}", flush=True)

    regions = WORK / "marker_query_regions.bed"
    region_lines = [f"{s['chrom']}\t{s['pos']}\t{s['pos']}\n" for s in sites.values()]
    regions.write_text("".join(region_lines), encoding="utf-8")

    mpileup = [
        BCF, "mpileup", "--no-BAQ", "-f", REF, "-R", str(regions),
        "-Ou", "-q", "20", "-Q", "20", "-d", "120", BAM,
    ]
    call = [BCF, "call", "-c", "-Ou"]
    query = [BCF, "query", "-f", "%CHROM:%POS\t%REF\t%ALT\t[%GT]\n"]

    proc1 = subprocess.Popen(mpileup, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc2 = subprocess.Popen(call, stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc1.stdout:
        proc1.stdout.close()
    proc3 = subprocess.run(query, stdin=proc2.stdout, capture_output=True, text=True)
    if proc2.stdout:
        proc2.stdout.close()
    proc1.wait()
    proc2.wait()

    if proc1.returncode or proc2.returncode or proc3.returncode:
        err = ""
        if proc1.stderr:
            err += proc1.stderr.read().decode("utf-8", errors="replace")
        if proc2.stderr:
            err += proc2.stderr.read().decode("utf-8", errors="replace")
        print(err[:800], file=sys.stderr)
        print(proc3.stderr[:800], file=sys.stderr)
        return 1

    genotypes: dict[str, str] = {}
    for line in proc3.stdout.splitlines():
        cols = line.split("\t")
        if len(cols) < 4:
            continue
        key, ref, alt, gt_raw = cols[0], cols[1], cols[2], cols[3]
        gt_tokens = parse_gt(gt_raw)
        genotype = "NO_CALL" if gt_tokens is None else (gt_to_bases(gt_tokens, ref, alt) or "NO_CALL")
        genotypes[key] = genotype

    hits = 0
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["RSID", "RESULT", "SOURCE", "CONFIDENCE", "NOTES"])
        for rsid in missing:
            if rsid not in sites:
                w.writerow([rsid, "NOT_IN_DBSNP", "ensembl", "none", "marker_report"])
                continue
            key = f"{sites[rsid]['chrom']}:{sites[rsid]['pos']}"
            gt = genotypes.get(key, "NO_CALL")
            if gt not in SKIP:
                hits += 1
            w.writerow([rsid, gt, "ensembl+bam", "high" if gt not in SKIP else "low", "marker_report"])

    print(f"[done] Zapisano {OUT.name}: {hits}/{len(missing)} z genotypem.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
