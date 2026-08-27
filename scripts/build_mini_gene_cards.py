#!/usr/bin/env python3
"""Generuj uproszczone minikarty genów (md-mini/) z raportu markerów."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from rsid_allele_lookup import (  # noqa: E402
    allele_info_for_rsid,
    ensure_alleles,
    genotype_from_alleles,
    is_resolved_genotype,
    primary_rsid,
    resolve_genotype,
)
REPORT = ROOT / "data" / "reports" / "markery" / "Zbiorowe badanie markerów.md"
MD_DIR = ROOT / "docs" / "genes"
OUT_DIR = ROOT / "docs" / "genes-mini"
OUT_JS = ROOT / "public" / "html" / "genes-with-mini.js"
SKIP_GT = frozenset(
    {
        "",
        "NOT_FOUND",
        "NO_CALL",
        "BRAK",
        "NOT_IN_DBSNP",
        "NOT_IN_DBSNP.",
        "--",
    }
)
COMPLEMENT = str.maketrans("ACGT", "TGCA")

SKIP_PROFILE_TITLE = re.compile(
    r"główny (symbol|rsid|wariant)|pełna nazwa|lokalizacja|rola biologiczna|nazwy potoczne|dopasowany profil|mój genotyp",
    re.I,
)

GENOTYPE_PREFIX = re.compile(r"^(?:genotyp|diplotyp)\s+", re.I)
ALLELE_PAIR = re.compile(r"^([ACGT0-9]+/[ACGT0-9]+|\d+R/\d+R)$", re.I)
STAR_ALLELE_RE = re.compile(r"^\*[\w]+(/\*[\w]+)?$")
VNTR_GENOTYPE_RE = re.compile(r"^\d+R/\d+R$", re.I)
STRUCTURAL_GENOTYPE_RE = re.compile(
    r"^(ins|del|dup)(/(ins|del|dup))?$",
    re.I,
)

BULLET_KEYS = {
    "symbol": re.compile(r"główny symbol", re.I),
    "fullname": re.compile(r"pełna nazwa", re.I),
    "aliases": re.compile(r"nazwy potoczne", re.I),
    "rsid": re.compile(r"główny (rsid|wariant)", re.I),
    "location": re.compile(r"lokalizacja chromosomalna", re.I),
    "role": re.compile(r"rola biologiczna", re.I),
}


def parse_sections(text: str) -> list[tuple[str, str]]:
    parts = re.split(r"^### ", text, flags=re.M)[1:]
    sections: list[tuple[str, str]] = []
    for part in parts:
        gene = part.split("\n", 1)[0].strip()
        body = part.split("\n", 1)[1] if "\n" in part else ""
        sections.append((gene, body))
    return sections


def extract_bullet_value(line: str) -> str:
    m = re.match(r"^\* \*\*([^*]+):\*\*\s*(.+)$", line.strip())
    return m.group(2).strip() if m else ""


def parse_metadata(body: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for line in body.splitlines():
        if not line.startswith("* **"):
            continue
        for key, pat in BULLET_KEYS.items():
            if pat.search(line):
                meta[key] = extract_bullet_value(line)
    return meta


def rsid_from_wgs(wgs: str) -> str | None:
    hits = re.findall(r"rs\d+", wgs or "", flags=re.I)
    return hits[0].lower() if hits else None


def primary_wgs_rsid(wgs: str, wgs_rs: dict[str, str]) -> str | None:
    """Pierwszy rsID z bloku WGS z poprawnym calliem nukleotydowym (nie NOT_IN_DBSNP)."""
    for m in re.finditer(r"(rs\d+)", wgs or "", flags=re.I):
        rs = m.group(1).lower()
        gt = wgs_rs.get(rs, "")
        if gt in SKIP_GT or "/" in gt or len(gt) != 2 or not gt.isalpha():
            continue
        return rs
    return None


def is_cnv_deletion_profile(title: str, short_desc: str, long_desc: str) -> bool:
    """Warianty strukturalne bez pojedynczego genotypu nukleotydowego."""
    title_short = f"{title} {short_desc}".lower()
    if re.search(r"\bcnv\b|delecj|rearanż", title_short):
        return True
    if re.search(r"\bdelecj\b|rearanż", long_desc.lower()):
        return True
    return False


def parse_wgs_block(body: str) -> tuple[str, str | None]:
    lines = body.splitlines()
    wgs_lines: list[str] = []
    matched: str | None = None
    in_wgs = False
    for line in lines:
        if "* **Mój genotyp (WGS):**" in line:
            in_wgs = True
            continue
        if in_wgs:
            if line.startswith("* **Dopasowany profil:**"):
                matched = re.sub(r"\*+", "", line.split(":", 1)[-1]).strip().rstrip(":")
                in_wgs = False
                continue
            if line.strip() == "" and wgs_lines:
                in_wgs = False
                continue
            if line.startswith("**") or (line.startswith("* **") and "Wariant" in line):
                in_wgs = False
                break
            if in_wgs:
                wgs_lines.append(line.strip())
    wgs = "\n".join(wgs_lines).strip()
    return wgs, matched


def parse_profiles(body: str) -> list[tuple[str, str]]:
    """Return list of (title, description)."""
    profiles: list[tuple[str, str]] = []
    lines = body.splitlines()
    i = 0
    skip_wgs = False
    while i < len(lines):
        line = lines[i]
        if "* **Mój genotyp (WGS):**" in line:
            skip_wgs = True
            i += 1
            continue
        if skip_wgs:
            if line.strip() == "" and i > 0:
                skip_wgs = False
            elif line.startswith("**") or (line.startswith("* **") and "Wariant" in line and ":" in line):
                skip_wgs = False
            else:
                i += 1
                continue

        m_bold = re.match(r"^\*\*(.+)\*\*\s*$", line.strip())
        if m_bold:
            title = m_bold.group(1).strip()
            desc_parts: list[str] = []
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if re.match(r"^\*\*.+\*\*\s*$", nxt.strip()):
                    break
                if nxt.startswith("* **") and "Mój genotyp" not in nxt:
                    break
                if nxt.strip().startswith("---"):
                    break
                if nxt.strip():
                    desc_parts.append(nxt.strip())
                i += 1
            profiles.append((title, " ".join(desc_parts)))
            continue

        m_inline = re.match(r"^\* \*\*([^*]+):\*\*\s*(.+)$", line.strip())
        if m_inline and not SKIP_PROFILE_TITLE.search(m_inline.group(1)):
            profiles.append((m_inline.group(1).strip(), m_inline.group(2).strip()))
            i += 1
            continue

        m_allel = re.match(r"^\* Allel (.+?):\*\*\s*(.+)$", line.strip())
        if m_allel:
            profiles.append((f"Allel {m_allel.group(1).strip()}", m_allel.group(2).strip()))
            i += 1
            continue

        m_broken_title = re.match(r"^Allel (.+?)\s*\*\*\s*$", line.strip())
        if m_broken_title:
            title = f"Allel {m_broken_title.group(1).strip()}"
            desc_parts: list[str] = []
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if re.match(r"^\*\*.+\*\*\s*$", nxt.strip()) or re.match(
                    r"^Allel .+\*\*\s*$", nxt.strip()
                ):
                    break
                if nxt.strip().startswith("---"):
                    break
                if nxt.strip():
                    desc_parts.append(nxt.strip())
                i += 1
            profiles.append((title, " ".join(desc_parts)))
            continue

        i += 1

    return profiles[:3]


CNV_MARKERS = re.compile(
    r"\bcnv\b|liczba kopii|zmienność liczby|zmienność strukturalna|metylacja promotor",
    re.I,
)


def is_cnv_only_gene(meta: dict[str, str], profiles: list[tuple[str, str]]) -> bool:
    """Geny opisane głównie jako CNV / liczba kopii, nie klasyczny SNP 3-wierszowy."""
    rsid_field = meta.get("rsid", "")
    if CNV_MARKERS.search(rsid_field):
        return True
    if not profiles:
        return False
    cnv_profiles = sum(
        1 for title, desc in profiles if CNV_MARKERS.search(f"{title} {desc}")
    )
    return cnv_profiles >= len(profiles) - 1 and len(profiles) >= 2


def ensure_short_desc(
    title: str, short_desc: str, long_desc: str, *, cnv_only: bool = False
) -> tuple[str, str]:
    """Uzupełnij pusty opis krótki z tytułu profilu lub pierwszego zdania."""
    if short_desc.strip():
        return short_desc.strip(), long_desc.strip()

    title_clean = title.strip()
    paren = re.match(r"^([^(]+)\(([^)]+)\)\s*$", title_clean)
    if paren:
        label = paren.group(1).strip()
        inner = paren.group(2).strip()
        if cnv_only:
            return label, long_desc.strip() or inner
        if inner:
            return inner, long_desc.strip() or label

    if title_clean and len(title_clean) <= 80:
        return title_clean, long_desc.strip()

    if long_desc.strip():
        parts = re.split(r"(?<=[.!?])\s+", long_desc.strip(), maxsplit=1)
        if parts[0] and len(parts[0]) <= 120:
            rest = parts[1].strip() if len(parts) > 1 else ""
            return parts[0], rest or long_desc.strip()

    short = re.sub(r"\s+", " ", title_clean)
    if len(short) > 80:
        short = short[:77].rstrip() + "…"
    return short, long_desc.strip()


def dedupe_built_rows(
    rows: list[tuple[str, str, str, str, str]],
    *,
    matched: str | None = None,
) -> list[tuple[str, str, str, str, str]]:
    """Usuń zduplikowane wiersze po genotypie; zachowaj lepsze dopasowanie profilu."""
    best: dict[str, tuple[str, str, str, str, str]] = {}
    best_score: dict[str, int] = {}
    order: list[str] = []
    for row in rows:
        _title, short, long, genotype, _tone = row
        key = norm_genotype(genotype) if genotype not in {"—", "-"} else f"—:{short[:40]}"
        score = matched_profile_score(row[0], short, matched)
        if not short.strip() and long.strip():
            score -= 10
        if key not in best:
            order.append(key)
            best[key] = row
            best_score[key] = score
            continue
        if score > best_score[key]:
            best[key] = row
            best_score[key] = score
    return [best[k] for k in order]


def split_profile(title: str, desc: str) -> tuple[str, str, str]:
    """Rozbij profil na: genotyp, opis krótki, opis szczegółowy."""
    long_desc = desc.strip()
    bare = GENOTYPE_PREFIX.sub("", title.strip()).strip()

    allele_paren = re.match(
        r"^([ACGT0-9]+/[ACGT0-9]+|\d+R/\d+R)\s*\(([^)]+)\)\s*$",
        bare,
        re.I,
    )
    if allele_paren:
        return allele_paren.group(1), allele_paren.group(2).strip(), long_desc

    allele_only = re.match(r"^([ACGT0-9]+/[ACGT0-9]+|\d+R/\d+R)\s*$", bare, re.I)
    if allele_only:
        return allele_only.group(1), "", long_desc

    allel_paren = re.match(r"^Allel\s+(.+?)\s*\(([^)]+)\)\s*$", bare, re.I)
    if allel_paren:
        return allel_paren.group(1).strip(), allel_paren.group(2).strip(), long_desc

    label_paren = re.match(r"^([^(]+)\(([^)]+)\)\s*$", bare)
    if label_paren:
        label = label_paren.group(1).strip()
        short = label_paren.group(2).strip()
        if ALLELE_PAIR.match(label):
            return label, short, long_desc
        return label, short, long_desc

    return bare, "", long_desc


def norm_genotype(value: str) -> str:
    g = re.sub(r"\s+", "", (value or "").upper().strip("`*★ "))
    if not g:
        return g
    if "/" in g:
        a, b = g.split("/", 1)
        return f"{a}/{b}" if a <= b else f"{b}/{a}"
    if len(g) == 2:
        return f"{g[0]}/{g[1]}" if g[0] == g[1] else "/".join(sorted(g))
    return g


def parse_wgs_rs_genotypes(wgs: str) -> dict[str, str]:
    """Wyciągnij genotypy z bloku WGS: `rs123` — **CC**."""
    found: dict[str, str] = {}
    for line in (wgs or "").splitlines():
        m = re.search(
            r"`?(rs\d+)`?\s*[—–\-]\s*\*\*([A-Z0-9/]+)\*\*",
            line,
            flags=re.I,
        )
        if not m:
            continue
        rs = m.group(1).lower()
        gt = m.group(2).upper()
        if gt not in SKIP_GT:
            found[rs] = gt
    return found


GENOTYPE_IN_TITLE = re.compile(
    r"^(?:genotyp|diplotyp)\s+([ACGT0-9]+/[ACGT0-9]+)",
    re.I,
)


def genotype_from_title(title: str) -> str | None:
    bare = GENOTYPE_PREFIX.sub("", title.strip()).strip()
    m = GENOTYPE_IN_TITLE.match(title.strip())
    if m:
        return norm_genotype(m.group(1))
    m = re.match(r"^([ACGT0-9]+/[ACGT0-9]+|\d+R/\d+R)\s*(?:\(|$)", bare, re.I)
    if m:
        return norm_genotype(m.group(1))
    return None


def genotype_variants(value: str) -> set[str]:
    raw = (value or "").upper().strip("`*★ ")
    variants: set[str] = set()
    if not raw or raw in SKIP_GT:
        return variants
    if "/" in raw:
        a, b = raw.split("/", 1)
        variants.add(norm_genotype(f"{a}/{b}"))
        variants.add(norm_genotype(f"{a.translate(COMPLEMENT)}/{b.translate(COMPLEMENT)}"))
        return {v for v in variants if v}
    if len(raw) == 2:
        variants.add(norm_genotype(f"{raw[0]}/{raw[1]}"))
        comp = raw.translate(COMPLEMENT)
        variants.add(norm_genotype(f"{comp[0]}/{comp[1]}"))
    variants.add(norm_genotype(raw))
    return {v for v in variants if v}


def alleles_equivalent(left: str, right: str) -> bool:
    return left == right or left.translate(COMPLEMENT) == right


def diploid_matches_strand(row_genotype: str, user_genotype: str) -> bool:
    row = norm_genotype(row_genotype)
    user = user_gt_to_slash(user_genotype)
    if "/" not in row or "/" not in user:
        return False
    u_a, u_b = user.split("/", 1)
    a, b = row.split("/", 1)
    for left, right in ((u_a, u_b), (u_b, u_a)):
        if alleles_equivalent(left, a) and alleles_equivalent(right, b):
            return True
        if alleles_equivalent(left, b) and alleles_equivalent(right, a):
            return True
    return False


def genotype_matches_user(row_genotype: str, user_genotype: str) -> bool:
    row = norm_genotype(row_genotype)
    if not row or row in {"—", "-"}:
        return False
    if row in genotype_variants(user_genotype):
        return True
    return diploid_matches_strand(row, user_genotype)


def is_hom_wgs(user_genotype: str) -> bool:
    u = user_genotype.upper().strip()
    return len(u) == 2 and u[0] == u[1] and u.isalpha()


def is_het_wgs(user_genotype: str) -> bool:
    u = user_genotype.upper().strip()
    return len(u) == 2 and u[0] != u[1] and u.isalpha()


def user_gt_to_slash(user_genotype: str) -> str:
    user = user_genotype.upper().strip()
    if "/" in user:
        return norm_genotype(user)
    if len(user) == 2 and user.isalpha():
        return norm_genotype(f"{user[0]}/{user[1]}")
    return user


def direct_diploid_match(row_genotype: str, user_genotype: str) -> bool:
    row = norm_genotype(row_genotype)
    user = user_gt_to_slash(user_genotype)
    if not row or row in {"—", "-"} or "/" not in row:
        return False
    if "/" not in user:
        return False
    return user == row


def het_row_indices(genotypes: list[str]) -> list[int]:
    indices: list[int] = []
    for i, gt in enumerate(genotypes):
        if "/" not in gt:
            continue
        a, b = gt.split("/", 1)
        if a != b:
            indices.append(i)
    return indices


def matched_profile_score(title: str, short_desc: str, matched: str | None) -> int:
    if not matched:
        return 0
    title_clean = re.sub(r"\s+", " ", title.strip().lower())
    short_clean = re.sub(r"\s+", " ", short_desc.strip().lower())
    matched_clean = re.sub(r"\s+", " ", matched.strip().lower())
    if matched_clean == title_clean:
        return 120
    if matched_clean in title_clean or title_clean in matched_clean:
        return 110
    if matched_clean in short_clean:
        return 100
    matched_gt = genotype_from_title(matched)
    title_gt = genotype_from_title(title)
    if matched_gt and title_gt and matched_gt == title_gt:
        return 95
    return 0


def user_profile_index(
    user_genotype: str | None,
    ref: str | None,
    alt: str | None,
    total: int,
) -> int | None:
    if not user_genotype or not ref or not alt or total < 1:
        return None
    hom_user = is_hom_wgs(user_genotype)
    het_user = is_het_wgs(user_genotype)
    for i in range(total):
        expected = genotype_from_alleles(ref, alt, i, total)
        if "/" not in expected:
            continue
        exp_a, exp_b = expected.split("/", 1)
        if hom_user and exp_a != exp_b:
            continue
        if het_user and exp_a == exp_b:
            continue
        if direct_diploid_match(expected, user_genotype):
            return i
        if het_user and diploid_matches_strand(expected, user_genotype):
            return i
    return None


def personal_row_score(
    title: str,
    short_desc: str,
    row_genotype: str,
    matched: str | None,
    user_genotype: str | None,
    *,
    row_index: int,
    total_profiles: int,
    ref: str | None,
    alt: str | None,
    uses_report_alleles: bool = False,
    tones: list[str] | None = None,
) -> int:
    score = matched_profile_score(title, short_desc, matched)
    expected_idx = (
        user_profile_index(user_genotype, ref, alt, total_profiles)
        if user_genotype and ref and alt
        else None
    )

    row_parts = norm_genotype(row_genotype).split("/", 1)
    row_is_hom = len(row_parts) == 2 and row_parts[0] == row_parts[1]

    if user_genotype and row_genotype and row_genotype not in {"—", "-"}:
        if uses_report_alleles:
            if is_hom_wgs(user_genotype) and row_is_hom and direct_diploid_match(
                row_genotype, user_genotype
            ):
                score = max(score, 100)
            elif is_het_wgs(user_genotype) and not row_is_hom:
                if direct_diploid_match(row_genotype, user_genotype):
                    score = max(score, 100)
                elif diploid_matches_strand(row_genotype, user_genotype):
                    score = max(score, 92)
        else:
            title_gt = genotype_from_title(title)
            if title_gt and genotype_matches_user(title_gt, user_genotype):
                score = max(score, 90)
            if direct_diploid_match(row_genotype, user_genotype):
                score = max(score, 80)
            elif is_hom_wgs(user_genotype) and row_is_hom and genotype_matches_user(
                row_genotype, user_genotype
            ):
                score = max(score, 80)
            elif is_het_wgs(user_genotype) and not row_is_hom and genotype_matches_user(
                row_genotype, user_genotype
            ):
                score = max(score, 80)
            if expected_idx is not None and row_index == expected_idx:
                score = max(score, 85)

    if uses_report_alleles and expected_idx is not None and ref and alt:
        expected_gt = genotype_from_alleles(ref, alt, expected_idx, total_profiles)
        exp_parts = norm_genotype(expected_gt).split("/", 1)
        exp_is_hom = len(exp_parts) == 2 and exp_parts[0] == exp_parts[1]
        if is_hom_wgs(user_genotype or "") and row_is_hom and exp_is_hom:
            if norm_genotype(row_genotype) == norm_genotype(expected_gt):
                score = max(score, 95)
        elif is_het_wgs(user_genotype or "") and not row_is_hom and not exp_is_hom:
            if norm_genotype(row_genotype) == norm_genotype(expected_gt):
                score = max(score, 95)
            elif diploid_matches_strand(row_genotype, expected_gt):
                score = max(score, 93)

    if (
        uses_report_alleles
        and expected_idx is not None
        and row_index == expected_idx
        and tones
        and expected_idx < len(tones)
        and row_index < len(tones)
        and tones[row_index] == tones[expected_idx]
    ):
        if is_hom_wgs(user_genotype or "") or (
            is_het_wgs(user_genotype or "") and expected_idx == 1
        ):
            score = max(score, 88)

    return score


def personal_row_fallback_score(
    row_index: int,
    row_genotype: str,
    user_genotype: str | None,
    *,
    all_genotypes: list[str],
    expected_idx: int | None,
    tones: list[str] | None,
) -> int:
    if not user_genotype:
        return 0
    het_rows = het_row_indices(all_genotypes)
    hom_rows = [
        i
        for i, gt in enumerate(all_genotypes)
        if "/" in gt and gt.split("/", 1)[0] == gt.split("/", 1)[1]
    ]
    if is_het_wgs(user_genotype) and len(het_rows) == 1 and row_index == het_rows[0]:
        return 86
    if is_hom_wgs(user_genotype) and expected_idx is not None and row_index == expected_idx:
        return 84
    if (
        is_hom_wgs(user_genotype)
        and expected_idx is not None
        and tones
        and expected_idx < len(tones)
        and row_index < len(tones)
        and tones[row_index] == tones[expected_idx]
        and row_genotype in {"—", "-"}
    ):
        return 82
    if (
        is_hom_wgs(user_genotype)
        and len(hom_rows) == 2
        and expected_idx is not None
        and row_index == hom_rows[0]
        and expected_idx == 0
    ):
        return 81
    if (
        is_hom_wgs(user_genotype)
        and all(gt in {"—", "-"} for gt in all_genotypes)
        and row_index == 0
        and tones
        and tones[0] == "positive"
    ):
        return 80
    if (
        is_het_wgs(user_genotype)
        and expected_idx is None
        and het_rows
        and row_index == het_rows[0]
    ):
        return 85
    return 0


def user_genotype_for_rsid(
    rsid_key: str | None,
    wgs_rs: dict[str, str],
) -> str | None:
    if rsid_key and rsid_key in wgs_rs:
        return wgs_rs[rsid_key]
    for _rs, gt in wgs_rs.items():
        if gt not in SKIP_GT:
            return gt
    return None


def esc_table_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def format_genotype_cell(genotype: str, star: str) -> str:
    g = esc_table_cell(genotype)
    if g in {"—", "-"}:
        return f"{star}{g}"
    if "*" in g:
        return f"{star}`{g}`"
    if STRUCTURAL_GENOTYPE_RE.match(g):
        return f"**{star}{g}**"
    return f"**{star}{g}**"


# Ręczna kolorystyka profili minikart (edytuj tutaj, potem uruchom build_mini_gene_cards.py).
# Klucz: SYMBOL_GENU -> lista tonów w kolejności wierszy tabeli (positive | neutral | negative).
MANUAL_PROFILE_TONES: dict[str, list[str]] = {
    "GRM5": ["positive", "neutral", "neutral"],
    "AKAP11": ["positive", "neutral", "neutral"],
    "PTEN": ["positive", "neutral", "neutral"],
    "RIMS1": ["positive", "neutral", "neutral"],
    "UBE3A": ["positive", "neutral", "negative"],
    "MSRA": ["positive", "neutral", "neutral"],
    "NEGR1": ["positive", "neutral", "neutral"],
    "SHISA9": ["positive", "neutral", "neutral"],
    "USP35": ["positive", "neutral", "neutral"],
    "MDFIC": ["positive", "neutral", "neutral"],
}

# Gdy myvariant zwraca A/T, a call z BAM/Ensembl to G/G (wieloalleliczny A/G/T).
ALLELE_OVERRIDES: dict[str, tuple[str, str]] = {
    "rs2797285": ("G", "A"),
}


def default_profile_tones(count: int) -> list[str]:
    if count >= 3:
        return ["positive"] + ["neutral"] * (count - 2) + ["negative"]
    if count == 2:
        return ["positive", "neutral"]
    if count == 1:
        return ["neutral"]
    return []


def profile_tones_for_gene(gene: str, count: int) -> list[str]:
    manual = MANUAL_PROFILE_TONES.get(gene.upper())
    if manual and len(manual) >= count:
        return manual[:count]
    return default_profile_tones(count)


def build_card(
    gene: str,
    body: str,
    *,
    allele_cache: dict[str, dict],
) -> str:
    meta = parse_metadata(body)
    wgs, matched = parse_wgs_block(body)
    profiles = parse_profiles(body)
    wgs_rs_early = parse_wgs_rs_genotypes(wgs)
    meta_rs = primary_rsid(meta.get("rsid", ""))
    wgs_primary = primary_wgs_rsid(wgs, wgs_rs_early)

    def resolved_wgs_call(rsid: str | None) -> bool:
        if not rsid:
            return False
        gt = wgs_rs_early.get(rsid.lower(), "")
        return bool(
            gt
            and gt not in SKIP_GT
            and "/" not in gt
            and len(gt) == 2
            and gt.isalpha()
        )

    if meta_rs and resolved_wgs_call(meta_rs):
        rsid_key = meta_rs
    elif wgs_primary:
        rsid_key = wgs_primary
    else:
        rsid_key = meta_rs or rsid_from_wgs(wgs)
    ref, alt = allele_info_for_rsid(rsid_key, allele_cache)
    if rsid_key and rsid_key.lower() in ALLELE_OVERRIDES:
        ref, alt = ALLELE_OVERRIDES[rsid_key.lower()]
    if not ref:
        for rs in re.findall(r"rs\d+", wgs or "", flags=re.I):
            ref2, alt2 = allele_info_for_rsid(rs.lower(), allele_cache)
            if ref2 and alt2:
                rsid_key, ref, alt = rs.lower(), ref2, alt2
                break
    if not ref:
        for rs in wgs_rs_early:
            ref2, alt2 = allele_info_for_rsid(rs, allele_cache)
            if ref2 and alt2:
                rsid_key, ref, alt = rs, ref2, alt2
                break

    symbol = meta.get("symbol", gene)
    fullname = meta.get("fullname", "—")
    aliases = meta.get("aliases", "—")
    rsid = meta.get("rsid", "—")
    location = meta.get("location", "—")
    role = meta.get("role", "—")

    cnv_only = is_cnv_only_gene(meta, profiles)
    tones = profile_tones_for_gene(gene, len(profiles))
    wgs_rs = wgs_rs_early
    user_gt = user_genotype_for_rsid(rsid_key, wgs_rs)
    if not user_gt:
        user_gt = user_genotype_for_rsid(None, wgs_rs)
    total_profiles = len(profiles)
    uses_report_alleles = (
        not cnv_only
        and (
            any(genotype_from_title(t) for t, _ in profiles)
            or bool(user_gt and len(user_gt) == 2 and user_gt.isalpha())
        )
    )
    built_rows: list[tuple[str, str, str, str, str]] = []
    for i, (title, desc) in enumerate(profiles):
        genotype, short_desc, long_desc = split_profile(title, desc)
        if not long_desc.strip():
            long_desc = desc.strip()
        if cnv_only:
            short_desc, long_desc = ensure_short_desc(title, "", long_desc, cnv_only=True)
        else:
            short_desc, long_desc = ensure_short_desc(title, short_desc, long_desc)
        if not short_desc and long_desc:
            parts = re.split(r"(?<=[.!?])\s+", long_desc, maxsplit=1)
            if len(parts) == 2 and len(parts[0]) <= 120:
                short_desc, long_desc = parts[0].strip(), parts[1].strip()
        title_gt = genotype_from_title(title)
        if cnv_only or is_cnv_deletion_profile(title, short_desc, long_desc):
            genotype = "—"
        elif title_gt:
            genotype = title_gt
        elif (
            ref
            and alt
            and rsid_key
            and not STAR_ALLELE_RE.match(genotype)
            and not VNTR_GENOTYPE_RE.match(genotype)
            and not STRUCTURAL_GENOTYPE_RE.match(genotype)
        ):
            genotype = genotype_from_alleles(ref, alt, i, total_profiles)
        elif is_resolved_genotype(genotype):
            genotype = resolve_genotype(
                genotype,
                index=i,
                total=total_profiles,
                ref=ref,
                alt=alt,
            )
        else:
            genotype = "—"
        tone = tones[i] if i < len(tones) else "neutral"
        built_rows.append((title, short_desc, long_desc, genotype, tone))

    built_rows = dedupe_built_rows(built_rows, matched=matched)
    tones = profile_tones_for_gene(gene, len(built_rows))
    for i, row in enumerate(built_rows):
        built_rows[i] = (row[0], row[1], row[2], row[3], tones[i] if i < len(tones) else row[4])

    total_profiles = len(built_rows)
    all_genotypes = [row[3] for row in built_rows]
    expected_idx = (
        user_profile_index(user_gt, ref, alt, total_profiles)
        if user_gt and ref and alt and not cnv_only
        else None
    )
    personal_idx = -1
    personal_best = 0

    if cnv_only and user_gt and total_profiles == 3:
        if is_het_wgs(user_gt):
            personal_idx = 1
            personal_best = 100
        elif is_hom_wgs(user_gt):
            personal_idx = 0
            personal_best = 90
            for i, (title, short_desc, _long, _gt, _tone) in enumerate(built_rows):
                if matched_profile_score(title, short_desc, matched) >= 90:
                    personal_idx = i
                    personal_best = 100
                    break
    if personal_best == 0:
        for i, (title, short_desc, _long, genotype, _tone) in enumerate(built_rows):
            score = personal_row_score(
                title,
                short_desc,
                genotype,
                matched,
                user_gt,
                row_index=i,
                total_profiles=total_profiles,
                ref=ref,
                alt=alt,
                uses_report_alleles=uses_report_alleles,
                tones=tones,
            )
            score = max(
                score,
                personal_row_fallback_score(
                    i,
                    genotype,
                    user_gt,
                    all_genotypes=all_genotypes,
                    expected_idx=expected_idx,
                    tones=tones,
                ),
            )
            if score > personal_best:
                personal_best = score
                personal_idx = i

    rows: list[str] = []
    for i, (title, short_desc, long_desc, genotype, tone) in enumerate(built_rows):
        star = "★ " if i == personal_idx and personal_best > 0 else ""
        rows.append(
            f"| {format_genotype_cell(genotype, star)} | {esc_table_cell(short_desc)} | {tone} | {esc_table_cell(long_desc)} |"
        )
    if not rows:
        rows.append(
            "| **—** | Profil populacyjny | neutral | Brak szczegółowej tabeli wariantów w raporcie źródłowym. |"
        )

    display_rsid = rsid
    primary = primary_rsid(rsid)
    if primary and re.search(r"rs\d+", rsid, re.I):
        display_rsid = primary
    if rsid_key and rsid_key.startswith("rs") and not resolved_wgs_call(primary_rsid(rsid or "")):
        display_rsid = rsid_key

    rsid_label = display_rsid.split("/")[0].strip()
    if rsid_label.startswith("rs"):
        table_title = f"**{rsid_label}**"
    else:
        table_title = f"**{gene} — warianty**"

    return f"""### 1. Nagłówek i Nazwy
* **Główny symbol genu:** {symbol}
* **Pełna nazwa biochemiczna:** {fullname}
* **Nazwy potoczne i medialne:** {aliases}

### 2. Identyfikator (rsID)
* **Główny rsID / wariant:** {display_rsid}
* **Lokalizacja chromosomalna:** {location}

### 3. Mechanizm działania
* **Rola biologiczna genu/białka:** {role}

### 4. Tabela Wariantów
{table_title}

| Genotyp | Opis krótki | Ton | Wpływ fenotypowy |
| :--- | :--- | :--- | :--- |
{chr(10).join(rows)}
"""


def collect_mini_rsids(sections: list[tuple[str, str]], existing: set[str]) -> set[str]:
    rsids: set[str] = set()
    for gene, body in sections:
        if gene.upper() in existing:
            continue
        meta = parse_metadata(body)
        rs = primary_rsid(meta.get("rsid", ""))
        if rs:
            rsids.add(rs)
    return rsids


def main() -> int:
    existing = {p.stem.upper() for p in MD_DIR.glob("*.md")}
    text = REPORT.read_text(encoding="utf-8")
    sections = parse_sections(text)
    rsids = collect_mini_rsids(sections, existing)
    print(f"[info] Pobieranie alleli dla {len(rsids)} rsID (myvariant.info)…", flush=True)
    allele_cache = ensure_alleles(rsids)

    OUT_DIR.mkdir(exist_ok=True)
    mini_genes: list[str] = []

    for gene, body in sections:
        if gene.upper() in existing:
            continue
        card = build_card(gene, body, allele_cache=allele_cache)
        (OUT_DIR / f"{gene.upper()}.md").write_text(card, encoding="utf-8")
        mini_genes.append(gene.upper())

    mini_genes.sort()
    js_lines = [
        "/** Geny z uproszczoną minikartą md-mini/ (bez pełnej karty md/). */",
        "window.GENES_WITH_MINI = new Set([",
    ]
    js_lines += [f'  "{g}",' for g in mini_genes]
    js_lines.append("]);")
    js_lines.append("")
    OUT_JS.write_text("\n".join(js_lines), encoding="utf-8")

    print(f"[done] {len(mini_genes)} minikart -> {OUT_DIR.name}/")
    print(f"[done] {OUT_JS.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
