/** Strony tematyczne — zestawienia genów wg zaburzeń, szlaków i zastosowań.
 *
 * Tematy psychiatryczne (asd, adhd, mdd, chad, scz) pobierają sekcje z topic-psychiatry-sections.js.
 */
(function () {
  const PSY = window.TOPIC_PSYCHIATRY_SECTIONS || {};

  window.TOPIC_GROUPS = [
    {
      id: "psychiatry",
      label: "Psychiatria i neurorozwój",
      icon: "🧠",
      topics: [
        {
          id: "asd",
          label: "Spektrum autyzmu (ASD)",
          icon: "🧩",
          summary:
            "Geny związane z ASD — od mutacji de novo o wysokiej penetracji (SFARI) przez warianty PRS po modyfikatory metaboliczne i immunologiczne.",
          sections: PSY.asd || [],
        },
        {
          id: "adhd",
          label: "ADHD",
          icon: "⚡",
          summary:
            "Markery ADHD: szlaki dopaminergiczne i serotoninergiczne, neurorozwój synaptyczny, TWAS i sygnatury biotypów. Większość wariantów ma charakter poligenowy (PRS).",
          sections: PSY.adhd || [],
        },
        {
          id: "mdd",
          label: "Depresja (MDD)",
          icon: "🌧️",
          summary:
            "Architektura genetyczna depresji według biotypów: zapalny, poznawczy, lękowy/HPA, melancholijny oraz moduł farmakogenetyczny.",
          sections: PSY.mdd || [],
        },
        {
          id: "chad",
          label: "ChAD (choroba afektywna dwubiegunowa)",
          icon: "🌊",
          summary:
            "ChAD dzieli część architektury ze schizofrenią (plejotropia). Geny priorytetowe PGC, sygnatury TWAS biotypów psychozy i markery odpowiedzi na lit.",
          sections: PSY.chad || [],
        },
        {
          id: "scz",
          label: "Schizofrenia (SCZ)",
          icon: "🔮",
          summary:
            "Geny priorytetowe PGC3, architektura biotypów psychotycznych (TWAS/B-SNIP) i szlaki glutaminianowe/NMDA.",
          sections: PSY.scz || [],
        },
        {
          id: "neurodev",
          label: "Neurorozwój, ID i padaczka",
          icon: "🧬",
          summary:
            "Geny o wysokiej penetracji: encefalopatie rozwojowe, padaczka i zespoły syndromiczne — odrębna ścieżka od wariantów poligenowych.",
          sections: [
            {
              label: "Encefalopatie rozwojowe i padaczka",
              genes: [
                { symbol: "SCN2A", role: "Kanały Na⁺; DEE, ASD", evidence: "Patogenny LoF/GoF" },
                { symbol: "SYNGAP1", role: "Plastyczność synaptyczna; DEE", evidence: "De novo LoF" },
                { symbol: "SHANK3", role: "Phelan-McDermid; ciężkie ID", evidence: "De novo LoF" },
                { symbol: "GRIN2B", role: "Podjednostka NMDA; neurotransmisja", evidence: "SFARI / de novo" },
                { symbol: "GRIN2A", role: "Podjednostka NMDA; padaczka", evidence: "LoF" },
                { symbol: "CNTNAP2", role: "Adhezja; opóźnienia mowy", evidence: "Kandydat" },
              ],
            },
            {
              label: "Zespoły syndromiczne",
              genes: [
                { symbol: "ADNP", role: "Helsmoortel-Van der Aa", evidence: "De novo" },
                { symbol: "FMR1", role: "Zespół łamliwego X", evidence: "Trinukleotyd CGG" },
                { symbol: "MECP2", role: "Zespół Retta", evidence: "X-linked de novo" },
                { symbol: "TSC1", role: "Stwardnienie guzowate (hamartyna)", evidence: "Syndromiczny" },
                { symbol: "TSC2", role: "Stwardnienie guzowate (tuberyna)", evidence: "Syndromiczny" },
                { symbol: "PTEN", role: "Zespół Cowden; makrocefalia", evidence: "Kategoria S" },
                { symbol: "UBE3A", role: "Zespół Angelmana", evidence: "Kategoria S" },
                { symbol: "TCF4", role: "Zespół Pitta-Hopkinsa", evidence: "Kategoria S" },
                { symbol: "KMT2D", role: "Zespół Kabuki", evidence: "Kategoria S" },
                { symbol: "CHD8", role: "Remodelowanie chromatyny; makrocefalia", evidence: "SFARI Kategoria 1" },
                { symbol: "DYRK1A", role: "Proliferacja neuronów", evidence: "SFARI Kategoria 1" },
                { symbol: "ARID1B", role: "Kompleks SWI/SNF", evidence: "SFARI Kategoria 1" },
                { symbol: "ZEB2", role: "Mowat-Wilson; wady serca", evidence: "Syndromiczny" },
              ],
            },
          ],
        },
      ],
    },
    {
      id: "pathways",
      label: "Szlaki molekularne",
      icon: "🔗",
      topics: [
        {
          id: "dopamine",
          label: "Oś dopaminergiczna i nagroda",
          icon: "🎁",
          summary:
            "Synteza, transport, degradacja dopaminy i receptory D2–D5. Centralne dla ADHD, uzależnień, impulsywności i odpowiedzi na psychostymulancje.",
          sections: [
            {
              label: "Synteza i degradacja",
              genes: [
                { symbol: "DBH", role: "Dopamina → noradrenalina", evidence: "Funkcjonalny" },
                { symbol: "COMT", role: "Degradacja w PFC (Val158Met)", evidence: "Funkcjonalny" },
                { symbol: "MAOA", role: "Degradacja monoamin (X-linked)", evidence: "Funkcjonalny" },
                { symbol: "SLC6A3", role: "Transporter dopaminy (DAT1)", evidence: "VNTR; PGx metylofenidatu" },
                { symbol: "SLC6A2", role: "Transporter noradrenaliny (NET)", evidence: "Sygnatura biotypu ADHD" },
              ],
            },
            {
              label: "Receptory i modulatory",
              genes: [
                { symbol: "DRD2", role: "Receptor D2; Taq1A, C957T", evidence: "PRS / PGx" },
                { symbol: "DRD4", role: "Receptor D4; allel 7R", evidence: "Kandydat ADHD" },
                { symbol: "DRD5", role: "Receptor D5", evidence: "GWAS ADHD" },
                { symbol: "ANKK1", role: "Gęstość D2 w prążkowiu", evidence: "Funkcjonalny" },
                { symbol: "ADRA2A", role: "Receptor α2A; uwaga", evidence: "PGx" },
              ],
            },
          ],
        },
        {
          id: "serotonin",
          label: "Serotonina i regulacja nastroju",
          icon: "😊",
          summary:
            "Transporter, synteza i receptory serotoniny oraz modulatory plastyczności — kluczowe dla MDD, lęku i odpowiedzi na SSRI/SNRI.",
          sections: [
            {
              label: "Szlak serotoninergiczny",
              genes: [
                { symbol: "SLC6A4", role: "Transporter 5-HTT (5-HTTLPR)", evidence: "Funkcjonalny" },
                { symbol: "TPH2", role: "Synteza serotoniny (limitujący)", evidence: "Funkcjonalny" },
                { symbol: "MAOA", role: "Degradacja serotoniny i dopaminy", evidence: "Funkcjonalny" },
                { symbol: "HTR1B", role: "Receptor 5-HT1B", evidence: "ADHD / impulsywność" },
                { symbol: "HTR2A", role: "Receptor 5-HT2A; PGx SSRI", evidence: "PGx" },
                { symbol: "HTR4", role: "Receptor 5-HT4", evidence: "PRS" },
                { symbol: "HTR6", role: "Receptor 5-HT6", evidence: "Cel leków" },
              ],
            },
            {
              label: "Oś stresu i plastyczność",
              genes: [
                { symbol: "BDNF", role: "Neurotrofina; Val66Met", evidence: "Funkcjonalny / PGx" },
                { symbol: "FKBP5", role: "Modulacja osi HPA", evidence: "Epigenetyczny" },
                { symbol: "CRHR1", role: "Receptor CRH; kortyzol", evidence: "Biotyp lękowy MDD" },
                { symbol: "NR3C1", role: "Receptor glikokortykoidowy (GR)", evidence: "Oś HPA" },
                { symbol: "NR3C2", role: "Receptor mineralokortykoidowy (MR)", evidence: "Stabilność nastroju" },
              ],
            },
          ],
        },
        {
          id: "folate",
          label: "Foliany, homocysteina i metylacja",
          icon: "🧪",
          summary:
            "Szlak folianów i remetylacji homocysteiny. Modyfikuje ryzyko ASD, depresji, wady cewy neuralnej i profil lipidowy.",
          sections: [
            {
              label: "Enzymy szlaku",
              genes: [
                { symbol: "MTHFR", role: "C677T, A1298C — reduktaza MTHFR", evidence: "Funkcjonalny" },
                { symbol: "MTR", role: "Syntaza metioninowa (B12)", evidence: "Funkcjonalny" },
                { symbol: "MTRR", role: "Reduktaza MTRR (A66G)", evidence: "Funkcjonalny" },
                { symbol: "DHFR", role: "Reduktaza dihydrofolianu", evidence: "Modyfikator ASD" },
                { symbol: "CBS", role: "Syntaza cystationiny-beta", evidence: "Homocystynuria" },
              ],
            },
            {
              label: "Współdziałanie witaminy D",
              genes: [
                { symbol: "VDR", role: "Receptor witaminy D; ekspresja genowa", evidence: "Modyfikator" },
                { symbol: "GC", role: "Białko wiążące witaminę D (DBP)", evidence: "Poziom 25-OH-D" },
              ],
            },
          ],
        },
      ],
    },
    {
      id: "pgx",
      label: "Farmakogenomika",
      icon: "💊",
      topics: [
        {
          id: "cyp",
          label: "Metabolizm leków (CYP i dawki)",
          icon: "🧪",
          summary:
            "Enzymy cytochromu P450 i VKORC1 determinują szybkość metabolizmu wielu leków. Genotypowanie zalecane m.in. przez CPIC.",
          sections: [
            {
              label: "Faza I — cytochromy P450",
              genes: [
                { symbol: "CYP2D6", role: "~25% leków; antydepresanty, opioidy", evidence: "CPIC Level A" },
                { symbol: "CYP2C19", role: "PPI, klopidogrel, SSRI", evidence: "CPIC Level A" },
                { symbol: "CYP2B6", role: "Bupropion, mirtazapina", evidence: "CPIC" },
                { symbol: "CYP3A4", role: "TCA (amitryptylina), wiele leków", evidence: "PGx" },
                { symbol: "CYP1A2", role: "Kofeina, klozapina, teofilina", evidence: "PharmGKB 1A" },
              ],
            },
            {
              label: "Antykoagulacja",
              genes: [
                { symbol: "VKORC1", role: "Cel warfaryny; dawka początkowa", evidence: "CPIC Level A" },
              ],
            },
          ],
        },
        {
          id: "psychopharm",
          label: "Psychofarmakologia",
          icon: "🧠",
          summary:
            "Markery modulujące odpowiedź na leki psychiatryczne — metabolizm (CYP), receptory docelowe i transportery monoamin.",
          sections: [
            {
              label: "Metabolizm leków psychiatrycznych",
              genes: [
                { symbol: "CYP2D6", role: "Paroksetyna, fluoksetyna, risperidon", evidence: "CPIC" },
                { symbol: "CYP2C19", role: "Citalopram, escitalopram", evidence: "CPIC" },
                { symbol: "CYP2B6", role: "Bupropion", evidence: "CPIC" },
                { symbol: "CYP1A2", role: "Klozapina, olanzapina", evidence: "PGx" },
              ],
            },
            {
              label: "Receptory, transportery i odpowiedź kliniczna",
              genes: [
                { symbol: "COMT", role: "Dopamina w PFC; odpowiedź poznawcza", evidence: "PGx" },
                { symbol: "SLC6A4", role: "SSRI; 5-HTTLPR", evidence: "PGx" },
                { symbol: "HTR2A", role: "Nudności i odpowiedź na SSRI", evidence: "PGx" },
                { symbol: "BDNF", role: "Val66Met; opóźniona odpowiedź na SSRI", evidence: "PGx" },
                { symbol: "ABCB1", role: "P-gp; lekooporność (efflux)", evidence: "PGx" },
                { symbol: "ADRA2A", role: "Metylofenidat; gęstość α2A", evidence: "PGx" },
                { symbol: "DRD2", role: "Antypsychotyki; Taq1A", evidence: "PGx" },
                { symbol: "GSK3B", role: "Cel litu; stabilizacja nastroju", evidence: "PGx ChAD" },
              ],
            },
          ],
        },
      ],
    },
    {
      id: "lifestyle",
      label: "Metabolizm, dieta i zmysły",
      icon: "🍽️",
      topics: [
        {
          id: "substances",
          label: "Kofeina, alkohol i nikotyna",
          icon: "☕",
          summary:
            "Tolerancja kofeiny, metabolizm alkoholu (flush azjatycki) i predyspozycja do uzależnienia od nikotyny.",
          sections: [
            {
              label: "Detoks i tolerancja",
              genes: [
                { symbol: "CYP1A2", role: "Metabolizm kofeiny (>95%)", evidence: "Funkcjonalny" },
                { symbol: "ALDH2", role: "Aldehyd dehydrogenaza; flush azjatycki", evidence: "Patogenny / PGx" },
                { symbol: "CHRNA5", role: "Receptor nikotynowy α5; uzależnienie", evidence: "GWAS" },
                { symbol: "CHRNA4", role: "Receptor nikotynowy α4", evidence: "Sygnatura ADHD" },
                { symbol: "CHRNA7", role: "Receptor nikotynowy α7; uwaga", evidence: "Sygnatura ADHD" },
                { symbol: "ADRA2A", role: "Wrażliwość na kofeinę i stres", evidence: "Interakcja" },
                { symbol: "CNR1", role: "Receptor CB1; impulsywność", evidence: "Kandydat" },
              ],
            },
          ],
        },
        {
          id: "nutrition",
          label: "Intolerancje i odżywianie",
          icon: "🥛",
          summary:
            "Trawienie laktozy, smak goryczy i metabolizm kwasów tłuszczowych omega-3/omega-6.",
          sections: [
            {
              label: "Trawienie i smak",
              genes: [
                { symbol: "LCT", role: "Persystencja laktazy dorosłych", evidence: "Funkcjonalny" },
                { symbol: "TAS2R38", role: "Gorycz PROP; supersmak", evidence: "Funkcjonalny" },
              ],
            },
            {
              label: "Lipidy i masa ciała",
              genes: [
                { symbol: "FADS1", role: "Konwersja LA → EPA/DHA", evidence: "Funkcjonalny" },
                { symbol: "FADS2", role: "Desaturacja kwasów tłuszczowych", evidence: "Funkcjonalny" },
                { symbol: "FTO", role: "Apetyt i ryzyko otyłości", evidence: "GWAS" },
                { symbol: "MC4R", role: "Receptor melanokortyny 4; apetyt", evidence: "MDD somatogenny" },
              ],
            },
          ],
        },
        {
          id: "appearance",
          label: "Kolor oczu, skóry i włosów",
          icon: "👁️",
          summary:
            "Kaskada pigmentacji melaninowej w tęczówce, skórze i włosach.",
          sections: [
            {
              label: "Pigmentacja",
              genes: [
                { symbol: "HERC2", role: "Regulator OCA2; kolor oczu", evidence: "Funkcjonalny" },
                { symbol: "OCA2", role: "Transport melaniny w melanocytach", evidence: "Funkcjonalny" },
                { symbol: "SLC45A2", role: "MATP; jasna skóra", evidence: "Funkcjonalny" },
                { symbol: "SLC24A4", role: "Jasna karnacja i oczy", evidence: "Funkcjonalny" },
                { symbol: "MC1R", role: "Rude włosy; fototyping", evidence: "Funkcjonalny" },
                { symbol: "ABCC11", role: "Typ woskowiny i zapach potu", evidence: "Funkcjonalny" },
              ],
            },
          ],
        },
        {
          id: "smell-taste",
          label: "Węch i smak",
          icon: "👃",
          summary:
            "Receptory OR i TAS2R — percepcja zapachów i smaku goryczy.",
          sections: [
            {
              label: "Receptory",
              genes: [
                { symbol: "OR6A2", role: "Zapach „mydlanej” kolendry", evidence: "Funkcjonalny" },
                { symbol: "OR1A1", role: "Cytrusy i mięta", evidence: "Funkcjonalny" },
                { symbol: "OR2M", role: "Zapach szparagów w moczu", evidence: "Funkcjonalny" },
                { symbol: "TAS2R38", role: "Gorycz PROP (PAV/AVI)", evidence: "Funkcjonalny" },
              ],
            },
          ],
        },
        {
          id: "cognition-aging",
          label: "Poznanie, pamięć i starzenie",
          icon: "🧠",
          summary:
            "Pamięć epizodyczna, plastyczność mózgu i ryzyko otępienia.",
          sections: [
            {
              label: "Pamięć i plastyczność",
              genes: [
                { symbol: "BDNF", role: "Val66Met; plastyczność hipokampu", evidence: "Funkcjonalny" },
                { symbol: "WWC1", role: "KIBRA; pamięć epizodyczna", evidence: "GWAS" },
                { symbol: "COMT", role: "PFC; pamięć robocza", evidence: "Funkcjonalny" },
                { symbol: "NEGR1", role: "Adhezja neuronalna; MDD + IQ", evidence: "Plejotropia" },
                { symbol: "APOE", role: "ε2/ε3/ε4; Alzheimer, lipidy", evidence: "Patogenny / ryzyko" },
              ],
            },
          ],
        },
        {
          id: "sport",
          label: "Sport i wydolność",
          icon: "🏃",
          summary:
            "Typ włókien mięśniowych, metabolizm energetyczny i predyspozycja wytrzymałość vs. siła.",
          sections: [
            {
              label: "Wydolność",
              genes: [
                { symbol: "ACTN3", role: "Włókna szybko/kurczliwe (R577X)", evidence: "Funkcjonalny" },
                { symbol: "COMT", role: "Tolerancja bólu i stresu", evidence: "Funkcjonalny" },
                { symbol: "BDNF", role: "Plastyczność motoryczna", evidence: "Kandydat" },
                { symbol: "FTO", role: "Masa ciała i BMI", evidence: "GWAS" },
              ],
            },
          ],
        },
      ],
    },
  ];

  window.TOPIC_BY_ID = Object.fromEntries(
    window.TOPIC_GROUPS.flatMap((group) =>
      group.topics.map((topic) => [
        topic.id,
        { ...topic, groupId: group.id, groupLabel: group.label },
      ])
    )
  );

  window.TOPICS_FOR_GENE = (() => {
    const map = {};
    for (const [topicId, topic] of Object.entries(window.TOPIC_BY_ID)) {
      for (const section of topic.sections || []) {
        for (const { symbol } of section.genes || []) {
          if (!map[symbol]) map[symbol] = [];
          if (!map[symbol].includes(topicId)) map[symbol].push(topicId);
        }
      }
    }
    return map;
  })();
})();
