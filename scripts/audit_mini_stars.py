#!/usr/bin/env python3
"""Audit md-mini: czy ★ zgadza się z WGS (bezpośrednio vs tylko komplement)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_MINI = ROOT / "docs" / "genes-mini"
CACHE_PATH = ROOT / "scripts" / "data" / "rsid_allele_cache.json"

COMPLEMENT = str.maketrans("ACGT", "TGCA")
WGS_LINE = re.compile(
    r"`(rs\d+)`\s*[—\-]+\s*\*\*([A-Z0-9/*]+)\*\*",
    re.I,
)
WGS_BLOCK = re.compile(
    r"\* \*\*Mój genotyp \(WGS\):\*\*\s*\n((?:  \* .+\n)+)",
)
RSID_META = re.compile(r"\* \*\*Główny rsID.*?:\*\*\s*(.+)", re.I)


def norm_gt(g: str) -> str:
    g = g.strip().upper()
    if "/" in g:
        a, b = g.split("/", 1)
        if a > b:
            a, b = b, a
        return f"{a}/{b}"
    return g


def alleles_equiv(a: str, b: str) -> bool:
    return a == b or a.translate(COMPLEMENT) == b


def direct_match(row: str, user: str) -> bool:
    row = norm_gt(row)
    user = user.upper().strip()
    if "/" not in row or len(user) != 2 or "/" in user:
        return False
    a, b = row.split("/", 1)
    for left, right in ((user[0], user[1]), (user[1], user[0])):
        if left == a and right == b:
            return True
        if left == b and right == a:
            return True
    return False


def comp_match(row: str, user: str) -> bool:
    row = norm_gt(row)
    user = user.upper().strip()
    if "/" not in row or len(user) != 2 or "/" in user:
        return False
    a, b = row.split("/", 1)
    for left, right in ((user[0], user[1]), (user[1], user[0])):
        if alleles_equiv(left, a) and alleles_equiv(right, b):
            return True
        if alleles_equiv(left, b) and alleles_equiv(right, a):
            return True
    return False


def parse_wgs(body: str) -> dict[str, str]:
    m = WGS_BLOCK.search(body)
    if not m:
        return {}
    out: dict[str, str] = {}
    for ln in m.group(1).splitlines():
        mm = WGS_LINE.search(ln)
        if mm:
            out[mm.group(1).lower()] = mm.group(2).upper()
    return out


def parse_star_table(body: str) -> list[tuple[str, bool, str, str]]:
    rows: list[tuple[str, bool, str, str]] = []
    in_table = False
    for ln in body.splitlines():
        if ln.startswith("| Genotyp |"):
            in_table = True
            continue
        if in_table and ln.startswith("|"):
            if re.match(r"^\|\s*:?-{3,}", ln):
                continue
            parts = [p.strip() for p in ln.split("|")[1:-1]]
            if len(parts) >= 4:
                gt = re.sub(r"^\*\*★?\s*|\*\*$|`", "", parts[0]).strip()
                star = "★" in parts[0]
                rows.append((gt, star, parts[1], parts[2]))
        elif in_table and not ln.startswith("|"):
            break
    return rows


def primary_rsid(meta_line: str | None) -> str | None:
    if not meta_line:
        return None
    m = re.search(r"(rs\d+)", meta_line, re.I)
    return m.group(1).lower() if m else None


def dbsnp_row_index(user: str, ref: str, alt: str, total: int) -> int | None:
    from rsid_allele_lookup import genotype_from_alleles

    for i in range(total):
        expected = genotype_from_alleles(ref, alt, i, total)
        if comp_match(expected, user):
            return i
    return None


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    sys.path.insert(0, str(ROOT / "scripts"))
    cache = json.loads(CACHE_PATH.read_text(encoding="utf-8"))

    comp_only: list[tuple] = []
    no_match: list[tuple] = []
    no_star: list[tuple] = []
    ref_mismatch: list[tuple] = []

    for md in sorted(MD_MINI.glob("*.md")):
        gene = md.stem.upper()
        body = md.read_text(encoding="utf-8")
        wgs = parse_wgs(body)
        rows = parse_star_table(body)
        if not rows or not wgs:
            continue

        rsid = primary_rsid(
            RSID_META.search(body).group(1) if RSID_META.search(body) else None
        )
        user_gt = wgs.get(rsid) if rsid else None
        if not user_gt:
            user_gt = next(iter(wgs.values()), None)
        if not user_gt or "/" in user_gt or len(user_gt) != 2:
            continue

        star_rows = [r for r in rows if r[1]]
        row_gts = [r[0] for r in rows]

        if not star_rows:
            no_star.append((gene, user_gt, row_gts, rsid))
            continue

        star_gt, _, _, tone = star_rows[0]
        direct = direct_match(star_gt, user_gt)
        complement = comp_match(star_gt, user_gt)

        if not complement:
            no_match.append((gene, user_gt, star_gt, rsid, row_gts))
        elif not direct:
            info = cache.get(rsid or "", {})
            ref, alt = info.get("ref"), info.get("alt")
            idx = (
                dbsnp_row_index(user_gt, ref, alt, len(rows))
                if ref and alt
                else None
            )
            expected_gt = row_gts[idx] if idx is not None and idx < len(row_gts) else "?"
            comp_only.append(
                (gene, user_gt, star_gt, rsid, ref, alt, tone, row_gts, expected_gt, idx)
            )

            # hom-ref user starred on alt-alt row via complement only
            if ref and alt and user_gt == ref + ref:
                star_parts = norm_gt(star_gt).split("/")
                if alleles_equiv(star_parts[0], alt) and alleles_equiv(star_parts[1], alt):
                    ref_mismatch.append(
                        (gene, user_gt, star_gt, rsid, ref, alt, tone, expected_gt)
                    )

    print("=== HOM-REF WGS + ★ na wierszu alt/alt (tylko komplement) ===")
    for item in ref_mismatch:
        print(" | ".join(str(x) for x in item))

    print("\n=== COMPLEMENT-ONLY (★ pasuje tylko po komplementacji) ===")
    for item in comp_only:
        print(" | ".join(str(x) for x in item))

    print("\n=== NO MATCH ===")
    for item in no_match:
        print(item)

    print(f"\n=== NO STAR (ma WGS litery, brak ★): {len(no_star)} ===")
    for item in no_star:
        print(" | ".join(str(x) for x in item))

    issues = len(ref_mismatch) + len(no_match)
    if issues:
        print(f"\n[FAIL] Problemy gwiazdek: {issues}", flush=True)
        return 1
    print("\n[OK] Wszystkie minikarty z WGS: ★ zgodne", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
