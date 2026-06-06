#!/usr/bin/env python3
"""Ujednolicenie sekcji 8: linki SNPedia zawsze do rsID (główny marker z sekcji 2)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
SKIP = {"UNIWERSALNY_SZABLON_MARKERA.md"}

# Geny bez pojedynczego rsID w sekcji 2 — jawne mapowanie
OVERRIDE_RSIDS: dict[str, list[str]] = {
    "MAOA": ["rs1137070"],
    "APOE": ["rs429358", "rs7412"],
    "MTHFR": ["rs1801133", "rs1801131"],
    "MC1R": ["rs1805007"],
    "TAS2R38": ["rs713598", "rs1726866", "rs10246939"],
}

RSID_RE = re.compile(r"rs\d+", re.I)


def snpedia_link(rsid: str) -> str:
    rsid = rsid.lower()
    page = "Rs" + rsid[2:]
    return f"[SNPedia ({rsid})](https://www.snpedia.com/index.php/{page})"


def extract_main_rsids(text: str, gene: str) -> list[str]:
    if gene in OVERRIDE_RSIDS:
        return OVERRIDE_RSIDS[gene]

    sec2 = re.search(r"### 2\.[^\n]*\n([\s\S]*?)(?=### 3\.)", text)
    if not sec2:
        return []

    block = sec2.group(1)
    for pat in (
        r"\*\*Główny rsID[^:]*:\*\*\s*([^\n]+)",
        r"\*\*Główne rsID[^:]*:\*\*\s*([^\n]+)",
        r"\*\*Główny marker:\*\*\s*([^\n]+)",
    ):
        m = re.search(pat, block)
        if m:
            ids = RSID_RE.findall(m.group(1))
            if ids:
                return [r.lower() for r in ids]

    return []


def extract_snpedia_desc(sec8_body: str) -> str:
    m = re.search(r"\*\*Baza referencyjna:\*\*[^\n]+$", sec8_body, re.M)
    if m:
        line = m.group(0)
        if " – " in line:
            return line.rsplit(" – ", 1)[1].strip()
        if " - " in line:
            return line.rsplit(" - ", 1)[1].strip()
    return "Częstości alleli, fenotypy i adnotacje populacyjne."


def build_baza_line(rsids: list[str], desc: str) -> str:
    links = ", ".join(snpedia_link(r) for r in rsids)
    return f"* **Baza referencyjna:** {links} – {desc}"


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    gene = path.stem.upper()

    sec8 = re.search(r"(### 8\. Źródła \(Referencje\)\n)([\s\S]*?)(\Z)", text)
    if not sec8:
        return False

    rsids = extract_main_rsids(text, gene)
    if not rsids:
        print(f"  pominięto {gene}: brak rsID")
        return False

    desc = extract_snpedia_desc(sec8.group(2))
    new_baza = build_baza_line(rsids, desc)

    body = sec8.group(2)
    new_body, n = re.subn(
        r"\* \*\*Baza referencyjna:\*\*[^\n]+\n?",
        new_baza + "\n",
        body,
        count=1,
    )
    if n == 0:
        new_body = body.rstrip() + "\n" + new_baza + "\n"

    new_text = text[: sec8.start(2)] + new_body + sec8.group(3)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
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
