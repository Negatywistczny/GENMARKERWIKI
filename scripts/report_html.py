"""Convert Raport-osobisty-genom-wiki.md to standalone HTML."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_IN = ROOT / "data" / "reports" / "Raport-osobisty-genom-wiki.md"
HTML_OUT = ROOT / "data" / "reports" / "Raport-osobisty-genom-wiki.html"

THEMES_META = {
    "Mózg, nastrój, stres i uwaga": {"icon": "🧠", "color": "#6b8cff", "id": "theme-mozg"},
    "Metabolizm, dieta i substancje": {"icon": "🥗", "color": "#3ecf9a", "id": "theme-metabolizm"},
    "Wygląd, pigmentacja i sensoryka": {"icon": "👁️", "color": "#e8a84a", "id": "theme-wyglad"},
    "Serce, naczynia i hormony": {"icon": "❤️", "color": "#f07178", "id": "theme-serce"},
    "Inne": {"icon": "🧬", "color": "#b48cff", "id": "theme-inne"},
}


def slug(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    return re.sub(r"[-\s]+", "-", s).strip("-")


def parse_field_line(line: str) -> tuple[str, str] | None:
    m = re.match(r"^- \*\*([^*]+):\*\*\s*(.*)$", line.strip())
    if not m:
        return None
    key, val = m.group(1).strip(), m.group(2).strip()
    val = re.sub(r"`([^`]+)`", r"\1", val)
    val = re.sub(r"\*\*([^*]+)\*\*", r"\1", val)
    return key, val


def parse_variant_block(lines: list[str]) -> dict:
    variant: dict = {
        "title": "",
        "subtitle": "",
        "fields": {},
        "unmatched": False,
        "is_haplotype": False,
    }
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("#### "):
            variant["title"] = s[5:].strip()
            variant["is_haplotype"] = "haplotyp" in variant["title"].lower()
        elif s.startswith("_") and s.endswith("_") and len(s) > 2:
            variant["subtitle"] = s.strip("_")
        elif "brak dopasowania" in s.lower() or "brak potwierdzonych" in s.lower():
            variant["unmatched"] = True
        else:
            parsed = parse_field_line(s)
            if parsed:
                variant["fields"][parsed[0]] = parsed[1]
    return variant


def parse_gene_block(text: str) -> dict:
    lines = text.splitlines()
    header = lines[0] if lines else ""
    m = re.match(r"##\s+(\w+)\s+—\s+(.+)$", header)
    gene = m.group(1) if m else "?"
    title = m.group(2).strip() if m else header

    profile: list[str] = []
    mechanism: list[str] = []
    variants: list[dict] = []
    missing_markers: list[str] = []
    recommendations: list[str] = []
    no_genotypes_msg = ""

    section = "profile"
    variant_lines: list[str] = []

    def flush_variant() -> None:
        nonlocal variant_lines
        if variant_lines:
            variants.append(parse_variant_block(variant_lines))
            variant_lines = []

    for line in lines[1:]:
        s = line.strip()
        if s.startswith("### Mechanizm"):
            flush_variant()
            section = "mechanism"
            continue
        if s.startswith("### Twoje warianty"):
            flush_variant()
            section = "variants"
            continue
        if s.startswith("### Markery w panelu"):
            flush_variant()
            section = "missing"
            continue
        if s.startswith("### Zalecenia"):
            flush_variant()
            section = "recommendations"
            continue
        if s.startswith("#### "):
            flush_variant()
            variant_lines = [line]
            section = "variants"
            continue
        if section == "variants" and (
            s.startswith("- **") or (s.startswith("_") and s.endswith("_"))
        ):
            variant_lines.append(line)
            continue
        if section == "profile" and s.startswith("- "):
            profile.append(s[2:].strip())
        elif section == "mechanism" and s.startswith("- "):
            mechanism.append(s[2:].strip())
        elif section == "missing" and s.startswith("- "):
            missing_markers.append(s[2:].strip())
        elif section == "recommendations" and s.startswith("- "):
            recommendations.append(s[2:].strip())
        elif section == "variants" and s.startswith("_Brak potwierdzonych"):
            no_genotypes_msg = s.strip("_")

    flush_variant()

    return {
        "gene": gene,
        "title": title,
        "id": f"gene-{gene}",
        "profile": profile,
        "mechanism": mechanism,
        "variants": variants,
        "missing_markers": missing_markers,
        "recommendations": recommendations,
        "no_genotypes_msg": no_genotypes_msg,
    }


def parse_header_block(text: str) -> dict:
    date = ""
    disclaimer = ""
    stats: dict[str, str] = {}
    gene_index: list[dict] = []

    for line in text.splitlines():
        if line.startswith("**Data:**"):
            date = line.split("**Data:**", 1)[-1].strip()
        elif line.startswith("> "):
            disclaimer = line[2:].strip()
        elif line.startswith("| ") and ":---" not in line and "Metryka" not in line:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 2:
                stats[cells[0]] = cells[1]
        elif line.startswith("- **"):
            m = re.match(
                r"- \*\*(\w+)\*\* — (.+) \((\d+)/(\d+) markerów",
                line,
            )
            if m:
                gene_index.append(
                    {
                        "gene": m.group(1),
                        "label": m.group(2),
                        "known": int(m.group(3)),
                        "total": int(m.group(4)),
                    }
                )
    return {
        "date": date,
        "disclaimer": disclaimer,
        "stats": stats,
        "gene_index": gene_index,
    }


def parse_report_md(text: str) -> dict:
    header_end = re.search(r"\n# (?!#)", text)
    header_text = text[: header_end.start()] if header_end else text
    meta = parse_header_block(header_text)

    themes: list[dict] = []
    notes_intro = ""
    notes: list[str] = []
    footer_note = ""

    if not header_end:
        return {**meta, "themes": themes, "notes_intro": notes_intro, "notes": notes, "footer_note": footer_note}

    body = text[header_end.start() + 1 :]
    top_sections = re.split(r"\n(?=# )", body)

    for section in top_sections:
        if not section.strip():
            continue
        first_line, _, rest = section.partition("\n")
        title = first_line[2:].strip() if first_line.startswith("# ") else first_line.strip()

        if title.startswith("Uwagi"):
            for line in rest.splitlines():
                s = line.strip()
                if not s or s == "---":
                    continue
                if s.startswith("- "):
                    notes.append(s[2:])
                elif s.startswith("**26"):
                    footer_note = re.sub(r"\*\*", "", s)
                elif not s.startswith("#"):
                    notes_intro = s
            continue

        theme_meta = THEMES_META.get(
            title, {"icon": "📋", "color": "#888", "id": slug(title)}
        )
        genes: list[dict] = []
        for chunk in re.split(r"\n(?=## )", rest):
            chunk = chunk.strip()
            if not chunk or chunk == "---":
                continue
            if chunk.startswith("---"):
                chunk = chunk.lstrip("-").strip()
            if not chunk.startswith("##"):
                chunk = "## " + chunk
            genes.append(parse_gene_block(chunk))

        themes.append(
            {
                "name": title,
                "icon": theme_meta["icon"],
                "color": theme_meta["color"],
                "id": theme_meta["id"],
                "genes": genes,
            }
        )

    return {
        **meta,
        "themes": themes,
        "notes_intro": notes_intro,
        "notes": notes,
        "footer_note": footer_note,
    }


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def render_variant(v: dict) -> str:
    title = v.get("title", "")
    fields = v.get("fields", {})
    gt = fields.get("Genotyp (baza/MyHeritage)", fields.get("Twój profil", ""))
    source = fields.get("Źródło", "")
    table_gt = fields.get("Profil w tabeli wariantów", "")
    status = fields.get("Aktywność / status", "")
    effect = fields.get("Wpływ fenotypowy", fields.get("Wpływ", ""))

    cls = "variant-card"
    if v.get("unmatched"):
        cls += " variant-card--muted"
    elif effect and any(
        w in effect.lower()
        for w in ("ryzyko", "podatno", "obniżon", "spadek", "deficyt", "wysokie")
    ):
        cls += " variant-card--alert"
    elif effect and any(w in effect.lower() for w in ("ochron", "prawidłow", "niższe ryzyko", "referencyj")):
        cls += " variant-card--positive"

    parts = [
        f'<article class="{cls}">',
        '<div class="variant-card__head">',
        f'<code class="rsid">{esc(title)}</code>',
    ]
    if gt and not v.get("is_haplotype"):
        parts.append(f'<span class="genotype-badge">{esc(gt)}</span>')
    parts.append("</div>")
    if v.get("subtitle"):
        parts.append(f'<p class="variant-card__sub">{esc(v["subtitle"])}</p>')
    if v.get("unmatched"):
        parts.append('<p class="variant-card__warn">Brak dopasowania w tabeli wariantów</p>')
    meta = []
    if source:
        meta.append(f'<span class="tag tag--source">{esc(source)}</span>')
    if table_gt:
        meta.append(f'<span class="tag">Tabela: {esc(table_gt)}</span>')
    if status:
        meta.append(f'<span class="tag tag--status">{esc(status)}</span>')
    if meta:
        parts.append(f'<div class="variant-card__tags">{"".join(meta)}</div>')
    if effect:
        parts.append(f'<p class="variant-card__effect">{esc(effect)}</p>')
    for key, val in fields.items():
        if key in (
            "Genotyp (baza/MyHeritage)",
            "Źródło",
            "Profil w tabeli wariantów",
            "Aktywność / status",
            "Wpływ fenotypowy",
            "Wpływ",
            "Twój profil",
        ):
            continue
        parts.append(
            f'<p class="variant-card__extra"><strong>{esc(key)}:</strong> {esc(val)}</p>'
        )
    parts.append("</article>")
    return "\n".join(parts)


def render_gene(gene: dict, accent: str) -> str:
    parts = [
        f'<article class="gene-card" id="{esc(gene["id"])}" style="--gene-accent:{esc(accent)}">',
        '<header class="gene-card__header">',
        f'<span class="gene-card__symbol">{esc(gene["gene"])}</span>',
        f'<h3 class="gene-card__title">{esc(gene["title"])}</h3>',
        "</header>",
    ]
    if gene["profile"]:
        items = "".join(f"<li>{esc(p)}</li>" for p in gene["profile"])
        parts.append(
            f'<details class="gene-panel" open><summary>Profil genu</summary><ul class="gene-list">{items}</ul></details>'
        )
    if gene["mechanism"]:
        items = "".join(f"<li>{esc(p)}</li>" for p in gene["mechanism"])
        parts.append(
            f'<details class="gene-panel"><summary>Mechanizm i wpływ biologiczny</summary><ul class="gene-list">{items}</ul></details>'
        )
    parts.append('<section class="gene-variants">')
    parts.append("<h4>Twoje warianty</h4>")
    if gene["no_genotypes_msg"]:
        parts.append(f'<p class="muted">{esc(gene["no_genotypes_msg"])}</p>')
    elif gene["variants"]:
        parts.append('<div class="variant-grid">')
        for v in gene["variants"]:
            parts.append(render_variant(v))
        parts.append("</div>")
    parts.append("</section>")
    if gene["missing_markers"]:
        def _missing_item(m: str) -> str:
            rm = re.search(r"`(rs\d+)`", m)
            rs = rm.group(1) if rm else m
            desc = m.split("—", 1)[-1].strip() if "—" in m else ""
            return f"<li><code>{esc(rs)}</code> — {esc(desc)}</li>"

        items = "".join(_missing_item(m) for m in gene["missing_markers"])
        parts.append(
            f'<details class="gene-panel gene-panel--dim"><summary>Markery bez genotypemu ({len(gene["missing_markers"])})</summary><ul class="gene-list">{items}</ul></details>'
        )
    if gene["recommendations"]:
        items = "".join(f"<li>{esc(r)}</li>" for r in gene["recommendations"])
        parts.append(
            f'<details class="gene-panel gene-panel--tips"><summary>Zalecenia praktyczne</summary><ul class="gene-list gene-list--tips">{items}</ul></details>'
        )
    parts.append("</article>")
    return "\n".join(parts)


CSS = """
:root {
  color-scheme: light dark;
  --bg: #0c1022;
  --bg-elevated: #141a30;
  --card: #181f38;
  --card-hover: #1e2744;
  --text: #e8ecff;
  --muted: #9aa8d4;
  --border: #2a3558;
  --shadow: 0 20px 50px rgba(0,0,0,.35);
  --radius: 16px;
  --font: "Segoe UI", system-ui, -apple-system, sans-serif;
  --mono: "Cascadia Code", "Consolas", monospace;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #f0f4ff;
    --bg-elevated: #fff;
    --card: #fff;
    --card-hover: #f8faff;
    --text: #152040;
    --muted: #5a6b94;
    --border: #d8e2ff;
    --shadow: 0 16px 40px rgba(40,60,140,.1);
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  font-size: 15px;
}
body::before {
  content: "";
  position: fixed;
  inset: 0;
  background:
    radial-gradient(ellipse 80% 50% at 100% 0%, rgba(107,140,255,.15), transparent),
    radial-gradient(ellipse 60% 40% at 0% 100%, rgba(62,207,154,.1), transparent);
  pointer-events: none;
  z-index: -1;
}
a { color: #7aa2ff; text-decoration: none; }
a:hover { text-decoration: underline; }
.layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 1.5rem;
  max-width: 1280px;
  margin: 0 auto;
  padding: 1.25rem 1.5rem 3rem;
}
@media (max-width: 960px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { position: static !important; }
}
.sidebar {
  position: sticky;
  top: 1rem;
  align-self: start;
  max-height: calc(100vh - 2rem);
  overflow-y: auto;
}
.sidebar-inner {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1rem;
  box-shadow: var(--shadow);
}
.sidebar h2 {
  margin: 0 0 .75rem;
  font-size: .85rem;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--muted);
}
.toc-theme { margin-bottom: 1rem; }
.toc-theme__title {
  display: flex;
  align-items: center;
  gap: .4rem;
  font-weight: 600;
  font-size: .82rem;
  margin-bottom: .35rem;
  color: var(--text);
}
.toc-theme ul { margin: 0; padding-left: 1rem; list-style: none; }
.toc-theme li { margin: .2rem 0; }
.toc-theme a {
  font-size: .8rem;
  color: var(--muted);
  display: flex;
  justify-content: space-between;
  gap: .5rem;
}
.toc-theme a:hover { color: var(--text); }
.toc-count {
  font-size: .7rem;
  opacity: .7;
  font-variant-numeric: tabular-nums;
}
main { min-width: 0; }
.hero {
  background: linear-gradient(135deg, var(--card) 0%, var(--bg-elevated) 100%);
  border: 1px solid var(--border);
  border-radius: calc(var(--radius) + 4px);
  padding: 1.75rem 2rem;
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow);
}
.hero h1 {
  margin: 0 0 .35rem;
  font-size: clamp(1.5rem, 3vw, 2rem);
  font-weight: 700;
  letter-spacing: -.02em;
}
.hero-meta { color: var(--muted); font-size: .9rem; margin: 0 0 1.25rem; }
.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: .75rem;
}
.stat {
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: .85rem 1rem;
  text-align: center;
}
.stat__value {
  display: block;
  font-size: 1.75rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  line-height: 1.2;
}
.stat__label { font-size: .72rem; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
.disclaimer {
  margin: 1rem 0 0;
  padding: .75rem 1rem;
  border-left: 3px solid #e8a84a;
  background: rgba(232,168,74,.08);
  border-radius: 0 8px 8px 0;
  font-size: .88rem;
  color: var(--muted);
}
.theme-section {
  margin-bottom: 2.5rem;
  scroll-margin-top: 1rem;
}
.theme-header {
  display: flex;
  align-items: center;
  gap: .65rem;
  margin-bottom: 1.25rem;
  padding-bottom: .65rem;
  border-bottom: 2px solid var(--border);
}
.theme-header__icon { font-size: 1.5rem; }
.theme-header h2 {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 650;
}
.gene-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-left: 4px solid var(--gene-accent, #7aa2ff);
  border-radius: var(--radius);
  padding: 1.25rem 1.35rem;
  margin-bottom: 1rem;
  box-shadow: var(--shadow);
  scroll-margin-top: 1rem;
}
.gene-card__header {
  display: flex;
  align-items: baseline;
  flex-wrap: wrap;
  gap: .6rem;
  margin-bottom: .85rem;
}
.gene-card__symbol {
  font-family: var(--mono);
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--gene-accent, #7aa2ff);
  background: color-mix(in srgb, var(--gene-accent) 18%, transparent);
  padding: .15rem .5rem;
  border-radius: 6px;
}
.gene-card__title { margin: 0; font-size: 1.05rem; font-weight: 600; }
.gene-panel {
  margin: .65rem 0;
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
}
.gene-panel summary {
  cursor: pointer;
  padding: .55rem .85rem;
  font-weight: 600;
  font-size: .88rem;
  background: var(--bg-elevated);
  list-style: none;
}
.gene-panel summary::-webkit-details-marker { display: none; }
.gene-panel summary::before { content: "▸ "; opacity: .6; }
.gene-panel[open] summary::before { content: "▾ "; }
.gene-panel--tips summary { color: #4ee1c1; }
.gene-panel--dim { opacity: .85; }
.gene-list {
  margin: 0;
  padding: .65rem 1rem .85rem 1.5rem;
  font-size: .88rem;
  color: var(--muted);
}
.gene-list--tips { color: var(--text); }
.gene-variants h4 {
  margin: 1rem 0 .65rem;
  font-size: .8rem;
  text-transform: uppercase;
  letter-spacing: .05em;
  color: var(--muted);
}
.variant-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: .75rem;
}
.variant-card {
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: .85rem 1rem;
}
.variant-card--positive { border-color: rgba(62,207,154,.45); }
.variant-card--alert { border-color: rgba(240,113,120,.45); }
.variant-card--muted { opacity: .75; }
.variant-card__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: .5rem;
  margin-bottom: .4rem;
}
.rsid {
  font-family: var(--mono);
  font-size: .9rem;
  font-weight: 600;
  color: var(--text);
  background: transparent;
}
.genotype-badge {
  font-family: var(--mono);
  font-weight: 700;
  font-size: .95rem;
  padding: .2rem .55rem;
  border-radius: 8px;
  background: color-mix(in srgb, #7aa2ff 25%, transparent);
  color: #a8c0ff;
  letter-spacing: .05em;
}
@media (prefers-color-scheme: light) {
  .genotype-badge { color: #315efb; background: #e8efff; }
}
.variant-card__sub { margin: 0 0 .4rem; font-size: .78rem; color: var(--muted); font-style: italic; }
.variant-card__warn { margin: 0; font-size: .8rem; color: #f07178; }
.variant-card__tags { display: flex; flex-wrap: wrap; gap: .35rem; margin-bottom: .5rem; }
.tag {
  font-size: .68rem;
  padding: .15rem .45rem;
  border-radius: 6px;
  background: var(--card);
  border: 1px solid var(--border);
  color: var(--muted);
}
.tag--source { border-color: rgba(122,162,255,.4); }
.tag--status { border-color: rgba(78,225,193,.35); }
.variant-card__effect { margin: 0; font-size: .86rem; line-height: 1.55; }
.variant-card__extra { margin: .35rem 0 0; font-size: .8rem; color: var(--muted); }
.muted { color: var(--muted); font-size: .9rem; }
.notes-section {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem 1.5rem;
  margin-top: 2rem;
}
.notes-section h2 { margin-top: 0; }
.notes-section ul { padding-left: 1.2rem; }
.notes-section li { margin: .5rem 0; font-size: .9rem; }
.footer-note { margin-top: 1rem; font-size: .85rem; color: var(--muted); }
"""


def render_html(data: dict) -> str:
    stat_items = "".join(
        f'<div class="stat"><span class="stat__value">{esc(v)}</span>'
        f'<span class="stat__label">{esc(k)}</span></div>'
        for k, v in data["stats"].items()
    )

    index_map = {x["gene"]: x for x in data["gene_index"]}
    toc_parts = []
    for theme in data["themes"]:
        if theme["name"].startswith("Raport osobisty"):
            continue
        gene_links = "".join(
            f'<li><a href="#gene-{esc(g["gene"])}">{esc(g["gene"])} '
            f'<span class="toc-count">{index_map.get(g["gene"], {}).get("known", "?")}/'
            f'{index_map.get(g["gene"], {}).get("total", "?")}</span></a></li>'
            for g in theme["genes"]
        )
        toc_parts.append(
            f'<div class="toc-theme">'
            f'<div class="toc-theme__title"><span>{theme["icon"]}</span>'
            f'<a href="#{esc(theme["id"])}">{esc(theme["name"])}</a></div>'
            f"<ul>{gene_links}</ul></div>"
        )

    theme_sections = []
    for theme in data["themes"]:
        if theme["name"].startswith("Raport osobisty"):
            continue
        genes_html = "".join(
            render_gene(g, theme["color"]) for g in theme["genes"]
        )
        theme_sections.append(
            f'<section class="theme-section" id="{esc(theme["id"])}">'
            f'<div class="theme-header" style="border-color:{esc(theme["color"])}">'
            f'<span class="theme-header__icon">{theme["icon"]}</span>'
            f"<h2>{esc(theme['name'])}</h2></div>{genes_html}</section>"
        )

    notes_html = ""
    if data["notes"]:
        items = "".join(f"<li>{esc(n)}</li>" for n in data["notes"])
        notes_html = f"""
<section class="notes-section" id="uwagi">
  <h2>Uwagi i warianty bez automatycznego dopasowania</h2>
  <p class="muted">{esc(data["notes_intro"])}</p>
  <ul>{items}</ul>
  <p class="footer-note">{esc(data["footer_note"])}</p>
</section>"""

    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Raport genetyczny — GENMARKERWIKI</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <nav class="sidebar-inner" aria-label="Spis treści">
        <h2>Spis treści</h2>
        {''.join(toc_parts)}
        <p style="margin-top:1rem;font-size:.75rem;"><a href="#uwagi">Uwagi</a></p>
      </nav>
    </aside>
    <main>
      <header class="hero">
        <h1>Raport osobisty — geny i warianty</h1>
        <p class="hero-meta">GENMARKERWIKI · {esc(data["date"])}</p>
        <div class="stats">{stat_items}</div>
        <p class="disclaimer">{esc(data["disclaimer"])}</p>
      </header>
      {''.join(theme_sections)}
      {notes_html}
    </main>
  </div>
</body>
</html>"""


def convert_md_to_html(md_path: Path = MD_IN, html_path: Path = HTML_OUT) -> None:
    text = md_path.read_text(encoding="utf-8")
    data = parse_report_md(text)
    html_path.write_text(render_html(data), encoding="utf-8")
    print(f"HTML: {html_path}")


if __name__ == "__main__":
    convert_md_to_html()
