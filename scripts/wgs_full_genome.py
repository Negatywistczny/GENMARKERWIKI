#!/usr/bin/env python3
"""Lookup genotypów WGS z ULCEDCBF2693.full.csv (chr,pos,GT) po rsID."""

from __future__ import annotations

import csv
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FULL_CSV = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\BAM\ULCEDCBF2693.full.csv")
COORD_CACHE = Path(__file__).resolve().parent / "data" / "rsid_coord_cache.json"
DEFAULT_LOOKUP_CSV = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\wgs_full_genome_lookup.csv"
)

RSID_RE = re.compile(r"^rs\d{2,}$", re.I)

WORK_FALLBACK_CSVS = [
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\missing_sec4_genotypes.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\neurodev_wiki_genotypes.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\bam_genotypes_final.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\query_rsid_results.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\adhd_genotypes.csv"),
    Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work\neurodev_genotypes.csv"),
]


def load_coord_cache() -> dict[str, dict]:
    if not COORD_CACHE.exists():
        return {}
    try:
        return json.loads(COORD_CACHE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_coord_cache(cache: dict[str, dict]) -> None:
    COORD_CACHE.parent.mkdir(parents=True, exist_ok=True)
    COORD_CACHE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def fetch_ensembl_site(rsid: str) -> tuple[str, int] | None:
    url = f"https://rest.ensembl.org/variation/human/{rsid}?content-type=application/json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode())
    except Exception:
        return None
    mappings = [m for m in data.get("mappings", []) if m.get("assembly_name") == "GRCh38"]
    if not mappings:
        mappings = data.get("mappings", [])
    if not mappings:
        return None
    m = mappings[0]
    return str(m["seq_region_name"]), int(m["start"])


def ensure_coords(rsids: set[str]) -> dict[str, tuple[str, int]]:
    cache = load_coord_cache()
    out: dict[str, tuple[str, int]] = {}
    missing: list[str] = []
    for rs in sorted({r.lower() for r in rsids if RSID_RE.match(r or "")}):
        entry = cache.get(rs)
        if entry and entry.get("chrom") and entry.get("pos"):
            out[rs] = (str(entry["chrom"]), int(entry["pos"]))
        else:
            missing.append(rs)
    if missing:
        with ThreadPoolExecutor(max_workers=10) as pool:
            futs = {pool.submit(fetch_ensembl_site, rs): rs for rs in missing}
            for fut in as_completed(futs):
                rs = futs[fut]
                site = fut.result()
                if site:
                    chrom, pos = site
                    cache[rs] = {"chrom": chrom, "pos": pos}
                    out[rs] = site
                else:
                    cache[rs] = {"chrom": None, "pos": None}
        save_coord_cache(cache)
    return out


def lookup_from_full_csv(
    coords: dict[str, tuple[str, int]],
    *,
    full_path: Path = FULL_CSV,
) -> dict[str, str]:
    """Jednokrotny scan full.csv — zwraca rsID -> GT (2-literowy)."""
    if not coords or not full_path.exists():
        return {}

    by_chr: dict[str, list[tuple[int, str]]] = {}
    for rs, (chrom, pos) in coords.items():
        by_chr.setdefault(chrom, []).append((pos, rs))
    for chrom in by_chr:
        by_chr[chrom].sort()

    found: dict[str, str] = {}
    wanted_total = len(coords)
    active_chr: str | None = None
    idx = 0
    targets: list[tuple[int, str]] = []

    with full_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            chrom, pos_s, gt = parts
            if chrom != active_chr:
                active_chr = chrom
                targets = by_chr.get(chrom, [])
                idx = 0
            if not targets:
                continue
            try:
                pos = int(pos_s)
            except ValueError:
                continue
            while idx < len(targets) and pos > targets[idx][0]:
                idx += 1
            if idx < len(targets) and pos == targets[idx][0]:
                found[targets[idx][1]] = gt.upper()
                idx += 1
                if len(found) >= wanted_total:
                    break
    return found


def lookup_rsids(rsids: set[str]) -> dict[str, str]:
    coords = ensure_coords(rsids)
    return lookup_from_full_csv(coords)


def load_lookup_csv(path: Path, needed: set[str]) -> dict[str, str]:
    if not path.exists():
        return {}
    needed_l = {r.lower() for r in needed if RSID_RE.match(r or "")}
    found: dict[str, str] = {}
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rs = (row.get("RSID") or row.get("rsid") or "").strip().lower()
            gt = (row.get("RESULT") or row.get("GENOTYPE") or "").strip().upper()
            if rs in needed_l and gt and gt not in {"NOT_FOUND", "NO_CALL", ""}:
                found[rs] = gt
    return found


def load_work_fallback(rsids: set[str]) -> dict[str, str]:
    needed = {r.lower() for r in rsids if RSID_RE.match(r or "")}
    found: dict[str, str] = {}
    for path in WORK_FALLBACK_CSVS:
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rs = (row.get("RSID") or row.get("rsid") or "").strip().lower()
                gt = (
                    row.get("RESULT")
                    or row.get("GENOTYPE")
                    or row.get("genotype")
                    or ""
                ).strip().upper()
                if rs in needed and gt and gt not in {"NOT_FOUND", "NO_CALL", ""}:
                    found.setdefault(rs, gt)
    return found


def collect_rsids_from_md_tables(md_dir: Path) -> set[str]:
    """Tylko rsID z sekcji 4 (nagłówki tabel wariantów), nie z prozy sekcji 2."""
    rsids: set[str] = set()
    heading_re = re.compile(r"\*\*(rs\d+)", re.I)
    for md in md_dir.glob("*.md"):
        in_s4 = False
        for line in md.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if s.startswith("### 4."):
                in_s4 = True
                continue
            if s.startswith("### ") and not s.startswith("### 4."):
                in_s4 = False
            if in_s4:
                for m in heading_re.findall(line):
                    if RSID_RE.match(m):
                        rsids.add(m.lower())
    return rsids


def collect_all_rsids() -> set[str]:
    rsids: set[str] = set()
    rsids.update(collect_rsids_from_gene_rsids_js(ROOT / "public" / "html" / "gene-rsids.js"))
    rsids.update(collect_rsids_from_md_tables(ROOT / "docs" / "genes"))
    return rsids


def build_lookup_csv(
    rsids: set[str],
    out_path: Path = DEFAULT_LOOKUP_CSV,
) -> dict[str, str]:
    coords = ensure_coords(rsids)
    from_full = lookup_from_full_csv(coords)
    found = dict(from_full)
    from_work: dict[str, str] = {}
    for rs, gt in load_work_fallback(rsids).items():
        if rs not in found:
            from_work[rs] = gt
            found[rs] = gt
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["RSID", "RESULT", "SOURCE", "CONFIDENCE", "NOTES"],
        )
        w.writeheader()
        for rs in sorted(found):
            chrom, pos = coords.get(rs, ("?", "?"))
            source = "ULCEDCBF2693.full.csv" if rs in from_full else "work_fallback"
            notes = f"chr{chrom}:{pos}" if rs in coords else "no_ensembl_coord"
            w.writerow(
                {
                    "RSID": rs,
                    "RESULT": found[rs],
                    "SOURCE": source,
                    "CONFIDENCE": "high",
                    "NOTES": notes,
                }
            )
    return found


def collect_rsids_from_gene_rsids_js(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {m.lower() for m in re.findall(r"rs\d+", text, re.I)}


def main() -> int:
    rsids = collect_all_rsids()
    print(f"[info] rsID do lookupu: {len(rsids)}", flush=True)
    found = build_lookup_csv(rsids)
    missing = rsids - set(found)
    print(f"[info] znaleziono: {len(found)}/{len(rsids)} -> {DEFAULT_LOOKUP_CSV}", flush=True)
    if missing:
        print(f"[warn] brak genotypu dla {len(missing)} rsID:", flush=True)
        for rs in sorted(missing, key=lambda x: int(x[2:]))[:20]:
            print(f"  {rs}", flush=True)
        if len(missing) > 20:
            print(f"  ... i {len(missing) - 20} więcej", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
