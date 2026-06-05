#!/usr/bin/env python3
"""Remove duplicate variant tables in section 4 of gene markdown cards."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_DIR = ROOT / "md"
SKIP = {"UNIWERSALNY_SZABLON_MARKERA.md", "index.md"}

SECTION4_RE = re.compile(r"^### 4\.\s+Tabela Wariantów\s*$", re.M)
SECTION_NEXT_RE = re.compile(r"^### [56]\.\s+", re.M)
BOLD_TITLE_RE = re.compile(r"^\*\*(.+)\*\*\s*$")
TABLE_SEP_RE = re.compile(r"^\|\s*:?-+")
HEADER_LIKE_RE = re.compile(
    r"genotyp|rs\d|haplotyp|wariant|rs429358|rs7412",
    re.I,
)


def normalize_for_dedup(text: str) -> str:
    t = text.replace("★", "").replace("**", "")
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t


def is_table_start(lines: list[str], idx: int) -> bool:
    if idx >= len(lines) or not lines[idx].strip().startswith("|"):
        return False
    if idx + 1 >= len(lines):
        return False
    return TABLE_SEP_RE.match(lines[idx + 1].strip()) is not None


def extract_table(lines: list[str], start: int) -> tuple[list[str], int]:
    out = [lines[start], lines[start + 1]]
    i = start + 2
    while i < len(lines) and lines[i].strip().startswith("|"):
        out.append(lines[i])
        i += 1
    return out, i


def table_key(table_lines: list[str]) -> str:
    rows = [
        normalize_for_dedup(line)
        for line in table_lines
        if line.strip().startswith("|") and not TABLE_SEP_RE.match(line.strip())
    ]
    return hashlib.sha256("||".join(rows).encode()).hexdigest()


def has_star(lines: list[str]) -> bool:
    return any("★" in line for line in lines)


def parse_section4_blocks(body: str) -> list[list[str]]:
    lines = [ln for ln in body.splitlines() if not SECTION4_RE.match(ln)]
    blocks: list[list[str]] = []
    current: list[str] = []
    i = 0

    def flush() -> None:
        nonlocal current
        if current and any(l.strip().startswith("|") for l in current):
            blocks.append(current)
        current = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if BOLD_TITLE_RE.match(stripped):
            flush()
            current = [line]
            i += 1
            continue

        if is_table_start(lines, i):
            table, i = extract_table(lines, i)
            first_cell = table[0].split("|")[1].strip().lower() if table else ""
            if current and any(l.strip().startswith("|") for l in current):
                if HEADER_LIKE_RE.search(first_cell):
                    flush()
            if not current:
                current = []
            current.extend(table)
            if i < len(lines) and lines[i].strip() == "":
                current.append(lines[i])
                i += 1
            continue

        if stripped.startswith("*") and current:
            current.append(line)
            i += 1
            continue

        if stripped == "":
            if current:
                current.append(line)
            i += 1
            continue

        flush()
        i += 1

    flush()
    return blocks


def dedup_blocks(blocks: list[list[str]]) -> list[list[str]]:
    seen: dict[str, list[str]] = {}
    order: list[str] = []
    for block in blocks:
        # Hash each table inside block separately for intra-block dedup
        deduped_lines: list[str] = []
        title_lines: list[str] = []
        table_groups: list[list[str]] = []
        i = 0
        block_lines = block
        while i < len(block_lines):
            line = block_lines[i]
            if BOLD_TITLE_RE.match(line.strip()) and not is_table_start(block_lines, i):
                title_lines.append(line)
                i += 1
                continue
            if is_table_start(block_lines, i):
                table, i = extract_table(block_lines, i)
                table_groups.append(table)
                continue
            i += 1

        unique_tables: list[list[str]] = []
        table_seen: dict[str, list[str]] = {}
        for table in table_groups:
            key = table_key(table)
            if key not in table_seen:
                table_seen[key] = table
                unique_tables.append(table)
            elif has_star(table) and not has_star(table_seen[key]):
                idx = unique_tables.index(table_seen[key])
                unique_tables[idx] = table
                table_seen[key] = table

        if not unique_tables and not title_lines:
            continue

        rebuilt = title_lines[:]
        for ti, table in enumerate(unique_tables):
            if rebuilt and rebuilt[-1].strip():
                rebuilt.append("")
            rebuilt.extend(table)

        key = table_key([l for l in rebuilt if l.strip().startswith("|")])
        if key not in seen:
            seen[key] = rebuilt
            order.append(key)
        elif has_star(rebuilt) and not has_star(seen[key]):
            seen[key] = rebuilt

    return [seen[k] for k in order]


def rebuild_section4(blocks: list[list[str]]) -> str:
    parts = ["### 4. Tabela Wariantów", ""]
    for i, block in enumerate(blocks):
        if i:
            parts.append("")
        cleaned = []
        for line in block:
            if cleaned or line.strip():
                cleaned.append(line.rstrip())
        while cleaned and not cleaned[-1].strip():
            cleaned.pop()
        parts.extend(cleaned)
    parts.append("")
    return "\n".join(parts)


def process_file(path: Path) -> tuple[bool, int, int]:
    text = path.read_text(encoding="utf-8")
    m4 = SECTION4_RE.search(text)
    if not m4:
        return False, 0, 0
    m5 = SECTION_NEXT_RE.search(text, m4.end())
    if not m5:
        return False, 0, 0

    before = text[: m4.start()]
    after = text[m5.start() :]
    body = text[m4.end() : m5.start()]

    blocks = parse_section4_blocks(body)
    if not blocks:
        return False, 0, 0
    deduped = dedup_blocks(blocks)
    old_tables = body.count("|:---")
    new_body = rebuild_section4(deduped)
    new_tables = new_body.count("|:---")

    if new_body == rebuild_section4(blocks) and old_tables == new_tables:
        return False, old_tables, new_tables

    new_text = before + new_body + after
    path.write_text(new_text, encoding="utf-8")
    return True, old_tables, new_tables


def main() -> None:
    changed = []
    for path in sorted(MD_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        ok, old, new = process_file(path)
        if ok:
            changed.append((path.name, old, new))
    print(f"Deduplicated {len(changed)} files:")
    for name, old, new in changed:
        print(f"  {name}: {old} -> {new} tables")


if __name__ == "__main__":
    main()
