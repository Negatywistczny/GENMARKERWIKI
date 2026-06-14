#!/usr/bin/env python3
"""Wspólne reguły audytu rsID — whitelisty i filtrowanie fałszywych alarmów."""

from __future__ import annotations

# Celowo poza lokusem głównego genu (proxy / gen sąsiedni / GWAS tag-SNP)
GENE_RSID_WHITELIST: dict[str, set[str]] = {
    "ALDH2": {"rs1229984"},  # ADH1B chr4 — opisany w karcie ALDH2
    "ZEB2": {"rs2252641", "rs35500812"},  # cis-regulatory / CAD GWAS
    "OR1A1": {"rs2073153"},  # paralogia OR chr6/17 — HORDE/OR1A1 chr17, Ensembl czasem chr6
}

# Pary (gen, rsid) z błędnym chromosomem — po naprawie wiki powinno być puste
KNOWN_WRONG_RSIDS: set[tuple[str, str]] = set()


def is_whitelisted(gene: str, rsid: str) -> bool:
    return rsid.lower() in GENE_RSID_WHITELIST.get(gene.upper(), set())


def is_critical_wrong_chr(gene: str, rsid: str, issues: list[str]) -> bool:
    key = (gene.upper(), rsid.lower())
    if key in KNOWN_WRONG_RSIDS:
        return True
    if is_whitelisted(gene, rsid):
        return False
    return any(i.startswith("WRONG_CHR") for i in issues)


def is_critical_wrong_locus(gene: str, rsid: str, issues: list[str]) -> bool:
    if is_whitelisted(gene, rsid):
        return False
    for issue in issues:
        if issue.startswith("wrong_locus:"):
            # ten sam chromosom ale poza genem — tylko jeśli nie whitelist
            parts = issue.split("_gene_chr")
            if len(parts) == 2:
                rs_part = parts[0].replace("wrong_locus:rs_on_chr", "")
                rs_chr = rs_part.split(":")[0]
                gene_part = parts[1].split("-")[0]
                if rs_chr != gene_part.split(":")[0] if ":" in gene_part else rs_chr != gene_part:
                    return True
                return False
            return True
    return False


def filter_pathogenic_noise(result: dict) -> list[str]:
    """Zostaw tylko krytyczne flagi (zły chrom vs gen)."""
    gene = result.get("gene", "")
    rsid = result.get("rsid", "")
    issues = result.get("issues", [])
    if is_whitelisted(gene, rsid):
        return []
    critical: list[str] = []
    for issue in issues:
        if issue.startswith("wrong_locus:"):
            # chr mismatch inside wrong_locus string
            if "_gene_chr" in issue:
                loc = issue.split("_gene_chr", 1)[1]
                rs_loc = issue.split("wrong_locus:rs_on_chr", 1)[1].split("_gene_")[0]
                rs_chr = rs_loc.split(":")[0]
                g_chr = loc.split(":")[0]
                if rs_chr != g_chr:
                    critical.append(issue)
        elif issue in ("ensembl_not_found", "no_grch38_mapping"):
            critical.append(issue)
    return critical
