import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const mdDir = path.join(root, "md");
const SKIP = new Set(["UNIWERSALNY_SZABLON_MARKERA.md", "index.md"]);

const EXPECTED_SECTIONS = [
  "Nagłówek i Nazwy",
  "Identyfikator (rsID) i Charakterystyka Wariantu",
  "Mechanizm działania",
  "Tabela Wariantów",
  "Statystyki populacyjne",
  "Wpływ na życie (Zalecenia)",
  "Ciekawostki",
  "Źródła (Referencje)",
];

const STD_HEADER =
  "| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy (kliniczny i funkcjonalny) |";

const TITLE_EXCEPTIONS = [
  /rs\d+/i,
  /maoa-uvntr/i,
  /5-httlpr/i,
  /mutacje patogenne/i,
  /haplotyp złożony/i,
  /i425v/i,
];

function parseSections(md) {
  const lines = md.split(/\r?\n/);
  const sections = [];
  let current = null;
  for (const line of lines) {
    const m = line.match(/^###\s+(\d+)\.\s+(.+)$/);
    if (m) {
      if (current) sections.push(current);
      current = { num: Number(m[1]), title: m[2].trim(), body: [] };
    } else if (current) {
      current.body.push(line);
    }
  }
  if (current) sections.push(current);
  return sections;
}

function splitVariantBlocks(body) {
  const blocks = [];
  let current = { title: "", lines: [] };
  const push = () => {
    if (current.lines.some((l) => l.trim().startsWith("|"))) {
      blocks.push({ ...current });
    }
    current = { title: "", lines: [] };
  };
  for (const line of body) {
    const t = line.trim();
    const tm = t.match(/^\*\*(.+)\*\*$/);
    if (tm) {
      push();
      current.title = tm[1].trim();
      continue;
    }
    if (t.startsWith("|")) {
      current.lines.push(line);
      continue;
    }
    if (!t && current.lines.length) {
      current.lines.push(line);
      continue;
    }
    if (t) {
      push();
      current = { title: "", lines: [line] };
      push();
    }
  }
  push();
  if (!blocks.length) {
    const tl = body.filter((l) => l.trim().startsWith("|"));
    if (tl.length) return [{ title: "", lines: tl }];
  }
  return blocks;
}

function tableColCount(line) {
  if (!line.trim().startsWith("|") || /:?-+:?/.test(line.split("|")[1] || "")) {
    return null;
  }
  return line.split("|").slice(1, -1).length;
}

function hasValidBlockTitle(title) {
  if (!title) return false;
  return TITLE_EXCEPTIONS.some((re) => re.test(title));
}

const issues = [];

for (const file of fs.readdirSync(mdDir).sort()) {
  if (!file.endsWith(".md") || SKIP.has(file)) continue;
  const gene = file.replace(/\.md$/i, "");
  const md = fs.readFileSync(path.join(mdDir, file), "utf8");

  if (/\|###\s+\d+\./.test(md)) {
    issues.push({ gene, type: "glued-header", detail: "Sekcja sklejona z tabelą (|### N.)" });
  }

  const sections = parseSections(md);
  if (sections.length !== 8) {
    issues.push({
      gene,
      type: "section-count",
      detail: `Oczekiwano 8 sekcji, jest ${sections.length}`,
    });
  }

  for (let i = 0; i < EXPECTED_SECTIONS.length; i++) {
    const sec = sections[i];
    if (!sec || sec.num !== i + 1 || sec.title !== EXPECTED_SECTIONS[i]) {
      issues.push({
        gene,
        type: "section-order",
        detail: `Sekcja ${i + 1}: oczekiwano „${EXPECTED_SECTIONS[i]}”, jest „${sec?.title || "brak"}"`,
      });
      break;
    }
  }

  const sec4 = sections.find((s) => s.num === 4);
  if (sec4) {
    const blocks = splitVariantBlocks(sec4.body);
    for (const block of blocks) {
      if (!hasValidBlockTitle(block.title)) {
        issues.push({
          gene,
          type: "missing-snp-title",
          detail: `Brak tytułu bloku SNP: „${block.title || "(pusty)"}"`,
        });
      }
      const tableLines = block.lines.filter((l) => l.trim().startsWith("|"));
      if (!tableLines.length) continue;
      const header = tableLines[0].trim();
      if (header !== STD_HEADER) {
        issues.push({
          gene,
          type: "table-header",
          detail: `Niestandardowy nagłówek: ${header.slice(0, 80)}`,
        });
      }
      for (const line of tableLines) {
        const cols = tableColCount(line);
        if (cols !== null && cols !== 3) {
          issues.push({
            gene,
            type: "table-cols",
            detail: `${cols} kolumn(y): ${line.trim().slice(0, 70)}`,
          });
        }
      }
    }
    const sec4Text = sec4.body.join("\n");
    if (/\|[^|\n]+\n### 5\./.test(sec4Text)) {
      issues.push({
        gene,
        type: "spacing",
        detail: "Brak pustej linii między ostatnią tabelą §4 a ### 5",
      });
    }
  }

  const sec6 = sections.find((s) => s.num === 6);
  if (sec6 && !sec6.body.join("\n").includes("Ostrzeżenie kliniczne")) {
    issues.push({ gene, type: "clinical-warning", detail: "Brak „Ostrzeżenie kliniczne” w §6" });
  }

  const sec8 = sections.find((s) => s.num === 8);
  if (sec8) {
    const body = sec8.body.join("\n");
    const pmids = (body.match(/\*\*PMID:\s*\d+\*\*/g) || []).length;
    const hasSnpedia = /snpedia\.com/i.test(body);
    if (pmids < 3) {
      issues.push({
        gene,
        type: "pmid-count",
        detail: `§8: ${pmids} PMID (wymagane ≥3)`,
      });
    }
    if (!hasSnpedia) {
      issues.push({ gene, type: "snpedia", detail: "Brak linku SNPedia w §8" });
    }
  }
}

console.log("Karty sprawdzone:", fs.readdirSync(mdDir).filter((f) => f.endsWith(".md") && !SKIP.has(f)).length);
console.log("Problemy strukturalne:", issues.length);
for (const i of issues) {
  console.log(`${i.gene}: [${i.type}] ${i.detail}`);
}

process.exit(issues.length ? 1 : 0);
