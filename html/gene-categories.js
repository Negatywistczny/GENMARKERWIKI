/** Kategorie genów — wspólne źródło dla indeksu HTML i raportu osobistego.
 *
 * Kolejność kategorii: jak w tablicy poniżej (mózg → metabolizm → zmysły → serce → sport).
 * Kolejność genów w kategorii: alfabetycznie (A–Z).
 */
window.GENE_CATEGORIES = [
  {
    id: "brain",
    label: "Mózg, nastrój i zachowanie",
    icon: "🧠",
    genes: [
      "ADRA2A", "ANK3", "ANKK1", "APOE", "AVPR1A", "BDNF", "CACNA1C", "CHRM2",
      "COMT", "DBH", "DRD2", "FKBP5", "MAOA", "OXTR", "SLC6A4", "SNAP25",
      "TPH2", "WWC1",
    ],
  },
  {
    id: "metabolism",
    label: "Metabolizm i substancje",
    icon: "🍽️",
    genes: [
      "ALDH2", "CHRNA5", "CYP1A2", "CYP2C19", "CYP2D6", "FTO", "GC", "LCT",
      "MTHFR", "TAS2R38",
    ],
  },
  {
    id: "senses",
    label: "Wygląd i zmysły",
    icon: "👁️",
    genes: [
      "ABCC11", "HERC2", "KCNQ4", "MC1R", "OCA2", "OR2M", "OR6A2", "SLC24A4",
      "SLC45A2",
    ],
  },
  {
    id: "cardio",
    label: "Serce, naczynia i hormony",
    icon: "❤️",
    genes: ["AR", "CDH13", "CLOCK", "VKORC1", "ZEB2"],
  },
  {
    id: "sport",
    label: "Sport i wydolność",
    icon: "🏃",
    genes: ["ACTN3"],
  },
];

/** Poprawna odmiana liczby genów po polsku: 1 gen, 2–4 geny, 5+ genów (z wyjątkami 12–14). */
window.formatGeneCount = function formatGeneCount(n) {
  const count = Number(n);
  if (count === 1) return "1 gen";
  const mod10 = count % 10;
  const mod100 = count % 100;
  if (mod10 >= 2 && mod10 <= 4 && (mod100 < 12 || mod100 > 14)) {
    return `${count} geny`;
  }
  return `${count} genów`;
};
