#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
md = {p.stem.upper() for p in (ROOT / "md").glob("*.md")}
idx = (ROOT / "html" / "gene-index.js").read_text(encoding="utf-8")
index_genes = re.findall(r'gene: "([^"]+)"', idx)
report = (ROOT / "raporty" / "markery" / "Zbiorowe badanie markerów.md").read_text(encoding="utf-8")
report_genes = re.findall(r"^### ([A-Z0-9][A-Z0-9-]+)", report, re.M)
report_set = set(report_genes)
need_from_index = [g for g in index_genes if g not in md]
need_from_report = [g for g in sorted(report_set) if g not in md]
print("index total", len(index_genes))
print("md full", len(md))
print("index without md", len(need_from_index))
print("report without md", len(need_from_report))
only_index = sorted(set(need_from_index) - report_set)
only_report = sorted(report_set - set(index_genes) - md)
print("only in index not report", len(only_index), only_index[:15])
print("only in report not index", len(only_report), only_report)
