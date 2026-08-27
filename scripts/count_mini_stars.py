#!/usr/bin/env python3
"""Policz oznaczenia ★ (Twój wariant) w md-mini/."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_MINI = ROOT / "docs" / "genes-mini"
SKIP = frozenset({"NOT_IN_DBSNP", "NOT_FOUND", "NO_CALL", "BRAK", "--", ""})
WGS_LINE = re.compile(
    r"`(rs\d+)`\s*[\u2014\u2013\-]+\s*\*\*([A-Z0-9/*]+)\*\*",
    re.I,
)
RSID_META = re.compile(r"\* \*\*Główny rsID.*?:\*\*\s*(.+)", re.I)


def parse_wgs(body: str) -> dict[str, str]:
    out: dict[str, str] = {}
    in_wgs = False
    for ln in body.splitlines():
        if "Mój genotyp (WGS)" in ln:
            in_wgs = True
            continue
        if in_wgs:
            if ln.startswith("###") or (
                ln.startswith("* **")
                and "WGS" not in ln
                and "Dopasowany" not in ln
                and "Rola biologiczna" not in ln
            ):
                if out:
                    break
                continue
            mm = WGS_LINE.search(ln)
            if mm:
                out[mm.group(1).lower()] = mm.group(2).upper()
    return out


def has_star(body: str) -> bool:
    for ln in body.splitlines():
        if (
            ln.startswith("|")
            and "\u2605" in ln
            and "Genotyp" not in ln
            and not re.match(r"^\|\s*:?-{3,}", ln)
        ):
            return True
    return False


def primary_rsid(body: str) -> str | None:
    m = RSID_META.search(body)
    if not m:
        return None
    mm = re.search(r"(rs\d+)", m.group(1), re.I)
    return mm.group(1).lower() if mm else None


def usable_nuc_call(gt: str | None) -> bool:
    return bool(
        gt
        and gt not in SKIP
        and "/" not in gt
        and len(gt) == 2
        and gt.isalpha()
    )


def main() -> int:
    total = with_star = with_wgs_call = unmarked = 0
    unmarked_list: list[tuple[str, str, str | None]] = []
    no_wgs = 0

    for md in sorted(MD_MINI.glob("*.md")):
        total += 1
        body = md.read_text(encoding="utf-8")
        star = has_star(body)
        if star:
            with_star += 1
        wgs = parse_wgs(body)
        if not wgs:
            no_wgs += 1
            continue
        rsid = primary_rsid(body)
        user = wgs.get(rsid) if rsid else None
        if not usable_nuc_call(user):
            for gt in wgs.values():
                if usable_nuc_call(gt):
                    user = gt
                    break
        if usable_nuc_call(user):
            with_wgs_call += 1
            if not star:
                unmarked += 1
                unmarked_list.append((md.stem, user or "", rsid))

    print(f"Minikart razem: {total}")
    print(f"Z gwiazdka (Twój wariant): {with_star}")
    print(f"Z callem WGS (litery): {with_wgs_call}")
    print(f"Nieoznaczone (WGS litery, brak gwiazdki): {unmarked}")
    for gene, gt, rsid in unmarked_list:
        print(f"  {gene}: WGS={gt} rsid={rsid}")
    print(f"Bez bloku WGS: {no_wgs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
