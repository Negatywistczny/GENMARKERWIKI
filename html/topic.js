(function () {
  const params = new URLSearchParams(window.location.search);
  const topicId = (params.get("topic") || "").trim().toLowerCase();

  const titleNode = document.getElementById("topic-title");
  const subtitleNode = document.getElementById("topic-subtitle");
  const iconNode = document.getElementById("topic-icon");
  const contentNode = document.getElementById("topic-content");
  const statusNode = document.getElementById("topic-status");
  const navExtraNode = document.getElementById("topic-nav-extra");

  const byGene = Object.fromEntries((window.GENE_INDEX || []).map((e) => [e.gene, e]));
  const profiles = window.PERSONAL_GENE_PROFILES || {};
  const genesWithCard = window.GENES_WITH_MD || new Set();
  const genesWithMini = window.GENES_WITH_MINI || new Set();

  function hasGeneCard(symbol) {
    return genesWithCard.has(symbol) || genesWithMini.has(symbol);
  }

  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function parseProfileTone(value) {
    const tone = String(value || "").trim().toLowerCase();
    return tone === "positive" || tone === "negative" || tone === "neutral" ? tone : "";
  }

  function variantTone(symbol, block) {
    const fromBlock = parseProfileTone(block.tone);
    if (fromBlock) {
      return fromBlock;
    }
    return window.fixedVariantTone
      ? window.fixedVariantTone(symbol, block.heading, block.genotype)
      : "neutral";
  }

  function normalizeVariantBlock(block, fallbackHeadline) {
    return {
      heading: block.heading || "",
      headline: block.headline || fallbackHeadline || "",
      text: block.text || "",
      genotype: block.genotype || "",
      tone: block.tone || "",
    };
  }

  function personalBlocks(symbol) {
    const profile = profiles[symbol];
    if (!profile) return null;

    const topicEntry = profile.byTopic?.[topicId];
    if (topicEntry?.variants?.length) {
      return topicEntry.variants.map((block) =>
        normalizeVariantBlock(block, profile.headline)
      );
    }

    if (profile.variants?.length) {
      return profile.variants.map((block) => normalizeVariantBlock(block, profile.headline));
    }

    const text =
      (typeof topicEntry === "object" ? topicEntry?.text : topicEntry) || profile.impact;
    if (!text) return null;

    const ctx =
      (typeof topicEntry === "object" && topicEntry?.genotype
        ? { heading: topicEntry.heading, genotype: topicEntry.genotype }
        : null) ||
      profile.toneCtx ||
      {};

    return [
      {
        heading: ctx.heading || "",
        headline: profile.headline || "",
        text,
        genotype: ctx.genotype || "",
      },
    ];
  }

  function renderVariantBlock(symbol, block) {
    const tone = variantTone(symbol, block);
    const rsid = block.heading
      ? `<span class="topic-personal-rsid">${escapeHtml(block.heading)}</span>`
      : "";
    const headline = block.headline
      ? `<span class="topic-personal-genotype">${escapeHtml(block.headline)}</span>`
      : "";
    const title =
      rsid || headline
        ? `<div class="topic-personal-title">${rsid}${headline}</div>`
        : "";
    return `<div class="topic-personal topic-personal--${tone}">
      ${title}
      <p class="topic-personal-text">${escapeHtml(block.text)}</p>
    </div>`;
  }

  function renderPersonalCell(symbol) {
    if (!hasGeneCard(symbol)) {
      return `<span class="topic-personal-empty">—</span>`;
    }
    const blocks = personalBlocks(symbol);
    if (!blocks?.length) {
      return `<span class="topic-personal-empty">—</span>`;
    }
    const stackClass =
      blocks.length === 1
        ? "topic-personal-stack topic-personal-stack--single"
        : "topic-personal-stack";
    return `<div class="${stackClass}">${blocks
      .map((block) => renderVariantBlock(symbol, block))
      .join("")}</div>`;
  }

  function renderGeneRoleCell(symbol, role) {
    const entry = byGene[symbol];
    const symbolHtml = `<strong class="topic-gene-symbol">${escapeHtml(symbol)}</strong>`;
    let geneTop = symbolHtml;
    if (entry && hasGeneCard(symbol)) {
      const isMini = genesWithMini.has(symbol);
      const linkClass = isMini
        ? `topic-gene-card-link topic-gene-card-link--icon-only gene-card gene-card--${entry.tone}`
        : `topic-gene-card-link gene-card gene-card--${entry.tone}`;
      const labelHtml = isMini
        ? ""
        : `<span class="topic-gene-card-link__label">${escapeHtml(entry.label)}</span>`;
      const ariaLabel = isMini ? ` aria-label="${escapeHtml(entry.label)} — karta genu"` : "";
      geneTop += `<a class="${linkClass}" href="gene.html?gene=${encodeURIComponent(symbol)}" data-tone="${entry.tone}"${ariaLabel}>
        <span class="gene-card__icon" aria-hidden="true">${entry.icon}</span>${labelHtml}
      </a>`;
    }
    const roleHtml = role
      ? `<p class="topic-gene-role">${escapeHtml(role)}</p>`
      : `<p class="topic-gene-role topic-gene-role--empty">—</p>`;
    return `<div class="topic-gene-role-cell">
      <div class="topic-gene-cell">${geneTop}</div>
      ${roleHtml}
    </div>`;
  }

  function renderSection(section) {
    const rows = (section.genes || [])
      .map(
        ({ symbol, role }) => `<tr>
          <td class="topic-table__gene">${renderGeneRoleCell(symbol, role)}</td>
          <td class="topic-table__personal">${renderPersonalCell(symbol)}</td>
        </tr>`
      )
      .join("");

    return `<section class="topic-section">
      <h2 class="category-head">${escapeHtml(section.label)}</h2>
      <div class="topic-table-wrap">
        <table class="topic-table">
          <thead>
            <tr>
              <th scope="col">Gen</th>
              <th scope="col">U mnie</th>
            </tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
    </section>`;
  }

  function renderRelatedTopics(currentId) {
    const current = window.TOPIC_BY_ID[currentId];
    if (!current) return "";

    const siblings = window.TOPIC_GROUPS.find((g) => g.id === current.groupId);
    if (!siblings) return "";

    const links = siblings.topics
      .filter((t) => t.id !== currentId)
      .map(
        (t) =>
          `<a class="topic-related-link" href="topic.html?topic=${encodeURIComponent(t.id)}"><span aria-hidden="true">${t.icon}</span> ${escapeHtml(t.label)}</a>`
      )
      .join("");

    return `<section class="topic-section topic-section--related">
      <h2 class="category-head">Powiązane tematy</h2>
      <div class="topic-related">${links}</div>
    </section>`;
  }

  function showError(message) {
    statusNode.hidden = false;
    statusNode.textContent = message;
    contentNode.innerHTML = `<p class="topic-error">${escapeHtml(message)}</p>
      <p><a href="../index.html#tematy">Przejdź do listy tematów</a></p>`;
  }

  function render(topic) {
    document.title = `GenMarkerWiki — ${topic.label}`;

    titleNode.textContent = topic.label;
    subtitleNode.textContent = topic.summary;
    iconNode.textContent = topic.icon;
    navExtraNode.innerHTML = "";

    contentNode.innerHTML =
      topic.sections.map(renderSection).join("") + renderRelatedTopics(topic.id);

    statusNode.hidden = true;
  }

  if (!topicId) {
    showError("Brak parametru ?topic= w adresie URL.");
    return;
  }

  const topic = window.TOPIC_BY_ID[topicId];
  if (!topic) {
    const available = Object.keys(window.TOPIC_BY_ID).sort().join(", ");
    showError(`Nieznany temat „${topicId}". Dostępne: ${available}`);
    return;
  }

  render(topic);
})();
