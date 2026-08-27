#!/usr/bin/env python3
"""Znajdź genotypy brakujących minikart w eksporcie BAM (rsid.csv) lub bcftools."""

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
MD_MINI = ROOT / "docs" / "genes-mini"
REPORT = ROOT / "data" / "reports" / "markery" / "Zbiorowe badanie markerów.md"
FASTQ = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER")
BAM_DIR = FASTQ / "BAM"
RSID_CSV = BAM_DIR / "ULCEDCBF2693.rsid.csv"
BAM = BAM_DIR / "F25A910000190-04_HOMnzpvR_ULCEDCBF2693_ULCEDCBF2693.bam"
REF = FASTQ / ".work" / "hg38.fa"
BCF = FASTQ / "tools" / "bin" / "bcftools.exe"
OUT = ROOT / "scripts" / "data" / "missing_mini_wgs_from_bam.csv"
CACHE = ROOT / "scripts" / "data" / "rsid_allele_cache.json"

WGS_LINE = re.compile(
    r"`(rs\d+)`\s*[\u2014\u2013\-]+\s*\*\*([A-Z0-9/*]+)\*\*",
    re.I,
)
RSID_META = re.compile(r"\* \*\*Główny rsID.*?:\*\*\s*(.+)", re.I)
SKIP = frozenset({"", "NOT_FOUND", "NO_CALL", "BRAK", "--", "NOT_IN_DBSNP"})


def parse_wgs_calls(body: str) -> dict[str, str]:
    out: dict[str, str] = {}
    in_wgs = False
    for ln in body.splitlines():
        if "Mój genotyp (WGS)" in ln:
            in_wgs = True
            continue
        if in_wgs:
            if ln.startswith("###") or (
                ln.startswith("* **")
                and "WGS" not in ln
                and "Dopasowany" not in ln
            ):
                if out:
                    break
                continue
            mm = WGS_LINE.search(ln)
            if mm:
                out[mm.group(1).lower()] = mm.group(2).upper()
    return out


def genes_without_wgs_calls() -> list[str]:
    missing: list[str] = []
    for md in sorted({p.stem.upper() for p in MD_MINI.glob("*.md")}):
        body = (MD_MINI / f"{md}.md").read_text(encoding="utf-8")
        if not parse_wgs_calls(body):
            missing.append(md)
    return missing


def report_gene_rsids(genes: set[str]) -> dict[str, list[str]]:
    text = REPORT.read_text(encoding="utf-8")
    parts = re.split(r"^### ", text, flags=re.M)[1:]
    out: dict[str, list[str]] = {}
    for part in parts:
        gene = part.split("\n", 1)[0].strip().upper()
        if gene not in genes:
            continue
        body = part.split("\n", 1)[1] if "\n" in part else ""
        rsids = sorted(set(re.findall(r"rs\d+", body, re.I)), key=lambda x: int(x[2:]))
        out[gene] = [r.lower() for r in rsids]
    return out


def primary_rsid(line: str) -> str | None:
    m = re.search(r"(rs\d+)", line or "", re.I)
    return m.group(1).lower() if m else None


def mini_primary_rsid(gene: str) -> str | None:
    path = MD_MINI / f"{gene}.md"
    if not path.exists():
        return None
    body = path.read_text(encoding="utf-8")
    m = RSID_META.search(body)
    return primary_rsid(m.group(1) if m else "")


def load_rsid_csv(targets: set[str]) -> dict[str, str]:
    found: dict[str, str] = {}
    if not RSID_CSV.exists():
        return found
    print(f"[info] Skan {RSID_CSV.name} ({len(targets)} rsID)...", flush=True)
    with RSID_CSV.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:
                continue
            rs, gt = line.split(",", 1)
            rs = rs.strip().lower()
            if rs in targets and rs not in found:
                found[rs] = gt.strip().upper()
                if len(found) == len(targets):
                    break
    return found


def fetch_ensembl(rsid: str) -> tuple[str, dict | None]:
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
    if not chrom.lower().startswith("chr"):
        chrom = f"chr{chrom}"
    return rsid, {"chrom": chrom, "pos": int(m["start"])}


def query_bam_bcftools(rsids: list[str]) -> dict[str, str]:
    if not rsids or not BCF.exists() or not BAM.exists() or not REF.exists():
        return {}
    sites: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(fetch_ensembl, rs): rs for rs in rsids}
        for future in as_completed(futures):
            rsid, info = future.result()
            if info:
                sites[rsid] = info
    if not sites:
        return {}
    bed = FASTQ / ".work" / "missing_mini_regions.bed"
    bed.parent.mkdir(parents=True, exist_ok=True)
    bed.write_text(
        "".join(f"{s['chrom']}\t{s['pos']}\t{s['pos']}\n" for s in sites.values()),
        encoding="utf-8",
    )
    mpileup = [
        str(BCF), "mpileup", "--no-BAQ", "-f", str(REF), "-R", str(bed),
        "-Ou", "-q", "20", "-Q", "20", "-d", "120", str(BAM),
    ]
    call = [str(BCF), "call", "-c", "-Ou"]
    query = [str(BCF), "query", "-f", "%CHROM:%POS\t%REF\t%ALT\t[%GT]\n"]
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
        return {}
    pos_to_rsid = {f"{s['chrom']}:{s['pos']}": rs for rs, s in sites.items()}
    out: dict[str, str] = {}
    for line in proc3.stdout.splitlines():
        cols = line.split("\t")
        if len(cols) < 4:
            continue
        key, ref, alt, gt_raw = cols[0], cols[1], cols[2], cols[3]
        rsid = pos_to_rsid.get(key)
        if not rsid:
            continue
        gt_tokens = re.split(r"[/|]", gt_raw.strip("[]"))
        if not gt_tokens or any(t in {"", "."} for t in gt_tokens):
            out[rsid] = "NO_CALL"
            continue
        alts = alt.split(",") if alt and alt != "." else []
        alleles = [ref] + alts
        bases: list[str] = []
        try:
            for token in gt_tokens:
                bases.append(alleles[int(token)])
        except (ValueError, IndexError):
            out[rsid] = "NO_CALL"
            continue
        out[rsid] = (bases[0] + bases[0]) if len(bases) == 1 else "".join(bases)
    return out


def main() -> int:
    genes = genes_without_wgs_calls()
    print(f"[info] Minikarty bez calla rsID w WGS: {len(genes)}", flush=True)
    if not genes:
        return 0

    gene_rsids = report_gene_rsids(set(genes))
    all_rsids: set[str] = set()
    gene_primary: dict[str, str | None] = {}
    for gene in genes:
        primary = mini_primary_rsid(gene) or (gene_rsids.get(gene, [None])[0] if gene_rsids.get(gene) else None)
        gene_primary[gene] = primary
        for rs in gene_rsids.get(gene, []):
            all_rsids.add(rs)
        if primary:
            all_rsids.add(primary)

    from_csv = load_rsid_csv(all_rsids)
    still_missing = sorted(r for r in all_rsids if r not in from_csv)
    from_bam: dict[str, str] = {}
    if still_missing:
        print(f"[info] bcftools dla {len(still_missing)} rsID...", flush=True)
        from_bam = query_bam_bcftools(still_missing)

    rows: list[dict[str, str]] = []
    found_genes = 0
    for gene in sorted(genes):
        rsids = gene_rsids.get(gene, [])
        primary = gene_primary.get(gene)
        best_rs = primary
        best_gt = ""
        source = ""
        for rs in rsids:
            gt = from_csv.get(rs) or from_bam.get(rs, "")
            if gt and gt not in SKIP:
                if rs == primary or not best_gt:
                    best_rs, best_gt, source = rs, gt, (
                        "ULCEDCBF2693.rsid.csv" if rs in from_csv else "bcftools+bam"
                    )
        if best_gt:
            found_genes += 1
        rows.append(
            {
                "GENE": gene,
                "PRIMARY_RSID": primary or "",
                "ALL_RSIDS": ";".join(rsids),
                "GENOTYPE": best_gt or "NO_CALL",
                "SOURCE": source or ("no_data" if not rsids else "not_found"),
                "NOTES": f"primary={primary}" if primary else "",
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["GENE", "PRIMARY_RSID", "ALL_RSIDS", "GENOTYPE", "SOURCE", "NOTES"],
        )
        w.writeheader()
        w.writerows(rows)

    print(f"[done] Znaleziono genotypy dla {found_genes}/{len(genes)} genow -> {OUT}", flush=True)
    no_call = [r["GENE"] for r in rows if r["GENOTYPE"] in SKIP | {"NO_CALL"}]
    if no_call:
        print(f"[warn] Bez calla ({len(no_call)}): {', '.join(no_call[:20])}", flush=True)
        if len(no_call) > 20:
            print(f"       ... i {len(no_call) - 20} wiecej", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
