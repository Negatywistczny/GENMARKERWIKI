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
REPORT = ROOT / "raporty" / "markery" / "Zbiorowe badanie markerów.md"
MD_DIR = ROOT / "md"
OUT_DIR = ROOT / "md-mini"
OUT_JS = ROOT / "html" / "genes-with-mini.js"
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
    r"główny (symbol|rsid)|pełna nazwa|lokalizacja|rola biologiczna|nazwy potoczne|dopasowany profil|mój genotyp",
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
    "rsid": re.compile(r"główny rsid", re.I),
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


def is_cnv_deletion_profile(title: str, short_desc: str, long_desc: str) -> bool:
    """Warianty strukturalne bez pojedynczego genotypu nukleotydowego."""
    blob = f"{title} {short_desc} {long_desc}".lower()
    return bool(re.search(r"\bcnv\b|delecj|rearanż", blob))


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

    return profiles[:4]


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


def genotype_from_title(title: str) -> str | None:
    bare = GENOTYPE_PREFIX.sub("", title.strip()).strip()
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
    user = user_genotype.upper().strip()
    if "/" not in row or len(user) != 2 or "/" in user:
        return False
    a, b = row.split("/", 1)
    for left, right in ((user[0], user[1]), (user[1], user[0])):
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
    for i in range(total):
        expected = genotype_from_alleles(ref, alt, i, total)
        if genotype_matches_user(expected, user_genotype):
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
    use_dbsnp_index: bool = True,
) -> int:
    score = matched_profile_score(title, short_desc, matched)
    title_gt = genotype_from_title(title)
    if user_genotype and title_gt and genotype_matches_user(title_gt, user_genotype):
        score = max(score, 90)
    if use_dbsnp_index:
        expected_idx = user_profile_index(user_genotype, ref, alt, total_profiles)
        if expected_idx is not None and row_index == expected_idx:
            score = max(score, 85)
    if user_genotype and genotype_matches_user(row_genotype, user_genotype):
        score = max(score, 80)
    return score


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
    # Przykład — dopisz lub nadpisz per gen:
    # "HTR1B": ["positive", "neutral", "negative"],
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
    rsid_key = primary_rsid(meta.get("rsid", "")) or rsid_from_wgs(wgs)
    ref, alt = allele_info_for_rsid(rsid_key, allele_cache)
    wgs_rs_early = parse_wgs_rs_genotypes(wgs)
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

    tones = profile_tones_for_gene(gene, len(profiles))
    wgs_rs = wgs_rs_early
    user_gt = user_genotype_for_rsid(rsid_key, wgs_rs)
    if not user_gt:
        user_gt = user_genotype_for_rsid(None, wgs_rs)
    total_profiles = len(profiles)
    uses_report_alleles = any(genotype_from_title(t) for t, _ in profiles)
    built_rows: list[tuple[str, str, str, str, str]] = []
    for i, (title, desc) in enumerate(profiles):
        genotype, short_desc, long_desc = split_profile(title, desc)
        if not short_desc and long_desc:
            parts = re.split(r"(?<=[.!?])\s+", long_desc, maxsplit=1)
            if len(parts) == 2 and len(parts[0]) <= 120:
                short_desc, long_desc = parts[0].strip(), parts[1].strip()
        title_gt = genotype_from_title(title)
        if is_cnv_deletion_profile(title, short_desc, long_desc):
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

    personal_idx = -1
    personal_best = 0
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
            use_dbsnp_index=not uses_report_alleles,
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

    wgs_section = ""
    if wgs:
        wgs_bullets = "\n".join(
            f"  * {ln.strip().lstrip('-* ').strip()}" for ln in wgs.splitlines() if ln.strip()
        )
        wgs_section = f"\n* **Mój genotyp (WGS):**\n{wgs_bullets}\n"
        if matched:
            wgs_section += f"* **Dopasowany profil:** {matched}\n"

    rsid_label = rsid.split("/")[0].strip()
    if rsid_label.startswith("rs"):
        table_title = f"**{rsid_label}**"
    else:
        table_title = f"**{gene} — warianty**"

    return f"""### 1. Nagłówek i Nazwy
* **Główny symbol genu:** {symbol}
* **Pełna nazwa biochemiczna:** {fullname}
* **Nazwy potoczne i medialne:** {aliases}

### 2. Identyfikator (rsID)
* **Główny rsID / wariant:** {rsid}
* **Lokalizacja chromosomalna:** {location}

### 3. Mechanizm działania
* **Rola biologiczna genu/białka:** {role}
{wgs_section}
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
        wgs, _ = parse_wgs_block(body)
        rsids.update(parse_wgs_rs_genotypes(wgs).keys())
        for rs in re.findall(r"rs\d+", wgs or "", flags=re.I):
            rsids.add(rs.lower())
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

    print(f"[done] {len(mini_genes)} minikart → {OUT_DIR.name}/")
    print(f"[done] {OUT_JS.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
