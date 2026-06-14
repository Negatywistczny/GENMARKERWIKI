#!/usr/bin/env python3
"""Wstaw pustą linię przed ### 5. gdy poprzedza ją wiersz tabeli §4."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "md"
SKIP = frozenset({"UNIWERSALNY_SZABLON_MARKERA.md", "index.md"})


def main() -> int:
    fixed = 0
    for path in sorted(MD.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8")
        new = re.sub(r"(\|[^\n]*)\n(### 5\.)", r"\1\n\n\2", text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            fixed += 1
    print(f"Poprawiono spacing sec4->sec5: {fixed} plikow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
