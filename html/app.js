function getGene() {
  return (document.body.dataset.gene || "").trim();
}
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


const fixedVariantTone = window.fixedVariantTone;
const normalizeToneKey = window.normalizeToneKey || ((value) => String(value || "").toLowerCase());

function parseSections(markdown) {
  const lines = markdown.split(/\r?\n/);
  const sections = [];
  let current = null;

  for (const line of lines) {
    const match = line.trim().match(/^###\s+(\d+)\.\s+(.+)$/);
    if (match) {
      if (current) {
        sections.push(current);
      }
      current = { number: Number(match[1]), title: match[2].trim(), body: [] };
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
    .replace(/★\s*/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

function isPersonalMarker(value) {
  return /★/.test(String(value || ""));
}

function parseTableCell(raw) {
  const text = String(raw || "").trim();
  const majorBlocks = text.split(/<br\s*\/?>\s*<br\s*\/?>/gi);
  const segments = majorBlocks
    .map((block) =>
      block
        .split(/<br\s*\/?>/gi)
        .map((part) => stripMarkdown(part.trim()))
        .filter(Boolean)
        .join(" ")
    )
    .filter(Boolean);
  return {
    text: segments.length ? segments.join("\n\n") : stripMarkdown(text),
    personal: isPersonalMarker(text),
  };
}

function parseImpactSections(text) {
  return String(text || "")
    .split(/\n{2,}/)
    .map((part) => part.trim())
    .filter(Boolean)
    .map((chunk) => {
      const m = chunk.match(/^([^:]+):\s+(.+)$/s);
      if (m && m[1].length <= 72) {
        return { label: m[1].trim(), body: m[2].trim() };
      }
      return { label: "", body: chunk };
    });
}

function renderImpactSections(summary) {
  const sections = parseImpactSections(summary);
  if (!sections.length) {
    return "";
  }
  const structured = sections.length > 1 || sections.some((s) => s.label);
  if (!structured) {
    return `<p class="variant-impact">${escapeHtml(sections[0].body)}</p>`;
  }
  return `<dl class="variant-sections">${sections
    .map((section) =>
      section.label
        ? `<div><dt>${escapeHtml(section.label)}</dt><dd>${escapeHtml(section.body)}</dd></div>`
        : `<div><dd>${escapeHtml(section.body)}</dd></div>`
    )
    .join("")}</dl>`;
}

function formatMultilineEscaped(text) {
  return String(text || "")
    .split(/\n/)
    .map((part) => part.trim())
    .filter(Boolean)
    .map((part) => escapeHtml(part))
    .join("<br>");
}

function tableRowCells(row) {
  return Array.isArray(row) ? row : row.cells || [];
}

function tableRowIsPersonal(row) {
  if (!Array.isArray(row) && row.personal) {
    return true;
  }
  const cells = tableRowCells(row);
  return cells.some((cell) => isPersonalMarker(cell));
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
      .map((cell) => parseTableCell(cell.trim()))
      .filter((cell, index, arr) => !(index === 0 && !cell.text) && !(index === arr.length - 1 && !cell.text));

  const headers = toCells(tableLines[0]).map((cell) => cell.text);
  const rows = tableLines
    .slice(1)
    .filter((line) => !isTableSeparatorLine(line))
    .map(toCells)
    .filter((row) => row.length && row.some((cell) => cell.text))
    .map((row) => ({
      cells: row.map((cell) => cell.text),
      personal: row.some((cell) => cell.personal),
    }));

  if (!headers.length || !rows.length) {
    return null;
  }

  const headerKey = headers.join("|").toLowerCase();
  const dataRows = rows.filter((row) => row.cells.join("|").toLowerCase() !== headerKey);
  if (!dataRows.length) {
    return null;
  }

  return { headers, rows: dataRows };
}

function splitTableByIdentifierColumn(table) {
  const rsRows = table.rows.filter((row) => /^rs\d+/i.test(tableRowCells(row)[0] || ""));
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
    const cells = tableRowCells(row);
    const label = cells[0] || "";
    const isRs = /^rs\d+/i.test(label);

    if (isRs) {
      flush();
      group = {
        title: label,
        headers: table.headers.slice(1),
        rows: [{ cells: cells.slice(1), personal: tableRowIsPersonal(row) }],
      };
      continue;
    }

    flush();
    groups.push({
      title: label || "Wariant",
      headers: table.headers.slice(1),
      rows: [{ cells: cells.slice(1), personal: tableRowIsPersonal(row) }],
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
    const titleMatch = trimmed.match(/^\*\*(.+)\*\*$/);

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
  const isApoeHaplotypeTable =
    isApoe &&
    headers.some((h) => /rs429358/i.test(h)) &&
    headers.some((h) => /rs7412/i.test(h));
  const isApoeHaplotypeCombined =
    isApoe &&
    !isApoeHaplotypeTable &&
    /rs429358.*rs7412|haplotyp\s*[εe]2/i.test(context.heading || "");
  const isApoeHaplotype = isApoeHaplotypeTable || isApoeHaplotypeCombined;
  const toneHeading =
    isApoeHaplotype && !context.heading
      ? "haplotypy apoe rs429358 rs7412"
      : context.heading;

  return rows
    .map((row) => {
      const cells = tableRowCells(row);
      const personal = tableRowIsPersonal(row);
      const genotype = cells[0] || "Wariant";
      const summary = cells[cells.length - 1] || "";
      const headingText = isApoeHaplotypeCombined
        ? cells[1] || genotype
        : isApoeHaplotypeTable
          ? cells[2] || genotype
          : genotype;
      const status = isApoeHaplotypeCombined
        ? cells[0] || ""
        : isApoeHaplotypeTable
          ? `${headers[0] || "rs429358"}: ${cells[0] || "-"} | ${headers[1] || "rs7412"}: ${cells[1] || "-"}`
          : cells[1] || "";
      const details = headers
        .map((header, i) => ({ header, value: cells[i] || "" }))
        .slice(isApoeHaplotypeTable ? 3 : 2, Math.max(isApoeHaplotypeTable ? 3 : 2, headers.length - 1))
        .filter((item) => item.value);
      const tone = fixedVariantTone(
        context.gene,
        toneHeading,
        genotype,
        isApoeHaplotype ? { lookupKey: normalizeToneKey(cells.join(" ")) } : {}
      );

      return `
        <article class="variant-tile variant-tile--${tone}${personal ? " variant-tile--personal" : ""}${isApoeHaplotype ? " variant-tile--apoe" : ""}">
          <h4 class="variant-tile-heading">
            <span class="variant-tile-title">${escapeHtml(headingText)}</span>
            ${personal ? '<span class="variant-personal-badge" aria-label="Twój wariant z bazy">★ Twój wariant</span>' : ""}
          </h4>
          ${status ? `<p class="variant-status">${escapeHtml(status)}</p>` : ""}
          ${
            details.length
              ? `<dl>${details
                  .map(
                    (item) =>
                      `<div><dt>${escapeHtml(item.header)}</dt><dd>${formatMultilineEscaped(item.value)}</dd></div>`
                  )
                  .join("")}</dl>`
              : ""
          }
          ${summary ? renderImpactSections(summary) : ""}
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
            const apoeHeaders = subTable.headers || [];
            const isApoeHaplotypeGroup =
              getGene() === "APOE" &&
              ((apoeHeaders.some((h) => /rs429358/i.test(h)) &&
                apoeHeaders.some((h) => /rs7412/i.test(h))) ||
                /rs429358.*rs7412|haplotyp\s*[εe]2/i.test(block.title || ""));
            const heading =
              block.title ||
              subTitle ||
              (isApoeHaplotypeGroup ? "Haplotypy APOE (rs429358 + rs7412)" : "");
            return `
          <section class="variant-group">
            ${heading ? `<h4 class="variant-group-title">${escapeHtml(heading)}</h4>` : ""}
            <div class="variants-layout">${renderVariantTiles(subTable, { gene: getGene(), heading })}</div>
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

function mergeDuplicateVariantSections(sections) {
  const variantIndexes = sections
    .map((section, index) => (classifySection(section) === "variants" ? index : -1))
    .filter((index) => index >= 0);

  if (variantIndexes.length <= 1) {
    return sections;
  }

  const keep = variantIndexes[0];
  const merged = {
    ...sections[keep],
    body: variantIndexes.flatMap((index) => sections[index].body),
  };

  return sections
    .map((section, index) => {
      if (index === keep) {
        return merged;
      }
      if (variantIndexes.includes(index)) {
        return null;
      }
      return section;
    })
    .filter(Boolean);
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
  const heading = meta.label;

  return `
    <section class="section-card">
      <header class="section-head">
        <span class="section-icon">${meta.icon}</span>
        <h3>${heading}</h3>
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
  const sections = mergeDuplicateVariantSections(parseSections(markdown));
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
    titleNode.textContent = `${getGene()} - karta genu`;
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
  const geneSymbol = getGene();
  if (!geneSymbol || !contentNode) {
    if (statusNode) {
      statusNode.textContent =
        "Podaj symbol genu w adresie URL, np. gene.html?gene=COMT.";
    }
    return;
  }

  document.title = `${geneSymbol} | GenMarkerWiki`;

  try {
    const response = await fetch(`../md/${geneSymbol}.md`);
    if (!response.ok) {
      throw new Error(`Nie znaleziono karty genu ${geneSymbol}.`);
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

function resolveGeneFromUrl() {
  const params = new URLSearchParams(window.location.search);
  const fromQuery = params.get("gene");
  if (fromQuery) {
    document.body.dataset.gene = fromQuery.trim().toUpperCase();
  }
}

resolveGeneFromUrl();
loadGenePage();