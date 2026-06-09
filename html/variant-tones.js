/** Mapowanie genotypu na ton wariantu (positive / neutral / negative). */
(function () {
  function stripMarkdown(value) {
    return String(value || "")
      .replace(/\*\*([^*]+)\*\*/g, "$1")
      .replace(/\*([^*]+)\*/g, "$1")
      .replace(/`([^`]+)`/g, "$1")
      .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
      .replace(/\u2605\s*/g, "")
      .replace(/\s+/g, " ")
      .trim();
  }

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
    "rs1799978 a1 a2 taq1a d2r gestosc": {
      "t t": "negative",
      "t c": "neutral",
      "c c": "positive",
    },
    "rs1799978 taq1b gestosc d2r ankk1 drd2": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs2283265 intron modulacja drd2": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
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
      "t t": "negative",
      "t g": "neutral",
      "g g": "positive",
    },
    "i425v mutacja missense rzadka": {
      "wt wt": "positive",
      "i425v wt": "neutral",
      "i425v i425v": "negative",
      "i425v heterozygota homozygota": "negative",
    },
    "rs4795541 5 httlpr proxy vntr promotorowy s l xl": {
      "l l": "positive",
      "l l dlugi l a l a po rs25531": "positive",
      "l s": "neutral",
      "s s": "negative",
      "s s krotki": "negative",
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
    "rs1726866 c 785t c ile262val": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs10246939 c 886a g ala296val": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
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
  CNTNAP2: {
    "rs7794745 asd opoznienie mowy": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs2710102 haplotyp z rs7794745": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs17290659 intron marker asocjacyjny locus": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "mutacje patogenne cdfe epilepsja": {
      "dziki allel": "positive",
      "heterozygot de novo": "negative",
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
    "rs9939609": {
      "t t": "positive",
      "a t": "neutral",
      "a a": "negative",
    },
    "rs1421085 intron fto sprzezenie mozliwy wariant sprawczy vs rs9939609": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs17817449 intron fto ld z rs9939609": {
      "t t": "positive",
      "t a": "neutral",
      "a a": "negative",
    },
    "rs9930506 intron fto ld": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs8050136 intron fto ld": {
      "t t": "positive",
      "c t": "neutral",
      "c c": "negative",
    },
  },
  LCT: {
    "": {
      "t t a a komplementarnie": "positive",
      "c t g a komplementarnie": "neutral",
      "c c g g komplementarnie": "negative",
    },
    "rs182549 regulacyjny utrzymanie laktazy": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs182549 c 220 1g a w mcm6 tag persystencji laktazy": {
      "c c": "negative",
      "c t": "neutral",
      "t t": "positive",
    },
  },
  CHRNA5: {
    "": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs1051730": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs588765 eqtl chrna5 ekspresja mrna 5 w korze": {
      "t t": "positive",
      "t t major": "positive",
      "t c": "neutral",
      "c c": "neutral",
      "c c minor hom": "neutral",
    },
    "rs680244 eqtl chrna5 regulacja transkrypcji": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "neutral",
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
    "rs10885122 regulacyjny ld z rs553668 hiperglikemia stresowa": {
      "t t": "positive",
      "t c": "neutral",
      "t g": "neutral",
      "t c lub t g": "neutral",
      "c c": "negative",
      "g g": "negative",
      "c c lub g g": "negative",
    },
    "rs3750625 3 utr c 449c a g t bol miesniowo szkieletowy mir 34a": {
      "c c": "positive",
      "c a": "neutral",
      "c a lub c g c t": "neutral",
      "a a": "negative",
      "a a lub homozygoty alt": "negative",
    },
    "rs521674 upstream 2 kb upstream odraczanie gratyfikacji": {
      "t t": "positive",
      "t a": "neutral",
      "a a": "negative",
    },
  },
  ADNP: {
    "rs886041116 c 2188c t p arg730ter": {
      "g g": "positive",
      "g t": "negative",
      "t t": "negative",
    },
    "mutacje patogenne c 2491 2494delttaa hotspot": {
      "ttaa ttaa": "positive",
      "ttaa del": "negative",
    },
    "rs12480328 intron ryzyko raka prostaty": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
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
    "rs10761482 intron upstream ank3 plejotropia bd schizofrenia": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
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
    "rs1024582 intron modulacja ekspresji cav1 2": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs2007044 intron ryzyko bd i schizofrenii": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs216009 intron asocjacja psychiatryczna": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs2281845 regulacyjny cav1 2 w mozgu": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs4765905 intron kognicja i nastroj": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs723672 intron modulacja cav1 2": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
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
    "rs12919501 haplotyp rs11649622 impulsywnosc": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs4075942 haplotyp rs11649622": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs7190768 haplotyp rs11649622": {
      "c c": "positive",
      "c t": "neutral",
      "c t lub c a": "neutral",
      "t t": "negative",
      "t t lub a a": "negative",
    },
    "rs8059696 blok rs2199430 kognicja": {
      "t t": "positive",
      "t a": "neutral",
      "t a lub t c t g": "neutral",
      "a a": "negative",
      "a a lub c c g g": "negative",
    },
    "rs4783277 blok rs2199430": {
      "t t": "positive",
      "t c": "neutral",
      "t c lub t g": "neutral",
      "c c": "negative",
      "c c lub g g": "negative",
    },
    "rs12596958 blok rs2199430": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs12051272 enhancer w ld z rs4783244 3 kb od tss": {
      "g g": "negative",
      "g a": "neutral",
      "g a lub g c g t": "neutral",
      "a a": "positive",
      "a a lub homozygoty alt": "positive",
    },
    "rs3865188 ld rs4783244 adiponektyna": {
      "a a": "positive",
      "a g": "neutral",
      "a g lub a t": "neutral",
      "t t": "negative",
      "t t lub g g": "negative",
    },
    "rs8060301 meqtl promotorowy": {
      "t t": "positive",
      "t a": "neutral",
      "a a": "negative",
    },
    "rs12444338 meqtl 2 kb upstream": {
      "g g": "positive",
      "g t": "neutral",
      "g t lub g a g c": "neutral",
      "t t": "negative",
      "t t lub homozygoty alt": "negative",
    },
    "rs62040565 meqtl promotorowy maf 1 5": {
      "t t": "positive",
      "t a": "neutral",
      "t a lub t c": "neutral",
      "a a": "negative",
      "a a lub c c": "negative",
    },
    "rs113460564 rzadki meqtl maf 0 5": {
      "a a": "positive",
      "a c": "neutral",
      "c c": "negative",
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
    "rs3800373 intron 7 3 region bezsennosc stres zawodowy": {
      "c c": "positive",
      "c a": "neutral",
      "a a": "negative",
    },
    "rs7748266 intron fkbp5 haplotyp stresu": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs9394309 intron fkbp5 haplotyp regulacyjny": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
  },
  FMR1: {
    "mutacje patogenne ekspansja cgg 5 utr": {
      "normalny 5 44 cgg": "positive",
      "premutacja 55 200 cgg": "neutral",
      "pelna mutacja 200 cgg": "negative",
    },
    "rs2043856428 c 79g a p ser27ter rzadki": {
      "g g": "positive",
      "g a": "negative",
    },
    "mutacje patogenne p trp395ter": {
      "dziki allel": "positive",
      "mutacja de novo": "negative",
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
      "t t": "negative",
      "t c": "neutral",
      "c c": "positive",
    },
    "rs2519152": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
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
    "rs2873804 intron dbh atomoksetyna adhd": {
      "t t": "neutral",
      "t c": "neutral",
      "c c": "positive",
    },
    "rs1076150 intron dbh adhd sprzezenie": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs1548364 intron dbh a g atomoksetyna": {
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
    "rs1800466 vntr promotor aktywnosc enzymu": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs1800466 promotor tag aktywnosci mao a": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs2064070 promotor aktywnosc mao a": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs2064070 promotor modulacja transkrypcji mao a": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs3027407 region maoa adhd u dzieci": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
  },
  MECP2: {
    "rs2734647 regulacja ekspresji mecp2": {
      "t t": "positive",
      "c t": "neutral",
      "c c": "negative",
    },
    "rs2239464 intron modyfikator": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "mutacje patogenne np p thr158met": {
      "dziki allel": "positive",
      "heterozygot de novo": "negative",
      "hemizygot": "negative",
    },
    "rs2075596 intron autoimmunologia c 413 266t c": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
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
    "rs1805005 val60leu v60l slaby allel r": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs885479 arg163gln r163q allel r": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
  },
  ABCC11: {
    "rs17822931 gly180arg": {
      "a a": "positive",
      "g a": "neutral",
      "g g": "negative",
    },
    "rs17822471 c 1637c t gly546val mrp8 toksycznosc 5 fu": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  ALDH2: {
    "": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs1229984 adh1b arg48his szybki metabolizm etanolu aldehyd": {
      "t t": "positive",
      "t a": "neutral",
      "a a": "negative",
    },
    "rs747096195 aldh2 p arg101gly rzadki": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs190764869 aldh2 p arg114trp rzadki": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  AR: {
    "rs6152 uwaga gen na chromosomie x mezczyzni maja jeden allel": {
      "g": "negative",
      "g a": "neutral",
      "a": "positive",
      "a mezczyzni hemizygoti a kobiety a a": "positive",
      "g a wylacznie kobiety": "neutral",
      "g mezczyzni hemizygoti g kobiety g g": "negative",
    },
    "rs1385699 eda2r p glu57leu lysienie androgenowe silniejszy sygnal niz rs6152 u czesci kohort": {
      "c c": "positive",
      "c a": "neutral",
      "c a lub c t": "neutral",
      "a a": "negative",
      "a a lub t t": "negative",
    },
    "rs1204038 ar intron 8 psa rak prostaty autoimmunologia": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
  },
  GC: {
    "rs2282679 ekspresja vdbp i 25 oh d": {
      "a a": "positive",
      "a c": "neutral",
      "c c": "negative",
      "a a lub t t": "positive",
      "a c lub t g": "neutral",
      "c c lub g g": "negative",
    },
    "rs7041 rs4588 izofomy bialkowe gc1f gc1s gc2": {
      "gc1f 1f": "positive",
      "gc1s 1s": "positive",
      "gc1s 2": "neutral",
      "gc2 2": "negative",
    },
  },
  HERC2: {
    "rs12913832 regulacja oca2 kolor teczowki": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs1129038 3 utr ld z rs12913832 beh2": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs916977 intron herc2 beh3 pigmentacja": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs1667394 intron herc2 pigmentacja skory wlosow": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
  },
  OCA2: {
    "rs1800407 arg419gln bialko p": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
      "c c g g": "positive",
      "c t g a": "neutral",
      "t t a a": "negative",
    },
    "rs1800414 his615arg pigmentacja skory azja wschodnia": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
      "a a t t": "positive",
      "a g t c": "neutral",
      "g g c c": "negative",
    },
    "rs12913832 regulator w herc2 ekspresja oca2 w teczowce": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs1800401 oca2 his615arg r419q pigmentacja oczu skory": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
  },
  OR2M: {
    "rs4481887 anosmia szparagowa percepcja moczu": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs13373863 or2m region szparagi ld z rs4481887": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs71538191 or2m powiazany haplotyp": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs6689553 or2m ld": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs72765116 or2m ld": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs57711976 or2m ld": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
  },
  OR6A2: {
    "rs72921001 percepcja kolendry": {
      "a a": "positive",
      "c a": "neutral",
      "c c": "negative",
    },
    "rs7107418 proxy rs72921001 or10a2 ld": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs3930075 or10a2 his43arg ld rs72921001": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs10839631 or10a2 his207arg ld": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs7926083 or10a2 lys258thr ld": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
  },
  SLC24A4: {
    "rs12896399 pigmentacja wlosow i skory": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
    "rs11160059 cisnienie populacja afrykanska": {
      "g g": "positive",
      "a g": "neutral",
      "a a": "negative",
      "a g a a": "negative",
    },
    "rs12590654 regulacyjny load pozna postac alzheimer": {
      "g g": "neutral",
      "g a": "neutral",
      "a a": "positive",
    },
    "rs10498633 intron slc24a4 regulacja ekspresji": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
  },
  SLC45A2: {
    "rs16891982 l374f pigmentacja i ryzyko cmm": {
      "c c": "positive",
      "c g": "neutral",
      "g g": "negative",
    },
    "rs26722 e272k wariant wschodnioazjatycki": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "neutral",
    },
    "rs2287949 synonimiczny c 987a g t329t haplotypy migracji": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "neutral",
    },
    "rs121912621 p asp157asn oca4 patogenny": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs375077956 p tyr266ter oca4 nonsense": {
      "c c": "positive",
      "c a": "neutral",
      "a a": "negative",
    },
  },
  SCN2A: {
    "rs10174400 kognicja schizofrenia": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "neutral",
    },
    "rs2121371 farmakogenetyka aed": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "mutacje patogenne przyklady": {
      "gof np p ala263val": "negative",
      "lof np nonsense": "negative",
    },
    "rs1864885 farmakogenetyka aed pediatria": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs17183814 parkinson choroba afektywna dwubiegunowa": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs2304016 ivs7 32a g parkinson": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
  },
  SHANK3: {
    "rs9616915 ile342thr ekson 6": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "neutral",
    },
    "rs76224556 intron 10 epigenetyka cpg": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "mutacje patogenne delecja 22q13 3 pms": {
      "heterozygotyczna utrata genu": "negative",
      "duplikacja locus": "negative",
    },
    "rs13057681 missense marker asocjacyjny": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs2106112 synonimiczny marker asocjacyjny": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs6010065 intron marker asocjacyjny": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
  },
  ZEB2: {
    "rs2252641 cad enhancer zeb2 vsmc": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs17678683 cad eqtl tkanka tluszczowa szkieletowa": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
    "rs6740731 regulacyjny zeb2 naczynia mowat wilson kontekst": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs35500812 zeb2 powiazany marker": {
      "cc cc": "positive",
      "cc c": "neutral",
      "c c": "negative",
    },
    "rs137852981 zeb2 rzadki regulacyjny": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs786204815 zeb2 rzadki": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs587776604 zeb2 clinvar rzadki": {
      "g g": "positive",
      "g gt": "neutral",
      "gt gt": "negative",
    },
  },
  AVPR1A: {
    "rs1042615 3 utr stabilnosc mrna": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "neutral",
    },
    "rs11174811 regulacja pod stresem": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs10877969 proxy percepcji bolu asd": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs3 allel 334 mikrosatelita wiez partnerska": {
      "0 kopii": "positive",
      "1 kopia": "neutral",
      "2 kopie": "negative",
    },
    "rs7294536 rs3 dlugosc powtorzen proxy snp": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs7294536 rs3 proxy dlugosci powtorzen": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
  },
  CHRM2: {
    "rs324650 sine alu kognicja": {
      "a a": "positive",
      "a t": "neutral",
      "t t": "negative",
    },
    "rs1824024 intron alkohol pochp": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
    "rs8191992 3 utr autonomiczna odpowiedz serca": {
      "a a": "negative",
      "a t": "neutral",
      "t t": "positive",
    },
    "rs2061174 intron haplotyp t t t": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs324640 intron kognicja i alkohol": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
  },
  CYP2C19: {
    "rs4244285 c 681g a allel 2 lof": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs12248560 c 806c t allel 17 gof": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs4986893 c 636g a allel 3 lof": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs12769205 intron metabolizm klopidogrelu": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs6413438 regulacyjny ekspresja cyp2c19": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs6413438 regulacyjny allel 10 cyp2c19": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs72558186 allelic variant metabolizm ppi": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs72558186 allelic variant allel 7 metabolizm ppi": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  CYP2D6: {
    "rs3892097 g 6866g a allel 4 pm": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs1065852 100c t p p34s allel 10 obnizona funkcja": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs28371706 1023c t allel 17 obnizona funkcja": {
      "c c": "positive",
      "c a": "neutral",
      "a a": "negative",
    },
    "rs1058164 allelic variant metabolizm substratow": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs28371725 allelic variant obnizona funkcja": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs28371725 allelic variant allel 41 obnizona funkcja": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs35742686 allelic variant obnizona funkcja pm": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs35742686 allelic variant allel 3 brak aktywnosci": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs5030655 allelic variant metabolizm lekow": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs5030655 allelic variant allel 6 brak aktywnosci": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs5030865 allelic variant brak aktywnosci": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs5030865 allelic variant allel 8 14 brak aktywnosci": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs72549354 allelic variant metabolizm lekow": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs72549354 allelic variant allel 20": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs79802111 allelic variant rzadki lof": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs1135840 allelic variant pm im": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1135840 allelic variant pm im tag haplotypu": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  KCNQ4: {
    "rs4660470 nihl utrata sluchu indukowana halasem": {
      "t t": "positive",
      "t a": "negative",
      "a a": "negative",
    },
    "rs4660468 nihl haplotyp": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs28937588 p gly285ser dfna2a patogenny": {
      "g g": "positive",
      "g a": "negative",
      "a a": "negative",
    },
    "rs80358277 dfna2a patogenny proxy": {
      "g g": "positive",
      "g c": "negative",
      "g a": "negative",
      "c c": "negative",
      "a a": "negative",
    },
    "rs80358277 c 827g c p trp276ser dfna2a": {
      "g g": "positive",
      "g c": "negative",
      "g a": "negative",
      "c c": "negative",
      "a a": "negative",
    },
  },
  SNAP25: {
    "rs3746544 3 utr ekspresja w pfc": {
      "t t": "positive",
      "t g": "neutral",
      "g g": "negative",
    },
    "rs363050 promotor piq": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "neutral",
    },
    "rs363043 intron grubosc kory": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1051312 intron kognicja": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1051312 intron kognicja tag haplotypu snap25": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs362584 intron ekspresja w pfc": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs362990 intron modulacja fenotypu": {
      "t t": "positive",
      "t g": "neutral",
      "g g": "negative",
    },
    "rs362990 intron modulacja fenotypu poznawczego": {
      "t t": "positive",
      "t g": "neutral",
      "g g": "negative",
    },
    "rs363039 intron modulacja fenotypu": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs363039 intron modulacja fenotypu snap25": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  SYNGAP1: {
    "rs2151161955 c 703t c p ser235pro": {
      "t t": "positive",
      "t c": "negative",
      "c c": "negative",
    },
    "rs1064795331 c 1717c t p arg573trp": {
      "c c": "positive",
      "c t": "negative",
      "t t": "negative",
    },
    "mutacje patogenne c 3583 6g a splicing": {
      "g g": "positive",
      "g a": "negative",
      "a a": "negative",
    },
  },
  TSC1: {
    "rs7874234 ryzyko tsc": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1073123 intron modyfikator fenotypu": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs121912582 c 1844c t p ser615leu patogenny": {
      "c c": "positive",
      "c t": "negative",
      "t t": "negative",
    },
    "rs13295634 intron 5 przezywalnosc crc": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
    "rs627566 c 232g t p glu78ter patogenny nonsense": {
      "g g": "positive",
      "g t": "negative",
      "t t": "negative",
    },
  },
  TSC2: {
    "rs28934872 c 1832g a p arg611gln patogenny": {
      "g g": "positive",
      "g a": "negative",
      "a a": "negative",
    },
    "rs30259 intron modyfikator": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1748 synonimiczny ekspresja alleliczna tsc2": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs2074969 rs2073636 haplotyp regulacyjny": {
      "referencyjny haplotyp": "positive",
      "heterozygot": "neutral",
      "alternatywny haplotyp": "negative",
    },
  },
  VKORC1: {
    "rs9923231 promotor wrazliwosc na warfaryne": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs61742245 opornosc na warfaryne": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
    "rs2359612 intron haplotyp warfaryny": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs7294 regulacyjny wrazliwosc na antagonistow k": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs8050894 regulacyjny vkorc1": {
      "g g": "positive",
      "g c": "neutral",
      "c c": "negative",
    },
    "rs8050894 regulacyjny haplotyp vkorc1": {
      "g g": "positive",
      "g c": "neutral",
      "c c": "negative",
    },
    "rs9934438 intron dawka warfaryny": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs9934438 intron dawka warfaryny tag haplotypu": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
  },
  WWC1: {
    "rs17070145 kibra pamiec epizodyczna": {
      "c c": "negative",
      "c t": "positive",
      "t t": "positive",
    },
    "rs139606423 regulacyjny kibra": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs139606423 regulacyjny haplotyp kibra": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs3822659 intron kibra pamiec epizodyczna": {
      "t t": "positive",
      "t c": "neutral",
      "c c": "negative",
    },
    "rs3822660 intron kibra pamiec": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
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
    "rs4420638 apoc1 proxy 14 kb od apoe sprzezenie z e4": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs4420638 apoc1 proxy 14 kb od apoe sprzezenie z 4": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
  },
  FADS1: {
    "rs174537 l374f aktywnosc d5d": {
      "g g": "negative",
      "g t": "neutral",
      "t t": "positive",
    },
    "rs174547 indeks desaturacji": {
      "t t": "negative",
      "t c": "neutral",
      "c c": "positive",
    },
    "rs174546 intron indeks desaturacji": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs174548 intron metabolizm kwasow omega": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs174556 intron d5d aktywnosc": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  FADS2: {
    "rs174575 aktywnosc d6d": {
      "c c": "positive",
      "c g": "neutral",
      "g g": "negative",
    },
    "rs1535 karmienie piersia iq": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs968567 promotor 5 utr": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs174583 intron elongacja pufa": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs174583 intron elongacja pufa ld z fads1": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  IL2RA: {
    "rs2104286 ekspresja cd25": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs11594656 promotor 5 t1d": {
      "t t": "negative",
      "t a": "neutral",
      "a a": "positive",
    },
    "rs12722489 c t ld z ms": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  MTR: {
    "rs1805087 a2756g asp919gly": {
      "a a": "neutral",
      "a g": "positive",
      "g g": "positive",
    },
  },
  MTRR: {
    "rs1801394 a66g ile22met": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
    },
    "rs1532268 intron c t": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
  },
  OR1A1: {
    "rs2073153 funkcja or1a1": {
      "g g": "positive",
      "g t": "neutral",
      "t t": "negative",
    },
  },
  VDR: {
    "rs2228570 foki aktywnosc transkrypcyjna": {
      "c c": "positive",
      "c t": "neutral",
      "t t": "negative",
    },
    "rs1544410 bsmi ekspresja mrna": {
      "g g": "positive",
      "g a": "neutral",
      "a a": "negative",
    },
    "rs7975232 apai stabilnosc mrna": {
      "c c": "positive",
      "c a": "neutral",
      "a a": "negative",
    },
    "rs731236 taqi stabilnosc transkryptu": {
      "t t": "negative",
      "t c": "neutral",
      "c c": "positive",
    },
    "rs1544410 bsmi rs7975232 apai rs731236 taqi haplotyp": {
      "haplotyp 1 bat bat": "positive",
      "haplotyp 2 bat bat": "negative",
      "haplotyp 3 bat bat": "positive",
    },
  },


};

function normalizeToneKey(value) {
  return stripMarkdown(String(value || ""))
    .toLowerCase()
    .replace(/\u0142/g, "l")
    .replace(/[\u0105\u0107\u0119\u0144\u00f3\u015b\u017a\u017c]/g, (ch) =>
      ({
        "\u0105": "a",
        "\u0107": "c",
        "\u0119": "e",
        "\u0144": "n",
        "\u00f3": "o",
        "\u015b": "s",
        "\u017a": "z",
        "\u017c": "z",
      })[ch] || ch
    )
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

/** Keys to match genotype cells with ?(lub ?)? and multi-token labels. */
function genotypeLookupKeys(genotype) {
  const raw = stripMarkdown(String(genotype || ""));
  const keys = new Set();
  const add = (token) => {
    const key = normalizeToneKey(token);
    if (key) {
      keys.add(key);
    }
  };

  add(raw);
  add(raw.split("(")[0]);

  const tokenRe =
    /(?:^|[\s,;]|lub\s+)([ACGT]{1,2}\/[ACGT]{1,2}|[ACGT]{2}|wt\/wt|i425v\/wt|i425v\/i425v|l\/l|l\/s|s\/s|gc[\d/]+|ref\/\w+|alt\/\w+|minor hom|major)/gi;
  for (const inner of raw.matchAll(/\(([^)]+)\)/g)) {
    for (const m of inner[1].matchAll(tokenRe)) {
      add(m[1]);
    }
  }
  for (const m of raw.matchAll(tokenRe)) {
    add(m[1]);
  }

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
  if (!byGene) {
    return "neutral";
  }

  let byHeading = null;
  for (const headingKey of headingLookupKeys(heading)) {
    if (byGene[headingKey]) {
      byHeading = byGene[headingKey];
      break;
    }
  }
  byHeading = byHeading || byGene[""];
  if (!byHeading) {
    return "neutral";
  }

  const keys = options.lookupKey
    ? [options.lookupKey]
    : genotypeLookupKeys(genotype);

  for (const key of keys) {
    if (byHeading[key]) {
      return byHeading[key];
    }
  }

  return "neutral";
}

  window.FIXED_VARIANT_TONES = FIXED_VARIANT_TONES;
  window.fixedVariantTone = fixedVariantTone;
  window.normalizeToneKey = normalizeToneKey;
})();
