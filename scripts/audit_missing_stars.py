#!/usr/bin/env python3
"""Audit markers: no genotype, no table row match, or no ★ in md."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_personal_report import (  # noqa: E402
    MD_DIR,
    STAR,
    _primary_genotype,
    block_for_rsid,
    load_markers,
    match_apoe,
    match_row,
    parse_sections,
    primary_rsid,
    row_keys,
    split_rs_blocks,
)

SPECIAL_PAIRS = {
    ("APOE", "rs429358"),
    ("APOE", "rs7412"),
    ("GC", "rs7041"),
    ("GC", "rs4588"),
}


def main() -> None:
    by_gene = load_markers()
    no_genotype: list[tuple[str, str]] = []
    no_match: list[tuple[str, str, str, str]] = []
    no_star: list[tuple[str, str, str, str]] = []

    for gene, entries in sorted(by_gene.items()):
        md_path = MD_DIR / f"{gene}.md"
        if not md_path.exists():
            continue
        md_text = md_path.read_text(encoding="utf-8")
        sections = parse_sections(md_text)
        sec4 = sections.get(4, "")
        intro, blocks = split_rs_blocks(sec4)

        known = {e["rsid"]: e for e in entries if e.get("genotype")}
        unknown = [e for e in entries if not e.get("genotype")]

        for e in unknown:
            no_genotype.append((gene, e["rsid"]))

        # APOE haplotype
        if gene == "APOE" and "rs429358" in known and "rs7412" in known:
            for _, block in blocks:
                if "rs429358" in block or "haplotyp" in block.lower():
                    row = match_apoe(
                        known["rs429358"]["genotype"],
                        known["rs7412"]["genotype"],
                        block,
                    )
                    if not row:
                        continue
                    star_ok = any(
                        STAR in line and row["keys"] & row_keys(line.split("|")[1])
                        for line in block.splitlines()
                        if line.startswith("|") and ":---" not in line
                    )
                    if not star_ok:
                        no_star.append(
                            (
                                gene,
                                "APOE haplotyp",
                                f"{known['rs429358']['genotype']}+{known['rs7412']['genotype']}",
                                row["genotype_cell"],
                            )
                        )

        for rsid, entry in known.items():
            if (gene, rsid) in SPECIAL_PAIRS:
                continue
            gt = entry["genotype"]
            src = entry.get("source") or ""
            block = block_for_rsid(rsid, blocks, sec4, intro)
            row = match_row(gene, rsid, gt, block)

            if not row:
                no_match.append((gene, rsid, gt, src))
                continue

            star_in_md = False
            prim = _primary_genotype(row["genotype_cell"])
            star_block = block_for_rsid(rsid, blocks, sec4, intro)
            for line in star_block.splitlines():
                if STAR not in line:
                    continue
                if "|" not in line:
                    continue
                cell = line.split("|")[1]
                if _primary_genotype(cell) == prim:
                    star_in_md = True
                    break

            if not star_in_md:
                no_star.append((gene, rsid, gt, row["genotype_cell"]))

    print("=== BEZ GENOTYPU W ŹRÓDŁACH (panel ma rsID, brak w CSV/WGS/MH) ===")
    for gene, rsid in no_genotype:
        print(f"  {gene:10} {rsid}")
    print(f"Razem: {len(no_genotype)}\n")

    print("=== GENOTYP JEST, BRAK DOPASOWANIA WIERSZA W TABELI §4 ===")
    for gene, rsid, gt, src in no_match:
        print(f"  {gene:10} {rsid:15} genotyp={gt:8} ({src})")
    print(f"Razem: {len(no_match)}\n")

    print("=== DOPASOWANIE OK, BRAK GWIAZDKI W MD ===")
    for gene, rsid, gt, row_gt in no_star:
        print(f"  {gene:10} {rsid:15} BAM={gt:8} wiersz={row_gt}")
    print(f"Razem: {len(no_star)}")


if __name__ == "__main__":
    main()
