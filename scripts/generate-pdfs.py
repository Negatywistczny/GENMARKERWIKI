#!/usr/bin/env python3
"""Generuje karty genów jako PDF (4 strony, układ z html/print.html)."""

from __future__ import annotations

import http.server
import socketserver
import threading
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "pdf"
PORT = 4173

GENES = [
    "ABCC11", "ACTN3", "ADRA2A", "ALDH2", "ANK3", "ANKK1", "APOE", "AR",
    "BDNF", "CACNA1C", "CDH13", "CHRNA5", "CLOCK", "COMT", "CYP1A2", "DBH",
    "DRD2", "FKBP5", "FTO", "GC", "HERC2", "LCT", "MAOA", "MC1R", "MTHFR",
    "OCA2", "OR2M", "OR6A2", "OXTR", "SLC24A4", "SLC45A2", "SLC6A4", "TAS2R38", "TPH2",
    "ZEB2",
]

WAIT_READY_JS = """
() => {
  const pages = document.querySelectorAll('.print-document .print-page');
  return pages.length === 4 && pages[0].querySelector('.section-card');
}
"""

FIT_JS = """
async () => {
  if (typeof window.fitPrintPagesToSheet === 'function') {
    window.fitPrintPagesToSheet();
  }
  await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
  if (typeof window.fitPrintPagesToSheet === 'function') {
    window.fitPrintPagesToSheet();
  }
}
"""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, format, *args):
        pass


def start_server() -> socketserver.TCPServer:
    server = socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def wait_for_ready(page) -> None:
    page.wait_for_function(WAIT_READY_JS, timeout=30_000)
    page.evaluate(FIT_JS)
    page.wait_for_timeout(200)


def generate_pdf(page, gene: str) -> bool:
    url = f"http://127.0.0.1:{PORT}/html/print.html?gene={gene}"
    out_path = PDF_DIR / f"{gene}.pdf"
    try:
        page.goto(url, wait_until="networkidle", timeout=60_000)
        wait_for_ready(page)
        page.pdf(
            path=str(out_path),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "10mm", "right": "10mm", "bottom": "10mm", "left": "10mm"},
        )
        print(f"OK  {gene}.pdf")
        return True
    except Exception as exc:
        print(f"ERR {gene}: {exc}")
        return False


def main() -> int:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    server = start_server()
    time.sleep(0.3)

    ok = 0
    fail = 0

    print(f"Generowanie {len(GENES)} PDF do: {PDF_DIR}\n")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            for gene in GENES:
                if generate_pdf(page, gene):
                    ok += 1
                else:
                    fail += 1
        finally:
            context.close()
            browser.close()
            server.shutdown()

    print(f"\nGotowe: {ok} sukces, {fail} bledow.")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
