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
    "rs3027407 region maoa adhd u dzieci": {
      "a a": "positive",
      "a g": "neutral",
      "g g": "negative",
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

/** Keys to match genotype cells with „(lub …)” and multi-token labels. */
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

function fixedVariantTone(geneSymbol, heading, genotype, options = {}) {
  const byGene = FIXED_VARIANT_TONES[String(geneSymbol || "").toUpperCase()];
  if (!byGene) {
    return "neutral";
  }

  const headingKey = normalizeToneKey(heading);
  const byHeading = byGene[headingKey] || byGene[""];
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
  const segments = text
    .split(/<br\s*\/?>/gi)
    .map((part) => stripMarkdown(part.trim()))
    .filter(Boolean);
  return {
    text: segments.length ? segments.join("\n") : stripMarkdown(text),
    personal: isPersonalMarker(text),
  };
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
  return isPersonalMarker(cells[0]);
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
      personal: Boolean(row[0]?.personal),
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
  const isApoeHaplotype =
    isApoe && /haplotypy apoe|rs429358.*rs7412/i.test(context.heading || "");

  return rows
    .map((row) => {
      const cells = tableRowCells(row);
      const personal = tableRowIsPersonal(row);
      const genotype = cells[0] || "Wariant";
      const summary = cells[cells.length - 1] || "";
      const headingText = isApoeHaplotype ? cells[2] || genotype : genotype;
      const status = isApoeHaplotype
        ? `${headers[0] || "rs429358"}: ${cells[0] || "-"} | ${headers[1] || "rs7412"}: ${cells[1] || "-"}`
        : cells[1] || "";
      const details = headers
        .map((header, i) => ({ header, value: cells[i] || "" }))
        .slice(isApoeHaplotype ? 3 : 2, Math.max(isApoeHaplotype ? 3 : 2, headers.length - 1))
        .filter((item) => item.value);
      const tone = fixedVariantTone(
        context.gene,
        context.heading,
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
          ${summary ? `<p class="variant-impact">${formatMultilineEscaped(summary)}</p>` : ""}
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

function renderSectionCard(section, options = {}) {
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
  const heading =
    options.showSectionNumber && section.number
      ? `${section.number}. ${meta.label}`
      : meta.label;

  return `
    <section class="section-card${options.print ? " section-card--print" : ""}">
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

function renderPrintSectionCard(section) {
  return renderSectionCard(section, { print: true, showSectionNumber: true });
}

const PRINT_PAGE_COUNT = 4;

function renderPrintPageStack(pageSections) {
  return pageSections
    .map((section) => {
      const html = renderPrintSectionCard(section);
      return html ? `<div class="print-block">${html}</div>` : "";
    })
    .filter(Boolean)
    .join("");
}

function renderPrintPage(sections, facts) {
  const pages = [
    sections.slice(0, 3),
    sections.slice(3, 4),
    sections.slice(4, 6),
    sections.slice(6, 8),
  ];
  const subtitle = facts.find((item) => item.key.toLowerCase().includes("pełna nazwa"));

  const renderPage = (pageSections, pageNum) => `
    <section class="print-page" aria-label="Strona ${pageNum}" data-print-page="${pageNum}">
      <header class="print-page-header">
        <p class="print-page-meta">GenMarkerWiki · karta do druku · strona ${pageNum}/${PRINT_PAGE_COUNT}</p>
        <h2>${escapeHtml(getGene())}</h2>
        ${
          pageNum === 1 && subtitle
            ? `<p class="print-page-subtitle">${escapeHtml(subtitle.value)}</p>`
            : ""
        }
      </header>
      <div class="print-page-body">
        <div class="print-page-sections">${renderPrintPageStack(pageSections)}</div>
      </div>
    </section>
  `;

  return `
    <div class="print-document">
      ${pages.map((pageSections, index) => renderPage(pageSections, index + 1)).join("")}
    </div>
  `;
}

function fitPrintPagesToSheet() {
  if (document.body.dataset.mode !== "print") {
    return;
  }

  const sheetHeight = () => {
    const probe = document.createElement("div");
    probe.style.cssText = "position:absolute;visibility:hidden;height:277mm;width:1px;";
    document.body.appendChild(probe);
    const height = probe.offsetHeight;
    probe.remove();
    return height || 1040;
  };

  const maxHeight = sheetHeight();

  document.querySelectorAll(".print-page").forEach((page) => {
    const header = page.querySelector(".print-page-header");
    const sections = page.querySelector(".print-page-sections");
    if (!sections) {
      return;
    }

    sections.style.transform = "";
    sections.style.width = "";
    sections.style.height = "";

    const headerHeight = header ? header.offsetHeight : 0;
    const available = Math.max(120, maxHeight - headerHeight - 4);

    page.style.height = `${maxHeight}px`;
    page.style.maxHeight = `${maxHeight}px`;

    const body = page.querySelector(".print-page-body");
    if (body) {
      body.style.maxHeight = `${available}px`;
      body.style.height = `${available}px`;
    }

    const contentHeight = sections.scrollHeight;
    if (contentHeight > available) {
      const scale = available / contentHeight;
      sections.style.transform = `scale(${scale})`;
      sections.style.transformOrigin = "top left";
      sections.style.width = `${(100 / scale).toFixed(3)}%`;
    }
  });
}

function renderGenePrintPresentation(markdown) {
  const sections = mergeDuplicateVariantSections(parseSections(markdown));
  const profileSection = sections.find((section) => classifySection(section) === "profile");
  const facts = extractHeaderFacts(profileSection);

  if (titleNode) {
    titleNode.textContent = `${getGene()} — wersja do druku`;
  }
  if (subtitleNode) {
    subtitleNode.textContent =
      "Układ 4-stronicowy: 1) sekcje 1–3, 2) sekcja 4, 3) sekcje 5–6, 4) sekcje 7–8.";
  }

  return renderPrintPage(sections, facts);
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

function injectPrintLink() {
  const nav = document.querySelector(".nav");
  const geneSymbol = getGene();
  if (!nav || !geneSymbol) {
    return;
  }

  const printLink = document.createElement("a");
  printLink.className = "btn";
  printLink.href = `print.html?gene=${encodeURIComponent(geneSymbol)}`;
  printLink.textContent = "Wersja do druku";
  nav.appendChild(printLink);
}

async function loadGenePage() {
  const geneSymbol = getGene();
  if (!geneSymbol || !contentNode) {
    if (statusNode && document.body.dataset.mode !== "print") {
      statusNode.textContent =
        "Podaj symbol genu w adresie URL, np. gene.html?gene=COMT.";
    }
    return;
  }

  const isPrint = document.body.dataset.mode === "print";
  document.title = isPrint
    ? `${geneSymbol} — druk | GenMarkerWiki`
    : `${geneSymbol} | GenMarkerWiki`;

  try {
    const response = await fetch(`../md/${geneSymbol}.md`);
    if (!response.ok) {
      throw new Error(`Nie znaleziono karty genu ${geneSymbol}.`);
    }

    const markdown = await response.text();
    contentNode.innerHTML = isPrint
      ? renderGenePrintPresentation(markdown)
      : renderGenePresentation(markdown);
    if (isPrint) {
      requestAnimationFrame(() => {
        fitPrintPagesToSheet();
        requestAnimationFrame(fitPrintPagesToSheet);
      });
    }
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

if (document.body.dataset.mode === "print") {
  document.documentElement.classList.add("print-mode");
  window.fitPrintPagesToSheet = fitPrintPagesToSheet;
  window.addEventListener("beforeprint", fitPrintPagesToSheet);
  window.addEventListener("resize", fitPrintPagesToSheet);
}

loadGenePage();

if (document.body.dataset.mode !== "print") {
  injectPrintLink();
}
