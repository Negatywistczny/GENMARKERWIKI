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

function parseMarkdownTable(lines) {
  const tableLines = lines.map((line) => line.trim()).filter((line) => line.startsWith("|"));
  if (tableLines.length < 3) {
    return null;
  }

  const toCells = (line) =>
    line
      .split("|")
      .map((cell) => stripMarkdown(cell.trim()))
      .filter((cell, index, arr) => !(index === 0 && cell === "") && !(index === arr.length - 1 && cell === ""));

  const headers = toCells(tableLines[0]);
  const rows = tableLines.slice(2).map(toCells).filter((row) => row.length);
  if (!headers.length || !rows.length) {
    return null;
  }

  return { headers, rows };
}

function renderVariantsSection(section) {
  const table = parseMarkdownTable(section.body);
  if (!table) {
    return null;
  }

  const { headers, rows } = table;
  const cards = rows
    .map((row) => {
      const genotype = row[0] || "Wariant";
      const status = row[1] || "";
      const summary = row[row.length - 1] || "";
      const details = headers
        .map((header, index) => ({ header, value: row[index] || "" }))
        .slice(2, Math.max(2, headers.length - 1))
        .filter((item) => item.value);

      return `
        <article class="variant-tile">
          <h4>${escapeHtml(genotype)}</h4>
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

  return `<div class="variants-layout">${cards}</div>`;
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
