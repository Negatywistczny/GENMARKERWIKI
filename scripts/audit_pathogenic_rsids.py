#!/usr/bin/env python3
"""Audyt rsID oznaczonych jako patogenne: locus genu, MAF, zgodność z WGS."""

from __future__ import annotations

import csv
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
from audit_rsID_rules import filter_pathogenic_noise

MD = ROOT / "md"
REPORT = ROOT / "raporty" / "Raport-osobisty-genom-wiki.md"
WGS_PATHS = [
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\wgs_full_genome_lookup.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\missing_sec4_genotypes.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\neurodev_wiki_genotypes.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\bam_genotypes_final.csv"),
]

PATHOGENIC_MARKERS = re.compile(
    r"patogenn|nonsense|pathogenic|heterozygot patogen|p\.\w+Ter|LoF.*patogen",
    re.I,
)
RSID_RE = re.compile(r"rs\d+", re.I)
GENE_SYMBOL_RE = re.compile(r"\*\*Główny symbol genu:\*\*\s*([A-Z0-9-]+)", re.I)

# Znane poprawki / wyjątki (proxy, tag-SNP)
SKIP_RSIDS = set()


def load_wgs() -> dict[str, str]:
    out: dict[str, str] = {}
    for path in WGS_PATHS:
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rs = (row.get("RSID") or row.get("rsid") or "").strip().lower()
                gt = (row.get("RESULT") or row.get("GENOTYPE") or row.get("genotype") or "").strip().upper()
                if rs.startswith("rs") and gt:
                    out.setdefault(rs, gt)
    return out


def rsids_with_local_pathogenic(text: str) -> list[str]:
    """rsID tylko gdy marker patogenny dotyczy tego samego fragmentu linii."""
    out: list[str] = []
    for m in RSID_RE.finditer(text):
        start = m.start()
        nxt = RSID_RE.search(text, m.end())
        end = nxt.start() if nxt else len(text)
        chunk = text[start:end]
        if PATHOGENIC_MARKERS.search(chunk):
            out.append(m.group(0).lower())
    return out


def parse_md_pathogenic() -> list[dict]:
    items: list[dict] = []
    for md in sorted(MD.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        gene = GENE_SYMBOL_RE.search(text)
        gene_sym = (gene.group(1) if gene else md.stem).upper()
        current_heading = ""
        for line in text.splitlines():
            s = line.strip()
            if s.startswith("**") and "rs" in s.lower():
                current_heading = s.strip("*")
            heading_hit = bool(PATHOGENIC_MARKERS.search(current_heading))
            line_rsids = rsids_with_local_pathogenic(s)
            if heading_hit:
                for rs in RSID_RE.findall(current_heading):
                    line_rsids.append(rs.lower())
            if not line_rsids:
                continue
            for rs in dict.fromkeys(line_rsids):
                items.append(
                    {
                        "gene": gene_sym,
                        "rsid": rs,
                        "heading": current_heading[:120],
                        "file": md.name,
                    }
                )
    # dedupe
    seen: set[tuple[str, str]] = set()
    uniq: list[dict] = []
    for it in items:
        key = (it["gene"], it["rsid"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(it)
    return uniq


def fetch_ensembl(rsid: str) -> dict | None:
    url = f"https://rest.ensembl.org/variation/human/{rsid}?content-type=application/json;pops=1"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def fetch_gene_region(symbol: str) -> tuple[str, int, int] | None:
    url = (
        f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{symbol}"
        "?content-type=application/json"
    )
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            d = json.loads(resp.read().decode())
        return str(d["seq_region_name"]), int(d["start"]), int(d["end"])
    except Exception:
        return None


def maf_from_data(data: dict) -> float | None:
    m = data.get("MAF")
    if m is not None:
        try:
            return float(m)
        except (TypeError, ValueError):
            pass
    pops = data.get("populations") or []
    freqs = []
    for p in pops:
        f = p.get("frequency")
        if f is not None:
            try:
                freqs.append(float(f))
            except (TypeError, ValueError):
                pass
    return max(freqs) if freqs else None


def audit_item(item: dict, wgs: dict[str, str], gene_region: tuple[str, int, int] | None) -> dict:
    rsid = item["rsid"]
    data = fetch_ensembl(rsid)
    result = {**item, "issues": []}
    if not data:
        result["issues"].append("ensembl_not_found")
        return result

    mappings = [m for m in data.get("mappings", []) if m.get("assembly_name") == "GRCh38"]
    if not mappings:
        mappings = data.get("mappings", [])
    if not mappings:
        result["issues"].append("no_grch38_mapping")
        return result

    m = mappings[0]
    chrom = str(m["seq_region_name"])
    pos = int(m["start"])
    result["chrom"] = chrom
    result["pos"] = pos
    result["alleles"] = m.get("allele_string", "")
    result["consequence"] = data.get("most_severe_consequence", "")
    result["clinical"] = data.get("clinical_significance") or []

    maf = maf_from_data(data)
    result["maf"] = maf
    if maf is not None and maf >= 0.01:
        result["issues"].append(f"common_snp_maf={maf:.3f}")

    if gene_region:
        g_chr, g_start, g_end = gene_region
        pad = 500_000
        if chrom != g_chr or pos < g_start - pad or pos > g_end + pad:
            result["issues"].append(
                f"wrong_locus:rs_on_chr{chrom}:{pos}_gene_chr{g_chr}:{g_start}-{g_end}"
            )

    # ClinVar ID collision heuristic: rs number small + common + wrong locus
    rs_num = int(rsid[2:])
    if rs_num < 2_000_000 and maf and maf >= 0.05:
        result["issues"].append("suspect_clinvar_id_collision")

    gt = wgs.get(rsid)
    result["wgs"] = gt or ""
    if gt and result["issues"]:
        # het/common call + flagged = likely false pathogenic profile
        if "/" not in gt and len(gt) == 2 and gt[0] != gt[1]:
            het = True
        else:
            het = len(set(gt.replace("/", ""))) > 1 if gt else False
        if het or (maf and maf >= 0.01):
            result["issues"].append(f"wgs_call={gt}_with_flags")

    return result


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    items = [x for x in parse_md_pathogenic() if x["rsid"] not in SKIP_RSIDS]
    wgs = load_wgs()
    gene_regions: dict[str, tuple[str, int, int] | None] = {}
    for gene in {i["gene"] for i in items}:
        gene_regions[gene] = fetch_gene_region(gene)

    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = {
            pool.submit(audit_item, it, wgs, gene_regions.get(it["gene"])): it
            for it in items
        }
        for fut in as_completed(futs):
            results.append(fut.result())

    bad = [r for r in results if filter_pathogenic_noise(r)]
    info = [r for r in results if r.get("issues") and not filter_pathogenic_noise(r)]
    print(f"Sprawdzono patogennych rsID: {len(results)}")
    print(f"Krytyczne: {len(bad)}")
    print(f"Informacyjne (powszechne SNP / ref): {len(info)}\n")
    for r in sorted(bad, key=lambda x: (x["gene"], x["rsid"])):
        print(f"## {r['gene']} / {r['rsid']} [KRYTYCZNE]")
        print(f"   plik: {r['file']}")
        print(f"   nagłówek: {r.get('heading','')[:90]}")
        if r.get("chrom"):
            print(f"   locus: chr{r['chrom']}:{r['pos']} alleles={r.get('alleles')} MAF={r.get('maf')}")
        if r.get("wgs"):
            print(f"   WGS: {r['wgs']}")
        for issue in filter_pathogenic_noise(r):
            print(f"   ! {issue}")
        print()

    if info:
        print(f"=== Informacyjne ({len(info)} wpisów, OK przy hom ref) ===")
        for r in sorted(info[:5], key=lambda x: (x["gene"], x["rsid"])):
            print(f"  {r['gene']}/{r['rsid']}: {', '.join(r['issues'][:2])}")
        if len(info) > 5:
            print(f"  ... i {len(info) - 5} więcej")

    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
