const gene = document.body.dataset.gene;
const contentNode = document.getElementById("gene-content");
const statusNode = document.getElementById("gene-status");
const titleNode = document.getElementById("gene-title");
const subtitleNode = document.getElementById("gene-subtitle");

const SECTION_META = [
  { key: "nagłówek", icon: "🧬", label: "Profil genu" },
  { key: "nazwy", icon: "🧬", label: "Profil genu" },
  { key: "identyfikator", icon: "🆔", label: "Identyfikatory i SNP" },
  { key: "rsid", icon: "🆔", label: "Identyfikatory i SNP" },
  { key: "mechanizm", icon: "⚙️", label: "Mechanizm działania" },
  { key: "tabela wariantów", icon: "📊", label: "Warianty i fenotyp" },
  { key: "wariantów", icon: "📊", label: "Warianty i fenotyp" },
  { key: "statystyki", icon: "🌍", label: "Statystyki populacyjne" },
  { key: "wpływ", icon: "🩺", label: "Znaczenie praktyczne" },
  { key: "zalecenia", icon: "🩺", label: "Znaczenie praktyczne" },
  { key: "ciekawostki", icon: "✨", label: "Ciekawostki" },
  { key: "źródła", icon: "📚", label: "Źródła" },
  { key: "referencje", icon: "📚", label: "Źródła" },
];

const FIXED_VARIANT_TONES = {
  DRD2: {
    "rs1800497 taq1a ankk1 nic kodujaca g a raporty komplementarne c t": {
      "g g": "positive",
      "a g": "neutral",
      "a a": "negative",
    },
    "rs6277 c957t ekson 6": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1076560 intron 6 g t": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
    "rs1799732 141c ins del promotor": {
      "ins ins": "positive",
      "ins del": "neutral",
      "del del": "negative",
    },
  },
  TPH2: {
    "": {
      "t t": "positive",
      "g t": "neutral",
      "g g": "negative",
    },
  },
  SLC6A4: {
    "a haplotypy regionu promotorowego 5 httlpr rs25531": {
      "l a l a l l a a": "positive",
      "l a l g lub l a s a": "neutral",
      "s a s a lub l g l g": "negative",
    },
    "rs25532 c t": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1042173 3 utr t g": {
      "g g": "positive",
      "t g": "neutral",
      "t t": "negative",
    },
    "i425v mutacja missense rzadka": {
      "i425v heterozygota homozygota": "negative",
    },
  },
  MTHFR: {
    "rs1801133 c677t ala222val egzon 4": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1801131 a1298c glu429ala egzon 7": {
      "a a": "positive",
      "a c": "neutral",
      "c c": "negative",
    },
    "haplotyp zlozony oba snp na jednym chromosomie": {
      "677c t 1298a c heterozygota zlozona": "negative",
    },
  },
  TAS2R38: {
    "": {
      "g g pav pav": "positive",
      "g c pav avi": "neutral",
      "c c avi avi": "negative",
    },
  },
  OXTR: {
    "": {
      "g g": "positive",
      "a g": "neutral",
      "a a": "negative",
    },
  },
  ANKK1: {
    "": {
      "g g c c": "positive",
      "a g c t": "neutral",
      "a a t t": "negative",
    },
  },
  ACTN3: {
    "": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  COMT: {
    "": {
      "a a": "negative",
      "a g": "neutral",
      "g g": "positive",
    },
  },
  CYP1A2: {
    "": {
      "a a": "positive",
      "a c": "neutral",
      "c c": "negative",
    },
  },
  CLOCK: {
    "": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
  },
  BDNF: {
    "": {
      "g g": "positive",
      "a g": "neutral",
      "a a": "negative",
    },
  },
  FTO: {
    "": {
      "t t": "positive",
      "a t": "neutral",
      "a a": "negative",
    },
  },
  LCT: {
    "": {
      "t t a a komplementarnie": "positive",
      "c t g a komplementarnie": "neutral",
      "c c g g komplementarnie": "negative",
    },
  },
  CHRNA5: {
    "": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
  },
  ADRA2A: {
    "rs1800544 promotor 1291c g": {
      "c c": "negative",
      "c g": "neutral",
      "g g": "positive",
    },
    "rs553668 3 utr": {
      "g g": "positive",
      "a g": "neutral",
      "a a": "negative",
    },
  },
  ANK3: {
    "rs10994336 bd meqtl": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1938526 kognicja": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs9804190 dti peczek haczykowaty": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  CACNA1C: {
    "rs1006737 psychiatria eh": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs1051375 farmakogenetyka kardiologiczna": {
      "a a": "positive",
      "g a": "neutral",
      "g g": "negative",
    },
    "rs2159100 nastroj bd": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "mutacje patogenne zespol timothy ego": {
      "g406r g402s missense": "negative",
    },
  },
  CDH13: {
    "rs11649622 impulsywnosc": {
      "g g": "positive",
      "a g": "neutral",
      "a a": "negative",
    },
    "rs2199430 kognicja adhd": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs4783244 metabolizm serce": {
      "g g": "negative",
      "g t": "neutral",
      "t t": "positive",
    },
    "rs11646213": {
      "g g": "positive",
      "a g": "neutral",
      "a a": "negative",
    },
  },
  FKBP5: {
    "rs1360780 intron 2 glowny marker": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs9296158 intron 5 trauma dziecieca": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs9470080": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  DBH: {
    "rs1611115 c 1021t c 970t promotor": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1108580 444g a": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs2519154 farmakogenomika atomoksetyny": {
      "c c": "negative",
      "c t": "neutral",
      "t t": "positive",
    },
    "rs2519152": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs129882": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs7040170 a g": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
  },
  MAOA: {
    "maoa uvntr promotor liczba powtorzen nie klasyczny snp": {
      "4r 4 5r": "positive",
      "3 3r": "positive",
      "3r 3 5r": "negative",
      "2r 2 5r": "negative",
    },
    "rs6323 r297r": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
    "rs1137070 c 1410t c synonimiczny": {
      "t t": "positive",
      "c t": "neutral",
      "c c": "negative",
    },
    "rs909525 proxy uvntr": {
      "t t": "positive",
      "c t": "neutral",
      "c c": "negative",
    },
    "rs72554632 p gln296ter rzadka patologia": {
      "t nosiciel": "negative",
    },
  },
  MC1R: {
    "rs1805007 r151c": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1805008 r160w": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1805009 d294h": {
      "g g": "positive",
      "g c": "neutral",
      "c c": "negative",
    },
    "rs2228479 v92m": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "neutral",
    },
  },
  APOE: {
    "haplotypy apoe rs429358 rs7412": {
      "t t c c 3 3 e3 e3 cys112 arg158 typ referencyjny najbardziej powszechny calkowicie ewolucyjnie i metabolicznie poprawny optymalne zdolnosci wiazania vldl brak wplywu na akumulacje beta amyloidu": "positive",
      "c t c c 3 4 e3 e4 mieszane cys arg arg arg ryzyko podwyzszone wyzszy poziom utlenionych ldl nosiciele sa eksponowani na 2 do 4 krotnie wyzsze ryzyko rozwoju choroby alzheimera i wieksza podatnosc na miazdzyce": "negative",
      "c c c c 4 4 e4 e4 arg112 arg158 krytyczne ryzyko interakcja domenowa w calej apolipoproteinie powoduje 25 krotny wzrost ryzyka otepienia sredni wiek pojawienia sie alzheimera u homozygot e4 e4 obniza sie statystycznie do ledwie 68 lat": "negative",
      "t t t c 2 3 e2 e3 mieszane cys cys cys arg wysoce neuroprotekcyjny ochronny wariant promujacy dlugowiecznosc aparatu poznawczego charakteryzuje sie skrajnie niskim prawdopodobienstwem lagodnych zaburzen poznawczych mci i otepienia": "positive",
      "t t t t 2 2 e2 e2 cys112 cys158 dysfunkcja metaboliczna wariant swietnie chroni przed demencja ale wykazuje zerowe powinowactwo do receptorow w watrobie grozi tzw rodzinna dysbetalipoproteinemia przy diecie wysokotluszczowej": "neutral",
      "c t t c 2 4 e2 e4 mieszane cys cys arg arg efekt zniesienia pojawienie sie ochronnego 2 anuluje duza czesc zniszczen za ktore odpowiada patologiczny 4 lagodzac ryzyko do poziomu standardowego": "neutral",
    },
  },
};

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

function fixedVariantTone(geneSymbol, heading, genotype, options = {}) {
  const byGene = FIXED_VARIANT_TONES[String(geneSymbol || "").toUpperCase()];
  if (!byGene) {
    return "neutral";
  }

  const headingKey = normalizeToneKey(heading);
  const genotypeKey = options.lookupKey || normalizeToneKey(genotype);
  const byHeading = byGene[headingKey] || byGene[""];
  if (!byHeading) {
    return "neutral";
  }

  return byHeading[genotypeKey] || "neutral";
}

function parseSections(markdown) {
  const lines = markdown.split(/\r?\n/);
  const sections = [];
  let current = null;

  for (const line of lines) {
    const match = line.match(/^###\s+\d+\.\s+(.+)$/);
    if (match) {
      if (current) {
        sections.push(current);
      }
      current = { title: match[1].trim(), body: [] };
    } else if (current) {
      current.body.push(line);
    }
  }

  if (current) {
    sections.push(current);
  }

  return sections;
}

function sectionPresentation(title) {
  const low = title.toLowerCase();
  const meta = SECTION_META.find((item) => low.includes(item.key));
  return meta || { icon: "📄", label: title };
}

function stripMarkdown(value) {
  return value
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\*([^*]+)\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function extractHeaderFacts(section) {
  if (!section) {
    return [];
  }
  return section.body
    .map((line) => line.trim())
    .filter((line) => /^[*-]\s+\*\*[^*]+\*\*:\s+.+$/.test(line))
    .map((line) => {
      const match = line.match(/^[*-]\s+\*\*([^*]+)\*\*:\s+(.+)$/);
      return match ? { key: stripMarkdown(match[1]), value: stripMarkdown(match[2]) } : null;
    })
    .filter(Boolean)
    .slice(0, 6);
}

function linkPmids(html) {
  return html.replace(
    /(PMID[:\s]*)(\d{6,9})/gi,
    '$1<a href="https://pubmed.ncbi.nlm.nih.gov/$2/" target="_blank" rel="noreferrer">$2</a>'
  );
}

function isTableSeparatorLine(line) {
  const cells = line
    .split("|")
    .map((cell) => cell.trim())
    .filter((cell, index, arr) => !(index === 0 && cell === "") && !(index === arr.length - 1 && cell === ""));
  return cells.length > 0 && cells.every((cell) => /^:?-{3,}:?$/.test(cell));
}

function parseMarkdownTable(lines) {
  const tableLines = lines.map((line) => line.trim()).filter((line) => line.startsWith("|"));
  if (tableLines.length < 2) {
    return null;
  }

  const toCells = (line) =>
    line
      .split("|")
      .map((cell) => stripMarkdown(cell.trim()))
      .filter((cell, index, arr) => !(index === 0 && cell === "") && !(index === arr.length - 1 && cell === ""));

  const headers = toCells(tableLines[0]);
  const rows = tableLines
    .slice(1)
    .filter((line) => !isTableSeparatorLine(line))
    .map(toCells)
    .filter((row) => row.length && row.some((cell) => cell));

  if (!headers.length || !rows.length) {
    return null;
  }

  const headerKey = headers.join("|").toLowerCase();
  const dataRows = rows.filter((row) => row.join("|").toLowerCase() !== headerKey);
  if (!dataRows.length) {
    return null;
  }

  return { headers, rows: dataRows };
}

function splitTableByIdentifierColumn(table) {
  const rsRows = table.rows.filter((row) => /^rs\d+/i.test(stripMarkdown(row[0] || "")));
  if (rsRows.length < 2) {
    return [{ table, title: "" }];
  }

  const groups = [];
  let group = null;

  const flush = () => {
    if (group && group.rows.length) {
      groups.push(group);
    }
    group = null;
  };

  for (const row of table.rows) {
    const label = stripMarkdown(row[0] || "");
    const isRs = /^rs\d+/i.test(label);

    if (isRs) {
      flush();
      group = { title: label, headers: table.headers.slice(1), rows: [row.slice(1)] };
      continue;
    }

    flush();
    groups.push({
      title: label || "Wariant",
      headers: table.headers.slice(1),
      rows: [row.slice(1)],
    });
  }

  flush();
  return groups.map((item) => ({ table: { headers: item.headers, rows: item.rows }, title: item.title }));
}

function splitVariantBlocks(body) {
  const blocks = [];
  let current = { title: "", lines: [] };

  const pushCurrent = () => {
    if (!current.title && !current.lines.some((line) => line.trim())) {
      return;
    }
    blocks.push(current);
    current = { title: "", lines: [] };
  };

  for (const line of body) {
    const trimmed = line.trim();
    const titleMatch = trimmed.match(/^\*\*([^*]+)\*\*$/);

    if (titleMatch) {
      pushCurrent();
      current.title = stripMarkdown(titleMatch[1]);
      continue;
    }

    if (trimmed.startsWith("|")) {
      current.lines.push(line);
      continue;
    }

    if (!trimmed && current.lines.length) {
      current.lines.push(line);
      continue;
    }

    if (trimmed) {
      pushCurrent();
      current = { title: "", lines: [line] };
      pushCurrent();
    }
  }

  pushCurrent();

  if (blocks.length) {
    return blocks;
  }

  const tableLines = body.filter((line) => line.trim().startsWith("|"));
  if (tableLines.length) {
    return [{ title: "", lines: tableLines }];
  }

  return [];
}

function renderVariantTiles(table, context = {}) {
  const { headers, rows } = table;
  const isApoe = context.gene === "APOE";

  return rows
    .map((row) => {
      const genotype = row[0] || "Wariant";
      const summary = row[row.length - 1] || "";
      const headingText = isApoe ? row[2] || genotype : genotype;
      const status = isApoe
        ? `${headers[0] || "rs429358"}: ${row[0] || "-"} | ${headers[1] || "rs7412"}: ${row[1] || "-"}`
        : row[1] || "";
      const details = headers
        .map((header, i) => ({ header, value: row[i] || "" }))
        .slice(isApoe ? 3 : 2, Math.max(isApoe ? 3 : 2, headers.length - 1))
        .filter((item) => item.value);
      const lookupKey =
        isApoe
          ? normalizeToneKey(row.join(" "))
          : normalizeToneKey(genotype);
      const tone = fixedVariantTone(context.gene, context.heading, genotype, { lookupKey });

      return `
        <article class="variant-tile variant-tile--${tone}${isApoe ? " variant-tile--apoe" : ""}">
          <h4>${escapeHtml(headingText)}</h4>
          ${status ? `<p class="variant-status">${escapeHtml(status)}</p>` : ""}
          ${
            details.length
              ? `<dl>${details
                  .map(
                    (item) =>
                      `<div><dt>${escapeHtml(item.header)}</dt><dd>${escapeHtml(item.value)}</dd></div>`
                  )
                  .join("")}</dl>`
              : ""
          }
          ${summary ? `<p class="variant-impact">${escapeHtml(summary)}</p>` : ""}
        </article>
      `;
    })
    .join("");
}

function renderVariantsSection(section) {
  const blocks = splitVariantBlocks(section.body);
  if (!blocks.length) {
    return null;
  }

  const groups = blocks
    .map((block) => {
      const table = parseMarkdownTable(block.lines);
      if (table) {
        const subTables = splitTableByIdentifierColumn(table);
        return subTables
          .map(({ table: subTable, title: subTitle }) => {
            const heading = block.title || subTitle;
            return `
          <section class="variant-group">
            ${heading ? `<h4 class="variant-group-title">${escapeHtml(heading)}</h4>` : ""}
            <div class="variants-layout">${renderVariantTiles(subTable, { gene, heading })}</div>
          </section>
        `;
          })
          .join("");
      }

      const markdown = block.lines.join("\n").trim();
      if (!markdown) {
        return "";
      }

      const parsed = window.marked ? window.marked.parse(markdown) : markdown;
      return `
        <section class="variant-group">
          ${block.title ? `<h4 class="variant-group-title">${escapeHtml(block.title)}</h4>` : ""}
          <div class="variant-group-note">${parsed}</div>
        </section>
      `;
    })
    .filter(Boolean)
    .join("");

  return groups ? `<div class="variants-stack">${groups}</div>` : null;
}

function classifySection(section) {
  const label = sectionPresentation(section.title).label;
  if (label === "Profil genu") {
    return "profile";
  }
  if (label === "Identyfikatory i SNP") {
    return "identifiers";
  }
  if (label === "Mechanizm działania") {
    return "mechanism";
  }
  if (label === "Warianty i fenotyp") {
    return "variants";
  }
  return "rest";
}

function renderSectionCard(section) {
  const meta = sectionPresentation(section.title);
  const markdownBody = section.body.join("\n").trim();
  if (!markdownBody) {
    return "";
  }

  let sectionBody = "";
  if (meta.label === "Warianty i fenotyp") {
    const variantBody = renderVariantsSection(section);
    sectionBody = variantBody || (window.marked ? window.marked.parse(markdownBody) : markdownBody);
  } else {
    sectionBody = window.marked ? window.marked.parse(markdownBody) : markdownBody;
  }
  const enhancedBody = linkPmids(sectionBody);

  return `
    <section class="section-card">
      <header class="section-head">
        <span class="section-icon">${meta.icon}</span>
        <h3>${meta.label}</h3>
      </header>
      <div class="section-body">${enhancedBody}</div>
    </section>
  `;
}

function renderRow(className, html) {
  if (!html.trim()) {
    return "";
  }
  return `<div class="layout-row ${className}">${html}</div>`;
}

function renderCards(sections) {
  return sections.map(renderSectionCard).filter(Boolean).join("");
}

function renderGenePresentation(markdown) {
  const sections = parseSections(markdown);
  const buckets = {
    profile: [],
    identifiers: [],
    mechanism: [],
    variants: [],
    rest: [],
  };

  for (const section of sections) {
    buckets[classifySection(section)].push(section);
  }

  const profileSection = buckets.profile[0];
  const facts = extractHeaderFacts(profileSection);

  if (titleNode) {
    titleNode.textContent = `${gene} - karta genu`;
  }
  if (subtitleNode) {
    const shortDesc = facts.find((item) => item.key.toLowerCase().includes("pełna nazwa"));
    subtitleNode.textContent = shortDesc
      ? shortDesc.value
      : "Uporządkowana prezentacja informacji medyczno-genetycznych.";
  }

  return `
    <div class="gene-layout">
      ${renderRow("layout-row--full", renderCards(buckets.profile))}
      ${renderRow(
        "layout-row--split",
        `${renderCards(buckets.identifiers)}${renderCards(buckets.mechanism)}`
      )}
      ${renderRow("layout-row--full", renderCards(buckets.variants))}
      ${renderRow("layout-row--rest", `<div class="presentation-rest">${renderCards(buckets.rest)}</div>`)}
    </div>
  `;
}

async function loadGenePage() {
  if (!gene || !contentNode) {
    return;
  }

  document.title = `${gene} | GenMarkerWiki`;

  try {
    const response = await fetch(`../md/${gene}.md`);
    if (!response.ok) {
      throw new Error(`Nie znaleziono pliku md/${gene}.md`);
    }

    const markdown = await response.text();
    contentNode.innerHTML = renderGenePresentation(markdown);
    if (statusNode) {
      statusNode.textContent = "";
    }
  } catch (error) {
    contentNode.innerHTML = "";
    if (statusNode) {
      statusNode.textContent =
        `Nie udało się wczytać treści (${error.message}). ` +
        "Uruchom lokalny serwer HTTP (np. Live Server), zamiast otwierać plik bezpośrednio.";
    }
  }
}

loadGenePage();
