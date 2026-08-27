#!/usr/bin/env python3
"""Uzupełnij Zbiorowe badanie markerów.md o osobiste genotypy WGS i dopasowanie profili."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "data" / "reports" / "markery" / "Zbiorowe badanie markerów.md"
WORK = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\.work")
FASTQ = Path(r"C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER")
MARKER_GT = WORK / "marker_report_genotypes.csv"
RSID_LIST = WORK / "marker_report_rsids.txt"

GENE_ALIASES = {
    "DAT1": "SLC6A3",
    "DAT": "SLC6A3",
    "5-HTT": "SLC6A4",
    "GR": "NR3C1",
    "MR": "NR3C2",
}

SKIP_GT = {"", "NOT_FOUND", "NO_CALL", "BRAK", "--", "NOT_IN_DBSNP"}
WGS_MARKER = "* **Mój genotyp (WGS):**"
PROFILE_MARKER = "* **Dopasowany profil:**"

VNTR_GENES = {
    "DRD4": "VNTR 48-bp (egzon 3, 2R–11R) — brak bezpośredniego calla w WGS; proxy SNP:",
    "SLC6A3": "VNTR 40-bp (3'UTR, 9R/10R) — brak bezpośredniego calla w WGS; proxy SNP:",
    "DRD5": "Mikrosatelita promotorowa — brak VNTR w WGS; proxy SNP:",
    "SLC6A4": "VNTR 5-HTTLPR — imputacja z tag-SNP:",
}

DENOVO_NOTE = (
    "Brak populacyjnego tag-SNP — ocena wyłącznie sekwencyjna/CNV "
    "(mutacje de novo / LoF nie wykrywalne w panelu SNP)."
)

HLA_NOTE = (
    "Allele HLA wymagają typowania haplotypowego (nie pojedynczego rsID); "
    "brak pełnego calla w uproszczonym WGS SNP."
)


def canonical_gene(name: str) -> str:
    raw = name.strip().upper()
    raw = re.sub(r"\s*\(.*\)", "", raw)
    return GENE_ALIASES.get(raw, raw)


def normalize_gt(gt: str) -> str:
    gt = gt.strip().upper().replace("/", "")
    if len(gt) == 2 and gt[0] != gt[1]:
        return "".join(sorted(gt))
    return gt


def load_rsid_genotypes() -> dict[str, dict]:
    """rsid -> {genotype, source, confidence, notes}"""
    found: dict[str, dict] = {}

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
            conf_key = fields.get("CONFIDENCE") or fields.get("confidence")
            notes_key = fields.get("NOTES") or fields.get("notes")
            src_key = fields.get("SOURCE") or fields.get("source")
            if not rs_key or not gt_key:
                return
            for row in reader:
                rs = row.get(rs_key, "").strip().lower()
                gt = row.get(gt_key, "").strip()
                if not rs.startswith("rs"):
                    continue
                if rs in found and found[rs]["genotype"] not in SKIP_GT and gt in SKIP_GT:
                    continue
                found[rs] = {
                    "genotype": gt,
                    "source": row.get(src_key, path.stem) if src_key else path.stem,
                    "confidence": row.get(conf_key, "").strip() if conf_key else "",
                    "notes": row.get(notes_key, "").strip() if notes_key else "",
                }

    for path in sorted(WORK.glob("query_rsid*.csv")):
        ingest(path)
    for name in (
        "bam_genotypes_final.csv",
        "pharmaco_genotypes.csv",
        "neurodev_wiki_genotypes.csv",
        "missing_sec4_genotypes.csv",
        "missing_mini_bam_genotypes.csv",
        "vntr_genotypes.csv",
        "marker_report_genotypes.csv",
    ):
        ingest(WORK / name)
    return found


def load_gene_variants() -> dict[str, list[dict]]:
    by_gene: dict[str, list[dict]] = defaultdict(list)
    for name in ("adhd_genotypes.csv", "neurodev_genotypes.csv"):
        path = WORK / name
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                gene_raw = row.get("GENE", row.get("gene", "")).strip()
                g = canonical_gene(gene_raw)
                if not g:
                    continue
                rsid = row.get("RSID", row.get("rsid", "")).strip()
                gt = row.get("GENOTYPE", row.get("genotype", "")).strip()
                status = row.get("STATUS", row.get("status", "OK")).strip().upper()
                if status in ("BRAK", "NOT_FOUND") or gt in SKIP_GT:
                    continue
                by_gene[g].append(
                    {
                        "rsid": rsid,
                        "genotype": gt,
                        "notes": row.get("NOTES", row.get("notes", "")).strip(),
                        "confidence": row.get("CONFIDENCE", row.get("confidence", "")).strip(),
                        "source": row.get("SOURCE", row.get("source", name)).strip(),
                    }
                )
    return dict(by_gene)


def extract_rsids_from_section(text: str) -> list[str]:
    primary: list[str] = []
    other: list[str] = []
    for line in text.splitlines():
        m = re.search(r"rs\d+", line, re.I)
        if not m:
            continue
        rs = m.group(0).lower()
        if "główny rsid" in line.lower() or "rsid /" in line.lower():
            primary.append(rs)
        else:
            other.append(rs)
    seen: set[str] = set()
    ordered: list[str] = []
    for rs in primary + other:
        if rs not in seen:
            seen.add(rs)
            ordered.append(rs)
    return ordered


def format_gt_entry(rsid: str, info: dict) -> str:
    gt = info.get("genotype", "").strip()
    if gt in SKIP_GT:
        label = "brak calla" if gt in ("NO_CALL", "") else gt
        return f"`{rsid}` — {label}"
    parts = [f"`{rsid}` — **{gt}**"]
    src = info.get("source", "")
    conf = info.get("confidence", "")
    if src:
        parts.append(f"({src}" + (f", {conf}" if conf else "") + ")")
    notes = info.get("notes", "")
    if notes and len(notes) < 120:
        parts.append(f"— {notes}")
    return " ".join(parts)


def profile_alleles(header: str) -> set[str] | None:
    m = re.search(
        r"(?:Genotyp|Wariant|Diplotyp|Typ)\s+([ACGT/]+|[HL]\d/[HL]?\d?)",
        header,
        re.I,
    )
    if not m:
        return None
    token = m.group(1).upper()
    if "/" in token and all(c in "ACGT" for c in token.replace("/", "")):
        a, b = token.split("/", 1)
        if a == b:
            return {a * 2}
        return {"".join(sorted(a + b))}
    if re.match(r"H\d/H\d", token):
        return {token}
    return None


def match_profile(section: str, rsid: str, genotype: str) -> str | None:
    if genotype in SKIP_GT:
        return None
    norm = normalize_gt(genotype)
    headers = re.findall(r"\*\*([^*]+)\*\*", section)
    for header in headers:
        low = header.lower()
        if not any(k in low for k in ("genotyp", "wariant", "diplotyp", "typ dziki", "typ referencyjny")):
            continue
        alleles = profile_alleles(header)
        if alleles and norm in alleles:
            return header.strip()
        if "/" in genotype or len(genotype) == 2:
            if f"{genotype[0]}/{genotype[1]}" in header or f"{genotype[1]}/{genotype[0]}" in header:
                return header.strip()
    return None


def bam_proxy_variants(gene: str, bam_hit: dict | None, rsid_gt: dict[str, dict]) -> list[dict]:
    """Proxy tag-SNP z BAM gdy rsID w sekcji raportu jest nieaktualny lub brak."""
    if not bam_hit:
        return []
    primary = bam_hit.get("PRIMARY_RSID", "").strip()
    gt = bam_hit.get("GENOTYPE", "").strip().upper()
    if not primary.lower().startswith("rs") or gt in SKIP_GT:
        return []
    info = rsid_gt.get(primary.lower(), {})
    return [
        {
            "rsid": primary,
            "genotype": gt,
            "source": bam_hit.get("SOURCE", "ensembl+bam"),
            "confidence": info.get("confidence", ""),
            "notes": bam_hit.get("NOTES", info.get("notes", "")),
        }
    ]


def build_wgs_block(
    gene: str,
    section: str,
    rsid_gt: dict[str, dict],
    gene_vars: dict[str, list[dict]],
    *,
    bam_hit: dict | None = None,
) -> list[str]:
    lines: list[str] = []
    g = canonical_gene(gene)
    proxies = bam_proxy_variants(g, bam_hit, rsid_gt)

    if g.startswith("HLA"):
        if proxies:
            lines.append(WGS_MARKER)
            for v in proxies:
                rs = v["rsid"].lower()
                info = rsid_gt.get(rs, v)
                lines.append(f"  - {format_gt_entry(v['rsid'], info)}")
            lines.append(
                "  - (OptiType niedostepny; proxy tag-SNP — nie pelne typowanie alleli HLA)"
            )
            return lines
        return [WGS_MARKER, f"  {HLA_NOTE}"]

    if g in VNTR_GENES:
        lines.append(WGS_MARKER)
        lines.append(f"  {VNTR_GENES[g]}")
        variants = list(gene_vars.get(g, [])) or proxies
        for v in variants:
            rs = v["rsid"].lower()
            info = rsid_gt.get(rs, v)
            lines.append(f"  - {format_gt_entry(v['rsid'], info)}")
        if not variants:
            lines.append("  - brak proxy SNP w panelu ADHD/WGS")
        return lines

    rsids = extract_rsids_from_section(section)
    if proxies:
        proxy_rs = proxies[0]["rsid"].lower()
        if proxy_rs not in rsids:
            rsids = [proxy_rs] + rsids
    if not rsids:
        if proxies:
            rsids = [proxies[0]["rsid"].lower()]
        else:
            return [WGS_MARKER, f"  {DENOVO_NOTE}"]

    entries: list[str] = []
    matched_profile: str | None = None
    primary_rsid = rsids[0]

    for rs in rsids:
        info = rsid_gt.get(rs)
        if info:
            entries.append(format_gt_entry(rs, info))
            if not matched_profile and info["genotype"] not in SKIP_GT:
                matched_profile = match_profile(section, rs, info["genotype"])
        else:
            entries.append(f"`{rs}` — nie zbadano w WGS")

    for v in gene_vars.get(g, []):
        rs = v["rsid"].lower()
        if rs not in {r.lower() for r in rsids}:
            entries.append(format_gt_entry(v["rsid"], rsid_gt.get(rs, v)))

    lines.append(WGS_MARKER)
    if len(entries) == 1:
        lines.append(f"  {entries[0]}")
    else:
        for e in entries:
            lines.append(f"  - {e}")

    if matched_profile:
        lines.append(f"{PROFILE_MARKER} {matched_profile}")
    elif any("de novo" in section.lower() or "lof" in section.lower() for _ in [1]) and not rsids:
        pass

    return lines


def find_insert_index(lines: list[str]) -> int:
    """Index after metadata bullets, before profile descriptions."""
    role_idx = None
    first_profile = None
    for i, line in enumerate(lines):
        low = line.lower()
        if role_idx is None and "* **rola biologiczna" in low:
            role_idx = i
        if first_profile is None:
            if line.startswith("**") and not line.startswith("* **"):
                first_profile = i
            elif re.match(r"^\* \*\*(Wariant|Genotyp|Diplotyp|Typ)", line):
                first_profile = i
    if role_idx is not None:
        return role_idx + 1
    if first_profile is not None:
        return first_profile
    return len(lines)


def section_has_wgs(lines: list[str]) -> bool:
    return any(WGS_MARKER in ln for ln in lines)


def dedupe_headers(text: str) -> str:
    return re.sub(r"^(### [^\n]+)\n\1\n", r"\1\n", text, flags=re.M)


def enrich_section(
    gene: str,
    body: str,
    rsid_gt: dict,
    gene_vars: dict,
    *,
    force: bool = False,
    bam_hit: dict | None = None,
) -> str:
    lines = body.splitlines()
    if not force and section_has_wgs(lines):
        return body

    if force and section_has_wgs(lines):
        cleaned: list[str] = []
        skip_until = -1
        for i, ln in enumerate(lines):
            if ln.strip() == WGS_MARKER:
                skip_until = i
                continue
            if skip_until >= 0:
                if ln.startswith(PROFILE_MARKER):
                    skip_until = i
                    continue
                if ln.strip() == "" and i > skip_until:
                    skip_until = -1
                    if cleaned and cleaned[-1] == "":
                        continue
                if skip_until >= 0 and (ln.startswith("* **") or ln.startswith("**")):
                    skip_until = -1
                elif skip_until >= 0:
                    continue
            if ln.startswith(PROFILE_MARKER):
                continue
            cleaned.append(ln)
        lines = cleaned

    wgs_lines = build_wgs_block(gene, body, rsid_gt, gene_vars, bam_hit=bam_hit)
    idx = find_insert_index(lines)
    new_lines = lines[:idx] + [""] + wgs_lines + [""] + lines[idx:]
    return "\n".join(new_lines).rstrip() + "\n"


def parse_sections(text: str) -> list[tuple[str, str, int, int]]:
    """Return (gene, body, start, end) for each ### section."""
    pattern = re.compile(r"^### ([^\n]+)\n", re.M)
    matches = list(pattern.finditer(text))
    sections: list[tuple[str, str, int, int]] = []
    for i, m in enumerate(matches):
        gene = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        sections.append((gene, body, start, end))
    return sections


def collect_missing_rsids(text: str, rsid_gt: dict) -> list[str]:
    all_rs = sorted(set(re.findall(r"rs\d+", text, re.I)), key=lambda x: int(x[2:]))
    missing = [rs for rs in all_rs if rs.lower() not in rsid_gt or rsid_gt[rs.lower()]["genotype"] in SKIP_GT]
    return missing


def run_bam_query(_rsids: list[str]) -> int:
    script = ROOT / "scripts" / "query_marker_rsids_bam.py"
    print("[info] Zapytanie Ensembl + BAM dla brakujących rsID...", flush=True)
    proc = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(proc.stdout, end="")
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr)
        return proc.returncode
    return 0


def enrich_report(*, query_bam: bool = False) -> None:
    text = REPORT.read_text(encoding="utf-8")
    rsid_gt = load_rsid_genotypes()
    if query_bam:
        missing = collect_missing_rsids(text, rsid_gt)
        run_bam_query(missing)
        rsid_gt = load_rsid_genotypes()

    gene_vars = load_gene_variants()
    sections = parse_sections(text)
    if not sections:
        print("Brak sekcji ### w raporcie.", file=sys.stderr)
        sys.exit(1)

    parts: list[str] = []
    cursor = 0
    enriched = 0
    force = "--force" in sys.argv
    for gene, body, start, end in sections:
        parts.append(text[cursor:start])
        new_body = enrich_section(gene, body, rsid_gt, gene_vars, force=force)
        if new_body != body:
            enriched += 1
        parts.append(new_body)
        cursor = end
    parts.append(text[cursor:])
    out = dedupe_headers("".join(parts))
    REPORT.write_text(out, encoding="utf-8")
    print(f"[done] Uzupełniono {enriched}/{len(sections)} genów w {REPORT.name}")


def main() -> int:
    query = "--query-bam" in sys.argv
    enrich_report(query_bam=query)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
