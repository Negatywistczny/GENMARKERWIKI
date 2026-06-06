#!/usr/bin/env python3
"""Uzupełnij brakujące (Autor, ROK) w liniach PMID w §8."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

MD_DIR = Path(__file__).resolve().parent.parent / "md"
SKIP = {"UNIWERSALNY_SZABLON_MARKERA.md"}
CITE_RE = re.compile(r"\*\*PMID:\s*\d+\*\*\s*\([^)]+,\s*\d{4}\)")
PMID_LINE_RE = re.compile(
    r"^(\* \*\*PMID: (\d+)\*\*)(?:\s*\([^)]*\))?\s*(–|-)\s*(.+)$"
)


def first_author_surname(name: str) -> str:
    return name.split()[0] if name else "?"


def cite_from_record(rec: dict) -> str:
    authors = rec.get("authors") or []
    pubdate = rec.get("pubdate") or ""
    year_m = re.search(r"\d{4}", pubdate)
    year = year_m.group() if year_m else "????"
    if not authors:
        return f"(?, {year})"
    surname = first_author_surname(authors[0].get("name", ""))
    if len(authors) == 1:
        return f"({surname}, {year})"
    return f"({surname} et al., {year})"


def fetch_citations(pmids: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    batch_size = 50
    for i in range(0, len(pmids), batch_size):
        batch = pmids[i : i + batch_size]
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            f"?db=pubmed&id={','.join(batch)}&retmode=json"
        )
        req = urllib.request.Request(url, headers={"User-Agent": "GENMARKERWIKI/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.load(resp)
        except urllib.error.URLError as exc:
            print(f"  błąd API: {exc}")
            continue
        result = data.get("result", {})
        for pmid in batch:
            rec = result.get(pmid)
            if rec:
                out[pmid] = cite_from_record(rec)
        time.sleep(0.35)
    return out


def needs_cite(line: str) -> bool:
    return "PMID:" in line and not CITE_RE.search(line)


def fix_line(line: str, cites: dict[str, str]) -> str:
    m = PMID_LINE_RE.match(line)
    if not m:
        return line
    pmid = m.group(2)
    cite = cites.get(pmid)
    if not cite:
        return line
    return f"{m.group(1)} {cite} – {m.group(4)}"


def process_file(path: Path, cites: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    sec8 = re.search(r"(### 8\. Źródła \(Referencje\)\n)([\s\S]*?)(\Z)", text)
    if not sec8:
        return False
    body = sec8.group(2)
    lines = body.splitlines()
    changed = False
    new_lines: list[str] = []
    for line in lines:
        if needs_cite(line):
            fixed = fix_line(line, cites)
            if fixed != line:
                changed = True
                line = fixed
        new_lines.append(line)
    if not changed:
        return False
    new_body = "\n".join(new_lines)
    if body.endswith("\n") and not new_body.endswith("\n"):
        new_body += "\n"
    path.write_text(text[: sec8.start(2)] + new_body + sec8.group(3), encoding="utf-8")
    return True


def collect_pmids() -> list[str]:
    pmids: set[str] = set()
    for path in MD_DIR.glob("*.md"):
        if path.name in SKIP:
            continue
        sec8 = re.search(r"### 8\.[^\n]*\n([\s\S]*?)\Z", path.read_text(encoding="utf-8"))
        if not sec8:
            continue
        for line in sec8.group(1).splitlines():
            if needs_cite(line):
                m = PMID_LINE_RE.match(line)
                if m:
                    pmids.add(m.group(2))
    return sorted(pmids)


def main() -> None:
    pmids = collect_pmids()
    print(f"PMID do uzupełnienia: {len(pmids)}")
    cites = fetch_citations(pmids)
    print(f"Pobrano cytowań: {len(cites)}")
    changed = 0
    for path in sorted(MD_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        if process_file(path, cites):
            print(path.stem)
            changed += 1
    print(f"Zaktualizowano: {changed} kart")


if __name__ == "__main__":
    main()
