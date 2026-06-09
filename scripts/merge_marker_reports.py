#!/usr/bin/env python3
"""Scala Zbiorowe badanie markerów1-6.md w jeden uporządkowany plik."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER_DIR = ROOT / "raporty" / "markery"
SOURCES = [MARKER_DIR / f"Zbiorowe badanie markerów{i}.md" for i in range(1, 7)]
OUT = MARKER_DIR / "Zbiorowe badanie markerów.md"

# Kolejność sekcji tematycznych (gen → id sekcji)
SECTIONS: list[tuple[str, str]] = [
    ("I", "Neurorozwój syndromiczny, chromatyna i geny o wysokiej penetracji"),
    ("II", "Szlaki monoaminergiczne — transportery i receptory"),
    ("III", "Glutaminian, GABA i plastyczność synaptyczna"),
    ("IV", "Receptory cholinergiczne, kanabinoidowe i histaminowe"),
    ("V", "Neurorozwój poligenowy — GWAS, TWAS i architektura mózgu"),
    ("VI", "Neuroimmunologia, HLA i zapalenie OUN"),
    ("VII", "Oś stresu (HPA), hormony i modulatory behawioralne"),
    ("VIII", "Kanały jonowe i homeostaza elektrofizjologiczna"),
    ("IX", "Adhezja, migracja neuronów i architektura synaptyczna"),
    ("X", "Czynniki transkrypcyjne i cytoarchitektura kory"),
    ("XI", "Modyfikacje RNA, translacja i epigenetyka enzymatyczna"),
    ("XII", "Foliany, metylacja i szlaki metaboliczne"),
    ("XIII", "Farmakogenetyka, detoksykacja i bariera krew–mózg"),
    ("XIV", "Transportery, lizosomy, naprawa DNA i markery strukturalne"),
    ("XV", "Tau, pamięć epizodyczna i starzenie neuronalne"),
]

GENE_SECTION: dict[str, str] = {
    # I — syndromiczne
    "ANK2": "I", "ARID1B": "I", "CHD8": "I", "DYRK1A": "I", "GRIN2B": "I",
    "PTEN": "I", "UBE3A": "I", "TCF4": "I", "KMT2D": "I",
    # II — monoamina
    "SLC6A3": "II", "SLC6A2": "II", "DRD4": "II", "DRD5": "II",
    "HTR1B": "II", "HTR2A": "II", "HTR4": "II", "HTR6": "II",
    # III — glutaminian/GABA
    "GRIN2A": "III", "GRM3": "III", "GRM5": "III", "GRIA2": "III",
    "GABBR2": "III", "SLC12A5": "III", "GADL1": "III",
    # IV — cholinergiczny itd.
    "CHRNA4": "IV", "CHRNA7": "IV", "CHRNA2": "IV",
    "CNR1": "IV", "HRH3": "IV", "MCHR1": "IV",
    # V — GWAS neurorozwój
    "ADGRL3": "V", "AKAP11": "V", "FOXP2": "V", "TRANK1": "V",
    "XRN2": "V", "NKX2-4": "V", "MSRA": "V", "SOX7": "V", "ZSWIM6": "V",
    "MACROD2": "V", "AKT3": "V", "ASTN2": "V", "ATP2A2": "V",
    "BCL11B": "V", "MEIS1": "V", "NKX2-2": "V", "RORB": "V",
    "SORCS3": "V", "DUSP6": "V", "ARTN": "V", "MDFIC": "V", "MED8": "V",
    "MPL": "V", "NEK4": "V", "SESTD1": "V", "ST3GAL3": "V",
    "STX16-NPEPL1": "V", "LINC01795": "V", "POU3F2": "V",
    # VI — immunologia
    "C4A": "VI", "IDO1": "VI", "KMO": "VI", "IL6": "VI", "TNFA": "VI",
    "CRP": "VI", "TDO2": "VI", "HLA-B": "VI", "HLA-DQB1": "VI",
    "HLA-DRB1": "VI", "MICA": "VI", "C1R": "VI",
    # VII — HPA / hormony
    "NR3C1": "VII", "NR3C2": "VII", "CRHR1": "VII", "GPR151": "VII",
    # VIII — kanały
    "KCNN2": "VIII", "CACNB2": "VIII", "HCN1": "VIII", "KCNQ3": "VIII",
    # IX — adhezja / synapsy
    "THSD7A": "IX", "CSMD1": "IX", "DCC": "IX", "NCAN": "IX",
    "PCDHG": "IX", "RET": "IX", "NEGR1": "IX", "TIE1": "IX",
    "PTPRE": "IX", "PTPRF": "IX", "NCAM1": "IX", "RIMS1": "IX",
    "SHISA9": "IX", "FURIN": "IX",
    # X — transkrypcja
    "GSK3B": "X", "PDE4B": "X",
    # XI — RNA
    "NSUN2": "XI", "NSUN6": "XI", "TRMT61A": "XI", "TYW5": "XI",
    "QTRT1": "XI", "LSM6": "XI", "RPS26": "XI",
    # XII — foliany
    "DHFR": "XII", "CBS": "XII", "MC4R": "XII",
    # XIII — farmako
    "ABCB1": "XIII", "CYP2B6": "XIII", "ABCB6": "XIII", "CYP3A4": "XIII",
    # XIV — transportery / strukturalne
    "SLC4A1": "XIV", "TMEM140": "XIV", "NAGA": "XIV", "ALMS1": "XIV",
    "CYREN": "XIV", "PROZ": "XIV", "USP35": "XIV", "GOLPH3L": "XIV",
    # XV — tau / starzenie
    "MAPT": "XV",
}

ALIASES = {
    "DAT1": "SLC6A3",
    "NET": "SLC6A2",
    "LPHN3": "ADGRL3",
    "MDR1": "ABCB1",
    "KCC2": "SLC12A5",
    "BRN2": "POU3F2",
    "TNF": "TNFA",
}


def canonical_gene(heading: str) -> str | None:
    raw = heading.strip()
    raw = re.sub(r"\s*\(.*$", "", raw).strip()
    raw = raw.split("/")[0].strip()
    if raw.upper().startswith("STX16"):
        return "STX16-NPEPL1"
    if raw.upper().startswith("PCDHG"):
        return "PCDHG"
    sym = raw.upper()
    return ALIASES.get(sym, sym)


def split_gene_blocks(text: str) -> list[tuple[str, str]]:
    """Zwraca [(symbol, treść sekcji bez nagłówka ##/###)]."""
    lines = text.splitlines()
    blocks: list[tuple[str, str]] = []
    current_sym: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_sym, current_lines
        if current_sym and current_lines:
            body = "\n".join(current_lines).strip()
            if body:
                blocks.append((current_sym, body))
        current_sym = None
        current_lines = []

    for line in lines:
        m2 = re.match(r"^##\s+([A-Z][A-Z0-9-]{1,20})(?:\s|$)", line)
        m3 = re.match(r"^###\s+([A-Z][A-Z0-9-]{1,20})", line)
        if m2 and not line.upper().startswith("## BLOK") and not line.upper().startswith("## BOK"):
            flush()
            current_sym = canonical_gene(m2.group(1))
            current_lines = []
            continue
        if m3:
            flush()
            current_sym = canonical_gene(m3.group(1))
            current_lines = []
            continue
        if current_sym is not None:
            current_lines.append(line)

    flush()
    return blocks


def normalize_body(body: str) -> str:
    body = body.strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def merge() -> None:
    by_gene: dict[str, str] = {}
    order_seen: list[str] = []

    for path in SOURCES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for sym, body in split_gene_blocks(text):
            if not sym:
                continue
            body = normalize_body(body)
            if sym not in by_gene or len(body) > len(by_gene[sym]):
                if sym not in by_gene:
                    order_seen.append(sym)
                by_gene[sym] = body

    # sekcje
    section_genes: dict[str, list[str]] = {sid: [] for sid, _ in SECTIONS}
    unassigned: list[str] = []

    for sym in sorted(by_gene, key=lambda s: (GENE_SECTION.get(s, "ZZ"), s)):
        sid = GENE_SECTION.get(sym)
        if sid:
            section_genes[sid].append(sym)
        else:
            unassigned.append(sym)

    lines = [
        "# Zbiorowe badanie markerów",
        "",
        "Scalony kompendium genów bez pełnych kart w wiki — źródła: tematy psychiatryczne "
        "i molekularne, dane WGS/Bazy ryzyka. Każdy gen: trzy profile genotypowe "
        "(referencyjny / pośredni / ryzyko lub patogenny).",
        "",
        f"**Łącznie genów:** {len(by_gene)}",
        "",
        "---",
        "",
    ]

    for sid, title in SECTIONS:
        genes = sorted(section_genes[sid])
        if not genes:
            continue
        lines.append(f"## CZĘŚĆ {sid}. {title}")
        lines.append("")
        for sym in genes:
            lines.append(f"### {sym}")
            lines.append("")
            lines.append(by_gene[sym])
            lines.append("")
            lines.append("---")
            lines.append("")

    if unassigned:
        lines.append("## CZĘŚĆ XVI. Pozostałe markery")
        lines.append("")
        for sym in sorted(unassigned):
            lines.append(f"### {sym}")
            lines.append("")
            lines.append(by_gene[sym])
            lines.append("")
            lines.append("---")
            lines.append("")

    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(by_gene)} genów, {len(unassigned)} bez przypisanej sekcji)")


if __name__ == "__main__":
    merge()
