#!/usr/bin/env python3
"""Generate personal variant report from wybrane_markery.csv + MyHeritage + md/*.md."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
OUT = ROOT / "raporty" / "Raport-osobisty-genom-wiki.md"

CSV_PATH = Path(
    r"C:\Users\kacpe\Documents\.PERSONALNA BAZA DANYCH"
    r"\01_zdrowie\03_genetyka\wybrane_markery.csv"
)
MH_PATH = Path(
    r"C:\Users\kacpe\Documents\.PERSONALNA BAZA DANYCH"
    r"\01_zdrowie\03_genetyka\01_surowe_dane\myheritage_raw_dna_data.csv"
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


def load_markers() -> dict[str, list[dict]]:
    rows: list[dict] = []
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    needed = {r["rsid"].strip().lower() for r in rows if r["rsid"].strip()}
    mh = load_myheritage(needed)
    by_gene: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        gene = row["Gen"].strip()
        rsid = row["rsid"].strip()
        gt = row.get("genotype", "").strip() or mh.get(rsid.lower(), "")
        by_gene[gene].append(
            {
                "rsid": rsid,
                "opis": row["Opis"].strip(),
                "genotype": gt,
                "source": "CSV" if row.get("genotype", "").strip() else ("MyHeritage" if gt else ""),
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
        r"alt/alt|ref/ref|ref/alt|C/alt|CC/C|Gc[\w/]+|Ins/Del|Del/Ins|"
        r"wt/wt|L/L|S/S|major|minor)"
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
        add(strip_md(bold).split("(")[0])
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
        m = re.match(r"^\*\*(?:★\s*)?(rs\d+)", line)
        if m:
            flush()
            current_rsid = m.group(1)
            current_lines = [line]
            continue
        if not current_rsid and (line.strip().startswith("|") or not line.strip()):
            intro += line + "\n"
        elif current_rsid:
            current_lines.append(line)
    flush()
    if not blocks and "|" in sec4:
        blocks.append(("", sec4))
    return intro, blocks


def block_for_rsid(
    rsid: str, blocks: list[tuple[str, str]], sec4: str, intro: str = ""
) -> str:
    for brsid, block in blocks:
        if brsid == rsid or block.lstrip().startswith(f"**{rsid}"):
            return block
    if intro and rsid in intro and "|" in intro:
        return intro
    for brsid, block in blocks:
        if rsid in brsid or rsid in block:
            return block
    if len(blocks) == 1 and not blocks[0][0]:
        return blocks[0][1]
    return sec4


def match_row(gene: str, rsid: str, gt: str, block: str) -> dict | None:
    if rsid == "rs4588" and "rs7041" in block:
        return match_gc_diplotype(gt, block)
    if gene == "APOE" and rsid in ("rs429358", "rs7412") and "rs7412" in block:
        return None  # handled as pair
    targets = genotype_targets(gene, rsid, gt)
    for row in parse_table_block(block):
        if row["keys"] & targets:
            return row
    return None


def match_gc_diplotype(gt7041: str, block: str) -> dict | None:
    # caller passes single gt; pair handled in main
    return None


def match_apoe(rs358: str, rs412: str, block: str) -> dict | None:
    t1 = genotype_targets("APOE", "rs429358", rs358)
    t2 = genotype_targets("APOE", "rs7412", rs412)
    for row in parse_table_block(block):
        if len(row["cols"]) < 3:
            continue
        k1, k2 = row_keys(row["cols"][0]), row_keys(row["cols"][1])
        if (k1 & t1) and (k2 & t2):
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
        lines.append("_Brak potwierdzonych genotypów w bazie/MyHeritage dla tego genu._")
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
            row = match_row(gene, rsid, entry["genotype"], block)
            m = re.search(rf"\*\*(?:★\s*)?{re.escape(rsid)}[^*]*\*\*", block)
            block_title = strip_md(m.group(0)) if m else (
                main_rsid if rsid == main_rsid else rsid
            )
            lines.append(f"#### {rsid}")
            if block_title and block_title != rsid:
                lines.append(f"_{block_title}_\n")
            lines.append(f"- **Genotyp (baza/MyHeritage):** `{entry['genotype']}`")
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
                lines.append(
                    "- _Brak dopasowania wiersza w tabeli wariantów "
                    "(różna orientacja nici lub allel referencyjny)._"
                )
            lines.append("")

    if unknown:
        lines.append("### Markery w panelu bez genotypu w Twoich danych")
        for e in unknown:
            lines.append(f"- `{e['rsid']}` — brak wpisu w CSV/MyHeritage (chip GSA może nie raportować SNP)")
        lines.append("")

    if sec6:
        lines.append("### Zalecenia praktyczne")
        for b in extract_bullets(sec6)[:12]:
            if "ostrzeg" not in b.lower() and "pmid" not in b.lower():
                lines.append(f"- {b}")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    by_gene = load_markers()
    genes = sorted(by_gene.keys())

    known_total = sum(1 for g in genes for e in by_gene[g] if e["genotype"])
    marker_total = sum(len(by_gene[g]) for g in genes)

    out: list[str] = [
        "# Raport osobisty — geny i warianty (GENMARKERWIKI)",
        "",
        f"**Data:** {date.today().isoformat()}  ",
        "**Źródła genotypów:** panel wybranych markerów (CSV) + uzupełnienie z surowych danych MyHeritage (build 37)  ",
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
    themes = {
        "Mózg, nastrój, stres i uwaga": [
            "COMT", "BDNF", "DRD2", "ANKK1", "MAOA", "SLC6A4", "TPH2", "OXTR",
            "FKBP5", "ANK3", "ADRA2A", "CACNA1C", "DBH", "APOE",
        ],
        "Metabolizm, dieta i substancje": [
            "ALDH2", "CYP1A2", "LCT", "FTO", "GC", "MTHFR", "TAS2R38", "CHRNA5",
        ],
        "Wygląd, pigmentacja i sensoryka": [
            "HERC2", "OCA2", "SLC45A2", "SLC24A4", "MC1R", "OR6A2", "OR2M", "ABCC11",
        ],
        "Serce, naczynia i hormony": ["CDH13", "ZEB2", "AR", "CLOCK"],
        "Inne": ["ACTN3"],
    }

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

    out.append("# Uwagi i warianty bez automatycznego dopasowania\n")
    out.append(
        "Poniższe genotypy są w Twoich danych, ale nie mają osobnego wiersza w tabeli wariantów "
        "(allely referencyjne, inna orientacja nici):\n"
    )
    notes = [
        ("MAOA", "rs72554632", "CC", "W tabeli opisano tylko nosiciela allelu patogenicznego (T); CC = genotyp referencyjny (brak Gln296Ter)."),
        ("FKBP5", "rs3800373", "CA", "Chip raportuje CA; tabela wariantów używa notacji C/alt lub C/A (inna orientacja nici)."),
        ("TAS2R38", "rs1726866", "GG", "Chip raportuje GG; tabela używa C/C, C/T, T/T — funkcjonalnie haplotyp z rs713598 G/G i rs10246939 wskazuje supersmakosza."),
        ("MC1R", "rs1805005", "GG", "Val60Leu — GG zwykle odpowiada allelowi referencyjnemu (brak słabego allelu „r”)."),
        ("ABCC11", "rs17822931", "CC", "Gly180Arg — CC = brak wariantu (woskowa wydzielina, nie suchy typ)."),
        ("ABCC11", "rs17822471", "GG", "Gly546Val — GG = referencja w kontekście MRP8/5-FU."),
    ]
    for gene, rsid, gt, note in notes:
        out.append(f"- **{gene}** `{rsid}` **{gt}** — {note}")
    out.append(
        "\n**26 markerów** z panelu nadal bez genotypemu w CSV ani MyHeritage "
        "(m.in. APOE rs429358/rs7412, FTO, MTHFR rs1801133, ACTN3) — chip GSA nie pokrywa wszystkich SNP.\n"
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
    main()
