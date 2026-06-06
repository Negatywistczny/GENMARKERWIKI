#!/usr/bin/env python3
"""Ujednolicenie struktury kart md/*.md (odstępy, tabele 3-kol., sekcje 2/6/8)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
SKIP = {"UNIWERSALNY_SZABLON_MARKERA.md"}

STD_HEADER = "| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy (kliniczny i funkcjonalny) |"
STD_SEP = "| :--- | :--- | :--- |"

MISSING_TITLES: dict[str, str] = {
    "APOE": "**rs429358 + rs7412 (haplotyp ε2/ε3/ε4)**",
    "MAOA": "**MAOA-uVNTR (promotor — aktywność MAOA-L/H)**",
    "SLC6A4": "**5-HTTLPR / rs4795541 (transporter serotoniny)**",
    "TAS2R38": "**rs713598 (PAV/NAV/AVI — gorycz PROP)**",
}

COL1_RENAMES = [
    (re.compile(r"^\| Genotyp \(DNA\)", re.I), "| Genotyp"),
    (re.compile(r"^\| Genotyp rs\d+", re.I), "| Genotyp"),
    (re.compile(r"^\| Genotyp współczesny", re.I), "| Genotyp"),
    (re.compile(r"^\| Wariant \(VNTR\)", re.I), "| Genotyp"),
    (re.compile(r"^\| Haplotyp / genotyp", re.I), "| Genotyp"),
    (re.compile(r"^\| Haplotyp \(diplotyp\)", re.I), "| Genotyp"),
    (re.compile(r"^\| Haplotyp \(uproszczony\)", re.I), "| Genotyp"),
    (re.compile(r"^\| Genotyp rs713598 \(Diplotyp\)", re.I), "| Genotyp"),
]

# Eriksson 2012 GWAS kolendra
ERIKSSON_PMID = "22962365"


def repair_glued_section_headers(text: str) -> str:
    return re.sub(r"(\|)\s*(### \d+\.)", r"\1\n\2", text)


MAX_COL2_LEN = 85

def join_cells(parts: list[str]) -> str:
    return "; ".join(p.strip() for p in parts if p.strip())


def abbrev_header(header: str) -> str:
    h = header.strip().lower()
    rules: list[tuple[str, str]] = [
        (r"deskrypcja fenotyp", "Fenotyp"),
        (r"behawioraln", "Profil behawioralny"),
        (r"charakterystyka neuro|neurobiolog.*kognicj", "Neurobiologia / kognicja"),
        (r"somatyczne|metaboliczne|korelaty somat", "Korelaty somatyczne"),
        (r"demetyl|ekspresja tkankowa", "Ekspresja tkankowa"),
        (r"ryzyko zdrowotne|fenotyp i ryzyko", "Ryzyko zdrowotne"),
        (r"kognicj", "Neurobiologia / kognicja"),
        (r"ekspresja i aktywność|aktywność comt", "Mechanizm enzymatyczny"),
        (r"jamie ustnej|wapń i atp", "Aktywność receptora"),
        (r"immunologiczny i metaboliczny", "Fenotyp immunologiczny"),
        (r"profil neurochemiczny", "Profil neurochemiczny"),
        (r"pigmentacj|fenotyp fizyczny", "Pigmentacja"),
        (r"nocycepcj|opioid", "Nocycepcja"),
        (r"izoforma|aminokwas", "Haplotyp / aminokwasy"),
        (r"wpływ fenotyp|dogłębny wpływ", "Wpływ fenotypowy"),
        (r"zapis historyczny", "Zapis historyczny"),
        (r"fenotyp, budowa|wydolność", "Fenotyp / wydolność"),
        (r"zapis rflp|taq1", "RFLP / ekspresja"),
    ]
    for pattern, label in rules:
        if re.search(pattern, h):
            return label
    short = header.split("(")[0].strip()
    if len(short) > 42:
        short = short[:39] + "…"
    return short


def labeled_section(header: str, content: str) -> str:
    content = content.strip()
    if not content:
        return ""
    label = abbrev_header(header)
    if re.match(rf"^\*\*{re.escape(label)}", content, re.I):
        return content
    return f"**{label}:** {content}"


def join_col3_sections(headers: list[str], indices: list[int], cells: list[str]) -> str:
    parts: list[str] = []
    for i in indices:
        if i < len(cells) and cells[i].strip():
            parts.append(labeled_section(headers[i], cells[i]))
    return "<br><br>".join(parts)


def restructure_col3(col3: str) -> str:
    """Rozbij ścianę tekstu w col3 na sekcje z etykietami (jak oryginalne kolumny)."""
    col3 = col3.strip()
    if not col3 or "<br>" in col3.lower():
        return col3
    if re.match(r"^\*\*[^*]+\*\*[^:]", col3) and ";" not in col3:
        return col3
    if len(col3) < 200:
        return col3
    parts = [p.strip() for p in col3.split(";") if p.strip()]
    if len(parts) < 2:
        return col3
    if all(len(p) < 35 for p in parts):
        return col3
    sections = list(parts)
    if not any(re.match(r"^\*\*[^*]+:\*\*", s) for s in sections):
        default_labels = [
            "Mechanizm / ekspresja",
            "Profil funkcjonalny",
            "Fenotyp kliniczny",
            "Dodatkowe korelaty",
        ]
        sections = [
            f"**{default_labels[min(i, len(default_labels) - 1)]}:** {s}"
            for i, s in enumerate(sections)
        ]
    return "<br><br>".join(sections)


def short_activity_label(text: str) -> tuple[str, str]:
    """Wydziel wyłącznie bold-etykietę aktywności (np. **Bardzo wysoka.**); reszta → col3."""
    text = text.strip()
    m = re.match(r"^(\*\*[^*]+\*\*\.?)\s*(.*)$", text, re.DOTALL)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "", text


def is_apoe_col2_fragment(part: str) -> bool:
    return bool(
        re.search(r"Cys\d+|Arg\d+|Mieszane \(Cys", part, re.I)
        or "ε" in part
    )


def is_secondary_activity_label(part: str) -> bool:
    """Drugi fragment col2 — wyłącznie krótka etykieta poziomu aktywności."""
    part = part.strip()
    if is_apoe_col2_fragment(part):
        return True
    if re.fullmatch(r"\*\*[^*]+\*\*\.?", part):
        return True
    if re.search(r"\d+%", part):
        return True
    return len(part) <= 30 and is_short_activity_fragment(part)


def is_short_activity_fragment(part: str) -> bool:
    """Czy fragment to krótka etykieta aktywności (nie opis szczegółowy)."""
    part = part.strip()
    if re.fullmatch(r"\*\*[^*]+\*\*\.?", part):
        return True
    if re.search(r"\d+%", part) and len(part) <= 55:
        return True
    if len(part) <= 45 and re.search(
        r"optymaln|obniżon|wysoka|niska|pośredni|referencyj|pełna|skrajnie|"
        r"nominalna|całkowit|deficyt|mieszan|dziki|mutacj|taster|smakosz|"
        r"non-taster|wojownik|zamartwiacz|val/val|met/met",
        part,
        re.I,
    ):
        return True
    return False


def repair_col2_brevity(col2: str, col3: str) -> tuple[str, str]:
    """Col2 = krótki opis aktywności; nadmiar → col3."""
    parts = [p.strip() for p in col2.split(";") if p.strip()]
    if not parts:
        return col2, col3

    if len(parts) == 1:
        if len(parts[0]) <= MAX_COL2_LEN:
            return col2, col3
        short, rest = short_activity_label(parts[0])
        if short:
            return short, join_cells([rest, col3])
        cut = parts[0][:MAX_COL2_LEN].rsplit(" ", 1)[0]
        return cut, join_cells([parts[0][len(cut) :].strip(), col3])

    kept = [parts[0]]
    overflow: list[str] = []
    for part in parts[1:]:
        if len(kept) >= 2:
            overflow.append(part)
            continue
        if is_secondary_activity_label(part) and len(join_cells(kept + [part])) <= MAX_COL2_LEN:
            kept.append(part)
            continue
        short, rest = short_activity_label(part)
        if short and len(kept) < 2 and len(join_cells(kept + [short])) <= MAX_COL2_LEN:
            kept.append(short)
            if rest:
                overflow.append(rest)
        else:
            overflow.append(part)

    new_col2 = join_cells(kept)
    overflow_text = join_cells(overflow)
    if overflow_text:
        new_col3 = f"{overflow_text}<br><br>{col3}" if col3.strip() else overflow_text
    else:
        new_col3 = col3
    return new_col2, new_col3


def orphan_col3_label(gene: str, chunk: str, idx: int) -> str:
    cl = chunk.lower()
    if gene == "DRD2" and idx == 0:
        return "Gęstość D2"
    if gene == "DRD2":
        return "Profil behawioralny"
    if gene == "AR" and "lyonizacji" in cl:
        return "Uwagi lyonizacji"
    if gene == "AR" and len(chunk) < 35 and "psa" in cl:
        return "Stężenie PSA"
    if gene == "ACTN3" and chunk.strip() == "Częściowa":
        return "Aktywność resztkowa"
    if idx == 0:
        return "Mechanizm / ekspresja"
    return "Wpływ fenotypowy"


def repair_col3_orphans(col3: str, gene: str = "") -> str:
    if "<br><br>" not in col3.lower():
        return col3
    chunks = [c.strip() for c in re.split(r"<br><br>", col3, flags=re.I) if c.strip()]
    if not chunks:
        return col3
    out: list[str] = []
    orphan_idx = 0
    for chunk in chunks:
        if re.match(r"^\*\*[^*]+:\*\*", chunk):
            out.append(chunk)
            continue
        label = orphan_col3_label(gene, chunk, orphan_idx)
        orphan_idx += 1
        out.append(f"**{label}:** {chunk}")
    return "<br><br>".join(out)


def trim_table_block_col2(block: list[str], gene: str = "") -> list[str]:
    if len(block) < 2:
        return block
    header = parse_table_row(block[0])
    if not header or len(header) != 3:
        return block
    out = block[:2]
    for line in block[2:]:
        cells = parse_table_row(line)
        if not cells or len(cells) != 3 or cells[0].lower().startswith("genotyp"):
            out.append(line)
            continue
        c2, c3 = repair_col2_brevity(cells[1], cells[2])
        c3 = repair_col3_orphans(c3, gene)
        out.append("| " + " | ".join([cells[0], c2, c3]) + " |")
    return out


def parse_table_row(line: str) -> list[str] | None:
    if not line.strip().startswith("|") or ":---" in line:
        return None
    return [c.strip() for c in line.split("|")[1:-1]]


def is_apoe_haplotype_table(headers: list[str]) -> bool:
    joined = " ".join(headers).lower()
    return "rs429358" in joined and "rs7412" in joined


def strip_gt_cell(cell: str) -> tuple[str, bool]:
    has_star = "★" in cell
    inner = re.sub(r"\*\*|★\s*", "", cell).strip()
    inner = re.sub(r"\s+", "", inner)
    return inner, has_star


def merge_row(headers: list[str], cells: list[str]) -> list[str]:
    n = len(cells)
    if n == 3 and tuple(headers) == (
        "Genotyp",
        "Aktywność / ekspresja",
        "Wpływ fenotypowy (kliniczny i funkcjonalny)",
    ):
        return cells
    if n == 3:
        h0 = headers[0].lower()
        if h0 != "genotyp" and not h0.startswith("genotyp"):
            return [cells[0], cells[1], cells[2]]
        return cells

    if n == 4:
        h = [x.lower() for x in headers]
        # COMT: allel + krótka aktywność | mechanizm + fenotyp (sekcje)
        if any("alleli" in x for x in h) and any(
            "ekspresja" in x or "aktywność" in x for x in h
        ):
            short, rest = short_activity_label(cells[2])
            col2 = join_cells([cells[1], short]) if short else cells[1]
            sections: list[str] = []
            if rest:
                sections.append(labeled_section(headers[2], rest))
            sections.append(labeled_section(headers[3], cells[3]))
            return [cells[0], col2, "<br><br>".join(sections)]
        # TAS2R38: status | aktywność + fenotyp (sekcje)
        if any("status" in x or "wrażliwo" in x for x in h):
            return [cells[0], cells[1], join_col3_sections(headers, [2, 3], cells)]
        # ACTN3: nomenklatura + ekspresja | fenotyp
        if any("nomenklatura" in x for x in h):
            return [cells[0], join_cells([cells[1], cells[2]]), cells[3]]
        # MC1R: aktywność | pigmentacja + nocycepcja
        if any("campa" in x or "receptora" in x for x in h[:2]):
            return [cells[0], cells[1], join_col3_sections(headers, [2, 3], cells)]
        # DBH: aktywność | profil + fenotyp
        if any("profil" in x for x in h):
            return [cells[0], cells[1], join_col3_sections(headers, [2, 3], cells)]
        # DRD2: RFLP + aktywność | fenotyp
        if any("rflp" in x or "taq1" in x for x in h):
            col2 = join_cells([cells[1], cells[2]])
            return [cells[0], col2, cells[3]]
        # CLOCK: genotyp współczesny | zapis historyczny | charakterystyka | wpływ
        if any("współczesny" in x for x in h) and any("historyczny" in x for x in h):
            col2 = cells[2].rstrip(".")
            return [cells[0], col2, join_col3_sections(headers, [1, 3], cells)]
        if "aktywność" in h[1] or "ekspresja" in h[1]:
            if any(
                k in headers[2].lower() + headers[3].lower()
                for k in ("pigment", "nocycepc", "fenotyp", "wpływ")
            ):
                return [cells[0], cells[1], join_col3_sections(headers, [2, 3], cells)]
        return [cells[0], cells[1], join_col3_sections(headers, list(range(2, n)), cells)]

    if n == 5 and is_apoe_haplotype_table(headers):
        g1, s1 = strip_gt_cell(cells[0])
        g2, s2 = strip_gt_cell(cells[1])
        star = "★ " if (s1 or s2) else ""
        geno = f"**{star}{g1} + {g2}**"
        return [geno, join_cells(cells[2:4]), cells[4]]

    if n == 5:
        h = [x.lower() for x in headers]
        # BDNF: status + poziom | neuro + somatyczne
        if any("sekrecj" in x or "poziom" in x for x in h):
            return [
                cells[0],
                join_cells([cells[1], cells[2]]),
                join_col3_sections(headers, [3, 4], cells),
            ]
        # FTO: status | ekspresja + behawior + ryzyko
        return [cells[0], cells[1], join_col3_sections(headers, [2, 3, 4], cells)]

    return cells


def merge_table_block(lines: list[str]) -> list[str]:
    if len(lines) < 2:
        return lines
    header_cells = parse_table_row(lines[0])
    if not header_cells or len(header_cells) < 3:
        return lines
    if len(header_cells) == 3 and lines[0].strip() == STD_HEADER.strip():
        return lines

    out = [STD_HEADER, STD_SEP]
    for line in lines[2:]:
        cells = parse_table_row(line)
        if not cells or len(cells) != len(header_cells):
            out.append(line)
            continue
        merged = merge_row(header_cells, cells)
        if len(merged) == 3:
            out.append("| " + " | ".join(merged) + " |")
        else:
            out.append(line)
    return out


def fix_col1_header(line: str) -> str:
    for pat, repl in COL1_RENAMES:
        if pat.match(line.strip()):
            return repl + line[line.index("|", 1) :]
    return line


def normalize_section4_spacing(sec4: str, gene: str = "") -> str:
    lines = sec4.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("**") and stripped.endswith("**"):
            if out and out[-1].strip():
                out.append("")
            out.append(line)
            i += 1
            if i < len(lines) and lines[i].strip().startswith("|"):
                out.append("")
            continue

        if stripped.startswith("|") and ":---" not in stripped:
            if (
                out
                and out[-1].strip()
                and not out[-1].strip().startswith("|")
                and not out[-1].strip().startswith("**")
            ):
                out.append("")
            block = [line]
            i += 1
            while i < len(lines) and (
                lines[i].strip().startswith("|")
                or (not lines[i].strip() and block)
            ):
                if lines[i].strip():
                    block.append(lines[i])
                i += 1
            while block and not block[-1].strip().startswith("|"):
                block.pop()
            if block:
                header = parse_table_row(block[0])
                if header and len(header) != 3:
                    block = merge_table_block(block)
                elif header and len(header) == 3:
                    block[0] = fix_col1_header(block[0])
                    h = parse_table_row(block[0]) or []
                    if h and (
                        h[0].lower().startswith("genotyp")
                        or h[0].lower().startswith("haplotyp")
                        or "genotypy rs" in h[1].lower()
                        or "ekspresja vdr" in h[1].lower()
                    ):
                        block[0] = STD_HEADER
                    block = trim_table_block_col2(block, gene)
                out.extend(block)
            if i < len(lines) and lines[i].strip().startswith("**"):
                out.append("")
            continue

        out.append(line)
        i += 1

    return "\n".join(out).rstrip("\n") + "\n"


def add_missing_titles(gene: str, sec4: str) -> str:
    title = MISSING_TITLES.get(gene)
    if not title:
        return sec4

    if gene == "APOE":
        old = "\n\n| rs429358 | rs7412 |"
        if title not in sec4 and old in sec4:
            return sec4.replace(old, f"\n\n{title}\n\n| rs429358 | rs7412 |", 1)
    if gene == "MAOA":
        old = "\n\n| Wariant (VNTR) |"
        if title not in sec4 and old in sec4:
            return sec4.replace(old, f"\n\n{title}\n\n| Wariant (VNTR) |", 1)
    if gene == "SLC6A4":
        old = "\n\n| Haplotyp / genotyp |"
        if title not in sec4 and old in sec4:
            return sec4.replace(old, f"\n\n{title}\n\n| Haplotyp / genotyp |", 1)
    if gene == "TAS2R38":
        old = "\n| Genotyp rs713598 (Diplotyp) |"
        if title not in sec4 and "Genotyp rs713598" in sec4:
            return sec4.replace(old, f"\n\n{title}\n\n| Genotyp rs713598 (Diplotyp) |", 1)
    if gene in ("MAOA", "SLC6A4") and title not in sec4:
        marker = "\n\n| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy"
        if marker in sec4:
            return sec4.replace(marker, f"\n\n{title}\n\n| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy", 1)
    return sec4


def fix_actn3_warning(text: str) -> str:
    if "* **Ostrzeżenie kliniczne:**" in text:
        return text
    marker = "### 6. Wpływ na życie (Zalecenia)"
    idx = text.find(marker)
    if idx < 0:
        return text
    sec6_end = text.find("### 7.", idx)
    if sec6_end < 0:
        return text
    sec6 = text[idx:sec6_end]
    insert = "\n* **Ostrzeżenie kliniczne:** Materiał ma charakter informacyjny i nie zastępuje konsultacji lekarskiej.\n"
    return text[:sec6_end].rstrip() + insert + text[sec6_end:]


def normalize_section2_labels(text: str) -> str:
    reps = [
        (
            "* **Główny marker:** MAOA-uVNTR (region promotorowy; brak pojedynczego rsID ze względu na charakter VNTR)",
            "* **Główny rsID:** MAOA-uVNTR (brak pojedynczego rsID — VNTR promotorowy)",
        ),
        (
            "* **Główny marker:** 5-HTTLPR (rs4795541) + rs25531 (A>G w regionie promotorowym)",
            "* **Główny rsID:** rs4795541 (5-HTTLPR) + rs25531 (promotor A>G)",
        ),
        (
            "* **Główne rsID (haplotyp):** rs429358 i rs7412",
            "* **Główny rsID:** rs429358 + rs7412 (haplotyp ε2/ε3/ε4)",
        ),
        (
            "* **Główne rsID (haplotyp):** rs713598, rs1726866, rs10246939",
            "* **Główny rsID:** rs713598 (+ rs1726866, rs10246939 — haplotyp PAV/AVI)",
        ),
        (
            "* **Główne rsID (panel):** rs1801133 (C677T, Ala222Val) oraz rs1801131 (A1298C, Glu429Ala)",
            "* **Główny rsID:** rs1801133 (+ rs1801131 — panel C677T/A1298C)",
        ),
        (
            "* **Główne rsID (panel):** rs1805007, rs1805008, rs1805009, rs2228479, rs1805005, rs885479",
            "* **Główny rsID:** rs1805007 (+ panel MC1R: rs1805008, rs1805009, rs2228479, rs1805005, rs885479)",
        ),
        (
            "* **Główny rsID (kodujący):** rs1800407",
            "* **Główny rsID:** rs1800407",
        ),
        (
            "* **Główny rsID (GWAS / kardiologia):** rs2252641",
            "* **Główny rsID:** rs2252641",
        ),
    ]
    for old, new in reps:
        text = text.replace(old, new)
    return text


def normalize_section8(text: str) -> str:
    sec8 = re.search(r"(### 8\. Źródła \(Referencje\)\n)([\s\S]*?)(\Z)", text)
    if not sec8:
        return text

    body = sec8.group(2)
    body = body.replace(
        "* **Eriksson et al. (2012)** – GWAS rs72921001, Flavour / arXiv:1209.2096.",
        f"* **PMID: {ERIKSSON_PMID}** (Eriksson et al., 2012) – GWAS rs72921001 i percepcja kolendry.",
    )
    # PMID bez autora — dodaj tylko gdy linia ma samo PMID: N –
    def add_author_if_missing(m: re.Match[str]) -> str:
        line = m.group(0)
        if "(" in line.split("–")[0].split("-")[0]:
            return line
        pmid = m.group(1)
        rest = m.group(2).strip()
        return f"* **PMID: {pmid}** – {rest}"

    body = re.sub(
        r"^\* \*\*PMID: (\d+)\*\* – (.+)$",
        add_author_if_missing,
        body,
        flags=re.M,
    )
    return text[: sec8.start(2)] + body + sec8.group(3)


def process_file(path: Path) -> bool:
    text = repair_glued_section_headers(path.read_text(encoding="utf-8"))
    gene = path.stem.upper()

    m4 = re.search(
        r"(### 4\. Tabela Wariantów\n)([\s\S]*?)(?=^### 5\.|\Z)",
        text,
        re.M,
    )
    if m4:
        sec4 = m4.group(2)
        sec4 = add_missing_titles(gene, sec4)
        sec4 = normalize_section4_spacing(sec4, gene)
        if not sec4.endswith("\n\n"):
            sec4 = sec4.rstrip("\n") + "\n\n"
        text = text[: m4.start(2)] + sec4 + text[m4.end(2) :]

    if gene == "ACTN3":
        text = fix_actn3_warning(text)

    text = normalize_section2_labels(text)
    text = normalize_section8(text)

    original = path.read_text(encoding="utf-8")
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(MD_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        if process_file(path):
            print(path.stem)
            changed += 1
    print(f"Zaktualizowano: {changed} kart")


if __name__ == "__main__":
    main()
