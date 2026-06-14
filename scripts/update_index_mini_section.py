#!/usr/bin/env python3
"""Dopisz sekcje minikart do index.md (generowane z genes-with-mini.js)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.md"
MINI_JS = ROOT / "html" / "genes-with-mini.js"
MARKER = "## Minikarty (md-mini/)"


def mini_genes() -> list[str]:
    text = MINI_JS.read_text(encoding="utf-8")
    return sorted(re.findall(r'"([A-Z0-9-]+)"', text))


def build_section(genes: list[str]) -> str:
    lines = [
        MARKER,
        "",
        "Geny bez pełnej karty w `md/` — uproszczone minikarty z "
        "[Zbiorowego badania markerów](raporty/markery/Zbiorowe%20badanie%20markerów.md). "
        "Podgląd: `[html/gene.html](html/gene.html)?gene=SYMBOL`.",
        "",
        "| Gen | Markdown | Podgląd |",
        "| --- | --- | --- |",
    ]
    for g in genes:
        lines.append(
            f"| {g} | `md-mini/{g}.md` | [podgląd](html/gene.html?gene={g}) |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    genes = mini_genes()
    section = build_section(genes)
    text = INDEX.read_text(encoding="utf-8")
    if MARKER in text:
        before, _rest = text.split(MARKER, 1)
        # drop old section until next ## or EOF
        rest_parts = text.split(MARKER, 1)[1]
        after = ""
        if "\n## " in rest_parts:
            after = rest_parts[rest_parts.index("\n## ") :]
        text = before.rstrip() + "\n\n" + section.rstrip() + after
    else:
        anchor = "Szablon nowych kart:"
        if anchor in text:
            text = text.replace(
                f"{anchor} [UNIWERSALNY_SZABLON_MARKERA](md/UNIWERSALNY_SZABLON_MARKERA.md).",
                f"{section.rstrip()}\n{anchor} [UNIWERSALNY_SZABLON_MARKERA](md/UNIWERSALNY_SZABLON_MARKERA.md).",
            )
        else:
            text = text.rstrip() + "\n\n" + section
    INDEX.write_text(text, encoding="utf-8")
    print(f"index.md: sekcja minikart ({len(genes)} genow)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
