#!/usr/bin/env python3
"""Usuń zduplikowane nagłówki i bloki WGS z raportu markerów, potem wzbogać ponownie."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "data" / "reports" / "markery" / "Zbiorowe badanie markerów.md"

WGS_MARKER = "* **Mój genotyp (WGS):**"
PROFILE_MARKER = "* **Dopasowany profil:**"


def dedupe_headers(text: str) -> str:
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r"^(### [^\n]+)\n\1\n", r"\1\n", text, flags=re.M)
    return text


def strip_wgs_blocks(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if WGS_MARKER in line:
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.startswith(PROFILE_MARKER):
                    i += 1
                    continue
                if nxt.strip() == "":
                    i += 1
                    break
                if nxt.startswith("**") or (nxt.startswith("* **") and WGS_MARKER not in nxt):
                    break
                i += 1
            continue
        if line.startswith(PROFILE_MARKER):
            i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out)


def main() -> int:
    text = REPORT.read_text(encoding="utf-8")
    text = dedupe_headers(strip_wgs_blocks(text))
    REPORT.write_text(text, encoding="utf-8")
    print("[fix] Usunięto duplikaty i bloki WGS.")
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "enrich_marker_report_genotypes.py")],
        check=False,
    )
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
