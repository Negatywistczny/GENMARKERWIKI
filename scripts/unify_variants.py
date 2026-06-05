#!/usr/bin/env python3
"""Ujednolicenie nagłówków i oznaczeń w sekcji 4 kart md/*.md (bez usuwania treści)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
SKIP = {"UNIWERSALNY_SZABLON_MARKERA.md"}

STD_HEADER = "| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy (kliniczny i funkcjonalny) |"
STD_SEP = "| :--- | :--- | :--- |"

HEADER_MAP: dict[tuple[str, ...], str] = {
    ("Genotyp", "Fenotyp sensoryczny", "Aktywność receptora i przekaźnictwo"): "swap_23",
    ("Genotyp", "Percepcja sensoryczna", "Aktywność receptora"): "swap_23",
}

# Nagłówki bloków rs bez opisu → uzupełnienie (em dash)
BLOCK_ENRICH: dict[str, str] = {
    "rs671": "rs671 (Glu504Lys — azjatycki rumieniec alkoholowy)",
    "rs6265": "rs6265 (Val66Met — sekrecja BDNF)",
    "rs762551": "rs762551 (*1F/*1A — metabolizm kofeiny)",
    "rs9939609": "rs9939609 (intron 1 — enhancer IRX3/IRX5)",
    "rs1801260": "rs1801260 (3'UTR — rytm dobowy CLOCK)",
    "rs4570625": "rs4570625 (promotor — synteza serotoniny TPH2)",
    "rs2519152": "rs2519152 (farmakogenomika atomoksetyny / ADHD)",
    "rs129882": "rs129882 (ekspresja DBH — Parkinson)",
    "rs9470080": "rs9470080 (PTSD + depresja — oś HPA)",
    "rs11646213": "rs11646213 (CDH13 — metabolizm / NSCLC)",
    "rs1815739": "rs1815739 (R577X — włókna szybkokurczliwe)",
}

# Zamiany w kolumnie aktywności (środkowa); zachowują szczegóły w nawiasach
MID_REPLACEMENTS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\| Pośredni \|"), "| Pośrednia |"),
    (re.compile(r"\| Referencyjny \|"), "| Referencyjna |"),
    (re.compile(r"\| Obniżony \|"), "| Obniżona |"),
    (re.compile(r"\| Podwyższony \|"), "| Podwyższona |"),
    (re.compile(r"\| Standardowy \|"), "| Standardowa |"),
    (re.compile(r"\| Alternatywny \|"), "| Alternatywna |"),
    (re.compile(r"\| Pośrednio obniżony \|"), "| Pośrednia (obniżona) |"),
    (re.compile(r"\| Pośrednio obniżona \|"), "| Pośrednia (obniżona) |"),
    (re.compile(r"\| Umiarkowanie obniżony \|"), "| Pośrednia (obniżona) |"),
    (re.compile(r"\| Umiarkowanie obniżona \|"), "| Pośrednia (obniżona) |"),
    (re.compile(r"\| Referencyjny \(major\) \|"), "| Referencyjna (major) |"),
    (re.compile(r"\| Referencyjny \(globalny\) \|"), "| Referencyjna (globalna) |"),
    (re.compile(r"\| Referencyjny \(~71% EUR\) \|"), "| Referencyjna (~71% EUR) |"),
    (re.compile(r"\| Referencyjny w haplotypie \|"), "| Referencyjna (w haplotypie) |"),
    (re.compile(r"\| Referencyjny w haplotypie ochronnym \|"), "| Referencyjna (w haplotypie ochronnym) |"),
    (re.compile(r"\| Standardowy DBH \|"), "| Standardowa (DBH) |"),
    (re.compile(r"\| Standardowy promotor \|"), "| Standardowa (promotor) |"),
    (re.compile(r"\| Profil referencyjny \|"), "| Referencyjna (profil referencyjny) |"),
    (re.compile(r"\| Pośredni profil CAG i PSA \|"), "| Pośrednia (profil CAG i PSA) |"),
    (re.compile(r"\| Alternatywny haplotyp \|"), "| Alternatywna (haplotyp) |"),
]

BLOCK_TITLE = re.compile(r"^(\*\*(?:★\s*)?)(rs\d+[^*]*)(\*\*)\s*$", re.M)


def normalize_block_titles(sec4: str) -> str:
    def repl(m: re.Match[str]) -> str:
        body = m.group(2).strip()
        rs_m = re.match(r"(rs\d+)", body)
        if rs_m and body == rs_m.group(1) and rs_m.group(1) in BLOCK_ENRICH:
            body = BLOCK_ENRICH[rs_m.group(1)]
        body = re.sub(r" - ", " — ", body)
        return f"{m.group(1)}{body}{m.group(3)}"

    return BLOCK_TITLE.sub(repl, sec4)


def normalize_mid_column(line: str) -> str:
    for pat, repl in MID_REPLACEMENTS:
        line = pat.sub(repl, line)
    return line


def parse_table_row(line: str) -> list[str] | None:
    if not line.strip().startswith("|") or ":---" in line:
        return None
    return [c.strip() for c in line.split("|")[1:-1]]


def is_header_row(cells: list[str]) -> bool:
    return bool(cells) and cells[0].lower().startswith("genotyp")


def standardize_section4(sec4: str) -> tuple[str, int]:
    lines = sec4.splitlines()
    out: list[str] = []
    changes = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        cells = parse_table_row(line)
        if cells and is_header_row(cells) and len(cells) == 3:
            key = tuple(cells)
            action = HEADER_MAP.get(key)
            if action == "swap_23":
                changes += 1
                out.append(STD_HEADER)
                i += 1
                if i < len(lines) and ":---" in lines[i]:
                    out.append(STD_SEP)
                    i += 1
                while i < len(lines):
                    row = parse_table_row(lines[i])
                    if not row or len(row) != 3:
                        break
                    if ":---" in lines[i]:
                        i += 1
                        continue
                    out.append(normalize_mid_column(f"| {row[0]} | {row[2]} | {row[1]} |"))
                    i += 1
                continue
            if key != ("Genotyp", "Aktywność / ekspresja", "Wpływ fenotypowy (kliniczny i funkcjonalny)"):
                changes += 1
            out.append(STD_HEADER)
            i += 1
            if i < len(lines) and ":---" in lines[i]:
                out.append(STD_SEP)
                i += 1
            while i < len(lines):
                row_line = lines[i]
                row = parse_table_row(row_line)
                if not row or len(row) != 3:
                    break
                if ":---" in row_line:
                    i += 1
                    continue
                out.append(normalize_mid_column(f"| {row[0]} | {row[1]} | {row[2]} |"))
                i += 1
            continue
        out.append(normalize_mid_column(line))
        i += 1
    return "\n".join(out), changes


def fix_oxtr(sec4: str) -> tuple[str, int]:
    if "Udokumentowany Wpływ na Fenotyp" not in sec4:
        return sec4, 0
    sec4 = sec4.replace(
        "**rs53576**",
        "**rs53576 (3'-UTR — receptor oksytocyny)**",
    )
    sec4 = sec4.replace(
        "| Genotyp rs53576 | Oznaczenie Alleliczne | Udokumentowany Wpływ na Fenotyp, Kognicję i Biochemię |",
        STD_HEADER,
    )
    return sec4, 1


def fix_lct(sec4: str) -> tuple[str, int]:
    old_h = (
        "| Genotyp rs4988235 (Zapis Nici) | Fenotyp i Aktywność Enzymatyczna "
        "| Opis Wpływu i Skutki Kliniczne |"
    )
    if old_h not in sec4:
        return sec4, 0
    return sec4.replace(old_h, STD_HEADER), 1


def fix_chrna5_block_title(sec4: str) -> tuple[str, int]:
    if "**rs1051730**" not in sec4:
        return sec4, 0
    sec4 = sec4.replace("**rs1051730**", "**rs16969968 (D398N — α5 nAChR)**")
    sec4 = sec4.replace(
        "| Genotyp rs16969968 | Funkcja receptora (kinetyka i Ca²⁺) | "
        "Wpływ fenotypowy (behawioralny i patologia) |",
        STD_HEADER,
    )
    return sec4, 1


def repair_glued_section_headers(text: str) -> str:
    return re.sub(r"(\|)\s*(### \d+\.)", r"\1\n\2", text)


def process_file(path: Path) -> int:
    text = repair_glued_section_headers(path.read_text(encoding="utf-8"))
    m = re.search(r"(### 4\.[^\n]*\n)([\s\S]*?)(?=^### 5\.|\Z)", text, re.M)
    if not m:
        return 0
    sec4 = m.group(2)
    changes = 0

    for fixer in (fix_oxtr, fix_lct, fix_chrna5_block_title):
        sec4, n = fixer(sec4)
        changes += n

    old = sec4
    sec4 = normalize_block_titles(sec4)
    if sec4 != old:
        changes += 1

    sec4, n = standardize_section4(sec4)
    changes += n

    tail = text[m.end(2) :]
    if tail and not sec4.endswith("\n"):
        sec4 = sec4.rstrip("\n") + "\n"
    new_text = text[: m.start(2)] + sec4 + tail
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return changes


def main() -> None:
    total = 0
    for path in sorted(MD_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        n = process_file(path)
        if n:
            print(f"{path.stem}: {n}")
            total += n
    print(f"Łącznie: {total} zmian")


if __name__ == "__main__":
    main()
