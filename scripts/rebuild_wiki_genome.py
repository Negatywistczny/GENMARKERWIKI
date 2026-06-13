#!/usr/bin/env python3
"""Pełny rebuild raportu wiki + audyty jakości."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(label: str, cmd: list[str]) -> int:
    print(f"\n=== {label} ===", flush=True)
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode != 0:
        print(f"[FAIL] {label} (exit {r.returncode})", flush=True)
    else:
        print(f"[OK] {label}", flush=True)
    return r.returncode


def main() -> int:
    py = sys.executable
    steps = [
        ("WGS lookup z full.csv", [py, str(SCRIPTS / "wgs_full_genome.py")]),
        ("Raport osobisty + gwiazdki", [py, str(SCRIPTS / "generate_personal_report.py")]),
        ("Profile genów JS", [py, str(SCRIPTS / "build_personal_gene_profiles_js.py")]),
        ("Audyt rsID (locus)", [py, str(SCRIPTS / "audit_all_gene_rsids.py")]),
        ("Audyt patogennych rsID", [py, str(SCRIPTS / "audit_pathogenic_rsids.py")]),
        ("Audyt profili tematów", [py, str(SCRIPTS / "audit_topic_profiles.py")]),
        ("Audyt gwiazdek minikart", [py, str(SCRIPTS / "audit_mini_stars.py")]),
    ]
    failed = []
    for label, cmd in steps:
        if run(label, cmd) != 0:
            failed.append(label)
    print("\n=== PODSUMOWANIE ===", flush=True)
    if failed:
        print("Nie przeszło:", ", ".join(failed), flush=True)
        return 1
    print("Wszystkie kroki OK.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
