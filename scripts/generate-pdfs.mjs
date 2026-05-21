import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const PDF_DIR = path.join(ROOT, "pdf");
const PORT = 4173;

const GENES = [
  "ACTN3", "ADRA2A", "ANK3", "ANKK1", "APOE", "BDNF", "CACNA1C", "CDH13",
  "CHRNA5", "CLOCK", "COMT", "CYP1A2", "DBH", "DRD2", "FKBP5", "FTO",
  "LCT", "MAOA", "MC1R", "MTHFR", "OXTR", "SLC6A4", "TAS2R38", "TPH2",
];

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".md": "text/plain; charset=utf-8",
  ".json": "application/json; charset=utf-8",
};

function startStaticServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      try {
        const url = new URL(req.url || "/", `http://127.0.0.1:${PORT}`);
        let rel = decodeURIComponent(url.pathname);
        if (rel === "/") {
          rel = "/index.html";
        }
        const safe = path.normalize(rel).replace(/^(\.\.(\/|\\|$))+/, "");
        const filePath = path.join(ROOT, safe.replace(/^\//, ""));
        if (!filePath.startsWith(ROOT) || !fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
          res.writeHead(404);
          res.end("Not found");
          return;
        }
        const ext = path.extname(filePath).toLowerCase();
        res.writeHead(200, { "Content-Type": MIME[ext] || "application/octet-stream" });
        fs.createReadStream(filePath).pipe(res);
      } catch {
        res.writeHead(500);
        res.end("Server error");
      }
    });
    server.listen(PORT, "127.0.0.1", () => resolve(server));
  });
}

async function waitForPrintReady(page) {
  await page.waitForFunction(
    () => {
      const pages = document.querySelectorAll(".print-document .print-page");
      return pages.length === 4 && pages[0].querySelector(".section-card");
    },
    { timeout: 30000 }
  );
  await page.evaluate(async () => {
    if (typeof window.fitPrintPagesToSheet === "function") {
      window.fitPrintPagesToSheet();
    }
    await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    if (typeof window.fitPrintPagesToSheet === "function") {
      window.fitPrintPagesToSheet();
    }
  });
  await page.waitForTimeout(200);
}

async function generatePdf(browser, gene) {
  const page = await browser.newPage();
  const url = `http://127.0.0.1:${PORT}/html/print.html?gene=${encodeURIComponent(gene)}`;

  try {
    await page.goto(url, { waitUntil: "networkidle" });
    await waitForPrintReady(page);

    const outPath = path.join(PDF_DIR, `${gene}.pdf`);
    await page.pdf({
      path: outPath,
      format: "A4",
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: "10mm", right: "10mm", bottom: "10mm", left: "10mm" },
    });
    console.log(`OK  ${gene}.pdf`);
    return true;
  } catch (error) {
    console.error(`ERR ${gene}: ${error.message}`);
    return false;
  } finally {
    await page.close();
  }
}

async function main() {
  fs.mkdirSync(PDF_DIR, { recursive: true });

  const server = await startStaticServer();
  const browser = await chromium.launch({ headless: true });

  let ok = 0;
  let fail = 0;

  try {
    console.log(`Generowanie ${GENES.length} PDF do: ${PDF_DIR}\n`);
    for (const gene of GENES) {
      const success = await generatePdf(browser, gene);
      if (success) {
        ok += 1;
      } else {
        fail += 1;
      }
    }
  } finally {
    await browser.close();
    server.close();
  }

  console.log(`\nGotowe: ${ok} sukces, ${fail} błędów.`);
  process.exit(fail > 0 ? 1 : 0);
}

main();
