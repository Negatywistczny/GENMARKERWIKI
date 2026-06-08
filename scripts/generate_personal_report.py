#!/usr/bin/env python3
"""Generate personal variant report and sync ★ markers from genotype sources + md/*.md.

Źródła genotypów (priorytet): wybrane_markery.csv → WGS (query_rsid_results.csv) → WGS (raw/*.ai_full.csv) → MyHeritage.

Gwiazdka ★ w md/*.md (sekcja 4) oznacza wyłącznie wiersz potwierdzonego genotypem
właściciela — ustawiana tylko przez dopasowanie do powyższych źródeł.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
OUT = ROOT / "raporty" / "Raport-osobisty-genom-wiki.md"
RSIDS_JS = ROOT / "html" / "gene-rsids.js"
GENE_INDEX_JS = ROOT / "html" / "gene-index.js"
GENE_CATEGORIES_JS = ROOT / "html" / "gene-categories.js"

CSV_PATH = Path(
    r"C:\Users\kacpe\Documents\.PERSONALNA BAZA DANYCH"
    r"\01_zdrowie\03_genetyka\wybrane_markery.csv"
)
MH_PATH = Path(
    r"C:\Users\kacpe\Documents\.PERSONALNA BAZA DANYCH"
    r"\01_zdrowie\03_genetyka\01_surowe_dane\myheritage_raw_dna_data.csv"
)
BAM_GENOTYPES_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\bam_genotypes_final.csv"
)
QUERY_RSID_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\query_rsid_results.csv"
)
NEURODEV_GENOTYPES_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\neurodev_genotypes.csv"
)
NEURODEV_WIKI_RSIDS_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\neurodev_wiki_genotypes.csv"
)
MISSING_SEC4_GENOTYPES_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\missing_sec4_genotypes.csv"
)
ADHD_GENOTYPES_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\adhd_genotypes.csv"
)
MAOA_VNTR_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\maoa_uvntr.json"
)
AR_CAG_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\ar_cag.json"
)
AVPR1A_RS3_PATH = Path(
    r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
    r"\.work\avpr1a_rs3.json"
)

STAR = "★"

RSID_ALIASES: dict[tuple[str, str, str], list[str]] = {
    ("DRD2", "rs6277", "GA"): ["C/T", "T/C", "A/G", "G/A"],
    ("DRD2", "rs1799732", "TGTG"): ["Ins/Del", "Del/Ins", "INS/DEL", "DEL/INS"],
    ("DRD2", "rs1799732", "TG"): ["Ins/Del", "Del/Ins"],
    ("AR", "rs1385699", "TT"): ["A/A", "T/T"],
    ("ALDH2", "rs1229984", "CC"): ["T/T", "C/C"],
    ("FKBP5", "rs3800373", "CA"): ["C/alt", "C/A", "A/C"],
    ("OR2M", "rs71538191", "GC"): ["G/A", "A/G", "G/C", "C/G"],
    ("OR6A2", "rs7926083", "CC"): ["G/G", "C/C"],
    ("SLC6A4", "rs1042173", "AC"): ["T/G", "G/T", "A/C", "C/A"],
    ("SLC45A2", "rs2287949", "CC"): ["G/G", "C/C"],
    ("SLC24A4", "rs11160059", "CC"): ["G/G", "C/C"],
    ("CDH13", "rs8059696", "TC"): ["T/A", "A/T", "T/C", "C/T"],
    ("CDH13", "rs4783277", "TG"): ["T/G", "G/T"],
    ("ZEB2", "rs2252641", "TC"): ["A/G", "G/A", "T/C", "C/T"],
    ("ZEB2", "rs35500812", "ACA"): ["CC/C"],
    ("TAS2R38", "rs713598", "GG"): ["G/G"],
    ("TAS2R38", "rs1726866", "GG"): ["C/C", "G/G"],
    ("TAS2R38", "rs10246939", "CC"): ["C/C", "A/A", "G/G"],
    ("MTHFR", "rs1801131", "TG"): ["T/G", "C/G", "A/C"],
    ("GC", "rs7041", "AC"): ["G/T", "T/G", "A/C", "C/A"],
    ("GC", "rs4588", "GT"): ["G/T", "T/G", "C/A", "A/C"],
    ("LCT", "rs4988235", "GG"): ["G/G", "C/C"],
    ("MTHFR", "rs1801133", "GG"): ["G/G", "C/C"],
    ("DRD2", "rs1076560", "CC"): ["G/G", "C/C"],
    ("AVPR1A", "rs1042615", "AG"): ["C/T", "T/C"],
    ("AVPR1A", "rs11174811", "CA"): ["C/T", "T/C"],
    ("AVPR1A", "rs10877969", "GG"): ["C/C", "G/G"],
    ("CHRNA5", "rs16969968", "GA"): ["A/G", "G/A"],
    ("VDR", "rs2228570", "AG"): ["A/G", "G/A", "C/T", "T/C"],
    ("VDR", "rs1544410", "TT"): ["T/T", "A/A"],
    ("VDR", "rs7975232", "AA"): ["A/A"],
    ("VDR", "rs731236", "GG"): ["G/G", "C/C"],
    ("IL2RA", "rs11594656", "TA"): ["T/A", "A/T"],
    ("IL2RA", "rs2104286", "TC"): ["T/C", "C/T"],
    ("IL2RA", "rs12722489", "CT"): ["C/T", "T/C"],
    ("OR1A1", "rs2073153", "GG"): ["G/G"],
    ("MTRR", "rs1532268", "CT"): ["C/T", "T/C"],
    ("ABCC11", "rs17822931", "CC"): ["G/G", "C/C"],
    ("ABCC11", "rs17822471", "GG"): ["C/C", "G/G"],
    ("MC1R", "rs1805005", "GG"): ["C/C", "G/G"],
    ("ACTN3", "rs1815739", "TT"): ["T/T", "X/X"],
    ("SLC6A4", "rs25532", "GG"): ["C/C", "G/G"],
    ("SLC6A4", "rs4795541", "L/S"): ["L/S", "S/L", "LS", "SL"],
    ("SLC6A4", "rs25531", "AG"): ["A/G", "G/A"],
    ("MAOA", "MAOA-uVNTR", "4R"): ["4R, 4.5R", "4R/4.5R"],
    ("MAOA", "MAOA-uVNTR", "3R"): ["3R, 3.5R", "3R/3.5R"],
    ("AVPR1A", "AVPR1A-RS3", "0 KOPII ALLELU 334"): ["0 kopii", "0KOPII", "0 kopii allelu 334"],
    ("AVPR1A", "AVPR1A-RS3", "1 KOPIA"): ["1 kopia"],
    ("AVPR1A", "AVPR1A-RS3", "2 KOPIE"): ["2 kopie"],
    ("SLC45A2", "rs26722", "CC"): ["G/G", "C/C"],
    ("SLC45A2", "rs121912621", "CC"): ["G/G", "C/C"],
    ("SLC45A2", "rs375077956", "GG"): ["C/C", "G/G"],
    ("ZEB2", "rs587776604", "TT"): ["G/G", "T/T"],
    ("TSC1", "rs13295634", "GT"): ["G/T", "T/G"],
    ("TSC1", "rs627566", "CT"): ["G/T", "T/G", "C/T", "T/C"],
    ("MECP2", "rs2075596", "GG"): ["C/C", "G/G"],
    ("CHRM2", "rs1824024", "CC"): ["G/G", "C/C"],
    ("SLC45A2", "rs2287949", "TT"): ["A/A", "T/T"],
    ("CDH13", "rs11646213", "TT"): ["A/A", "T/T"],
    ("VKORC1", "rs61742245", "CC"): ["G/G", "C/C"],
    ("SNAP25", "rs363039", "GA"): ["C/T", "T/C", "G/A", "A/G"],
    ("DRD2", "rs1799732", "GG"): ["Ins/Ins", "INS/INS"],
    ("DRD2", "rs1799732", "II"): ["Ins/Ins", "INS/INS"],
    ("CYP2D6", "rs3892097", "CC"): ["G/G", "C/C"],
    ("CYP2D6", "rs1065852", "GG"): ["C/C", "G/G"],
    ("CYP2D6", "rs28371706", "GG"): ["C/C", "G/G"],
    ("CYP2D6", "rs1058164", "CC"): ["G/G", "C/C"],
    ("CYP2D6", "rs72549354", "CC"): ["G/G", "C/C"],
    ("CHRNA5", "rs1051730", "GA"): ["A/G", "G/A"],
    ("CHRNA5", "rs1051730", "AG"): ["A/G", "G/A"],
    ("MAOA", "rs72554632", "CC"): ["C/C", "G/G"],
}

# rsID bez własnej tabeli w md — dopasuj do bloku proxy (np. CHRNA3 rs1051730 → CHRNA5 rs16969968)
RSID_BLOCK_PROXY: dict[str, str] = {
    "rs1051730": "rs16969968",
}

ALIASES: dict[str, list[str]] = {
    "CT": ["C/T", "T/C", "A/G", "G/A"],
    "TC": ["T/C", "C/T"],
    "AG": ["A/G", "G/A"],
    "GA": ["G/A", "A/G"],
    "CA": ["C/A", "A/C"],
    "AC": ["A/C", "C/A"],
    "TG": ["T/G", "G/T"],
    "GT": ["G/T", "T/G"],
}


def norm_genotype(g: str) -> str:
    g = g.strip().upper()
    if not g:
        return g
    if "/" in g:
        parts = [p.strip() for p in g.split("/") if p.strip()]
        return "/".join(sorted(parts))
    if len(g) == 2:
        return "/".join(sorted([g[0], g[1]])) if g[0] != g[1] else f"{g[0]}/{g[1]}"
    return g


def genotype_targets(gene: str, rsid: str, csv_gt: str) -> set[str]:
    g = csv_gt.strip().upper()
    keys = {norm_genotype(g), g}
    if len(g) == 2:
        keys.add(f"{g[0]}/{g[1]}")
        keys.add(f"{g[1]}/{g[0]}")
        if g[0] == g[1]:
            keys.add(f"{g[0]}/{g[0]}")
    for alias in ALIASES.get(g, []):
        keys.add(norm_genotype(alias))
        keys.add(alias.upper())
    for alias in RSID_ALIASES.get((gene, rsid, g), []):
        keys.add(norm_genotype(alias))
        keys.add(alias.upper())
    return {k for k in keys if k}


def wgs_path() -> Path | None:
    raw = ROOT / "raw"
    if not raw.is_dir():
        return None
    candidates = sorted(raw.glob("*.ai_full.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def _load_rsid_csv(path: Path, needed_l: set[str]) -> dict[str, str]:
    if not path.exists():
        return {}
    found: dict[str, str] = {}
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rs = row.get("RSID", row.get("rsid", "")).strip().lower()
            gt = row.get("RESULT", row.get("result", "")).strip().upper()
            if rs in needed_l and gt not in ("NOT_FOUND", "NO_CALL", ""):
                found[rs] = gt
    return found


def _load_neurodev_genotypes(path: Path, needed_l: set[str]) -> dict[str, str]:
    if not path.exists():
        return {}
    found: dict[str, str] = {}
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rs = row.get("RSID", row.get("rsid", "")).strip().lower()
            gt = row.get("GENOTYPE", row.get("genotype", "")).strip().upper()
            status = row.get("STATUS", row.get("status", "")).strip().upper()
            if rs in needed_l and gt not in ("NOT_FOUND", "NO_CALL", "", "BRAK"):
                if status not in ("BRAK", "NOT_FOUND"):
                    found[rs] = gt
    return found


def load_query_rsid(needed: set[str]) -> dict[str, str]:
    needed_l = {r.lower() for r in needed}
    found = _load_rsid_csv(BAM_GENOTYPES_PATH, needed_l)
    for rs, gt in _load_rsid_csv(QUERY_RSID_PATH, needed_l).items():
        found.setdefault(rs, gt)
    for rs, gt in _load_rsid_csv(NEURODEV_WIKI_RSIDS_PATH, needed_l).items():
        found.setdefault(rs, gt)
    for rs, gt in _load_neurodev_genotypes(NEURODEV_GENOTYPES_PATH, needed_l).items():
        found.setdefault(rs, gt)
    for rs, gt in _load_neurodev_genotypes(ADHD_GENOTYPES_PATH, needed_l).items():
        found.setdefault(rs, gt)
    for rs, gt in _load_rsid_csv(MISSING_SEC4_GENOTYPES_PATH, needed_l).items():
        found.setdefault(rs, gt)
    return found


def load_wgs_raw(needed: set[str]) -> dict[str, str]:
    path = wgs_path()
    if not path:
        return {}
    needed_l = {r.lower() for r in needed}
    found: dict[str, str] = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.startswith("rs"):
                continue
            rs, _, gt = line.strip().partition(",")
            rl = rs.lower()
            if rl in needed_l and rl not in found:
                found[rl] = gt.strip().upper()
            if len(found) == len(needed_l):
                break
    return found


def load_wgs(needed: set[str]) -> dict[str, str]:
    found = load_query_rsid(needed)
    for rs, gt in load_wgs_raw(needed).items():
        found.setdefault(rs, gt)
    return found


def load_maoa_uvntr() -> dict | None:
    return _load_vntr_json(MAOA_VNTR_PATH)


def _load_vntr_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    result = data.get("result") or {}
    gt = (result.get("genotype") or "").strip()
    if not gt:
        return None
    return {
        "genotype": gt,
        "confidence": result.get("confidence", ""),
        "method": result.get("method", ""),
        "notes": result.get("notes", ""),
        "source": "WGS (BAM/VNTR)",
    }


def load_ar_cag() -> dict | None:
    return _load_vntr_json(AR_CAG_PATH)


def load_avpr1a_rs3() -> dict | None:
    return _load_vntr_json(AVPR1A_RS3_PATH)


def append_vntr_section(
    lines: list[str],
    gene: str,
    marker_id: str,
    title: str,
    uvntr: dict,
    blocks: list[tuple[str, str]],
    sec4: str,
    intro4: str,
) -> None:
    block = block_for_rsid(marker_id, blocks, sec4, intro4)
    if not block and marker_id == "AVPR1A-RS3":
        for _, b in blocks:
            if "RS3" in b[:120]:
                block = b
                break
    row = match_row(gene, marker_id, uvntr["genotype"], block) if block else None
    lines.append(f"#### {marker_id}")
    lines.append(f"_{title}_\n")
    conf = uvntr.get("confidence", "")
    lines.append(f"- **Genotyp (WGS):** `{uvntr['genotype']}`")
    lines.append(f"- **Źródło:** {uvntr['source']}" + (f" (pewność: {conf})" if conf else ""))
    if uvntr.get("method"):
        lines.append(f"- **Metoda:** {uvntr['method']}")
    if uvntr.get("notes"):
        lines.append(f"- **Uwaga:** {uvntr['notes']}")
    if row:
        lines.append(f"- **Profil w tabeli wariantów:** {row['genotype_cell']}")
        if len(row["cols"]) > 1:
            lines.append(f"- **Aktywność / status:** {row['cols'][1]}")
        if len(row["cols"]) > 2:
            lines.append(f"- **Wpływ fenotypowy:** {row['cols'][2]}")
    else:
        lines.append(
            "- _Brak dopasowania wiersza w tabeli wariantów "
            "(allele VNTR poza listą wiki lub proxy)._"
        )
    lines.append("")


def load_gene_categories() -> dict[str, list[str]]:
    text = GENE_CATEGORIES_JS.read_text(encoding="utf-8")
    themes: dict[str, list[str]] = {}
    for block in re.finditer(
        r'label:\s*"([^"]+)"[\s\S]*?genes:\s*\[([\s\S]*?)\],',
        text,
    ):
        label = block.group(1)
        genes = re.findall(r'"([A-Z0-9]+)"', block.group(2))
        themes[label] = genes
    return themes


def load_wiki_panel() -> tuple[dict[str, list[str]], dict[str, str]]:
    rsids_text = RSIDS_JS.read_text(encoding="utf-8")
    index_text = GENE_INDEX_JS.read_text(encoding="utf-8")
    by_gene: dict[str, list[str]] = {}
    for m in re.finditer(
        r'^\s+(?:"([^"]+)"|([A-Z0-9-]+)):\s*\[([^\]]+)\]', rsids_text, re.M
    ):
        gene = m.group(1) or m.group(2)
        by_gene[gene] = re.findall(r"rs\d+", m.group(3))
    labels: dict[str, str] = {}
    for m in re.finditer(r'\{\s*gene:\s*"([^"]+)",\s*label:\s*"([^"]+)"', index_text):
        labels[m.group(1)] = m.group(2)
    return by_gene, labels


def load_myheritage(needed: set[str]) -> dict[str, str]:
    if not MH_PATH.exists():
        return {}
    needed_l = {r.lower() for r in needed}
    found: dict[str, str] = {}
    with MH_PATH.open(encoding="utf-8", newline="") as f:
        for line in f:
            if not line.startswith('"rs'):
                continue
            row = next(csv.reader([line]))
            if len(row) < 4:
                continue
            rs = row[0].lower()
            if rs in needed_l and rs not in found:
                gt = row[3].strip().upper()
                if gt and gt != "--":
                    found[rs] = gt
    return found


def genotype_source(csv_gt: str, wgs: dict[str, str], mh: dict[str, str], rsid: str) -> tuple[str, str]:
    rs = rsid.lower()
    if csv_gt:
        return csv_gt, "CSV"
    if wgs.get(rs):
        return wgs[rs], "WGS"
    if mh.get(rs):
        return mh[rs], "MyHeritage"
    return "", ""


def load_markers() -> dict[str, list[dict]]:
    wiki_genes, labels = load_wiki_panel()
    needed = {rs.lower() for rslist in wiki_genes.values() for rs in rslist}
    wgs = load_wgs(needed)
    mh = load_myheritage(needed)

    if CSV_PATH.exists():
        rows: list[dict] = []
        with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                rows.append(row)
        by_gene: dict[str, list[dict]] = defaultdict(list)
        for row in rows:
            gene = row["Gen"].strip()
            rsid = row["rsid"].strip()
            gt, source = genotype_source(
                row.get("genotype", "").strip(), wgs, mh, rsid
            )
            by_gene[gene].append(
                {
                    "rsid": rsid,
                    "opis": row["Opis"].strip(),
                    "genotype": gt,
                    "source": source,
                }
            )
        return dict(by_gene)

    by_gene: dict[str, list[dict]] = defaultdict(list)
    for gene, rsids in sorted(wiki_genes.items()):
        for rsid in rsids:
            gt, source = genotype_source("", wgs, mh, rsid)
            by_gene[gene].append(
                {
                    "rsid": rsid,
                    "opis": labels.get(gene, gene),
                    "genotype": gt,
                    "source": source,
                }
            )
    return dict(by_gene)


def strip_md(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(rf"{re.escape(STAR)}\s*", "", s)
    return s.strip()


def row_keys(cell: str) -> set[str]:
    cell = cell.strip()
    keys: set[str] = set()
    token_re = (
        r"(?:lub\s+)?([ACGT]{1,2}/[ACGT]{1,2}|[ACGT]{2}|"
        r"alt/alt|ref/ref|ref/alt|C/alt|CC/C|Gc[\w/]+|Ins/Ins|Del/Del|Ins/Del|Del/Ins|"
        r"wt/wt|L/L|S/S|L/S|S/L|major|minor)"
    )

    def add(tok: str) -> None:
        tok = re.sub(r"\s+", "", tok.strip())
        if tok and tok.lower() not in {"lub", "hom"}:
            if "/" in tok or len(tok) == 2:
                keys.add(norm_genotype(tok))
            else:
                keys.add(tok.upper())

    plain = strip_md(cell)
    if plain:
        add(plain.split("(")[0])
    for bold in re.findall(r"\*\*(?:★\s*)?([^*]+)\*\*", cell):
        text = strip_md(bold).split("(")[0]
        add(text)
        if "," in text:
            for part in text.split(","):
                add(part.strip())
        for inner in re.findall(r"\(([^)]+)\)", bold):
            for m in re.findall(token_re, inner, re.I):
                add(m)
    for inner in re.findall(r"\(([^)]+)\)", cell):
        for m in re.findall(token_re, inner, re.I):
            add(m)
    return keys


def parse_sections(text: str) -> dict[int, str]:
    parts: dict[int, list[str]] = defaultdict(list)
    current = 0
    for line in text.splitlines():
        m = re.match(r"^###\s+(\d+)\.\s+", line)
        if m:
            current = int(m.group(1))
        parts[current].append(line)
    return {n: "\n".join(lines).strip() for n, lines in parts.items()}


def parse_table_block(block: str) -> list[dict]:
    rows = []
    for line in block.splitlines():
        if not line.startswith("|") or ":---" in line:
            continue
        raw = [c.strip() for c in line.split("|")[1:-1]]
        cells = [strip_md(c) for c in raw]
        if not cells or cells[0].lower().startswith("genotyp"):
            continue
        rows.append(
            {
                "genotype_cell": cells[0],
                "keys": row_keys(raw[0]),
                "cols": cells,
            }
        )
    return rows


def primary_rsid(sec2: str) -> str:
    m = re.search(r"rs\d+", sec2, re.I)
    return m.group(0) if m else ""


def repair_glued_section_headers(text: str) -> str:
    """Naprawia przypadki `| ... |### 5.` powstałe przy sklejaniu sekcji."""
    return re.sub(r"(\|)\s*(### \d+\.)", r"\1\n\2", text)


def split_rs_blocks(sec4: str) -> tuple[str, list[tuple[str, str]]]:
    blocks: list[tuple[str, str]] = []
    intro = ""
    current_rsid = ""
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_rsid, current_lines
        if current_lines:
            blocks.append((current_rsid, "\n".join(current_lines)))
        current_lines = []

    for line in sec4.splitlines():
        if re.match(r"^###\s+\d+\.", line.strip()):
            flush()
            current_rsid = ""
            continue
        title_m = re.match(r"^\*\*(?:★\s*)?(.+?)\*\*\s*$", line.strip())
        if title_m:
            flush()
            rs_m = re.search(r"rs\d+", title_m.group(1))
            current_rsid = rs_m.group(0) if rs_m else ""
            current_lines = [line]
            continue
        if not current_rsid and not current_lines and (
            line.strip().startswith("|") or not line.strip()
        ):
            intro += line + "\n"
        elif current_rsid or current_lines:
            current_lines.append(line)
    flush()
    if not blocks and "|" in sec4:
        blocks.append(("", sec4))
    return intro, blocks


def block_for_rsid(
    rsid: str, blocks: list[tuple[str, str]], sec4: str, intro: str = ""
) -> str:
    exact: str | None = None
    partial: str | None = None
    lookup = {rsid, RSID_BLOCK_PROXY.get(rsid, "")}
    for brsid, block in blocks:
        if any(block.lstrip().startswith(f"**{r}") for r in lookup if r):
            exact = block
            break
        if brsid in lookup or any(r in brsid or r in block for r in lookup if r):
            partial = partial or block
    if exact:
        return exact
    if partial:
        return partial
    if intro and rsid in intro and "|" in intro:
        return intro
    if len(blocks) == 1 and not blocks[0][0]:
        return blocks[0][1]
    return sec4


def _primary_genotype(cell: str) -> str:
    plain = strip_md(re.sub(rf"{re.escape(STAR)}\s*", "", cell)).split("(")[0].strip()
    return norm_genotype(plain)


def match_row(gene: str, rsid: str, gt: str, block: str) -> dict | None:
    if rsid == "rs4588" and "rs7041" in block:
        return match_gc_diplotype(gt, block)
    if gene == "APOE" and rsid in ("rs429358", "rs7412") and "rs7412" in block:
        return None  # handled as pair
    targets = genotype_targets(gene, rsid, gt)
    best: dict | None = None
    best_score = -1
    gt_u = gt.strip().upper()
    for row in parse_table_block(block):
        overlap = row["keys"] & targets
        if not overlap:
            continue
        score = len(overlap)
        primary = _primary_genotype(row["genotype_cell"])
        if primary in targets:
            score += 10
        cell_u = strip_md(row["genotype_cell"]).upper()
        if gt_u in cell_u:
            score += 20
        if score > best_score:
            best_score = score
            best = row
    return best


def match_gc_diplotype(gt7041: str, block: str) -> dict | None:
    # caller passes single gt; pair handled in main
    return None


def match_apoe(rs358: str, rs412: str, block: str) -> dict | None:
    t1 = genotype_targets("APOE", "rs429358", rs358)
    t2 = genotype_targets("APOE", "rs7412", rs412)
    for row in parse_table_block(block):
        if len(row["cols"]) < 2:
            continue
        # Osobne kolumny rs429358 | rs7412
        k1, k2 = row_keys(row["cols"][0]), row_keys(row["cols"][1])
        if (k1 & t1) and (k2 & t2):
            return row
        # Połączony genotyp: „T/T + C/C” w pierwszej kolumnie
        parts = re.split(r"\s*\+\s*", row["cols"][0])
        if len(parts) == 2:
            pk1, pk2 = row_keys(parts[0]), row_keys(parts[1])
            if (pk1 & t1) and (pk2 & t2):
                return row
    return None


def extract_bullets(section: str) -> list[str]:
    out: list[str] = []
    for line in section.splitlines():
        s = line.strip()
        # List items use "* **Key:** value" — do not treat as nested italic "* *..."
        if s.startswith("* ") and ":**" in s:
            out.append(strip_md(s[2:].strip()))
        elif s.startswith("* ") and s[2:3] != "*":
            out.append(strip_md(s[2:].strip()))
    return out


def gene_label(gene: str, entries: list[dict]) -> str:
    return entries[0]["opis"] if entries else gene


def build_gene_section(gene: str, entries: list[dict], md_text: str) -> str:
    md_path = MD_DIR / f"{gene}.md"
    if not md_path.exists():
        return f"## {gene}\n\nBrak pliku wiki.\n"

    sections = parse_sections(md_text)
    sec1 = sections.get(1, "")
    sec2 = sections.get(2, "")
    sec3 = sections.get(3, "")
    sec4 = sections.get(4, "")
    sec6 = sections.get(6, "")

    title = gene_label(gene, entries)
    lines = [f"## {gene} — {title}", ""]

    # Profile from section 1-2
    for sec in (sec1, sec2):
        for b in extract_bullets(sec):
            if b and not b.startswith("http"):
                lines.append(f"- {b}")
    lines.append("")

    if sec3:
        lines.append("### Mechanizm i wpływ biologiczny")
        for b in extract_bullets(sec3):
            lines.append(f"- {b}")
        lines.append("")

    known = [e for e in entries if e["genotype"]]
    unknown = [e for e in entries if not e["genotype"]]

    lines.append("### Twoje warianty (znane genotypy)")
    if not known:
        lines.append("_Brak potwierdzonych genotypów w WGS/MyHeritage/CSV dla tego genu._")
    else:
        apoe_gt = {e["rsid"]: e for e in known if gene == "APOE"}
        intro4, blocks = split_rs_blocks(sec4)
        main_rsid = primary_rsid(sec2)

        if gene == "APOE" and "rs429358" in apoe_gt and "rs7412" in apoe_gt:
            for rsid, block in blocks:
                if "rs429358" in block or "Haplotypy" in block:
                    row = match_apoe(
                        apoe_gt["rs429358"]["genotype"],
                        apoe_gt["rs7412"]["genotype"],
                        block,
                    )
                    if row:
                        iso = row["cols"][2] if len(row["cols"]) > 2 else ""
                        lines.append(
                            f"#### Haplotyp APOE (rs429358 + rs7412)\n"
                        )
                        lines.append(
                            f"- **Twój profil:** rs429358 `{apoe_gt['rs429358']['genotype']}`, "
                            f"rs7412 `{apoe_gt['rs7412']['genotype']}`"
                            f"{' → ' + iso if iso else ''}\n"
                            f"- **Źródło:** {apoe_gt['rs429358']['source']}\n"
                        )
                        if len(row["cols"]) > 3:
                            lines.append(f"- **Wpływ fenotypowy:** {row['cols'][-1]}\n")
                    break

        gc_pair = (
            gene == "GC"
            and any(e["rsid"] == "rs7041" for e in known)
            and any(e["rsid"] == "rs4588" for e in known)
        )
        if gene == "MAOA":
            uvntr = load_maoa_uvntr()
            if uvntr:
                append_vntr_section(
                    lines,
                    gene,
                    "MAOA-uVNTR",
                    "MAOA-uVNTR (promotor — aktywność MAOA-L/H)",
                    uvntr,
                    blocks,
                    sec4,
                    intro4,
                )

        if gene == "AR":
            cag = load_ar_cag()
            if cag:
                append_vntr_section(
                    lines,
                    gene,
                    "AR-CAG",
                    "CAGn (VNTR ekson 1 — długość powtórzeń)",
                    cag,
                    blocks,
                    sec4,
                    intro4,
                )

        if gene == "AVPR1A":
            rs3 = load_avpr1a_rs3()
            if rs3:
                append_vntr_section(
                    lines,
                    gene,
                    "AVPR1A-RS3",
                    "RS3 allel 334 (mikrosatelita — więź partnerska)",
                    rs3,
                    blocks,
                    sec4,
                    intro4,
                )

        if gc_pair:
            g7041 = next(e for e in known if e["rsid"] == "rs7041")
            g4588 = next(e for e in known if e["rsid"] == "rs4588")
            t1 = genotype_targets("GC", "rs7041", g7041["genotype"])
            t2 = genotype_targets("GC", "rs4588", g4588["genotype"])
            for rsid, block in blocks:
                if "rs7041" not in block:
                    continue
                for row in parse_table_block(block):
                    if len(row["cols"]) < 2:
                        continue
                    pair = re.split(r"\s*\+\s*", row["cols"][1])
                    if len(pair) == 2:
                        a, b = norm_genotype(pair[0]), norm_genotype(pair[1])
                        if (a in t1 and b in t2) or (a in t2 and b in t1):
                            lines.append(
                                f"#### Haplotyp GC (rs7041 + rs4588)\n"
                                f"- **Twój profil:** rs7041 `{g7041['genotype']}`, "
                                f"rs4588 `{g4588['genotype']}` → **{row['cols'][0]}** "
                                f"({row['cols'][1]})\n"
                                f"- **Wpływ:** {row['cols'][-1]}\n"
                            )
                            break

        handled_rsids = {"rs429358", "rs7412"} if gene == "APOE" else set()
        if gc_pair:
            handled_rsids |= {"rs7041", "rs4588"}

        for entry in known:
            rsid = entry["rsid"]
            if rsid in handled_rsids:
                continue
            block = block_for_rsid(rsid, blocks, sec4, intro4)
            if not block and rsid == main_rsid:
                block = intro4 + "\n" + sec4 if intro4 else sec4
            match_rsid, match_block = rsid, block
            if gene == "CHRNA5" and rsid == "rs1051730":
                match_rsid = "rs16969968"
                match_block = block_for_rsid("rs16969968", blocks, sec4, intro4) or block
            row = match_row(gene, match_rsid, entry["genotype"], match_block)
            m = re.search(rf"\*\*(?:★\s*)?{re.escape(rsid)}[^*]*\*\*", block)
            block_title = strip_md(m.group(0)) if m else (
                main_rsid if rsid == main_rsid else rsid
            )
            lines.append(f"#### {rsid}")
            if block_title and block_title != rsid:
                lines.append(f"_{block_title}_\n")
            src = entry["source"] or "dane"
            lines.append(f"- **Genotyp ({src}):** `{entry['genotype']}`")
            if entry["source"]:
                lines.append(f"- **Źródło:** {entry['source']}")
            if row:
                lines.append(f"- **Profil w tabeli wariantów:** {row['genotype_cell']}")
                if len(row["cols"]) > 1:
                    lines.append(f"- **Aktywność / status:** {row['cols'][1]}")
                if len(row["cols"]) == 3:
                    lines.append(f"- **Wpływ fenotypowy:** {row['cols'][2]}")
                elif len(row["cols"]) == 4:
                    lines.append(f"- **Wpływ fenotypowy:** {row['cols'][3]}")
                elif len(row["cols"]) > 4:
                    lines.append(
                        f"- **Wpływ fenotypowy:** {row['cols'][3]} "
                        f"({row['cols'][4]})" if len(row["cols"]) > 4 else row["cols"][3]
                    )
            else:
                if gene == "MAOA" and rsid == "rs72554632" and norm_genotype(
                    entry["genotype"]
                ) in ("CC", "C/C"):
                    lines.append(
                        "- **Status:** Brak allelu patogennego (Q296Ter); "
                        "brak wariantu Brunner z tego SNP"
                    )
                else:
                    lines.append(
                        "- _Brak dopasowania wiersza w tabeli wariantów "
                        "(różna orientacja nici lub allel referencyjny)._"
                    )
            lines.append("")

    if unknown:
        lines.append("### Markery w panelu bez genotypu w Twoich danych")
        for e in unknown:
            lines.append(
                f"- `{e['rsid']}` — brak wpisu w CSV/WGS/MyHeritage"
            )
        lines.append("")

    if sec6:
        lines.append("### Zalecenia praktyczne")
        for b in extract_bullets(sec6)[:12]:
            if "ostrzeg" not in b.lower() and "pmid" not in b.lower():
                lines.append(f"- {b}")
        lines.append("")

    return "\n".join(lines)


def apply_stars_to_block(
    gene: str,
    block: str,
    rsid: str | None,
    gt: str | None,
    matched_row: dict | None = None,
) -> tuple[str, int]:
    if matched_row is None and rsid and gt:
        matched_row = match_row(gene, rsid, gt, block)

    out: list[str] = []
    stars = 0
    for line in block.splitlines():
        if not line.strip().startswith("|") or ":---" in line:
            out.append(line)
            continue
        raw_cells = [c.strip() for c in line.split("|")[1:-1]]
        if not raw_cells or raw_cells[0].lower().startswith("genotyp"):
            out.append(line)
            continue
        cell = re.sub(r"★\s*", "", raw_cells[0])
        inner = strip_md(cell)
        is_match = (
            matched_row is not None
            and _primary_genotype(cell)
            == _primary_genotype(matched_row["genotype_cell"])
        )
        if is_match:
            raw_cells[0] = f"**★ {inner}**"
            stars += 1
        else:
            raw_cells[0] = f"**{inner}**"
        out.append("| " + " | ".join(raw_cells) + " |")
    return "\n".join(out), stars


def sync_gene_stars(gene: str, entries: list[dict], md_text: str) -> tuple[str, list[str]]:
    md_text = repair_glued_section_headers(md_text)
    sections = parse_sections(md_text)
    sec4 = sections.get(4, "")
    if not sec4:
        return md_text, []

    known = {e["rsid"]: e["genotype"] for e in entries if e.get("genotype")}
    intro, blocks = split_rs_blocks(sec4)
    sec2 = sections.get(2, "")
    main_rsid = primary_rsid(sec2)
    log: list[str] = []
    new_blocks: list[tuple[str, str]] = []

    for brsid, block in blocks:
        rsid = brsid or main_rsid
        matched_row = None
        stars = 0

        if gene == "APOE" and "rs429358" in known and "rs7412" in known:
            if "rs429358" in block or "haplotyp" in block.lower():
                matched_row = match_apoe(known["rs429358"], known["rs7412"], block)
        elif gene == "GC" and "rs7041" in known and "rs4588" in known and "rs7041" in block:
            t1 = genotype_targets("GC", "rs7041", known["rs7041"])
            t2 = genotype_targets("GC", "rs4588", known["rs4588"])
            for row in parse_table_block(block):
                if len(row["cols"]) < 2:
                    continue
                pair = re.split(r"\s*\+\s*", row["cols"][1])
                if len(pair) == 2:
                    a, b = norm_genotype(pair[0]), norm_genotype(pair[1])
                    if (a in t1 and b in t2) or (a in t2 and b in t1):
                        matched_row = row
                        break
        elif gene == "MAOA" and "MAOA-uVNTR" in block[:120]:
            uvntr = load_maoa_uvntr()
            if uvntr:
                matched_row = match_row(gene, "MAOA-uVNTR", uvntr["genotype"], block)
                rsid = "MAOA-uVNTR"
        elif gene == "AVPR1A" and block.lstrip().startswith("**RS3 allel"):
            rs3 = load_avpr1a_rs3()
            if rs3:
                matched_row = match_row(gene, "AVPR1A-RS3", rs3["genotype"], block)
                rsid = "AVPR1A-RS3"

        gt = known.get(rsid, "")
        if gene == "MAOA" and rsid == "MAOA-uVNTR":
            uvntr = load_maoa_uvntr()
            if uvntr:
                gt = uvntr["genotype"]
        if gene == "AVPR1A" and rsid == "AVPR1A-RS3":
            rs3 = load_avpr1a_rs3()
            if rs3:
                gt = rs3["genotype"]
        new_block, stars = apply_stars_to_block(gene, block, rsid, gt or None, matched_row)
        if stars:
            label = gt or known.get(rsid, "haplotyp")
            log.append(f"{rsid}={label} -> {stars} wiersz")
        new_blocks.append((brsid, new_block))

    rebuilt = intro.rstrip("\n")
    for brsid, block in new_blocks:
        if rebuilt and not rebuilt.endswith("\n"):
            rebuilt += "\n"
        rebuilt += block.rstrip("\n") + "\n"
    rebuilt = rebuilt.rstrip("\n") + "\n"

    sec4_match = re.search(
        r"(### 4\.[^\n]*\n)([\s\S]*?)(?=^### 5\.|\Z)",
        md_text,
        re.M,
    )
    if not sec4_match:
        return md_text, log
    tail = md_text[sec4_match.end() :]
    if tail and not rebuilt.endswith("\n"):
        rebuilt = rebuilt.rstrip("\n") + "\n"
    new_text = (
        md_text[: sec4_match.start()]
        + sec4_match.group(1)
        + rebuilt
        + tail
    )
    return new_text, log


def sync_stars_to_md(by_gene: dict[str, list[dict]]) -> None:
    total_stars = 0
    for gene in sorted(by_gene):
        md_path = MD_DIR / f"{gene}.md"
        if not md_path.exists():
            continue
        original = md_path.read_text(encoding="utf-8")
        updated, log = sync_gene_stars(gene, by_gene[gene], original)
        if updated != original:
            md_path.write_text(updated, encoding="utf-8")
            total_stars += len(log)
            print(f"{gene}: {', '.join(log) if log else 'wyczyszczono ★'}")
    print(f"Zsynchronizowano gwiazdke w {total_stars} wierszach (geny z dopasowaniem).")


def main(by_gene: dict[str, list[dict]] | None = None) -> None:
    if by_gene is None:
        by_gene = load_markers()
    genes = sorted(by_gene.keys())

    known_total = sum(1 for g in genes for e in by_gene[g] if e["genotype"])
    marker_total = sum(len(by_gene[g]) for g in genes)

    wgs_raw = wgs_path()
    sources = ["panel markerów z gene-rsids.js"]
    if CSV_PATH.exists():
        sources.insert(0, "wybrane_markery.csv")
    if BAM_GENOTYPES_PATH.exists():
        sources.append(f"WGS ({BAM_GENOTYPES_PATH.name})")
    elif QUERY_RSID_PATH.exists():
        sources.append(f"WGS ({QUERY_RSID_PATH.name})")
    if NEURODEV_GENOTYPES_PATH.exists():
        sources.append(f"WGS ({NEURODEV_GENOTYPES_PATH.name})")
    if NEURODEV_WIKI_RSIDS_PATH.exists():
        sources.append(f"WGS ({NEURODEV_WIKI_RSIDS_PATH.name})")
    if wgs_raw:
        sources.append(f"WGS ({wgs_raw.name})")
    if MH_PATH.exists():
        sources.append("MyHeritage (build 37)")

    out: list[str] = [
        "# Raport osobisty — geny i warianty (GENMARKERWIKI)",
        "",
        f"**Data:** {date.today().isoformat()}  ",
        f"**Źródła genotypów:** {' + '.join(sources)}  ",
        "**Opisy kliniczne:** włączone w niniejszy raport (profil, mechanizm, warianty, zalecenia)",
        "",
        "## Podsumowanie",
        "",
        f"| Metryka | Wartość |",
        f"|--------|---------|",
        f"| Genów w panelu | {len(genes)} |",
        f"| Markerów (rsID) w panelu | {marker_total} |",
        f"| Markerów z Twoim genotypem | {known_total} |",
        f"| Bez danych genotypowych | {marker_total - known_total} |",
        "",
        "> Raport ma charakter informacyjny. Nie zastępuje konsultacji lekarskiej ani genetyka klinicznego.",
        "",
        "---",
        "",
    ]

    # Group by theme
    themes = load_gene_categories()

    out.append("## Spis genów w raporcie\n")
    for gene in genes:
        n_known = sum(1 for e in by_gene[gene] if e["genotype"])
        n_all = len(by_gene[gene])
        out.append(f"- **{gene}** — {gene_label(gene, by_gene[gene])} ({n_known}/{n_all} markerów z genotypem)")
    out.append("\n---\n")

    for theme, gene_list in themes.items():
        out.append(f"# {theme}\n")
        for gene in gene_list:
            if gene not in by_gene:
                continue
            md_path = MD_DIR / f"{gene}.md"
            md_text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
            out.append(build_gene_section(gene, by_gene[gene], md_text))
            out.append("---\n")

    missing = marker_total - known_total
    out.append("# Uwagi\n")
    out.append(
        f"**{missing} markerów** z panelu ({marker_total} łącznie) bez genotypemu w dostępnych "
        "źródłach (CSV/WGS query/MyHeritage).\n"
    )
    out.append(
        "Genotypy bez dopasowanego wiersza w tabeli (allel referencyjny, inna orientacja nici) "
        "są w sekcjach „Twoje warianty” przy danym genie.\n"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Zapisano: {OUT}")
    print(f"Genów: {len(genes)}, genotypów: {known_total}/{marker_total}")

    try:
        from report_html import convert_md_to_html

        convert_md_to_html(OUT, ROOT / "raporty" / "Raport-osobisty-genom-wiki.html")
    except Exception as exc:
        print(f"Uwaga: HTML nie wygenerowany ({exc})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Raport osobisty i synchronizacja ★ z WGS")
    parser.add_argument(
        "--sync-stars",
        action="store_true",
        help="Tylko synchronizacja ★ w md/*.md (bez raportu)",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Tylko raport MD/HTML (bez zmiany gwiazdek)",
    )
    args = parser.parse_args()
    if args.sync_stars and args.report_only:
        print("Użyj co najwyżej jednej flagi: --sync-stars lub --report-only", file=sys.stderr)
        sys.exit(1)
    by_gene = load_markers()
    if not args.report_only:
        sync_stars_to_md(by_gene)
        try:
            import importlib.util

            spec = importlib.util.spec_from_file_location(
                "build_personal_gene_profiles_js",
                ROOT / "scripts" / "build_personal_gene_profiles_js.py",
            )
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                mod.main()
        except Exception as exc:
            print(f"Uwaga: personal-gene-profiles.js — {exc}", file=sys.stderr)
    if not args.sync_stars:
        main(by_gene)
