import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const variantTones = fs.readFileSync(path.join(root, "public", "html", "variant-tones.js"), "utf8");
const tonesMatch = variantTones.match(/const FIXED_VARIANT_TONES = (\{[\s\S]*?\n\});/);
if (!tonesMatch) {
  console.error("Nie znaleziono FIXED_VARIANT_TONES w html/variant-tones.js");
  process.exit(2);
}
const FIXED_VARIANT_TONES = Function(`return ${tonesMatch[1]}`)();

function stripMarkdown(value) {
  return value
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\*([^*]+)\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
}

function normalizeToneKey(value) {
  return stripMarkdown(String(value || ""))
    .toLowerCase()
    .replace(/ł/g, "l")
    .replace(/[ąćęńóśźż]/g, (ch) =>
      ({ ą: "a", ć: "c", ę: "e", ń: "n", ó: "o", ś: "s", ź: "z", ż: "z" })[ch] || ch
    )
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function genotypeLookupKeys(genotype) {
  const raw = stripMarkdown(String(genotype || ""));
  const keys = new Set();
  const add = (token) => {
    const key = normalizeToneKey(token);
    if (key) keys.add(key);
  };
  add(raw);
  add(raw.split("(")[0]);
  const tokenRe =
    /(?:^|[\s,;]|lub\s+)([ACGT]{1,2}\/[ACGT]{1,2}|[ACGT]{2}|wt\/wt|i425v\/wt|i425v\/i425v|l\/l|l\/s|s\/s|gc[\d/]+|ref\/\w+|alt\/\w+|minor hom|major)/gi;
  for (const inner of raw.matchAll(/\(([^)]+)\)/g)) {
    for (const m of inner[1].matchAll(tokenRe)) add(m[1]);
  }
  for (const m of raw.matchAll(tokenRe)) add(m[1]);
  return [...keys];
}

function headingLookupKeys(heading) {
  const keys = [];
  const h = String(heading || "");
  const full = normalizeToneKey(h);
  if (full) keys.push(full);
  if (/rs429358/i.test(h) && /rs7412/i.test(h)) {
    keys.push("haplotypy apoe rs429358 rs7412");
  }
  if (/maoa-uvntr/i.test(h)) {
    keys.push("maoa uvntr promotor liczba powtorzen nie klasyczny snp");
  }
  if (/5-httlpr/i.test(h) && /rs4795541/i.test(h)) {
    keys.push("a haplotypy regionu promotorowego 5 httlpr rs25531");
  }
  for (const rs of h.match(/rs\d+/gi) || []) {
    const rsKey = normalizeToneKey(rs);
    if (rsKey && !keys.includes(rsKey)) keys.push(rsKey);
  }
  return keys;
}

function fixedVariantTone(geneSymbol, heading, genotype, options = {}) {
  const byGene = FIXED_VARIANT_TONES[String(geneSymbol || "").toUpperCase()];
  if (!byGene) return { tone: "neutral", reason: "no-gene" };
  const headingKeys = headingLookupKeys(heading);
  let byHeading = null;
  let headingKey = headingKeys[0] || "";
  for (const key of headingKeys) {
    if (byGene[key]) {
      byHeading = byGene[key];
      headingKey = key;
      break;
    }
  }
  byHeading = byHeading || byGene[""];
  if (!byHeading) return { tone: "neutral", reason: "no-heading", headingKey };
  const keys = options.lookupKey ? [options.lookupKey] : genotypeLookupKeys(genotype);
  for (const key of keys) {
    if (byHeading[key]) {
      return { tone: byHeading[key], reason: "ok", headingKey, genotypeKey: key };
    }
  }
  return {
    tone: "neutral",
    reason: "no-genotype",
    headingKey,
    genotypeKey: keys[0] || "",
  };
}

function parseSections(md) {
  const lines = md.split(/\r?\n/);
  const sections = [];
  let current = null;
  for (const line of lines) {
    const m = line.match(/^###\s+\d+\.\s+(.+)$/);
    if (m) {
      if (current) sections.push(current);
      current = { title: m[1].trim(), body: [] };
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
      current.title = stripMarkdown(tm[1]);
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

function parseTable(lines) {
  const rows = lines
    .filter((l) => l.trim().startsWith("|"))
    .map((l) => l.split("|").slice(1, -1).map((c) => c.trim()));
  if (rows.length < 2) return null;
  const data = rows
    .slice(1)
    .filter((r) => !r.every((c) => /^:?-+:?$/.test(c.replace(/\s/g, ""))))
    .map((r) => r.map(stripMarkdown));
  return { rows: data };
}

const mdDir = path.join(root, "docs", "genes");
const issues = [];
let total = 0;

for (const file of fs.readdirSync(mdDir)) {
  if (!file.endsWith(".md") || file.startsWith("._") || file === "UNIWERSALNY_SZABLON_MARKERA.md" || file === "index.md" || file === "README.md") {
    continue;
  }
  const md = fs.readFileSync(path.join(mdDir, file), "utf8");
  const gene = file.replace(/\.md$/i, "").toUpperCase();
  const sec = parseSections(md).find((s) => s.title.toLowerCase().includes("tabela wariant"));
  if (!sec) {
    issues.push({ gene, file, type: "no-section" });
    continue;
  }
  if (!FIXED_VARIANT_TONES[gene]) {
    issues.push({ gene, file, type: "no-map" });
    continue;
  }
  for (const block of splitVariantBlocks(sec.body)) {
    const table = parseTable(block.lines);
    if (!table) continue;
    const tableHeaders = block.lines
      .filter((l) => l.trim().startsWith("|"))
      .map((l) => l.split("|").slice(1, -1).map((c) => c.trim()))[0] || [];
    const isApoeHaplotypeTable =
      gene === "APOE" &&
      tableHeaders.some((h) => /rs429358/i.test(h)) &&
      tableHeaders.some((h) => /rs7412/i.test(h));
    const isApoeHaplotype =
      gene === "APOE" &&
      (/haplotypy apoe|rs429358.*rs7412/i.test(block.title) || isApoeHaplotypeTable);
    const toneHeading =
      isApoeHaplotype && !block.title
        ? "haplotypy apoe rs429358 rs7412"
        : block.title;

    for (const row of table.rows) {
      const genotype = row[0] || "";
      const lookupKey = isApoeHaplotype ? normalizeToneKey(row.join(" ")) : null;
      total++;
      const r = fixedVariantTone(
        gene,
        toneHeading,
        genotype,
        lookupKey ? { lookupKey } : {}
      );
      if (r.reason === "no-genotype" || r.reason === "no-heading") {
        issues.push({ gene, file, heading: block.title, genotype, ...r });
      }
    }
  }
}

console.log("Genes in map:", Object.keys(FIXED_VARIANT_TONES).length);
console.log("Rows checked:", total);
console.log("Unmapped rows:", issues.length);
for (const i of issues) {
  console.log(JSON.stringify(i));
}

process.exit(issues.length ? 1 : 0);
