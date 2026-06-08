#!/usr/bin/env python3
"""Uproszczone karty md/ (sekcje 1–4) dla genów tematów — bez boilerplate'u."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
RISK_DIR = ROOT / "raporty" / "ryzyko"
WORK = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work")
GENE_RSIDS_JS = ROOT / "html" / "gene-rsids.js"
GENE_INDEX_JS = ROOT / "html" / "gene-index.js"
CARD_MARKER = "<!-- topic-card -->"

sys.path.insert(0, str(ROOT / "scripts"))
from build_topic_gene_profiles import (  # noqa: E402
    BAZA_ROW,
    SKIP_GENES,
    canonical_gene,
    load_baza_gene_info,
    load_gene_variant_rows,
    load_rsid_genotypes,
    topic_genes,
    wiki_genes,
)

STAR = "★"
MAX_SNPS = 2

GENERIC_EVIDENCE = (
    "sygnatura molekularna",
    "ryzyko poligenowe",
    "gen przyczynowy (twas)",
    "wariant podwyższonego ryzyka",
    "wariant funkcjonalny (prs)",
    "wariant funkcjonalny (eqtl)",
    "wariant funkcjonalny",
    "assoc. gwas",
    "kandydat adhd",
    "gwas adhd",
    "funkcjonalny",
    "marker biotypu",
)

# Etykiety meta z kolumny „Poziom ryzyka” / evidence — nie treść kliniczna
METADATA_EVIDENCE = (
    "wysoka pewność",
    "kategoria 1",
    "kategoria 2",
    "kategoria s",
    "credible gene",
    "wiarygodność",
    "biotyp",
    "pan-biotypowy",
    "szeroko obciążony",
    "gen priorytetowy",
    "profil farmakogenetyczny",
    "plejotropowe",
    "modyfikator farmakoterapii",
    "ryzyko strukturalne",
    "cel terapeutyczny",
    "predyktor",
    "wariant ryzyka",
    "ryzyko poligenowe (gwas)",
    "ryzyko poligenowe (prs)",
    "gen przyczynowy",
    "wariant podwyższonego ryzyka",
    "sygnatura molekularna",
    "modyfikator",
    "profil farmakogenetyczny",
    "marker dobrej",
    "silny marker",
    "silny kandydat",
    "wysoka wiarygodność",
)

GENE_EN: dict[str, str] = {
    "ADGRL3": "Adhesion G protein-coupled receptor L3",
    "DRD4": "Dopamine receptor D4",
    "DRD5": "Dopamine receptor D5",
    "HTR2A": "5-hydroxytryptamine receptor 2A",
    "HTR1B": "5-hydroxytryptamine receptor 1B",
    "HTR4": "5-hydroxytryptamine receptor 4",
    "CHRNA4": "Neuronal acetylcholine receptor subunit alpha-4",
    "CHRNA7": "Neuronal acetylcholine receptor subunit alpha-7",
    "CNR1": "Cannabinoid receptor 1",
    "GRM5": "Metabotropic glutamate receptor 5",
    "HRH3": "Histamine H3 receptor",
    "SLC6A2": "Sodium-dependent noradrenaline transporter",
    "SLC6A3": "Sodium-dependent dopamine transporter",
    "ASTN2": "Astrotactin-2",
    "SORCS3": "VPS10 domain-containing receptor SorCS3",
    "PTPRF": "Receptor-type tyrosine-protein phosphatase F",
    "FOXP2": "Forkhead box protein P2",
    "NKX2-2": "Homeobox protein Nkx-2.2",
    "CHD8": "Chromodomain-helicase-DNA-binding protein 8",
    "GRIN2B": "Glutamate receptor ionotropic, NMDA 2B",
    "SHANK3": "SH3 and multiple ankyrin repeat domains 3",
    "SYNGAP1": "Synaptic Ras GTPase-activating protein 1",
    "DYRK1A": "Dual specificity tyrosine-phosphorylation-regulated kinase 1A",
    "ARID1B": "AT-rich interactive domain-containing protein 1B",
    "FMR1": "Fragile X messenger ribonucleoprotein 1",
    "ANK2": "Ankyrin-2",
    "AKAP11": "A-kinase anchor protein 11",
    "MC4R": "Melanocortin 4 receptor",
    "SCN2A": "Voltage-gated sodium channel subunit alpha-2",
}

MANUAL_LEAD: dict[str, list[str]] = {
    "AKAP11": ["rs1400929"],
    "NEGR1": ["rs2568958"],
    "NCAN": ["rs1064395"],
    "KCNQ3": ["rs11706909"],
    "SHISA9": ["rs1700"],
    "GSK3B": ["rs334558"],
    "MC4R": ["rs17782313"],
    "FOXP2": ["rs7458242"],
    "GRIN2A": ["rs4958676"],
    "GRIN2B": ["rs7301328"],
    "CHD8": ["rs60316800"],
    "ARID1B": ["rs1124619"],
    "PTEN": ["rs701848"],
    "DYRK1A": ["rs2834171"],
    "UBE3A": ["rs1868188"],
    "TCF4": ["rs9960767"],
    "BCL11B": ["rs6542787"],
}


def norm_gt(g: str) -> str:
    g = g.strip().upper()
    if not g:
        return g
    if "/" in g:
        parts = sorted(p.strip() for p in g.split("/") if p.strip())
        return "/".join(parts)
    if len(g) == 2 and g[0] != g[1]:
        return "/".join(sorted(g))
    if len(g) == 2:
        return f"{g[0]}/{g[1]}"
    return g


def is_generic_evidence(text: str) -> bool:
    low = text.lower().strip()
    if not low:
        return True
    return any(m in low for m in GENERIC_EVIDENCE) or is_metadata_evidence(text)


def is_metadata_evidence(text: str) -> bool:
    low = text.lower().strip()
    if not low:
        return True
    if re.match(r"^(biotyp|pan-biotypowy|wariant|ryzyko|gen|marker|sygnatura|profil|modyfikator)", low):
        return True
    return any(m in low for m in METADATA_EVIDENCE)


def looks_like_mechanism_not_name(text: str) -> bool:
    """Opis funkcji z Bazy — nie pełna nazwa biochemiczna."""
    low = text.lower()
    markers = (
        "organizacja",
        "transport",
        "receptor",
        "synap",
        "ekspresja",
        "modulacja",
        "regulacja",
        "rozwój",
        "rozwoj",
        "adhezja",
        "transporter",
        "enzym",
        "kanał",
        "kanal",
        "remodelowanie",
        "plastyczność",
        "plastycznosc",
        "sygnalizacja",
        "neurotransmis",
        "synteza",
        "konwersja",
        "beta-",
        "alfa-",
    )
    return any(m in low for m in markers) or ";" in text or len(text.split()) > 6


def clean_clinical(text: str) -> str:
    text = re.sub(r"\s*\d+\s*$", "", text.strip())
    text = re.sub(r"!\[\]\[[^\]]+\]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def load_kompendium_table() -> dict[str, dict]:
    """Symbol | nazwa | locus | mechanizm — tabele HGNC w Kompendium."""
    info: dict[str, dict] = {}
    pat = re.compile(
        r"^\|\s*(?:\*\*)?([A-Z0-9-]+)(?:\*\*)?\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|",
        re.M,
    )
    for path in RISK_DIR.glob("Kompendium*.md"):
        for m in pat.finditer(path.read_text(encoding="utf-8", errors="ignore")):
            g = canonical_gene(m.group(1))
            if not g:
                continue
            name = clean_clinical(m.group(2))
            loc_raw = m.group(3).strip()
            mech = clean_clinical(m.group(4))
            if len(name) < 2 or name.lower().startswith("symbol"):
                continue
            entry = info.setdefault(g, {})
            if name and (not entry.get("name_en") or len(name) > len(entry["name_en"])):
                entry["name_en"] = name
            if mech and (not entry.get("mechanism") or len(mech) > len(entry.get("mechanism", ""))):
                entry["mechanism"] = mech
            if loc_raw and not entry.get("loc"):
                if re.search(r"chr", loc_raw, re.I):
                    entry["loc"] = loc_raw
                elif re.search(r"[\dXYpq]", loc_raw):
                    entry["loc"] = loc_raw if loc_raw.startswith("chr") else f"chr{loc_raw}"
    return info


def load_kompendium_clinical() -> dict[str, str]:
    notes: dict[str, str] = {}
    pat = re.compile(r"\|\s*\*\*([^*]+)\*\*\s*\|([^|]+)\|([^|]+)\|")
    for path in RISK_DIR.glob("Kompendium*.md"):
        for m in pat.finditer(path.read_text(encoding="utf-8", errors="ignore")):
            g = canonical_gene(m.group(1))
            if not g:
                continue
            clin = clean_clinical(m.group(3))
            if len(clin) < 18 or is_generic_evidence(clin):
                continue
            if g not in notes or len(clin) > len(notes[g]):
                notes[g] = clin
    return notes


def load_topic_roles() -> dict[str, dict]:
    roles: dict[str, dict] = {}
    for rel in ("html/topic-psychiatry-sections.js", "html/topic-pages.js"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for m in re.finditer(
            r'symbol:\s*"([^"]+)"\s*,\s*role:\s*"([^"]+)"\s*,\s*evidence:\s*"([^"]*)"',
            text,
        ):
            g = canonical_gene(m.group(1))
            if not g:
                continue
            role, ev = m.group(2).strip(), m.group(3).strip()
            prev = roles.get(g, {})
            if len(role) > len(prev.get("role", "")):
                roles[g] = {"role": role, "evidence": ev or prev.get("evidence", "")}
            elif g not in roles:
                roles[g] = {"role": role, "evidence": ev}
    return roles


def load_baza_locations() -> dict[str, str]:
    locs: dict[str, str] = {}
    for path in sorted(RISK_DIR.glob("Baza *.md")):
        text = path.read_text(encoding="utf-8")
        for m in BAZA_ROW.finditer(text):
            g = canonical_gene(m.group(1))
            if not g:
                continue
            cell = m.group(0).split("|")[1].strip()
            chr_m = re.search(r"chr[\dXYpq]+\.?[\d\w-]*", cell, re.I)
            if chr_m:
                locs.setdefault(g, chr_m.group(0))
    return locs


def load_adhd_rsids() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    path = WORK / "adhd_genotypes.csv"
    if not path.exists():
        return out
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            g = canonical_gene(row.get("GENE", ""))
            rs = row.get("RSID", "").strip().upper()
            if g and rs.startswith("RS"):
                out.setdefault(g, [])
                if rs not in out[g]:
                    out[g].append(rs)
    return out


def load_raporty_rsids(genes: set[str]) -> dict[str, list[str]]:
    blob = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in (ROOT / "raporty").rglob("*.md")
    )
    found: dict[str, list[str]] = {}
    for g in genes:
        rsids: set[str] = set()
        pat1 = re.compile(rf"(?i)\b{re.escape(g)}\b[^\n]{{0,120}}?(rs\d+)")
        pat2 = re.compile(rf"(?i)(rs\d+)[^\n]{{0,80}}\b{re.escape(g)}\b")
        for m in pat1.finditer(blob):
            rsids.add(m.group(1).upper())
        for m in pat2.finditer(blob):
            rsids.add(m.group(1).upper())
        if rsids:
            found[g] = sorted(rsids)
    return found


def collect_rsids(
    gene: str,
    baza: dict,
    gene_rows: dict,
    adhd: dict,
    raporty: dict,
) -> list[str]:
    rs: list[str] = []
    if gene in gene_rows:
        rs.extend(r["rsid"].upper() for r in gene_rows[gene])
    if gene in baza:
        rs.extend(baza[gene].get("rsids", []))
    rs.extend(adhd.get(gene, []))
    rs.extend(MANUAL_LEAD.get(gene, []))
    rs.extend(raporty.get(gene, []))
    return list(dict.fromkeys(r.lower() for r in rs if r.upper().startswith("RS")))[:MAX_SNPS]


def wgs_gt(gene: str, rsid: str, gene_rows: dict, rsid_gt: dict) -> str | None:
    rs_l = rsid.lower()
    for row in gene_rows.get(gene, []):
        if row["rsid"].upper() == rsid.upper():
            gt = row["genotype"].strip().upper()
            if gt not in {"", "NOT_FOUND", "NO_CALL", "BRAK", "--"}:
                return gt
    return rsid_gt.get(rs_l)


PARTNER = {"A": "G", "G": "A", "C": "T", "T": "C"}


def infer_allele_pair(gt: str) -> tuple[str, str]:
    gt = gt.upper().replace("/", "")
    if len(gt) == 2 and gt[0] != gt[1]:
        return tuple(sorted(gt))
    if len(gt) >= 1:
        a = gt[0]
        b = PARTNER.get(a, "C")
        return tuple(sorted({a, b}))
    return ("C", "T")


def snp_triple(gt: str | None) -> tuple[list[str], int | None]:
    if not gt or gt in {"NOT_FOUND", "NO_CALL", "BRAK"}:
        return [], None
    gt = gt.upper()
    if "/" in gt and len(gt) > 3:
        return [], None
    a, b = infer_allele_pair(gt)
    hom1, het, hom2 = f"{a}/{a}", f"{a}/{b}", f"{b}/{b}"
    disp = [hom1.replace("/", ""), het, hom2.replace("/", "")]
    star = None
    ng = norm_gt(gt)
    for i, cand in enumerate([hom1, het, hom2]):
        if norm_gt(cand) == ng:
            star = i
            break
        flat = cand.replace("/", "")
        if gt.replace("/", "") == flat or gt == disp[i]:
            star = i
            break
    return disp, star


def role_clauses(role: str) -> list[str]:
    parts = [p.strip().rstrip(".") for p in re.split(r"[;]", role) if p.strip()]
    if not parts:
        return [role.strip().rstrip(".")]
    deduped = [parts[0]]
    for p in parts[1:]:
        if p.lower() not in deduped[0].lower():
            deduped.append(p)
    return deduped


def impact_substantive(imp: str, role: str) -> bool:
    """Czy wpis w §4 wnosi coś ponad sam skrót roli z sekcji 3."""
    t = imp.strip()
    if not t or len(t) < 10:
        return False
    low = t.lower()
    main = role_clauses(role)[0].lower()
    role_low = role.strip().lower().rstrip(".")
    if low == main or low == role_low:
        return False
    if low.startswith("częściowa modulacja:"):
        return False
    if main in low and len(low) <= len(main) + 8:
        return False
    return True


def impact_for_star(star: int, role: str, clinical: str) -> str:
    """Treść fenotypowa dla wiersza ★ (0=ref, 1=het, 2=alt)."""
    clauses = role_clauses(role)
    main = clauses[0]
    extra = clauses[1] if len(clauses) > 1 else ""
    if star == 1:
        return extra
    if star == 2:
        if clinical and clinical.lower() not in main.lower():
            return clinical.rstrip(".")
        return extra
    return ""


def section4_snp_block(
    rsid: str,
    role: str,
    clinical: str,
    gt: str | None,
    *,
    gene: str = "",
) -> str:
    # Ręczne tabele §4 utrzymywane w topic_wgs_variant_data.py — nie nadpisuj generykiem.
    try:
        from topic_wgs_variant_data import VARIANT_TABLES  # noqa: WPS433

        if gene.upper() in VARIANT_TABLES:
            return ""
    except ImportError:
        pass
    if not gt or gt in {"NOT_FOUND", "NO_CALL", "BRAK"}:
        return ""

    triple, star = snp_triple(gt)
    if not triple or star is None:
        return ""

    imp = impact_for_star(star, role, clinical)
    if not impact_substantive(imp, role):
        return ""

    imp = imp[0].upper() + imp[1:]
    label = triple[star]

    return "\n".join([
        f"**{rsid}**",
        "",
        "| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy (kliniczny i funkcjonalny) |",
        "| :--- | :--- | :--- |",
        f"| **{STAR} {label}** | — | {imp} |",
    ])


def build_section1(gene: str, name_en: str, name_pl: str | None) -> str:
    lines = [f"* **Główny symbol genu:** {gene}"]
    if name_pl:
        ang = GENE_EN.get(gene) or name_en
        if ang and ang.lower() not in name_pl.lower():
            lines.append(f"* **Pełna nazwa biochemiczna:** {name_pl} (ang. *{ang}*)")
        else:
            lines.append(f"* **Pełna nazwa biochemiczna:** {name_pl}")
    elif GENE_EN.get(gene):
        lines.append(f"* **Pełna nazwa biochemiczna:** {GENE_EN[gene]}")
    return "### 1. Nagłówek i Nazwy\n" + "\n".join(lines)


def build_section2(rsids: list[str], loc: str) -> str:
    lines = ["### 2. Identyfikator (rsID) i Charakterystyka Wariantu"]
    if rsids:
        lines.append(f"* **Główny rsID:** {rsids[0]}")
    if loc:
        lines.append(f"* **Lokalizacja chromosomalna:** {loc}")
    if len(rsids) > 1:
        lines.append(f"* **Powiązane markery:** {', '.join(rsids[1:])}")
    if len(lines) == 1:
        return ""
    return "\n".join(lines)


def build_section3(role: str, clinical: str) -> str:
    lines = [
        "### 3. Mechanizm działania",
        f"* **Rola biologiczna genu/białka:** {role.rstrip('.')}.",
    ]
    clin = clinical.rstrip(".") if clinical else ""
    role_clean = role.rstrip(".")
    if clin and clin.lower() != role_clean.lower() and clin.lower() not in role_clean.lower():
        lines.append(f"* **Efekt funkcjonalny:** {clin}.")
    return "\n".join(lines)


def build_section4(
    rsids: list[str],
    role: str,
    clinical: str,
    gene_rows: dict,
    gene: str,
    rsid_gt: dict,
) -> str:
    if not rsids:
        return ""
    blocks = []
    for rs in rsids:
        gt = wgs_gt(gene, rs, gene_rows, rsid_gt)
        block = section4_snp_block(rs, role, clinical, gt, gene=gene)
        if block:
            blocks.append(block)
    if not blocks:
        return ""
    return "### 4. Tabela Wariantów\n\n" + "\n\n".join(blocks)


def build_card(
    gene: str,
    meta: dict,
    rsids: list[str],
    gene_rows: dict,
    rsid_gt: dict,
    loc: str,
    clinical: str,
    ktable: dict,
) -> str:
    role = meta.get("role", "").strip().rstrip(".")
    kinfo = ktable.get(gene, {})
    if kinfo.get("mechanism"):
        role = kinfo["mechanism"].rstrip(".")
    if not role:
        return ""

    name_en = kinfo.get("name_en", "")
    name_pl = polish_gene_name(name_en) if name_en else None
    loc = loc or kinfo.get("loc", "")

    parts = [build_section1(gene, name_en, name_pl)]
    sec2 = build_section2(rsids, loc)
    if sec2:
        parts.append(sec2)
    parts.append(build_section3(role, clinical))
    sec4 = build_section4(rsids, role, clinical, gene_rows, gene, rsid_gt)
    if sec4:
        parts.append(sec4)
    parts.append(CARD_MARKER)
    return "\n\n".join(parts)


def polish_gene_name(name_en: str) -> str:
    """Krótka polska etykieta z nazwy HGNC (Kompendium)."""
    n = name_en.strip()
    repl = {
        "Ankyrin 2, neuronal": "Ankyrin 2 (neuronalny)",
        "Chromodomain helicase DNA binding protein 8": "Białko CHD8 (remodelowanie chromatyny)",
        "Activity-dependent neuroprotector homeobox": "Neuroprotektor zależny od aktywności (ADNP)",
        "Fragile X messenger ribonucleoprotein 1": "Rybonukleoproteina FMR1 (zespół łamliwego X)",
    }
    return repl.get(n, n)


def update_gene_rsids(new_map: dict[str, list[str]]) -> None:
    text = GENE_RSIDS_JS.read_text(encoding="utf-8")
    for gene, rsids in sorted(new_map.items()):
        if not rsids:
            continue
        key = f'"{gene}"' if "-" in gene or not re.fullmatch(r"[A-Z0-9]+", gene) else gene
        block = ",\n".join(f'    "{r}"' for r in rsids)
        entry = f"  {key}: [\n{block},\n  ],"
        if re.search(rf"^\s+{re.escape(key)}:\s*\[", text, re.M):
            text = re.sub(
                rf"^\s+{re.escape(key)}:\s*\[[^\]]*\],?",
                entry,
                text,
                count=1,
                flags=re.M,
            )
        else:
            text = text.replace("\n};", f"\n{entry}\n}};")
    GENE_RSIDS_JS.write_text(text, encoding="utf-8")


def update_gene_index(new_genes: dict[str, str]) -> None:
    text = GENE_INDEX_JS.read_text(encoding="utf-8")
    for gene, label in sorted(new_genes.items()):
        if f'gene: "{gene}"' in text:
            continue
        short = label[:55] + ("…" if len(label) > 55 else "")
        entry = f'  {{ gene: "{gene}", label: "{short}", icon: "🧬", tone: "slate" }},'
        text = text.replace("\n];", f"\n{entry}\n];")
    GENE_INDEX_JS.write_text(text, encoding="utf-8")


def is_topic_card(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    if CARD_MARKER in text:
        return True
    return (
        "profil uproszczony — sekcje 1–4" in text
        or "Marker associacyjny" in text
        or "profil referencyjny" in text
    ) and "### 5." not in text


def main() -> None:
    force = "--force" in sys.argv
    wiki = wiki_genes()
    topics = topic_genes()
    baza = load_baza_gene_info()
    gene_rows = load_gene_variant_rows()
    rsid_gt = load_rsid_genotypes()
    topic_roles = load_topic_roles()
    locs = load_baza_locations()
    adhd = load_adhd_rsids()
    kompendium = load_kompendium_clinical()
    ktable = load_kompendium_table()

    if force:
        candidates = sorted(
            g for g in topics if g not in SKIP_GENES and is_topic_card(MD_DIR / f"{g}.md")
        )
    else:
        candidates = sorted(g for g in topics if g not in wiki and g not in SKIP_GENES)
    raporty_rs = load_raporty_rsids(set(candidates))

    created: list[str] = []
    rsid_map: dict[str, list[str]] = {}
    index_labels: dict[str, str] = {}

    for gene in candidates:
        meta = dict(baza.get(gene, {}))
        if gene in topic_roles:
            if not meta.get("role") or len(topic_roles[gene]["role"]) > len(meta.get("role", "")):
                meta["role"] = topic_roles[gene]["role"]
            if topic_roles[gene].get("evidence"):
                meta["evidence"] = topic_roles[gene]["evidence"]
        if not meta.get("role"):
            meta["role"] = topic_roles.get(gene, {}).get("role", "")
        if not meta.get("role"):
            continue

        clinical = kompendium.get(gene, "")
        if not clinical:
            clauses = role_clauses(meta["role"])
            clinical = clauses[1] if len(clauses) > 1 else ""

        rsids = collect_rsids(gene, baza, gene_rows, adhd, raporty_rs)
        rsid_map[gene] = rsids
        index_labels[gene] = meta["role"].split(";")[0][:60]

        path = MD_DIR / f"{gene}.md"
        card = build_card(
            gene, meta, rsids, gene_rows, rsid_gt, locs.get(gene, ""), clinical, ktable
        )
        if not card:
            continue
        path.write_text(card, encoding="utf-8")
        created.append(gene)

    if created:
        update_gene_rsids(rsid_map)
        update_gene_index(index_labels)

    print(f"Zaktualizowano {len(created)} kart md/")
    with_sec4 = sum(
        1
        for g in created
        if "### 4." in (MD_DIR / f"{g}.md").read_text(encoding="utf-8")
    )
    print(f"Sekcja 4 (tylko WGS + treść kliniczna): {with_sec4}")
    print(f"Bez sekcji 4: {len(created) - with_sec4}")


if __name__ == "__main__":
    main()
