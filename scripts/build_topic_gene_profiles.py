#!/usr/bin/env python3
"""Uzupełnij personal-gene-profiles.js o geny z tematów bez kart md/ (tylko z callami WGS)."""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "docs" / "genes"
RISK_DIR = ROOT / "data" / "reports" / "ryzyko"
OUT = ROOT / "public" / "html" / "personal-gene-profiles.js"
OUT_REPORT = ROOT / "data" / "reports" / "Raport-profile-tematow-bez-kart.md"
WORK = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work")

GENE_ALIASES = {
    "DAT1": "SLC6A3",
    "DAT": "SLC6A3",
    "5-HTT": "SLC6A4",
    "LPHN3": "ADGRL3",
    "MDR1": "ABCB1",
    "GR": "NR3C1",
    "MR": "NR3C2",
    "TAQ1A": "ANKK1",
}

SKIP_GENES = {
    "HLA-A", "HLA-B", "HLA-C", "HLA-DPA1", "HLA-DPB1", "HLA-DQA1", "HLA-DQB1",
    "HLA-DRA", "HLA-DRB1", "HLA-DRB5", "HLA-E", "HLA-F", "HLA-G", "MHC", "HLA",
    "XRN2", "NKX2-4",  # locus shared labels in ASD tables
}

TOPIC_KEYWORDS: dict[str, list[str]] = {
    "asd": ["autyzm", "asd", "mowa", "społeczn", "synap"],
    "adhd": ["adhd", "uwag", "metylofenidat", "impuls", "stymulant", "skupien"],
    "mdd": ["depresj", "mdd", "ssri", "snri", "nastrój", "nastroj", "lęk", "lek ", "anhedon", "ptsd"],
    "chad": ["dwubiegun", "chad", "mania", " lit", "afektyw", "bipolar"],
    "scz": ["schizofren", "psychoz", "antypsychot", "halucyn"],
    "neurodev": ["neurorozwoj", "padaczk", "epilep", " id", "rozwoj", "dee", "inteligencj"],
    "dopamine": ["dopamin", "rds", "nagrod", "prążkow", "prazkow", "dat1", "drd"],
    "serotonin": ["serotonin", "ssri", "5-htt", "5ht", "htl", "tryptofan", "htr"],
    "folate": ["folian", "homocyste", "metylac", "mthfr", "b12", "sam", "dhfr", "cbs"],
    "cyp": ["cyp", "metaboliz", "klirens", "dawka", "inhibitor", "substrat"],
    "psychopharm": ["farmak", " lek", "ssri", "metylofenidat", "antydepres", "antypsychot", "risper", "wenlaf"],
    "substances": ["kofein", "alkohol", "etanol", "nikotyn", "palen", "papieros", "chrna"],
    "nutrition": ["laktoz", "laktaz", "otyło", "bmi", "omega", "apetyt", "glikem", "mc4r"],
    "appearance": ["oczy", "skór", "pigment", "włos", "karnac", "melanin"],
    "smell-taste": ["smak", "gorycz", "węch", "wech", "zapach", "prop"],
    "cognition-aging": ["pamięć", "pamiec", "alzheimer", "apoe", "otępien", "otepien", "kognicj", "hipokamp", "negr1"],
    "sport": ["sport", "wytrzyma", "actn3", "mięśn", "miesn", "hiit", "trening"],
}

BAZA_ROW = re.compile(
    r"^\|[^|]+\|\s*\*\*([^*]+)\*\*\s*\|([^|]+)\|[^|]+\|\s*([^|]+)\s*\|",
    re.MULTILINE,
)
LOC_RS = re.compile(r"rs\d+", re.I)


def canonical_gene(raw: str) -> str | None:
    raw = raw.strip()
    if not raw:
        return None
    part = re.split(r"\s*/\s*", raw)[0].strip()
    paren = re.match(r"^([A-Z][A-Z0-9-]+)\s*\(", part)
    if paren:
        part = paren.group(1)
    else:
        part = re.sub(r"\s*\(.*$", "", part).strip()
    sym = part.upper()
    if sym in SKIP_GENES:
        return None
    return GENE_ALIASES.get(sym, sym)


def wiki_genes() -> set[str]:
    return {
        p.stem.upper()
        for p in MD_DIR.glob("*.md")
        if p.name != "UNIWERSALNY_SZABLON_MARKERA.md"
    }


TOPIC_GROUP_IDS = {"psychiatry", "pathways", "pgx", "lifestyle"}


def topic_genes() -> dict[str, set[str]]:
    """symbol -> set of topic ids."""
    by_gene: dict[str, set[str]] = defaultdict(set)

    # topic-pages.js — id: "asd" wewnątrz topics (pomijamy id grup)
    pages = (ROOT / "public" / "html" / "topic-pages.js").read_text(encoding="utf-8")
    for sym_m in re.finditer(r'symbol:\s*"([^"]+)"', pages):
        before = pages[: sym_m.start()]
        topic_id = None
        for id_m in re.finditer(r'\bid:\s*"([^"]+)"', before):
            tid = id_m.group(1)
            if tid not in TOPIC_GROUP_IDS:
                topic_id = tid
        if topic_id:
            g = canonical_gene(sym_m.group(1))
            if g:
                by_gene[g].add(topic_id)

    # topic-psychiatry-sections.js — asd: [ ... symbol: "GENE"
    psych = (ROOT / "public" / "html" / "topic-psychiatry-sections.js").read_text(encoding="utf-8")
    current: str | None = None
    for line in psych.splitlines():
        key_m = re.match(r"^\s{2}([a-z0-9-]+):\s*\[", line)
        if key_m:
            current = key_m.group(1)
            continue
        sym_m = re.search(r'symbol:\s*"([^"]+)"', line)
        if sym_m and current:
            g = canonical_gene(sym_m.group(1))
            if g:
                by_gene[g].add(current)

    return dict(by_gene)


def load_baza_gene_info() -> dict[str, dict]:
    """gene -> {role, evidence, rsids, sources}."""
    info: dict[str, dict] = {}
    for path in sorted(RISK_DIR.glob("Baza *.md")):
        text = path.read_text(encoding="utf-8")
        for m in BAZA_ROW.finditer(text):
            g = canonical_gene(m.group(1))
            if not g:
                continue
            role = m.group(2).strip()
            evidence = m.group(3).strip()
            loc_cell = m.group(0).split("|")[1] if "|" in m.group(0) else ""
            rsids = list(dict.fromkeys(r.upper() for r in LOC_RS.findall(loc_cell)))
            entry = info.setdefault(
                g,
                {"role": role, "evidence": evidence, "rsids": [], "sources": []},
            )
            if role and len(role) > len(entry.get("role", "")):
                entry["role"] = role
            if evidence:
                entry["evidence"] = evidence
            for rs in rsids:
                if rs not in entry["rsids"]:
                    entry["rsids"].append(rs)
            entry["sources"].append(path.name)
    return info


def load_rsid_genotypes() -> dict[str, str]:
    found: dict[str, str] = {}
    skip_gt = {"", "NOT_FOUND", "NO_CALL", "BRAK", "--"}

    def ingest(path: Path, rs_col: str = "RSID", gt_col: str = "RESULT") -> None:
        if not path.exists():
            return
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                return
            fields = {h.strip().upper(): h for h in reader.fieldnames}
            rs_key = fields.get(rs_col.upper()) or fields.get("RSID") or fields.get("rsid")
            gt_key = (
                fields.get(gt_col.upper())
                or fields.get("RESULT")
                or fields.get("GENOTYPE")
                or fields.get("result")
            )
            if not rs_key or not gt_key:
                return
            for row in reader:
                rs = row.get(rs_key, "").strip().lower()
                gt = row.get(gt_key, "").strip().upper()
                if rs.startswith("rs") and gt not in skip_gt:
                    found.setdefault(rs, gt)

    for path in sorted(WORK.glob("query_rsid*.csv")):
        ingest(path)
    ingest(WORK / "bam_genotypes_final.csv")
    ingest(WORK / "pharmaco_genotypes.csv")
    ingest(WORK / "neurodev_wiki_genotypes.csv")
    ingest(WORK / "missing_sec4_genotypes.csv")
    return found


def load_gene_variant_rows() -> dict[str, list[dict]]:
    """gene -> list of variant dicts from gene-tagged CSVs."""
    by_gene: dict[str, list[dict]] = defaultdict(list)
    skip_gt = {"", "NOT_FOUND", "NO_CALL", "BRAK", "--"}

    csv_paths = [
        WORK / "adhd_genotypes.csv",
        WORK / "neurodev_genotypes.csv",
    ]
    for path in csv_paths:
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                gene_raw = row.get("GENE", row.get("gene", "")).strip()
                g = canonical_gene(gene_raw)
                if not g:
                    continue
                rsid = row.get("RSID", row.get("rsid", "")).strip()
                gt = row.get("GENOTYPE", row.get("genotype", "")).strip().upper()
                status = row.get("STATUS", row.get("status", "OK")).strip().upper()
                if status in ("BRAK", "NOT_FOUND") or gt in skip_gt:
                    continue
                notes = row.get("NOTES", row.get("notes", "")).strip()
                interp = row.get("INTERPRETATION", row.get("interpretation", "")).strip()
                conf = row.get("CONFIDENCE", row.get("confidence", "")).strip()
                by_gene[g].append(
                    {
                        "rsid": rsid,
                        "genotype": gt,
                        "notes": notes,
                        "interpretation": interp,
                        "confidence": conf,
                        "source": path.name,
                    }
                )
    return dict(by_gene)


def score_topics(text: str, topics: set[str]) -> list[str]:
    low = text.lower()
    scored: list[tuple[int, str]] = []
    for tid in topics:
        score = sum(1 for k in TOPIC_KEYWORDS.get(tid, []) if k in low)
        if score > 0:
            scored.append((score, tid))
    scored.sort(reverse=True)
    return [t for _, t in scored]


def is_generic_topic_text(text: str) -> bool:
    """Tekst bez wartości klinicznej — nie pokazuj w kolumnie „U mnie”."""
    low = text.lower().strip()
    if not low:
        return True
    if low in {"wariant potwierdzony w wgs.", "wariant potwierdzony w wgs"}:
        return True
    generic_markers = (
        "sygnatura molekularna",
        "ryzyko poligenowe (prs)",
        "ryzyko poligenowe (gwas)",
        "gen przyczynowy (twas)",
        "wariant funkcjonalny (eqtl)",
        "wariant podwyższonego ryzyka",
        "wariant podwyższonego ryzyka)",
        "panel wgs:",
        "proxy snp",
    )
    if any(m in low for m in generic_markers):
        return True
    if re.search(r"\b(depth=|ensembl;|ncbi;|gt=\d)", low):
        return True
    # sama rola genu z Bazy bez fenotypu osobistego
    if re.fullmatch(
        r"[\w\sąćęłńóśźżĄĆĘŁŃÓŚŹŻ,;:\-]+"
        r"(\.\s*\([^)]+\))?\.\s*(ensembl|ncbi).*",
        low,
    ):
        return True
    return False


def strip_wgs_notes(text: str) -> str:
    """Usuń techniczne notatki WGS (depth, gt, ensembl)."""
    parts = re.split(r"\.\s+", text)
    kept = [
        p
        for p in parts
        if p
        and not re.search(r"^(ensembl|ncbi|gt=|depth=)", p.lower())
        and "depth=" not in p.lower()
    ]
    return ". ".join(kept).strip()


def variant_text(row: dict, baza: dict | None) -> str:
    parts: list[str] = []
    rsid = (row.get("rsid") or "").upper()
    baza_rs = {r.upper() for r in (baza or {}).get("rsids", [])}

    if row.get("interpretation"):
        parts.append(row["interpretation"].rstrip("."))

    # Baza tylko gdy rsID jest w locus i evidence nie jest generyczna
    if baza and rsid and rsid in baza_rs:
        evidence = (baza.get("evidence") or "").strip()
        if evidence and not is_generic_topic_text(f"({evidence})"):
            role = (baza.get("role") or "").strip()
            if role:
                parts.append(f"{role.rstrip('.')}. ({evidence.rstrip('.')})")

    if rsid and baza_rs and rsid not in baza_rs:
        parts.append(f"Proxy SNP {rsid} w locus (brak opisu ★ w wiki)")

    if row.get("notes"):
        note = strip_wgs_notes(row["notes"].rstrip("."))
        if note and note not in parts:
            parts.append(note)

    text = ". ".join(p for p in parts if p)
    text = strip_wgs_notes(text)
    return text


def build_variant_entry(rsid: str, gt: str, text: str) -> dict | None:
    if is_generic_topic_text(text):
        return None
    headline = f"{gt} — {text[:80]}{'…' if len(text) > 80 else ''}"
    return {
        "headline": headline,
        "text": text[:420] + ("…" if len(text) > 420 else ""),
        "heading": rsid,
        "genotype": gt,
    }


def js_str(s: str) -> str:
    return (
        '"'
        + s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", " ")
        + '"'
    )


def js_key(key: str) -> str:
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
        return key
    return js_str(key)


def load_existing_profiles_from_md() -> dict[str, dict]:
    """Odśwież profile genów z kart (★ w md/) przez build_personal_gene_profiles_js."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "build_pgp",
        ROOT / "scripts" / "build_personal_gene_profiles_js.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod.build_profiles()


def write_profiles(profiles: dict[str, dict]) -> None:
    lines = [
        "/** Profil osobisty per gen — ★ z md/*.md i md-mini/*.md (build_personal_gene_profiles_js.py). */",
        "window.PERSONAL_GENE_PROFILES = {",
    ]
    entries = []
    for gene in sorted(profiles):
        p = profiles[gene]
        topics = ", ".join(
            f'{js_key(tid)}: {js_by_topic_entry(entry)}'
            for tid, entry in sorted(p.get("byTopic", {}).items())
        )
        topics_block = f"{{ {topics} }}" if topics else "{}"
        variants_js = ", ".join(js_variant_entry(v) for v in p.get("variants", []))
        tone = p.get("toneCtx") or {}
        tone_ctx_parts = [
            f"heading: {js_str(tone.get('heading', ''))}",
            f"genotype: {js_str(tone.get('genotype', ''))}",
        ]
        if tone.get("tone"):
            tone_ctx_parts.append(f"tone: {js_str(tone['tone'])}")
        entries.append(
            f"  {js_key(gene)}: {{ headline: {js_str(p['headline'])}, "
            f"impact: {js_str(p['impact'])}, "
            f"toneCtx: {{ {', '.join(tone_ctx_parts)} }}, "
            f"variants: [{variants_js}], byTopic: {topics_block} }}"
        )
    lines.append(",\n".join(entries))
    lines.append("};")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")


def js_variant_entry(entry: dict) -> str:
    parts = [
        f"headline: {js_str(entry['headline'])}",
        f"text: {js_str(entry['text'])}",
        f"heading: {js_str(entry.get('heading', ''))}",
        f"genotype: {js_str(entry.get('genotype', ''))}",
    ]
    if entry.get("tone"):
        parts.append(f"tone: {js_str(entry['tone'])}")
    return "{ " + ", ".join(parts) + " }"


def js_by_topic_entry(entry: dict) -> str:
    if entry.get("variants"):
        items = ", ".join(js_variant_entry(v) for v in entry["variants"])
        return f"{{ variants: [{items}] }}"
    parts = [f"text: {js_str(entry['text'])}"]
    parts.append(f"heading: {js_str(entry.get('heading', ''))}")
    parts.append(f"genotype: {js_str(entry.get('genotype', ''))}")
    return "{ " + ", ".join(parts) + " }"


def write_report(
    profiles: dict,
    added: list[str],
    candidates: list[str],
    wiki: set[str],
    topics_by_gene: dict[str, set[str]],
    gene_rows: dict,
    baza: dict,
    rsid_gt: dict[str, str],
) -> None:
    lines = [
        "# Raport profili tematów — geny bez kart md/",
        "",
        f"Geny na stronach tematów bez kart wiki: **{len(candidates)}**",
        f"Z callami WGS uzupełniono w `personal-gene-profiles.js`: **{len(added)}**",
        f"Profile łącznie (★ z md/*.md i md-mini/*.md): **{len(profiles)}**",
        "",
        "_Geny tematów bez kart i bez ★ w md-mini nie dostają treści z Bazy/WGS._",
        "",
        "## Uzupełnione geny (kolumna „U mnie” na topic.html)",
        "",
    ]
    for g in added:
        p = profiles[g]
        tops = ", ".join(sorted(p.get("byTopic", {})))
        vars_txt = "; ".join(
            f"`{v['heading']}` {v['genotype']}" for v in p.get("variants", [])[:4]
        )
        lines.append(f"- **{g}** — tematy: {tops}; {vars_txt}")
    lines.extend(["", "## Bez calla WGS (pozostają „—”)", ""])
    no_wgs = [g for g in candidates if g not in added and g not in profiles]
    for g in sorted(no_wgs):
        tops = ", ".join(sorted(topics_by_gene.get(g, [])))
        lines.append(f"- **{g}** ({tops})")
    lines.append("")
    OUT_REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {OUT_REPORT}")


def main() -> None:
    wiki = wiki_genes()
    topics_by_gene = topic_genes()
    baza = load_baza_gene_info()
    rsid_gt = load_rsid_genotypes()
    gene_rows = load_gene_variant_rows()

    profiles = load_existing_profiles_from_md()
    added: list[str] = []

    candidates = sorted(
        g for g in topics_by_gene if g not in wiki and g not in SKIP_GENES
    )

    # Geny tematów bez kart md/ — celowo bez profilu w „U mnie”.
    # Treści z Bazy/WGS (Sygnatura molekularna, depth=…) są generyczne;
    # kolumna wypełnia się wyłącznie wierszami ★ z md/*.md.

    write_profiles(profiles)
    write_report(profiles, added, candidates, wiki, topics_by_gene, gene_rows, baza, rsid_gt)
    with_profile = len([g for g in candidates if g in profiles])
    print(f"Profile lacznie: {len(profiles)} genow (md/ + md-mini/)")
    print(f"Geny tematów z profilem: {with_profile}/{len(candidates)}")


if __name__ == "__main__":
    main()
