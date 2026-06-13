#!/usr/bin/env python3
"""Audyt wszystkich rsID z gene-rsids.js: chromosom i odległość od genu."""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(SCRIPTS))
from audit_rsID_rules import is_critical_wrong_chr, is_whitelisted

GENE_RSIDS = ROOT / "html" / "gene-rsids.js"

GENE_RE = re.compile(r"^\s+([A-Z0-9]+):\s*\[", re.M)
RS_RE = re.compile(r'"(rs\d+)"')


def parse_gene_rsids() -> dict[str, list[str]]:
    text = GENE_RSIDS.read_text(encoding="utf-8")
    out: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        gm = GENE_RE.match(line)
        if gm:
            current = gm.group(1)
            out[current] = []
            continue
        if current:
            for rs in RS_RE.findall(line):
                out[current].append(rs.lower())
    return out


def fetch_json(url: str) -> dict | None:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def fetch_gene_region(symbol: str) -> tuple[str, int, int] | None:
    d = fetch_json(
        f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{symbol}?content-type=application/json"
    )
    if not d:
        return None
    return str(d["seq_region_name"]), int(d["start"]), int(d["end"])


def fetch_rsid_locus(rsid: str) -> tuple[str, int, str] | None:
    d = fetch_json(
        f"https://rest.ensembl.org/variation/human/{rsid}?content-type=application/json;pops=1"
    )
    if not d:
        return None
    maps = [m for m in d.get("mappings", []) if m.get("assembly_name") == "GRCh38"]
    if not maps:
        maps = d.get("mappings", [])
    if not maps:
        return None
    m = maps[0]
    return str(m["seq_region_name"]), int(m["start"]), d.get("most_severe_consequence", "")


def audit(gene: str, rsid: str, region: tuple[str, int, int] | None) -> dict:
    loc = fetch_rsid_locus(rsid)
    r = {"gene": gene, "rsid": rsid, "issues": []}
    if not loc:
        r["issues"].append("ensembl_not_found")
        return r
    chrom, pos, cons = loc
    r["chrom"] = chrom
    r["pos"] = pos
    r["consequence"] = cons
    if not region:
        r["issues"].append("gene_region_unknown")
        return r
    g_chr, g_start, g_end = region
    pad = 500_000
    if chrom != g_chr:
        r["issues"].append(f"WRONG_CHR:rs_chr{chrom}_gene_chr{g_chr}")
    elif pos < g_start - pad or pos > g_end + pad:
        r["issues"].append(f"outside_gene:chr{chrom}:{pos}_gene_{g_start}-{g_end}")
    return r


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    mapping = parse_gene_rsids()
    regions: dict[str, tuple[str, int, int] | None] = {}
    for gene in mapping:
        regions[gene] = fetch_gene_region(gene)

    tasks = [(g, rs) for g, rss in mapping.items() for rs in rss]
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futs = {pool.submit(audit, g, rs, regions.get(g)): (g, rs) for g, rs in tasks}
        for fut in as_completed(futs):
            results.append(fut.result())

    wrong_chr = [
        r
        for r in results
        if is_critical_wrong_chr(r["gene"], r["rsid"], r["issues"])
    ]
    outside = [
        r
        for r in results
        if any(i.startswith("outside_gene") for i in r["issues"])
        and not is_whitelisted(r["gene"], r["rsid"])
    ]

    print(f"Sprawdzono rsID: {len(results)}")
    print(f"Zły chromosom (jak rs627566): {len(wrong_chr)}")
    print(f"Poza genem (ten sam chr): {len(outside)}\n")

    if wrong_chr:
        print("=== ZŁY CHROMOSOM ===")
        for r in sorted(wrong_chr, key=lambda x: (x["gene"], x["rsid"])):
            print(f"{r['gene']:10} {r['rsid']:14} chr{r['chrom']}:{r['pos']}  {r.get('consequence','')}")
            for i in r["issues"]:
                print(f"  ! {i}")
        print()

    if outside:
        print("=== POZA LOKUSEM GENU (±500kb, informacyjnie) ===")
        for r in sorted(outside, key=lambda x: (x["gene"], x["rsid"])):
            print(f"{r['gene']:10} {r['rsid']:14} chr{r['chrom']}:{r['pos']}  {r.get('consequence','')}")
            for i in r["issues"]:
                print(f"  ! {i}")

    return 1 if wrong_chr else 0


if __name__ == "__main__":
    raise SystemExit(main())
