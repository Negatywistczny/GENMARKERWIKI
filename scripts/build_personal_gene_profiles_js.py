#!/usr/bin/env python3
"""Eksport profili osobistych (★ w md/*.md i md-mini/*.md) do html/personal-gene-profiles.js."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md"
MD_MINI_DIR = ROOT / "md-mini"
OUT = ROOT / "html" / "personal-gene-profiles.js"
SKIP = {"UNIWERSALNY_SZABLON_MARKERA.md"}
STAR = "★"

TOPIC_KEYWORDS: dict[str, list[str]] = {
    "asd": ["autyzm", "asd", "mowa", "społeczn", "synap"],
    "adhd": ["adhd", "uwag", "metylofenidat", "impuls", "stymulant", "skupien"],
    "mdd": ["depresj", "mdd", "ssri", "snri", "nastrój", "nastroj", "lęk", "lek ", "anhedon", "ptsd"],
    "chad": ["dwubiegun", "chad", "mania", " lit", "afektyw", "bipolar"],
    "scz": ["schizofren", "psychoz", "antypsychot", "halucyn"],
    "neurodev": ["neurorozwoj", "padaczk", "epilep", " id", "rozwoj", "dee", "inteligencj"],
    "dopamine": ["dopamin", "rds", "nagrod", "prążkow", "prazkow", "wojownik", "zamartwiac"],
    "serotonin": ["serotonin", "ssri", "5-htt", "5ht", "htl", "tryptofan"],
    "folate": ["folian", "homocyste", "metylac", "mthfr", "b12", "sam"],
    "cyp": ["cyp", "metaboliz", "klirens", "dawka", "inhibitor", "substrat"],
    "psychopharm": ["farmak", " lek", "ssri", "metylofenidat", "antydepres", "antypsychot", "risper", "wenlaf"],
    "substances": ["kofein", "alkohol", "etanol", "nikotyn", "palen", "papieros"],
    "nutrition": ["laktoz", "laktaz", "otyło", "bmi", "omega", "apetyt", "glikem"],
    "appearance": ["oczy", "skór", "pigment", "włos", "karnac", "melanin"],
    "smell-taste": ["smak", "gorycz", "węch", "wech", "zapach", "prop"],
    "cognition-aging": ["pamięć", "pamiec", "alzheimer", "apoe", "otępien", "otepien", "kognicj", "hipokamp"],
    "sport": ["sport", "wytrzyma", "actn3", "mięśn", "miesn", "hiit", "trening"],
}


def strip_md(s: str) -> str:
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(rf"{re.escape(STAR)}\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def parse_sections(text: str) -> dict[int, str]:
    parts: dict[int, list[str]] = {}
    current = 0
    for line in text.splitlines():
        m = re.match(r"^###\s+(\d+)\.\s+", line)
        if m:
            current = int(m.group(1))
        parts.setdefault(current, []).append(line)
    return {n: "\n".join(lines).strip() for n, lines in parts.items()}


def parse_tone_cell(value: str) -> str:
    tone = strip_md(value).lower()
    if tone in ("positive", "neutral", "negative"):
        return tone
    return ""


def parse_personal_rows(sec4: str) -> list[dict]:
    rows: list[dict] = []
    current_heading = ""
    tone_idx: int | None = None
    for line in sec4.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("|") and not stripped.startswith("###"):
            if stripped.startswith("**") or stripped.startswith("####"):
                current_heading = strip_md(stripped)
            continue
        if not line.startswith("|") or ":---" in line:
            continue
        raw = [c.strip() for c in line.split("|")[1:-1]]
        if len(raw) < 3:
            continue
        if raw[0].lower().startswith("genotyp"):
            tone_idx = next(
                (i for i, h in enumerate(raw) if strip_md(h).lower() == "ton"),
                None,
            )
            if tone_idx is None and len(raw) >= 4:
                tone_idx = 2
            continue
        if STAR not in raw[0]:
            continue
        genotype_cell = strip_md(raw[0])
        genotype = strip_md(raw[0].split("(")[0]).strip("* ")
        activity = strip_md(raw[1]) if len(raw) > 1 else ""
        impact = strip_md(raw[-1])
        tone = parse_tone_cell(raw[tone_idx]) if tone_idx is not None and tone_idx < len(raw) else ""
        rows.append(
            {
                "genotype": genotype,
                "genotype_cell": genotype_cell,
                "activity": activity,
                "impact": impact,
                "heading": current_heading,
                "tone": tone,
            }
        )
    return rows


def extract_bullets(section: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("* "):
            continue
        body = strip_md(s[2:].strip())
        m = re.match(r"^([^:]{2,80}):\s*(.+)$", body)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
        else:
            out.append(("", body))
    return out


def score_text(text: str, topic_id: str) -> int:
    low = text.lower()
    keys = TOPIC_KEYWORDS.get(topic_id, [])
    return sum(1 for k in keys if k in low)


def variant_headline(row: dict) -> str:
    genotype = strip_md(row["genotype"]).strip("* ")
    activity = row["activity"]
    return f"{genotype} — {activity}" if activity else genotype


def variant_entry(row: dict, text: str) -> dict:
    snippet = text[:420] + ("…" if len(text) > 420 else "")
    entry: dict = {
        "headline": variant_headline(row),
        "text": snippet,
        "heading": row.get("heading", ""),
        "genotype": row.get("genotype_cell") or row.get("genotype", ""),
    }
    if row.get("tone"):
        entry["tone"] = row["tone"]
    return entry


def match_row_for_label(rows: list[dict], label: str) -> dict | None:
    m = re.search(r"rs\d+", label, re.I)
    if not m:
        return None
    rs = m.group(0).lower()
    for row in rows:
        if rs in row.get("heading", "").lower():
            return row
    return None


CLINICAL_ADVICE_LABELS = frozenset({
    "suplementacja",
    "farmakologia",
    "diagnostyka",
    "rehabilitacja",
    "genetyka rodzinna",
    "ostrzeżenie kliniczne",
})


def is_gene_level_advice(label: str) -> bool:
    return label.strip().lower() in CLINICAL_ADVICE_LABELS


def is_reference_profile(row: dict) -> bool:
    blob = f"{row.get('activity', '')} {row.get('impact', '')}".lower()
    if row.get("tone") == "positive":
        return True
    return any(
        w in blob
        for w in ("norma", "prawidłow", "prawidlow", "normotyp", "typ dziki", "referencyj")
    )


def pick_topic_variants(
    topic_id: str, rows: list[dict], bullets: list[tuple[str, str]]
) -> list[dict]:
    seen: set[tuple[str, str]] = set()
    out: list[dict] = []
    primary = rows[0] if rows else None

    def add(row: dict, text: str) -> None:
        key = (row.get("heading", ""), row.get("genotype_cell") or row.get("genotype", ""))
        if key in seen or is_generic_snippet(text):
            return
        seen.add(key)
        out.append(variant_entry(row, text))

    for row in rows:
        text = row["impact"]
        if score_text(text, topic_id) > 0:
            add(row, text)

    for label, body in bullets:
        if primary and is_gene_level_advice(label) and is_reference_profile(primary):
            continue
        combined = f"{label}: {body}" if label else body
        sc = score_text(combined, topic_id)
        if label and score_text(label, topic_id) > 0:
            sc += 2
        if sc > 0:
            row = match_row_for_label(rows, label) or rows[0]
            add(row, combined)

    return out


def tone_ctx(row: dict) -> dict:
    ctx: dict = {
        "heading": row.get("heading", ""),
        "genotype": row.get("genotype_cell") or row.get("genotype", ""),
    }
    if row.get("tone"):
        ctx["tone"] = row["tone"]
    return ctx


def default_summary(rows: list[dict]) -> dict | None:
    if not rows:
        return None
    primary = rows[0]
    return {
        "headline": variant_headline(primary),
        "impact": variant_entry(primary, primary["impact"])["text"],
    }


SKIP_SNIPPET_PREFIXES = (
    "ostrzeżenie kliniczne",
    "materiał ma charakter informacyjny",
)


def is_generic_snippet(text: str) -> bool:
    low = text.lower().strip()
    return any(low.startswith(p) for p in SKIP_SNIPPET_PREFIXES)


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


def profile_from_sections(sections: dict[int, str], *, bullets_section: int) -> dict | None:
    rows = parse_personal_rows(sections.get(4, ""))
    if not rows:
        return None
    bullets = extract_bullets(sections.get(bullets_section, ""))
    default = default_summary(rows)
    if not default:
        return None
    variants = [variant_entry(row, row["impact"]) for row in rows]
    by_topic: dict[str, dict] = {}
    for topic_id in TOPIC_KEYWORDS:
        topic_variants = pick_topic_variants(topic_id, rows, bullets)
        if topic_variants:
            by_topic[topic_id] = {"variants": topic_variants}
    return {
        "headline": default["headline"],
        "impact": default["impact"],
        "toneCtx": tone_ctx(rows[0]),
        "variants": variants,
        "byTopic": by_topic,
    }


def build_profiles() -> dict[str, dict]:
    profiles: dict[str, dict] = {}
    for path in sorted(MD_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        gene = path.stem.upper()
        sections = parse_sections(path.read_text(encoding="utf-8"))
        profile = profile_from_sections(sections, bullets_section=6)
        if profile:
            profiles[gene] = profile

    for path in sorted(MD_MINI_DIR.glob("*.md")):
        gene = path.stem.upper()
        if gene in profiles:
            continue
        sections = parse_sections(path.read_text(encoding="utf-8"))
        profile = profile_from_sections(sections, bullets_section=3)
        if profile:
            profiles[gene] = profile

    return profiles


def js_tone_ctx(ctx: dict) -> str:
    parts = [
        f"heading: {js_str(ctx.get('heading', ''))}",
        f"genotype: {js_str(ctx.get('genotype', ''))}",
    ]
    if ctx.get("tone"):
        parts.append(f"tone: {js_str(ctx['tone'])}")
    return "{ " + ", ".join(parts) + " }"


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
    if entry.get("heading") is not None or entry.get("genotype"):
        parts.append(f"heading: {js_str(entry.get('heading', ''))}")
        parts.append(f"genotype: {js_str(entry.get('genotype', ''))}")
    return "{ " + ", ".join(parts) + " }"


def write_js(profiles: dict[str, dict]) -> None:
    lines = [
        "/** Profil osobisty per gen — z wierszy ★ w md/*.md i md-mini/*.md. Generowane: scripts/build_personal_gene_profiles_js.py */",
        "window.PERSONAL_GENE_PROFILES = {",
    ]
    entries = []
    for gene in sorted(profiles):
        p = profiles[gene]
        topics = ", ".join(
            f"{js_key(tid)}: {js_by_topic_entry(entry)}"
            for tid, entry in sorted(p["byTopic"].items())
        )
        topics_block = f"{{ {topics} }}" if topics else "{}"
        variants_js = ", ".join(js_variant_entry(v) for v in p["variants"])
        entries.append(
            f"  {js_key(gene)}: {{ headline: {js_str(p['headline'])}, "
            f"impact: {js_str(p['impact'])}, toneCtx: {js_tone_ctx(p['toneCtx'])}, "
            f"variants: [{variants_js}], byTopic: {topics_block} }}"
        )
    lines.append(",\n".join(entries))
    lines.append("};")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    profiles = build_profiles()
    write_js(profiles)
    print(f"Wrote {OUT} ({len(profiles)} genow z profilem)")


if __name__ == "__main__":
    main()
