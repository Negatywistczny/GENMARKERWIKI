#!/usr/bin/env python3
"""Lookup variant tone (positive/neutral/negative) from html/variant-tones.js."""

from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TONES_JS = ROOT / "public" / "html" / "variant-tones.js"

_GENOTYPE_TOKEN_RE = re.compile(
    r"(?:^|[\s,;]|lub\s+)"
    r"([ACGT]{1,2}/[ACGT]{1,2}|[ACGT]{2}|wt/wt|i425v/wt|i425v/i425v|"
    r"l/l|l/s|s/s|gc[\d/]+|ref/\w+|alt/\w+|minor hom|major)",
    re.I,
)


def strip_md(value: str) -> str:
    text = str(value or "")
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"★\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_tone_key(value: str) -> str:
    text = strip_md(value).lower().replace("ł", "l")
    pl_map = str.maketrans(
        "ąćęńóśźż",
        "acenoszz",
    )
    text = text.translate(pl_map)
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def genotype_lookup_keys(genotype: str) -> list[str]:
    raw = strip_md(genotype)
    keys: list[str] = []

    def add(token: str) -> None:
        key = normalize_tone_key(token)
        if key and key not in keys:
            keys.append(key)

    add(raw)
    add(raw.split("(")[0])
    for inner in re.findall(r"\(([^)]+)\)", raw):
        for m in _GENOTYPE_TOKEN_RE.finditer(inner):
            add(m.group(1))
    for m in _GENOTYPE_TOKEN_RE.finditer(raw):
        add(m.group(1))
    return keys


def heading_lookup_keys(heading: str) -> list[str]:
    keys: list[str] = []
    h = str(heading or "")
    full = normalize_tone_key(h)
    if full:
        keys.append(full)
    if re.search(r"rs429358", h, re.I) and re.search(r"rs7412", h, re.I):
        keys.append("haplotypy apoe rs429358 rs7412")
    if re.search(r"maoa-uvntr", h, re.I):
        keys.append("maoa uvntr promotor liczba powtorzen nie klasyczny snp")
    if re.search(r"5-httlpr", h, re.I) and re.search(r"rs4795541", h, re.I):
        keys.append("a haplotypy regionu promotorowego 5 httlpr rs25531")
    for rs in re.findall(r"rs\d+", h, re.I):
        rs_key = normalize_tone_key(rs)
        if rs_key and rs_key not in keys:
            keys.append(rs_key)
    return keys


@lru_cache(maxsize=1)
def load_fixed_variant_tones() -> dict:
    text = TONES_JS.read_text(encoding="utf-8")
    m = re.search(
        r"const FIXED_VARIANT_TONES = (\{[\s\S]*)};\s*\n\nfunction normalizeToneKey",
        text,
    )
    if not m:
        return {}
    blob = m.group(1) + "}"
    blob = re.sub(r"(\n\s+)([A-Z][A-Z0-9_-]*)(\s*:)", r'\1"\2"\3', blob)
    blob = re.sub(r",(\s*[}\]])", r"\1", blob)
    try:
        return json.loads(blob)
    except json.JSONDecodeError:
        return {}


def fixed_variant_tone(gene: str, heading: str, genotype: str) -> str:
    by_gene = load_fixed_variant_tones().get(str(gene or "").upper())
    if not by_gene:
        return "neutral"

    by_heading = None
    for heading_key in heading_lookup_keys(heading):
        if heading_key in by_gene:
            by_heading = by_gene[heading_key]
            break
    by_heading = by_heading or by_gene.get("")
    if not by_heading:
        return "neutral"

    for key in genotype_lookup_keys(genotype):
        if key in by_heading:
            return by_heading[key]
    return "neutral"
