#!/usr/bin/env python3
"""Generuj html/topic-psychiatry-sections.js z plików Baza — *.md."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RISK_DIR = ROOT / "raporty" / "ryzyko"
OUT = ROOT / "html" / "topic-psychiatry-sections.js"

ALIASES = {
    "DAT1": "SLC6A3",
    "DAT": "SLC6A3",
    "5-HTT": "SLC6A4",
    "LPHN3": "ADGRL3",
    "MDR1": "ABCB1",
    "GR": "NR3C1",
    "MR": "NR3C2",
}

SECTION_RE = re.compile(r"^## \*\*([A-Z]\.\s*.+?)\*\*\s*$", re.MULTILINE)
ROW_RE = re.compile(
    r"^\|[^|]+\|\s*\*\*([^*]+)\*\*\s*\|([^|]+)\|[^|]+\|\s*([^|]+)\s*\|",
    re.MULTILINE,
)

TOPIC_MAP = {
    "Baza — ASD.md": "asd",
    "Baza — ADHD.md": "adhd",
    "Baza — MDD.md": "mdd",
    "Baza — ChAD.md": "chad",
    "Baza — SCZ.md": "scz",
}


def clean(text: str) -> str:
    return re.sub(r"\\", "", text.strip())


def normalize_symbols(raw: str) -> list[str]:
    raw = raw.strip()
    parts = re.split(r"\s*/\s*", raw)
    out: list[str] = []
    for part in parts:
        part = part.strip()
        if not part or part.lower().startswith("locus"):
            continue
        paren = re.match(r"^([A-Z][A-Z0-9-]+)\s*\(([^)]+)\)$", part)
        if paren:
            main, alias = paren.group(1), paren.group(2).strip()
            out.append(ALIASES.get(main, main))
            if re.fullmatch(r"[A-Z][A-Z0-9-]+", alias):
                out.append(ALIASES.get(alias, alias))
            continue
        sym = re.sub(r"\s*\(.*$", "", part).strip()
        if re.fullmatch(r"[A-Z][A-Z0-9-]+", sym):
            out.append(ALIASES.get(sym, sym))
        elif "," in sym:
            for piece in sym.split(","):
                piece = piece.strip()
                if re.fullmatch(r"[A-Z][A-Z0-9-]+", piece):
                    out.append(ALIASES.get(piece, piece))
    return out


def parse_baza(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    sections: list[dict] = []
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        label = clean(m.group(1))
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        genes: list[dict] = []
        seen: set[str] = set()
        for row in ROW_RE.finditer(block):
            role = clean(row.group(2))
            evidence = clean(row.group(3))
            for sym in normalize_symbols(row.group(1)):
                if sym in seen:
                    continue
                seen.add(sym)
                genes.append({"symbol": sym, "role": role, "evidence": evidence})
        if genes:
            sections.append({"label": label, "genes": genes})
    return sections


def js_string(s: str) -> str:
    return (
        '"'
        + s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", " ")
        + '"'
    )


def render_gene(g: dict) -> str:
    return (
        f'{{ symbol: {js_string(g["symbol"])}, '
        f'role: {js_string(g["role"])}, '
        f'evidence: {js_string(g["evidence"])} }}'
    )


def render_section(s: dict) -> str:
    genes = ",\n              ".join(render_gene(g) for g in s["genes"])
    return f"""          {{
            label: {js_string(s["label"])},
            genes: [
              {genes}
            ],
          }}"""


def main() -> None:
    lines = [
        "/** Sekcje genów dla tematów psychiatrycznych — generowane przez scripts/build_topic_sections.py */",
        "window.TOPIC_PSYCHIATRY_SECTIONS = {",
    ]
    entries = []
    for fname, tid in TOPIC_MAP.items():
        sections = parse_baza(RISK_DIR / fname)
        body = ",\n".join(render_section(s) for s in sections)
        entries.append(f"  {tid}: [\n{body}\n  ]")
    lines.append(",\n".join(entries))
    lines.append("};")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
