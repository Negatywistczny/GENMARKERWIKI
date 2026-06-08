#!/usr/bin/env python3
"""Zastosuj ręcznie opracowane tabele §4 (topic-card z WGS) + kolory w variant-tones.js."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
VARIANT_TONES = ROOT / "html" / "variant-tones.js"
WORK = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work")
FASTQ_SCRIPTS = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\scripts")
CARD_MARKER = "<!-- topic-card -->"
STAR = "★"

sys.path.insert(0, str(ROOT / "scripts"))
from topic_wgs_variant_data import VARIANT_TABLES  # noqa: E402

SEC4_START = re.compile(r"^### 4\. Tabela Wariantów\s*$", re.M)
SEC5_START = re.compile(r"^### 5\.", re.M)


def normalize_tone_key(value: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", value or "")
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = text.replace("★", "").lower()
    for src, dst in {
        "ł": "l", "ą": "a", "ć": "c", "ę": "e", "ń": "n",
        "ó": "o", "ś": "s", "ź": "z", "ż": "z",
    }.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return text.strip()


def genotype_tone_key(genotype: str) -> str:
    g = genotype.replace("★", "").strip()
    g = g.replace("/", " ").upper()
    if len(g) == 2 and "/" not in genotype:
        g = f"{g[0]} {g[1]}"
    return normalize_tone_key(g)


def build_section4(gene: str, tables: list[dict]) -> str:
    blocks: list[str] = ["### 4. Tabela Wariantów"]
    for tbl in tables:
        blocks.append("")
        blocks.append(f"**{tbl['heading']}**")
        blocks.append("")
        blocks.append(
            "| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy (kliniczny i funkcjonalny) |"
        )
        blocks.append("| :--- | :--- | :--- |")
        for row in tbl["rows"]:
            gt = row["genotype"]
            if row.get("star"):
                gt = f"**{STAR} {gt}**"
            else:
                gt = f"**{gt}**"
            blocks.append(f"| {gt} | {row['activity']} | {row['impact']} |")
    return "\n".join(blocks)


def replace_section4(text: str, section4: str) -> str:
    m4 = SEC4_START.search(text)
    if not m4:
        m3 = re.search(r"^### 3\.[^\n]*\n(?:.*\n)*?", text, re.M)
        insert_at = m3.end() if m3 else len(text)
        chunk = "\n\n" + section4 + "\n"
        if CARD_MARKER in text:
            return text[:insert_at] + chunk + text[insert_at:]
        return text

    m5 = SEC5_START.search(text, m4.end())
    end = m5.start() if m5 else text.find(CARD_MARKER, m4.end())
    if end < 0:
        end = len(text)
    return text[: m4.start()] + section4 + "\n\n" + text[end:].lstrip("\n")


def build_tone_entries(gene: str, tables: list[dict]) -> dict[str, dict[str, str]]:
    by_gene: dict[str, dict[str, str]] = {}
    for tbl in tables:
        heading_key = normalize_tone_key(tbl["heading"])
        by_heading: dict[str, str] = {}
        for row in tbl["rows"]:
            by_heading[genotype_tone_key(row["genotype"])] = row["tone"]
        by_gene[heading_key] = by_heading
    return by_gene


def patch_variant_tones(new_genes: dict[str, dict[str, dict[str, str]]]) -> None:
    text = VARIANT_TONES.read_text(encoding="utf-8")
    start = text.index("const FIXED_VARIANT_TONES = {")
    end = text.index("};", start)
    block = text[start:end + 2]

    for gene, headings in new_genes.items():
        gene_upper = gene.upper()
        gene_pat = re.compile(rf"(\n  {re.escape(gene_upper)}: \{{)", re.M)
        if gene_pat.search(block):
            continue
        entries: list[str] = [f"\n  {gene_upper}: {{"]
        for heading_key, genotypes in headings.items():
            entries.append(f'    "{heading_key}": {{')
            for gt_key, tone in genotypes.items():
                entries.append(f'      "{gt_key}": "{tone}",')
            entries.append("    },")
        entries.append("  },")
        block = block[:-2] + "".join(entries) + "\n};"

    new_text = text[:start] + block + text[end + 2:]
    VARIANT_TONES.write_text(new_text, encoding="utf-8")


def verify_bam(rsids: list[str]) -> dict[str, dict]:
    sys.path.insert(0, str(FASTQ_SCRIPTS))
    from bam_genotype_core import genotype_rsids  # noqa: E402

    rows = genotype_rsids(rsids)
    return {r["RSID"].lower(): r for r in rows}


def merge_bam_csv(rows: list[dict]) -> None:
    path = WORK / "bam_genotypes_final.csv"
    existing: dict[str, dict] = {}
    if path.exists():
        with path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                existing[row["RSID"].lower()] = row
    for row in rows:
        existing[row["RSID"].lower()] = row
    fields = ["RSID", "RESULT", "SOURCE", "CONFIDENCE", "NOTES"]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for rs in sorted(existing.keys()):
            w.writerow(existing[rs])


def apply_md() -> list[str]:
    updated: list[str] = []
    for gene, tables in VARIANT_TABLES.items():
        path = MD_DIR / f"{gene}.md"
        if not path.exists():
            print(f"SKIP missing md/{gene}.md")
            continue
        text = path.read_text(encoding="utf-8")
        if CARD_MARKER not in text:
            print(f"SKIP not topic-card: {gene}")
            continue
        sec4 = build_section4(gene, tables)
        new_text = replace_section4(text, sec4)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated.append(gene)
    return updated


def main() -> int:
    rsids = sorted(
        {
            rs
            for tables in VARIANT_TABLES.values()
            for tbl in tables
            for rs in [normalize_tone_key(tbl["heading"]).split()[0]]
            if rs.startswith("rs")
        }
    )
    # extract rsids from headings properly
    rsids = sorted(
        {
            m.group(0).lower()
            for tables in VARIANT_TABLES.values()
            for tbl in tables
            for m in [re.search(r"rs\d+", tbl["heading"], re.I)]
            if m
        }
    )

    print(f"BAM: weryfikacja {len(rsids)} rsID…")
    bam = verify_bam(rsids)
    merge_rows = [bam[rs] for rs in rsids if rs in bam]
    merge_bam_csv(merge_rows)

    mismatches = []
    for gene, tables in VARIANT_TABLES.items():
        for tbl in tables:
            m = re.search(r"(rs\d+)", tbl["heading"], re.I)
            if not m:
                continue
            rs = m.group(1).lower()
            expected = tbl.get("wgs_gt", "").upper().replace("/", "")
            got = bam.get(rs, {}).get("RESULT", "").upper().replace("/", "")
            if expected and got and expected != got:
                mismatches.append((gene, rs, expected, got))

    if mismatches:
        print("BŁĄD: niezgodność BAM vs dane:")
        for item in mismatches:
            print(" ", item)
        return 1

    for rs in rsids:
        row = bam.get(rs, {})
        print(f"  OK {rs} {row.get('RESULT')} ({row.get('NOTES', '')[:50]})")

    updated = apply_md()
    print(f"Zaktualizowano §4: {len(updated)} kart")

    tone_genes = {
        gene: build_tone_entries(gene, tables)
        for gene, tables in VARIANT_TABLES.items()
    }
    patch_variant_tones(tone_genes)
    print(f"variant-tones.js: dodano {len(tone_genes)} genów")

    sync = ROOT / "scripts" / "generate_personal_report.py"
    subprocess.run([sys.executable, str(sync), "--sync-stars"], check=True, cwd=ROOT)

    profiles = ROOT / "scripts" / "build_personal_gene_profiles_js.py"
    if profiles.exists():
        subprocess.run([sys.executable, str(profiles)], check=True, cwd=ROOT)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
