#!/usr/bin/env python3
"""Pobierz allel ref/alt dla rsID (myvariant.info / dbSNP) z lokalnym cache."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = Path(__file__).resolve().parent / "data" / "rsid_allele_cache.json"

RSID_RE = re.compile(r"rs\d+", re.I)
NUC_GENOTYPE_RE = re.compile(r"^[ACGT]{1,2}/[ACGT]{1,2}$", re.I)
VNTR_GENOTYPE_RE = re.compile(r"^\d+R/\d+R$", re.I)
STAR_ALLELE_RE = re.compile(r"^\*[\w]+(/\*[\w]+)?$")
STRUCTURAL_RE = re.compile(r"^(ins|del|dup|wt)(/(ins|del|dup|wt))?$", re.I)
SKIP_GENOTYPE = frozenset({"—", "-", "n/a", "brak"})


def clean_allele(value: str) -> str:
    raw = (value or "").upper().strip()
    if not raw:
        return ""
    if "/" in raw:
        parts = [p for p in raw.split("/") if len(p) == 1 and p in "ACGT"]
        return parts[0] if parts else raw.split("/")[0][:1]
    if len(raw) > 1 and set(raw) <= set("ACGT"):
        return raw[0]
    return raw


def primary_rsid(text: str) -> str | None:
    m = RSID_RE.search(text or "")
    return m.group(0).lower() if m else None


def is_resolved_genotype(value: str) -> bool:
    g = (value or "").strip().strip("`")
    if not g or g.lower() in SKIP_GENOTYPE:
        return False
    if NUC_GENOTYPE_RE.match(g):
        return True
    if VNTR_GENOTYPE_RE.match(g):
        return True
    if STAR_ALLELE_RE.match(g):
        return True
    if STRUCTURAL_RE.match(g):
        return True
    if "/" in g and re.match(r"^[A-Za-z0-9*]+/[A-Za-z0-9*]+$", g):
        left, right = g.split("/", 1)
        if left.lower() in {"ins", "del", "dup", "wt"} or right.lower() in {
            "ins",
            "del",
            "dup",
            "wt",
        }:
            return True
    return False


def normalize_genotype(value: str) -> str:
    g = (value or "").strip().strip("`").replace("★", "").strip()
    if NUC_GENOTYPE_RE.match(g):
        a, b = g.upper().split("/")
        return f"{a}/{b}"
    return g


def genotype_from_alleles(ref: str, alt: str, index: int, total: int) -> str:
    ref = (ref or "").upper()
    alt = (alt or "").upper()
    if not ref or not alt or ref == alt:
        return ref or alt or "—"
    if total <= 1:
        return f"{ref}/{ref}"
    if total == 2:
        return f"{ref}/{ref}" if index == 0 else f"{alt}/{alt}"
    if index == 0:
        return f"{ref}/{ref}"
    if index == total - 1:
        return f"{alt}/{alt}"
    return f"{ref}/{alt}"


def resolve_genotype(
    genotype: str,
    *,
    index: int,
    total: int,
    ref: str | None,
    alt: str | None,
) -> str:
    if is_resolved_genotype(genotype):
        return normalize_genotype(genotype)
    if ref and alt:
        return genotype_from_alleles(ref, alt, index, total)
    return genotype or "—"


def load_cache() -> dict[str, dict]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_cache(cache: dict[str, dict]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _parse_myvariant_record(rsid: str, data: dict) -> dict | None:
    dbsnp = data.get("dbsnp") or {}
    ref = (dbsnp.get("ref") or "").strip()
    alt_field = dbsnp.get("alt")
    alt = ""
    if isinstance(alt_field, list):
        alt = str(alt_field[0]).strip() if alt_field else ""
    elif alt_field:
        alt = str(alt_field).strip()
    if not ref and dbsnp.get("alleles"):
        alleles = [a.get("allele", "") for a in dbsnp["alleles"] if a.get("allele")]
        if len(alleles) >= 2:
            ref, alt = alleles[0], alleles[1]
    if not ref:
        return None
    if not alt:
        alt = ref
    return {
        "rsid": rsid.lower(),
        "ref": clean_allele(ref),
        "alt": clean_allele(alt),
        "source": "myvariant.info/dbsnp",
    }


def fetch_ncbi(rsid: str) -> dict | None:
    snp_id = rsid.lower().replace("rs", "")
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        f"?db=snp&id={snp_id}&retmode=json"
    )
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None
    doc = (data.get("result") or {}).get(snp_id)
    if not doc:
        return None
    docsum = doc.get("docsum", "")
    seq = re.search(r"SEQ=\[([^/\]]+)/([^\]]+)\]", docsum)
    if not seq:
        return None
    return {
        "rsid": f"rs{snp_id}",
        "ref": clean_allele(seq.group(1)),
        "alt": clean_allele(seq.group(2)),
        "source": "ncbi/dbsnp",
    }


def fetch_one(rsid: str) -> dict | None:
    rsid = rsid.lower()
    url = f"https://myvariant.info/v1/variant/{rsid}?fields=dbsnp"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return fetch_ncbi(rsid)
        return fetch_ncbi(rsid)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return fetch_ncbi(rsid)
    if isinstance(data, list):
        data = data[0] if data else {}
    if not isinstance(data, dict):
        return fetch_ncbi(rsid)
    parsed = _parse_myvariant_record(rsid, data)
    if parsed:
        return parsed
    return fetch_ncbi(rsid)


def ensure_alleles(rsids: set[str], *, refresh: bool = False) -> dict[str, dict]:
    cache = {} if refresh else load_cache()
    wanted = {rs.lower() for rs in rsids if RSID_RE.match(rs or "")}
    missing = sorted(
        {
            rs
            for rs in wanted
            if refresh
            or rs not in cache
            or not (cache.get(rs) or {}).get("ref")
            or "/" in str((cache.get(rs) or {}).get("alt", ""))
        },
        key=lambda x: int(x[2:]),
    )
    for i, rsid in enumerate(missing):
        info = fetch_one(rsid)
        if info:
            cache[rsid] = info
        else:
            cache[rsid] = {"rsid": rsid, "ref": "", "alt": "", "source": "unavailable"}
        if i < len(missing) - 1:
            time.sleep(0.15)
    save_cache(cache)
    return cache


def allele_info_for_rsid(rsid: str | None, cache: dict[str, dict]) -> tuple[str | None, str | None]:
    if not rsid:
        return None, None
    entry = cache.get(rsid.lower()) or {}
    ref = (entry.get("ref") or "").strip() or None
    alt = (entry.get("alt") or "").strip() or None
    if not ref or not alt:
        return None, None
    return ref, alt
