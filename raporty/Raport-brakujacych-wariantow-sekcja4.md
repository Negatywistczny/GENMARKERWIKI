# Raport: brakujące tabele wariantów w sekcji 4

Data: 2026-05-25

## Metodologia

- **Źródło indeksu rsID:** `html/gene-rsids.js` (wyświetlane w `index.html` w sekcji „Analizowane rsID”).
- **Kryterium obecności w sekcji 4:** rsID występuje w `md/<GEN>.md` między nagłówkami `### 4.` a `### 5.` jako własny blok tabeli genotypów (`**rs…**`, `Genotyp (rs…)`, kolumna `★ rs…`, haplotyp łączony typu rs429358+rs7412 lub rs7041+rs4588).
- **Dane zewnętrzne:** NCBI dbSNP (eSummary), uzupełnienie z `scripts/snp-external-data.json` oraz kontekst z sekcji 2/6 plików markdown.

## Podsumowanie

| Metryka | Wartość |
| --- | --- |
| Genów w indeksie | 35 |
| Genów z brakami w sekcji 4 | 21 |
| rsID w indeksie (łącznie) | 134 |
| rsID bez tabeli w sekcji 4 | 62 |
| Genów kompletnych | 14 |

### Geny kompletne (wszystkie rsID z indeksu mają tabelę w sekcji 4)

`ACTN3`, `ANKK1`, `BDNF`, `CACNA1C`, `CLOCK`, `COMT`, `CYP1A2`, `DRD2`, `GC`, `LCT`, `MTHFR`, `OXTR`, `TAS2R38`, `TPH2`

---

## ABCC11 — Gen woskowiny usznej

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs17822471**

**W sekcji 4 obecne:** `rs17822931`
**W indeksie łącznie:** `rs17822931`, `rs17822471`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs17822471

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 16, 48208468 |
| Funkcja (dbSNP) | non_coding_transcript_variant, missense_variant, coding_sequence_variant, genic_upstream_transcript_variant |
| ClinVar (dbSNP) | benign |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/17822471) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs17822471) | — |

**Kontekst w pliku `md/ABCC11.md` (poza sekcją 4):** **Powiązane markery:** rs17822471 (modulacja ekspresji MRP8 w wątrobie i toksyczność 5-fluorouracylu) **Onkologia i chemioterapia:** Wysoka ekspresja ABCC11 w nowotworach piersi (HER2+, potrójnie ujemne) wiąże się z gorszym rokowaniem. Genotyp A/A może zwiększać skuteczność antymetabolitów (pemetreksed, metotreksat, 5-FU) przez słabszy efflux. Osobno: rs17822471 CT/TT — podwyższone ryzyko ciężkiej leukopenii przy 5-FU; przed chemioterapią fluoropirymidynową warto omówić test genetyczny z onkologiem. **PMID: 24024896** – Polimorfizmy ABCC11/MRP8 a ciężka toksyczność 5-fluorouracylu (rs17822471).

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.48208468G>A,NC_000016.10:g.48208468G>C,NC_000016.9:g.48242379G>A,NC_000016.9:g.48242379G>C,NG_011522.2:g.44071C>T,NG_011522.2:g.44071C>G,NG_011522.1:g.31710C>T,NG_011522.1:g.31710C>G,NM_032583.4:c.1637C>T,NM_032583.4:c.1637C>G,NM_032583.3:c.1637C>T,NM_032583.3…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## ADRA2A — Gen uwagi, skupienia i pamięci roboczej

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs10885122**
- **rs3750625**
- **rs521674**

**W sekcji 4 obecne:** `rs1800544`, `rs553668`
**W indeksie łącznie:** `rs1800544`, `rs553668`, `rs10885122`, `rs3750625`, `rs521674`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs10885122

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 10, 111282335 |
| Funkcja (dbSNP) | — |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/C/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/10885122) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs10885122) | — |

**Kontekst w pliku `md/ADRA2A.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs10885122 (hiperglikemia stresowa), rs3750625 (ból mięśniowo-szkieletowy), rs521674 (odraczanie gratyfikacji)

**Skrót HGVS (NCBI):** HGVS=NC_000010.11:g.111282335T>C,NC_000010.11:g.111282335T>G,NC_000010.10:g.113042093T>C,NC_000010.10:g.113042093T>G · SEQ=[T/C/G] · LEN=1

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs3750625

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | ADRA |
| Lokalizacja | chr 10, 111079843 |
| Funkcja (dbSNP) | 3_prime_UTR_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: C/A/G/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/3750625) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs3750625) | — |

**Kontekst w pliku `md/ADRA2A.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs10885122 (hiperglikemia stresowa), rs3750625 (ból mięśniowo-szkieletowy), rs521674 (odraczanie gratyfikacji)

**Skrót HGVS (NCBI):** HGVS=NC_000010.11:g.111079843C>A,NC_000010.11:g.111079843C>G,NC_000010.11:g.111079843C>T,NC_000010.10:g.112839601C>A,NC_000010.10:g.112839601C>G,NC_000010.10:g.112839601C>T,NG_012020.1:g.7812C>A,NG_012020.1:g.7812C>G,NG_012020.1:g.7812C>T,NM_000681.4:c.*449C>A,NM_000681.4:c.*449C…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs521674

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | ADRA |
| Lokalizacja | chr 10, 111075832 |
| Funkcja (dbSNP) | upstream_transcript_variant, 2KB_upstream_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/521674) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs521674) | — |

**Kontekst w pliku `md/ADRA2A.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs10885122 (hiperglikemia stresowa), rs3750625 (ból mięśniowo-szkieletowy), rs521674 (odraczanie gratyfikacji)

**Skrót HGVS (NCBI):** HGVS=NC_000010.11:g.111075832T>A,NC_000010.10:g.112835590T>A,NG_012020.1:g.3801T>A · SEQ=[T/A] · LEN=1 · GENE=ADRA2A:150

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## ALDH2 — Gen azjatyckiego rumieńca

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs1229984**
- **rs747096195**
- **rs190764869**

**W sekcji 4 obecne:** `rs671`
**W indeksie łącznie:** `rs671`, `rs1229984`, `rs747096195`, `rs190764869`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs1229984

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 4, 99318162 |
| Funkcja (dbSNP) | missense_variant, coding_sequence_variant |
| ClinVar (dbSNP) | protective |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1229984) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1229984) | — |

**Kontekst w pliku `md/ALDH2.md` (poza sekcją 4):** **Powiązane markery:** ADH1B rs1229984 (szybki metabolizm etanolu do aldehydu — synergia z rs671); rzadkie warianty rs747096195, rs190764869

**Skrót HGVS (NCBI):** HGVS=NC_000004.12:g.99318162T>A,NC_000004.12:g.99318162T>C,NC_000004.12:g.99318162T>G,NC_000004.11:g.100239319T>A,NC_000004.11:g.100239319T>C,NC_000004.11:g.100239319T>G,NG_011435.1:g.8254A>T,NG_011435.1:g.8254A>G,NG_011435.1:g.8254A>C,NM_000668.6:c.143A>T,NM_000668.6:c.143A>G,NM…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs747096195

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | ALDH |
| Lokalizacja | chr 12, 111783239 |
| Funkcja (dbSNP) | missense_variant, intron_variant, coding_sequence_variant |
| ClinVar (dbSNP) | — |
| Zmiana białkowa (HGVS) | p.Arg101Gly |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/747096195) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs747096195) | — |

**Kontekst w pliku `md/ALDH2.md` (poza sekcją 4):** **Powiązane markery:** ADH1B rs1229984 (szybki metabolizm etanolu do aldehydu — synergia z rs671); rzadkie warianty rs747096195, rs190764869

**Skrót HGVS (NCBI):** HGVS=NC_000012.12:g.111783239A>G,NC_000012.11:g.112221043A>G,NG_012250.2:g.21353A>G,NM_000690.4:c.301A>G,NM_000690.3:c.301A>G,NP_000681.2:p.Arg101Gly · SEQ=[A/G] · LEN=1 · GENE=ALDH2:217

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs190764869

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | ALDH |
| Lokalizacja | chr 12, 111783278 |
| Funkcja (dbSNP) | intron_variant, missense_variant, coding_sequence_variant |
| ClinVar (dbSNP) | — |
| Zmiana białkowa (HGVS) | p.Arg114Trp |
| MAF / allely | allely ref/alt: C/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/190764869) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs190764869) | — |

**Kontekst w pliku `md/ALDH2.md` (poza sekcją 4):** **Powiązane markery:** ADH1B rs1229984 (szybki metabolizm etanolu do aldehydu — synergia z rs671); rzadkie warianty rs747096195, rs190764869

**Skrót HGVS (NCBI):** HGVS=NC_000012.12:g.111783278C>T,NC_000012.11:g.112221082C>T,NG_012250.2:g.21392C>T,NM_000690.4:c.340C>T,NM_000690.3:c.340C>T,NP_000681.2:p.Arg114Trp · SEQ=[C/T] · LEN=1 · GENE=ALDH2:217

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## ANK3 — Marker zaburzeń afektywnych

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs10761482**

**W sekcji 4 obecne:** `rs10994336`, `rs1938526`, `rs9804190`
**W indeksie łącznie:** `rs10994336`, `rs1938526`, `rs9804190`, `rs10761482`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs10761482

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | ANK |
| Lokalizacja | chr 10, 60325579 |
| Funkcja (dbSNP) | intron_variant, genic_upstream_transcript_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/10761482) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs10761482) | — |

**Kontekst w pliku `md/ANK3.md` (poza sekcją 4):** **Zapis zmiany nukleotydowej (HGVS):** rs10994336: intronowy C>T (allel ryzyka T); rs1938526, rs9804190, rs10761482 – warianty niekodujące w ANK3 **Powiązane markery / haplotyp:** rs1938526 (ekspresja transkryptu mózgowego, kognicja); rs9804190 (intron 36, DTI pęczek haczykowaty, BD vs schizofrenia); rs10761482 (asocjacja ze schizofrenią, plejotropia BD–SCZ)

**Skrót HGVS (NCBI):** HGVS=NC_000010.11:g.60325579T>C,NC_000010.10:g.62085337T>C,NG_029917.1:g.412948A>G · SEQ=[T/C] · LEN=1 · GENE=ANK3:288

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## APOE — Gen Alzheimera

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs4420638**

**W sekcji 4 obecne:** `rs429358`, `rs7412`
**W indeksie łącznie:** `rs429358`, `rs7412`, `rs4420638`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs4420638

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | APOC |
| Lokalizacja | chr 19, 44919689 |
| Funkcja (dbSNP) | downstream_transcript_variant, 500B_downstream_variant |
| ClinVar (dbSNP) | not-provided |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/4420638) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs4420638) | — |

**Kontekst w pliku `md/APOE.md` (poza sekcją 4):** **Powiązane markery / proxy:** rs4420638 (APOC1) jako marker zastępczy sprzężony z haplotypem APOE

**Skrót HGVS (NCBI):** HGVS=NC_000019.10:g.44919689A>G,NC_000019.9:g.45422946A>G,NG_012859.1:g.10026A>G · SEQ=[A/G] · LEN=1 · GENE=APOC1:341

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## AR — Gen męskości

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs1385699**
- **rs1204038**

**W sekcji 4 obecne:** `rs6152`
**W indeksie łącznie:** `rs6152`, `rs1385699`, `rs1204038`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs1385699

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr X, X |
| Funkcja (dbSNP) | non_coding_transcript_variant, missense_variant, intron_variant, coding_sequence_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1385699) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1385699) | — |

**Kontekst w pliku `md/AR.md` (poza sekcją 4):** **Powiązane markery:** CAGn (VNTR w eksonie 1 — długość CAG moduluje czułość receptora; ekspansja >40 powtórzeń → choroba Kennedy'ego); rs1385699 (EDA2R, silniejszy sygnał AGA u części kohort); rs1204038 (PSA, rak prostaty)

**Skrót HGVS (NCBI):** HGVS=NC_000023.11:g.66605144C>A,NC_000023.11:g.66605144C>T,NC_000023.10:g.65824986C>A,NC_000023.10:g.65824986C>T,NG_013271.3:g.39125G>T,NG_013271.3:g.39125G>A,NG_013271.2:g.39123G>T,NG_013271.2:g.39123G>A,NM_021783.5:c.170G>T,NM_021783.5:c.170G>A,NM_021783.4:c.170G>T,NM_021783.4:…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs1204038

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | AR |
| Lokalizacja | chr X, X |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | benign |
| MAF / allely | allely ref/alt: G/A |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1204038) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1204038) | — |

**Kontekst w pliku `md/AR.md` (poza sekcją 4):** **Powiązane markery:** CAGn (VNTR w eksonie 1 — długość CAG moduluje czułość receptora; ekspansja >40 powtórzeń → choroba Kennedy'ego); rs1385699 (EDA2R, silniejszy sygnał AGA u części kohort); rs1204038 (PSA, rak prostaty)

**Skrót HGVS (NCBI):** HGVS=NC_000023.11:g.67568383G>A,NC_000023.10:g.66788225G>A,NG_009014.2:g.29352G>A · SEQ=[G/A] · LEN=1 · GENE=AR:367

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## CDH13 — Kadheryna sercowa

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs12919501**
- **rs4075942**
- **rs7190768**
- **rs8059696**
- **rs4783277**
- **rs12596958**
- **rs12051272**
- **rs3865188**
- **rs8060301**
- **rs12444338**
- **rs62040565**
- **rs113460564**

**W sekcji 4 obecne:** `rs11649622`, `rs2199430`, `rs4783244`
**W indeksie łącznie:** `rs11649622`, `rs12919501`, `rs4075942`, `rs7190768`, `rs2199430`, `rs8059696`, `rs4783277`, `rs12596958`, `rs4783244`, `rs12051272`, `rs3865188`, `rs8060301`, `rs12444338`, `rs62040565`, `rs113460564`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs12919501

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 83477411 |
| Funkcja (dbSNP) | genic_downstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/12919501) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs12919501) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.83477411T>C,NC_000016.9:g.83511016T>C,NG_052819.2:g.855444T>C,NG_052819.1:g.855618T>C · SEQ=[T/C] · LEN=1 · GENE=CDH13:1012

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs4075942

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 83516215 |
| Funkcja (dbSNP) | genic_downstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/4075942) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs4075942) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.83516215T>C,NC_000016.9:g.83549820T>C,NG_052819.2:g.894248T>C,NG_052819.1:g.894422T>C · SEQ=[T/C] · LEN=1 · GENE=CDH13:1012

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs7190768

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 83708286 |
| Funkcja (dbSNP) | upstream_transcript_variant, 2KB_upstream_variant, genic_downstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: C/A/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/7190768) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs7190768) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.83708286C>A,NC_000016.10:g.83708286C>T,NC_000016.9:g.83741891C>A,NC_000016.9:g.83741891C>T,NG_052819.2:g.1086319C>A,NG_052819.2:g.1086319C>T,NG_052819.1:g.1086493C>A,NG_052819.1:g.1086493C>T · SEQ=[C/A/T] · LEN=1 · GENE=CDH13:1012,LOC124900603:124900603

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs8059696

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82794977 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A/C/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/8059696) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs8059696) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82794977T>A,NC_000016.10:g.82794977T>C,NC_000016.10:g.82794977T>G,NC_000016.9:g.82828582T>A,NC_000016.9:g.82828582T>C,NC_000016.9:g.82828582T>G,NG_052819.2:g.173010T>A,NG_052819.2:g.173010T>C,NG_052819.2:g.173010T>G,NG_052819.1:g.173184T>A,NG_052819.1:g.173184…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs4783277

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82795796 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/C/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/4783277) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs4783277) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82795796T>C,NC_000016.10:g.82795796T>G,NC_000016.9:g.82829401T>C,NC_000016.9:g.82829401T>G,NG_052819.2:g.173829T>C,NG_052819.2:g.173829T>G,NG_052819.1:g.174003T>C,NG_052819.1:g.174003T>G · SEQ=[T/C/G] · LEN=1 · GENE=CDH13:1012,LOC101928446:101928446

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs12596958

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82798037 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: C/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/12596958) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs12596958) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82798037C>T,NC_000016.9:g.82831642C>T,NG_052819.2:g.176070C>T,NG_052819.1:g.176244C>T · SEQ=[C/T] · LEN=1 · GENE=CDH13:1012,LOC101928446:101928446

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs12051272

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82629683 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A/C/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/12051272) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs12051272) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82629683G>A,NC_000016.10:g.82629683G>C,NC_000016.10:g.82629683G>T,NC_000016.9:g.82663288G>A,NC_000016.9:g.82663288G>C,NC_000016.9:g.82663288G>T,NG_052819.2:g.7716G>A,NG_052819.2:g.7716G>C,NG_052819.2:g.7716G>T,NG_052819.1:g.7890G>A,NG_052819.1:g.7890G>C,NG_052…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs3865188

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 16, 82617112 |
| Funkcja (dbSNP) | — |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: A/G/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/3865188) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs3865188) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82617112A>G,NC_000016.10:g.82617112A>T,NC_000016.9:g.82650717A>G,NC_000016.9:g.82650717A>T · SEQ=[A/G/T] · LEN=1

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs8060301

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82628139 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/8060301) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs8060301) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82628139T>A,NC_000016.9:g.82661744T>A,NG_052819.2:g.6172T>A,NG_052819.1:g.6346T>A · SEQ=[T/A] · LEN=1 · GENE=CDH13:1012

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs12444338

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82626550 |
| Funkcja (dbSNP) | 2KB_upstream_variant, upstream_transcript_variant |
| ClinVar (dbSNP) | benign |
| MAF / allely | allely ref/alt: G/A/C/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/12444338) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs12444338) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82626550G>A,NC_000016.10:g.82626550G>C,NC_000016.10:g.82626550G>T,NC_000016.9:g.82660155G>A,NC_000016.9:g.82660155G>C,NC_000016.9:g.82660155G>T,NG_052819.2:g.4583G>A,NG_052819.2:g.4583G>C,NG_052819.2:g.4583G>T,NG_052819.1:g.4757G>A,NG_052819.1:g.4757G>C,NG_052…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs62040565

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82627341 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/62040565) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs62040565) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82627341T>A,NC_000016.10:g.82627341T>C,NC_000016.9:g.82660946T>A,NC_000016.9:g.82660946T>C,NG_052819.2:g.5374T>A,NG_052819.2:g.5374T>C,NG_052819.1:g.5548T>A,NG_052819.1:g.5548T>C · SEQ=[T/A/C] · LEN=1 · GENE=CDH13:1012

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs113460564

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CDH |
| Lokalizacja | chr 16, 82627819 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: A/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/113460564) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs113460564) | — |

**Kontekst w pliku `md/CDH13.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs11649622 – haplotyp z rs12919501, rs4075942, rs7190768; rs2199430 – z rs8059696, rs4783277, rs12596958; rs4783244 – LD z rs12051272 (enhancer +1,7× przy G), rs3865188; meQTL: rs8060301, rs12444338, rs62040565, rs113460564

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.82627819A>C,NC_000016.9:g.82661424A>C,NG_052819.2:g.5852A>C,NG_052819.1:g.6026A>C · SEQ=[A/C] · LEN=1 · GENE=CDH13:1012

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## CHRNA5 — Gen uzależnienia od nikotyny

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs588765**
- **rs680244**

**W sekcji 4 obecne:** `rs16969968`, `rs1051730`
**W indeksie łącznie:** `rs16969968`, `rs1051730`, `rs588765`, `rs680244`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs588765

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CHRNA |
| Lokalizacja | chr 15, 78573083 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A/C/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/588765) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs588765) | — |

**Kontekst w pliku `md/CHRNA5.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs1051730 (CHRNA3, proxy SNP dla rs16969968 w wczesnych GWAS); rs588765, rs680244 (eQTL – regulacja mRNA α5 w korze przedczołowej; homozygoty rs588765 – do ~2× mRNA vs referencja)

**Skrót HGVS (NCBI):** HGVS=NC_000015.10:g.78573083T>A,NC_000015.10:g.78573083T>C,NC_000015.10:g.78573083T>G,NC_000015.9:g.78865425T>A,NC_000015.9:g.78865425T>C,NC_000015.9:g.78865425T>G,NG_023328.1:g.12564T>A,NG_023328.1:g.12564T>C,NG_023328.1:g.12564T>G · SEQ=[T/A/C/G] · LEN=1 · GENE=CHRNA5:1138

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs680244

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | CHRNA |
| Lokalizacja | chr 15, 78578946 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A/C/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/680244) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs680244) | — |

**Kontekst w pliku `md/CHRNA5.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs1051730 (CHRNA3, proxy SNP dla rs16969968 w wczesnych GWAS); rs588765, rs680244 (eQTL – regulacja mRNA α5 w korze przedczołowej; homozygoty rs588765 – do ~2× mRNA vs referencja)

**Skrót HGVS (NCBI):** HGVS=NC_000015.10:g.78578946T>A,NC_000015.10:g.78578946T>C,NC_000015.10:g.78578946T>G,NC_000015.9:g.78871288T>A,NC_000015.9:g.78871288T>C,NC_000015.9:g.78871288T>G,NG_023328.1:g.18427T>A,NG_023328.1:g.18427T>C,NG_023328.1:g.18427T>G · SEQ=[T/A/C/G] · LEN=1 · GENE=CHRNA5:1138

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## DBH — Gen równowagi stresowej

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs2873804**
- **rs1076150**
- **rs1548364**

**W sekcji 4 obecne:** `rs1611115`, `rs1108580`, `rs2519154`, `rs2519152`, `rs129882`, `rs7040170`
**W indeksie łącznie:** `rs1611115`, `rs1108580`, `rs2519154`, `rs2519152`, `rs2873804`, `rs1076150`, `rs1548364`, `rs129882`, `rs7040170`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs2873804

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | DBH |
| Lokalizacja | chr 9, 133640522 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/2873804) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs2873804) | — |

**Kontekst w pliku `md/DBH.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs1108580 (LD z rs1611115); rs2519154, rs2519152, rs2873804, rs1076150, rs1548364 (atomoksetyna, ADHD); rs129882 (Parkinson); rs7040170 (A>G, allel G obniża DBH, zaburzenia koncentracji)

**Skrót HGVS (NCBI):** HGVS=NC_000009.12:g.133640522T>A,NC_000009.12:g.133640522T>C,NC_000009.11:g.136505644T>A,NC_000009.11:g.136505644T>C,NG_008645.1:g.9160T>A,NG_008645.1:g.9160T>C · SEQ=[T/A/C] · LEN=1 · GENE=DBH:1621

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs1076150

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 9, 133633639 |
| Funkcja (dbSNP) | — |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1076150) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1076150) | — |

**Kontekst w pliku `md/DBH.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs1108580 (LD z rs1611115); rs2519154, rs2519152, rs2873804, rs1076150, rs1548364 (atomoksetyna, ADHD); rs129882 (Parkinson); rs7040170 (A>G, allel G obniża DBH, zaburzenia koncentracji)

**Skrót HGVS (NCBI):** HGVS=NC_000009.12:g.133633639T>C,NC_000009.11:g.136498761T>C,NG_008645.1:g.2277T>C · SEQ=[T/C] · LEN=1

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs1548364

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | DBH |
| Lokalizacja | chr 9, 133642620 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | benign |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1548364) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1548364) | — |

**Kontekst w pliku `md/DBH.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs1108580 (LD z rs1611115); rs2519154, rs2519152, rs2873804, rs1076150, rs1548364 (atomoksetyna, ADHD); rs129882 (Parkinson); rs7040170 (A>G, allel G obniża DBH, zaburzenia koncentracji)

**Skrót HGVS (NCBI):** HGVS=NC_000009.12:g.133642620A>G,NC_000009.11:g.136507742A>G,NG_008645.1:g.11258A>G · SEQ=[A/G] · LEN=1 · GENE=DBH:1621

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## FKBP5 — Gen stresu

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs3800373**
- **rs7748266**
- **rs9394309**

**W sekcji 4 obecne:** `rs1360780`, `rs9296158`, `rs9470080`
**W indeksie łącznie:** `rs1360780`, `rs9296158`, `rs3800373`, `rs9470080`, `rs7748266`, `rs9394309`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs3800373

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 6, 35574699 |
| Funkcja (dbSNP) | 3_prime_UTR_variant, genic_downstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | benign |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/3800373) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs3800373) | — |

**Kontekst w pliku `md/FKBP5.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs9296158 (intron 5, trauma dziecięca), rs3800373 (sprzężony z rs1360780), rs9470080 (PTSD+depresja), rs7748266, rs9394309 *Haplotyp blokowy ryzyka:* rs3800373-A, rs9296158-G, rs1360780-C, rs9470080-T (A-G-C-T) – sprzężone objawy po traumie; interpretuj łącznie z pojedynczymi SNP.

**Skrót HGVS (NCBI):** HGVS=NC_000006.12:g.35574699C>A,NC_000006.12:g.35574699C>G,NC_000006.12:g.35574699C>T,NC_000006.11:g.35542476C>A,NC_000006.11:g.35542476C>G,NC_000006.11:g.35542476C>T,NG_012645.2:g.158885G>T,NG_012645.2:g.158885G>C,NG_012645.2:g.158885G>A,NM_004117.4:c.*1136G>T,NM_004117.4:c.*113…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs7748266

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | FKBP |
| Lokalizacja | chr 6, 35624967 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/7748266) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs7748266) | — |

**Kontekst w pliku `md/FKBP5.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs9296158 (intron 5, trauma dziecięca), rs3800373 (sprzężony z rs1360780), rs9470080 (PTSD+depresja), rs7748266, rs9394309

**Skrót HGVS (NCBI):** HGVS=NC_000006.12:g.35624967T>A,NC_000006.12:g.35624967T>C,NC_000006.11:g.35592744T>A,NC_000006.11:g.35592744T>C,NG_012645.2:g.108617A>T,NG_012645.2:g.108617A>G · SEQ=[T/A/C] · LEN=1 · GENE=FKBP5:2289

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs9394309

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | FKBP |
| Lokalizacja | chr 6, 35654004 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/9394309) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs9394309) | — |

**Kontekst w pliku `md/FKBP5.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** rs9296158 (intron 5, trauma dziecięca), rs3800373 (sprzężony z rs1360780), rs9470080 (PTSD+depresja), rs7748266, rs9394309

**Skrót HGVS (NCBI):** HGVS=NC_000006.12:g.35654004G>A,NC_000006.11:g.35621781G>A,NG_012645.2:g.79580C>T · SEQ=[G/A] · LEN=1 · GENE=FKBP5:2289

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## FTO — Gen otyłości

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs1421085**
- **rs17817449**
- **rs9930506**
- **rs8050136**

**W sekcji 4 obecne:** `rs9939609`
**W indeksie łącznie:** `rs9939609`, `rs1421085`, `rs17817449`, `rs9930506`, `rs8050136`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs1421085

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | FTO |
| Lokalizacja | chr 16, 53767042 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | risk-factor |
| MAF / allely | allely ref/alt: T/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1421085) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1421085) | — |

**Kontekst w pliku `md/FTO.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** Silne sprzężenie z rs1421085, rs17817449, rs9930506, rs8050136; haplotypy C-G-A (ryzyka) i T-T-T (ochronny)

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.53767042T>C,NC_000016.9:g.53800954T>C,NG_012969.2:g.68081T>C,NG_012969.1:g.68080T>C · SEQ=[T/C] · LEN=1 · GENE=FTO:79068,LOC124903691:124903691

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs17817449

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | FTO |
| Lokalizacja | chr 16, 53779455 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | benign |
| MAF / allely | allely ref/alt: T/A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/17817449) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs17817449) | — |

**Kontekst w pliku `md/FTO.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** Silne sprzężenie z rs1421085, rs17817449, rs9930506, rs8050136; haplotypy C-G-A (ryzyka) i T-T-T (ochronny)

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.53779455T>A,NC_000016.10:g.53779455T>G,NC_000016.9:g.53813367T>A,NC_000016.9:g.53813367T>G,NG_012969.2:g.80494T>A,NG_012969.2:g.80494T>G,NG_012969.1:g.80493T>A,NG_012969.1:g.80493T>G · SEQ=[T/A/G] · LEN=1 · GENE=FTO:79068

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs9930506

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | FTO |
| Lokalizacja | chr 16, 53796553 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/9930506) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs9930506) | — |

**Kontekst w pliku `md/FTO.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** Silne sprzężenie z rs1421085, rs17817449, rs9930506, rs8050136; haplotypy C-G-A (ryzyka) i T-T-T (ochronny)

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.53796553A>G,NC_000016.9:g.53830465A>G,NG_012969.2:g.97592A>G,NG_012969.1:g.97591A>G · SEQ=[A/G] · LEN=1 · GENE=FTO:79068

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs8050136

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | FTO |
| Lokalizacja | chr 16, 53782363 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: C/A |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/8050136) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs8050136) | — |

**Kontekst w pliku `md/FTO.md` (poza sekcją 4):** **Powiązane markery / haplotyp:** Silne sprzężenie z rs1421085, rs17817449, rs9930506, rs8050136; haplotypy C-G-A (ryzyka) i T-T-T (ochronny)

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.53782363C>A,NC_000016.9:g.53816275C>A,NG_012969.2:g.83402C>A,NG_012969.1:g.83401C>A · SEQ=[C/A] · LEN=1 · GENE=FTO:79068

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## HERC2 — Gen niebieskich oczu

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs1129038**
- **rs916977**
- **rs1667394**

**W sekcji 4 obecne:** `rs12913832`
**W indeksie łącznie:** `rs12913832`, `rs1129038`, `rs916977`, `rs1667394`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs1129038

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 15, 28111713 |
| Funkcja (dbSNP) | genic_downstream_transcript_variant, 3_prime_UTR_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1129038) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1129038) | — |

**Kontekst w pliku `md/HERC2.md` (poza sekcją 4):** **Orientacja nici i mapowanie alleli:** Na nici komplementarnej często C/T; rs1129038 w 3' UTR w niemal pełnym LD z rs12913832 (haplotyp BEH2) **Powiązane markery:** rs1129038, rs916977, rs1667394; patogeniczne mutacje kodujące (np. c.1781C>T) — zespół HERC2 / opóźnienie rozwoju **Genetyka sądowa:** rs12913832 — fundament systemu IrisPlex; rs1129038 w pełnym LD — redundantny genotypowo w EUR.

**Skrót HGVS (NCBI):** HGVS=NC_000015.10:g.28111713C>A,NC_000015.10:g.28111713C>G,NC_000015.10:g.28111713C>T,NC_000015.9:g.28356859C>A,NC_000015.9:g.28356859C>G,NC_000015.9:g.28356859C>T,NG_016355.1:g.215437G>T,NG_016355.1:g.215437G>C,NG_016355.1:g.215437G>A,NM_004667.6:c.*50G>T,NM_004667.6:c.*50G>C,NM…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs916977

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 15, 28268218 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | affects |
| MAF / allely | allely ref/alt: T/A/C/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/916977) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs916977) | — |

**Kontekst w pliku `md/HERC2.md` (poza sekcją 4):** **Powiązane markery:** rs1129038, rs916977, rs1667394; patogeniczne mutacje kodujące (np. c.1781C>T) — zespół HERC2 / opóźnienie rozwoju

**Skrót HGVS (NCBI):** HGVS=NC_000015.10:g.28268218T>A,NC_000015.10:g.28268218T>C,NC_000015.10:g.28268218T>G,NC_000015.9:g.28513364T>A,NC_000015.9:g.28513364T>C,NC_000015.9:g.28513364T>G,NG_016355.1:g.58932A>T,NG_016355.1:g.58932A>G,NG_016355.1:g.58932A>C,NW_011332701.1:g.401663C>T,NW_011332701.1:g.401…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs1667394

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 15, 28285036 |
| Funkcja (dbSNP) | genic_upstream_transcript_variant, intron_variant |
| ClinVar (dbSNP) | association |
| MAF / allely | allely ref/alt: C/A/G/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1667394) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1667394) | — |

**Kontekst w pliku `md/HERC2.md` (poza sekcją 4):** **Powiązane markery:** rs1129038, rs916977, rs1667394; patogeniczne mutacje kodujące (np. c.1781C>T) — zespół HERC2 / opóźnienie rozwoju

**Skrót HGVS (NCBI):** HGVS=NC_000015.10:g.28285036C>A,NC_000015.10:g.28285036C>G,NC_000015.10:g.28285036C>T,NC_000015.9:g.28530182C>A,NC_000015.9:g.28530182C>G,NC_000015.9:g.28530182C>T,NG_016355.1:g.42114G>T,NG_016355.1:g.42114G>C,NG_016355.1:g.42114G>A,NW_011332701.1:g.418481T>C,NW_011332701.1:g.418…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## MAOA — Gen Wojownika

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs3027407**

**W sekcji 4 obecne:** `rs909525`, `rs6323`, `rs1137070`, `rs72554632`
**W indeksie łącznie:** `rs909525`, `rs6323`, `rs1137070`, `rs72554632`, `rs3027407`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs3027407

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | MAOA |
| Lokalizacja | chr X, X |
| Funkcja (dbSNP) | 3_prime_UTR_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/3027407) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs3027407) | — |

**Kontekst w pliku `md/MAOA.md` (poza sekcją 4):** **Powiązane markery / proxy:** rs909525 (proxy), rs6323 (R297R), rs1137070 (c.1410T>C), rs72554632 (p.Gln296Ter), rs3027407

**Skrót HGVS (NCBI):** HGVS=NC_000023.11:g.43745594A>G,NC_000023.10:g.43604841A>G,NG_008957.2:g.94434A>G,NM_000240.4:c.*1081A>G,NM_000240.3:c.*1081A>G,NM_001270458.2:c.*1081A>G,NM_001270458.1:c.*1081A>G · SEQ=[A/G] · LEN=1 · GENE=MAOA:4128

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## MC1R — Gen rudych włosów

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs1805005**
- **rs885479**

**W sekcji 4 obecne:** `rs1805007`, `rs1805008`, `rs1805009`, `rs2228479`
**W indeksie łącznie:** `rs1805007`, `rs1805008`, `rs1805009`, `rs2228479`, `rs1805005`, `rs885479`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs1805005

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | MC |
| Lokalizacja | chr 16, 89919436 |
| Funkcja (dbSNP) | coding_sequence_variant, missense_variant, 500B_downstream_variant, downstream_transcript_variant |
| ClinVar (dbSNP) | benign,association,likely-benign |
| Zmiana białkowa (HGVS) | p.Val60Leu |
| MAF / allely | allely ref/alt: G/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1805005) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1805005) | — |

**Kontekst w pliku `md/MC1R.md` (poza sekcją 4):** **Główne rsID (panel):** rs1805007, rs1805008, rs1805009, rs2228479, rs1805005, rs885479 **Powiązane markery / kategorie:** "R" - rs1805007, rs1805008, rs1805009; "r" - rs2228479, rs1805005, rs885479 **Średnia globalna (ALL):** Częstości zależą od konkretnego rsID; przykładowo rs1805005 wynosi globalnie ok. 8,20%

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.89919436G>T,NC_000016.9:g.89985844G>T,NG_134986.2:g.1020G>T,NG_134986.1:g.1020G>T,NG_027810.1:g.2428G>T,NG_012026.1:g.6558G>T,NM_002386.4:c.178G>T,NM_002386.3:c.178G>T,NP_002377.4:p.Val60Leu · SEQ=[G/T] · LEN=1 · GENE=MC1R:4157,LOC124903759:124903759

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs885479

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 16, 89919746 |
| Funkcja (dbSNP) | coding_sequence_variant, missense_variant |
| ClinVar (dbSNP) | benign |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/885479) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs885479) | — |

**Kontekst w pliku `md/MC1R.md` (poza sekcją 4):** **Główne rsID (panel):** rs1805007, rs1805008, rs1805009, rs2228479, rs1805005, rs885479 **Powiązane markery / kategorie:** "R" - rs1805007, rs1805008, rs1805009; "r" - rs2228479, rs1805005, rs885479

**Skrót HGVS (NCBI):** HGVS=NC_000016.10:g.89919746G>A,NC_000016.10:g.89919746G>C,NC_000016.10:g.89919746G>T,NC_000016.9:g.89986154G>A,NC_000016.9:g.89986154G>C,NC_000016.9:g.89986154G>T,NG_134986.2:g.1330G>A,NG_134986.2:g.1330G>C,NG_134986.2:g.1330G>T,NG_027810.1:g.2738G>A,NG_027810.1:g.2738G>C,NG_027…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## OCA2 — Gen pigmentacji oczu i skóry

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs1800401**

**W sekcji 4 obecne:** `rs1800407`, `rs12913832`, `rs1800414`
**W indeksie łącznie:** `rs1800407`, `rs12913832`, `rs1800414`, `rs1800401`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs1800401

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 15, 28014907 |
| Funkcja (dbSNP) | missense_variant, non_coding_transcript_variant, coding_sequence_variant |
| ClinVar (dbSNP) | affects,benign |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/1800401) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs1800401) | — |

**Kontekst w pliku `md/OCA2.md` (poza sekcją 4):** **Powiązane markery:** rs12913832 (HERC2, enhancer — główny determinant barwy tęczówki); rs1800414 (p.His615Arg, pigmentacja skóry w Azji Wschodniej); rs1800401 (p.Arg305Trp); delecja 2,7 kb (albinizm typu 2 w Afryce)

**Skrót HGVS (NCBI):** HGVS=NC_000015.10:g.28014907G>A,NC_000015.9:g.28260053G>A,NG_009846.2:g.89408C>T,NG_009846.1:g.89406C>T,NM_000275.3:c.913C>T,NM_000275.2:c.913C>T,NM_001300984.2:c.913C>T,NM_001300984.1:c.913C>T,NW_011332701.1:g.149207G>A,NT_187660.1:g.149207G>A,XM_011521640.3:c.913C>T,XM_01152164…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## OR2M — Gen zapachu szparagów

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs13373863**
- **rs71538191**
- **rs6689553**
- **rs72765116**
- **rs57711976**

**W sekcji 4 obecne:** `rs4481887`
**W indeksie łącznie:** `rs4481887`, `rs13373863`, `rs71538191`, `rs6689553`, `rs72765116`, `rs57711976`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs13373863

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | OR |
| Lokalizacja | chr 1, 247994384 |
| Funkcja (dbSNP) | intron_variant, genic_upstream_transcript_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A/C/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/13373863) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs13373863) | — |

**Kontekst w pliku `md/OR2M.md` (poza sekcją 4):** **Powiązane markery:** rs13373863 (OR2L3), rs71538191, rs6689553; OR2M3: rs72765116, rs57711976 (tiole cebulowe)

**Skrót HGVS (NCBI):** HGVS=NC_000001.11:g.247994384G>A,NC_000001.11:g.247994384G>C,NC_000001.11:g.247994384G>T,NC_000001.10:g.248157686G>A,NC_000001.10:g.248157686G>C,NC_000001.10:g.248157686G>T · SEQ=[G/A/C/T] · LEN=1 · GENE=OR2L13:284521

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs71538191

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 1, 248306916 |
| Funkcja (dbSNP) | — |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/71538191) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs71538191) | — |

**Kontekst w pliku `md/OR2M.md` (poza sekcją 4):** **Powiązane markery:** rs13373863 (OR2L3), rs71538191, rs6689553; OR2M3: rs72765116, rs57711976 (tiole cebulowe)

**Skrót HGVS (NCBI):** HGVS=NC_000001.11:g.248306916G>A,NC_000001.11:g.248306916G>C,NC_000001.10:g.248470218G>A,NC_000001.10:g.248470218G>C · SEQ=[G/A/C] · LEN=1

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs6689553

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 1, 248313953 |
| Funkcja (dbSNP) | — |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: T/A/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/6689553) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs6689553) | — |

**Kontekst w pliku `md/OR2M.md` (poza sekcją 4):** **Powiązane markery:** rs13373863 (OR2L3), rs71538191, rs6689553; OR2M3: rs72765116, rs57711976 (tiole cebulowe)

**Skrót HGVS (NCBI):** HGVS=NC_000001.11:g.248313953T>A,NC_000001.11:g.248313953T>C,NC_000001.10:g.248477255T>A,NC_000001.10:g.248477255T>C · SEQ=[T/A/C] · LEN=1

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs72765116

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | OR |
| Lokalizacja | chr 1, 248209910 |
| Funkcja (dbSNP) | 3_prime_UTR_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A/C |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/72765116) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs72765116) | — |

**Kontekst w pliku `md/OR2M.md` (poza sekcją 4):** **Powiązane markery:** rs13373863 (OR2L3), rs71538191, rs6689553; OR2M3: rs72765116, rs57711976 (tiole cebulowe)

**Skrót HGVS (NCBI):** HGVS=NC_000001.11:g.248209910G>A,NC_000001.11:g.248209910G>C,NC_000001.10:g.248373212G>A,NC_000001.10:g.248373212G>C,NM_001004689.2:c.*5904G>A,NM_001004689.2:c.*5904G>C · SEQ=[G/A/C] · LEN=1 · GENE=OR2M3:127062

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs57711976

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | OR |
| Lokalizacja | chr 1, 248199715 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/57711976) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs57711976) | — |

**Kontekst w pliku `md/OR2M.md` (poza sekcją 4):** **Powiązane markery:** rs13373863 (OR2L3), rs71538191, rs6689553; OR2M3: rs72765116, rs57711976 (tiole cebulowe)

**Skrót HGVS (NCBI):** HGVS=NC_000001.11:g.248199715G>A,NC_000001.10:g.248363017G>A · SEQ=[G/A] · LEN=1 · GENE=OR2M3:127062

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## OR6A2 — Gen mydlanej kolendry

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs7107418**
- **rs3930075**
- **rs10839631**
- **rs7926083**

**W sekcji 4 obecne:** `rs72921001`
**W indeksie łącznie:** `rs72921001`, `rs7107418`, `rs3930075`, `rs10839631`, `rs7926083`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs7107418

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | OR |
| Lokalizacja | chr 11, 6871595 |
| Funkcja (dbSNP) | 3_prime_UTR_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: A/C/G/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/7107418) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs7107418) | — |

**Kontekst w pliku `md/OR6A2.md` (poza sekcją 4):** **Powiązane markery:** rs7107418 (proxy, r²≈1 w EUR); rs3930075, rs10839631, rs7926083 (OR10A2, LD) **Średnia globalna (ALL):** MAF allelu A (proxy rs7107418-G) ok. 25–40% w kohortach mieszanych **Baza referencyjna:** [SNPedia (rs72921001)](https://www.snpedia.com/index.php/Rs72921001) – Kolendra i proxy rs7107418.

**Skrót HGVS (NCBI):** HGVS=NC_000011.10:g.6871595A>C,NC_000011.10:g.6871595A>G,NC_000011.10:g.6871595A>T,NC_000011.9:g.6892826A>C,NC_000011.9:g.6892826A>G,NC_000011.9:g.6892826A>T,NM_001004460.2:c.*929A>C,NM_001004460.2:c.*929A>G,NM_001004460.2:c.*929A>T · SEQ=[A/C/G/T] · LEN=1 · GENE=OR10A2:341276

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs3930075

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | OR |
| Lokalizacja | chr 11, 6869882 |
| Funkcja (dbSNP) | coding_sequence_variant, missense_variant |
| ClinVar (dbSNP) | — |
| Zmiana białkowa (HGVS) | p.His43Arg |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/3930075) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs3930075) | — |

**Kontekst w pliku `md/OR6A2.md` (poza sekcją 4):** **Powiązane markery:** rs7107418 (proxy, r²≈1 w EUR); rs3930075, rs10839631, rs7926083 (OR10A2, LD)

**Skrót HGVS (NCBI):** HGVS=NC_000011.10:g.6869882A>G,NC_000011.9:g.6891113A>G,NM_001004460.2:c.128A>G,NM_001004460.1:c.128A>G,NP_001004460.1:p.His43Arg · SEQ=[A/G] · LEN=1 · GENE=OR10A2:341276

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs10839631

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | OR |
| Lokalizacja | chr 11, 6870374 |
| Funkcja (dbSNP) | coding_sequence_variant, missense_variant |
| ClinVar (dbSNP) | — |
| Zmiana białkowa (HGVS) | p.His207Arg |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/10839631) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs10839631) | — |

**Kontekst w pliku `md/OR6A2.md` (poza sekcją 4):** **Powiązane markery:** rs7107418 (proxy, r²≈1 w EUR); rs3930075, rs10839631, rs7926083 (OR10A2, LD)

**Skrót HGVS (NCBI):** HGVS=NC_000011.10:g.6870374A>G,NC_000011.9:g.6891605A>G,NM_001004460.2:c.620A>G,NM_001004460.1:c.620A>G,NP_001004460.1:p.His207Arg · SEQ=[A/G] · LEN=1 · GENE=OR10A2:341276

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs7926083

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 11, 6870527 |
| Funkcja (dbSNP) | coding_sequence_variant, missense_variant |
| ClinVar (dbSNP) | — |
| Zmiana białkowa (HGVS) | p.Lys258Thr |
| MAF / allely | allely ref/alt: A/C/G/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/7926083) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs7926083) | — |

**Kontekst w pliku `md/OR6A2.md` (poza sekcją 4):** **Powiązane markery:** rs7107418 (proxy, r²≈1 w EUR); rs3930075, rs10839631, rs7926083 (OR10A2, LD)

**Skrót HGVS (NCBI):** HGVS=NC_000011.10:g.6870527A>C,NC_000011.10:g.6870527A>G,NC_000011.10:g.6870527A>T,NC_000011.9:g.6891758A>C,NC_000011.9:g.6891758A>G,NC_000011.9:g.6891758A>T,NM_001004460.2:c.773A>C,NM_001004460.2:c.773A>G,NM_001004460.2:c.773A>T,NM_001004460.1:c.773A>C,NM_001004460.1:c.773A>G,NM…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## SLC24A4 — Gen jasnej karnacji

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs12590654**
- **rs10498633**

**W sekcji 4 obecne:** `rs12896399`, `rs11160059`
**W indeksie łącznie:** `rs12896399`, `rs11160059`, `rs12590654`, `rs10498633`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs12590654

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | SLC |
| Lokalizacja | chr 14, 92472511 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A/C/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/12590654) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs12590654) | — |

**Kontekst w pliku `md/SLC24A4.md` (poza sekcją 4):** **Powiązane markery:** rs11160059 (SBP u Afroamerykanów, nie w LD z rs12896399); rs12590654, rs10498633 (LOAD, ekspresja w korze) **Neurologia:** rs12590654 — możliwa redukcja ryzyka LOAD (dane europejskie, niejednorodne w Azji); dieta MIND, cardio, omega-3.

**Skrót HGVS (NCBI):** HGVS=NC_000014.9:g.92472511G>A,NC_000014.9:g.92472511G>C,NC_000014.9:g.92472511G>T,NC_000014.8:g.92938855G>A,NC_000014.8:g.92938855G>C,NC_000014.8:g.92938855G>T,NG_023408.1:g.154931G>A,NG_023408.1:g.154931G>C,NG_023408.1:g.154931G>T · SEQ=[G/A/C/T] · LEN=1 · GENE=SLC24A4:123041

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs10498633

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | SLC |
| Lokalizacja | chr 14, 92460608 |
| Funkcja (dbSNP) | intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/10498633) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs10498633) | — |

**Kontekst w pliku `md/SLC24A4.md` (poza sekcją 4):** **Powiązane markery:** rs11160059 (SBP u Afroamerykanów, nie w LD z rs12896399); rs12590654, rs10498633 (LOAD, ekspresja w korze)

**Skrót HGVS (NCBI):** HGVS=NC_000014.9:g.92460608G>T,NC_000014.8:g.92926952G>T,NG_023408.1:g.143028G>T · SEQ=[G/T] · LEN=1 · GENE=SLC24A4:123041

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## SLC45A2 — Gen jasnej skóry (MATP)

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs2287949**
- **rs121912621**
- **rs375077956**

**W sekcji 4 obecne:** `rs16891982`, `rs26722`
**W indeksie łącznie:** `rs16891982`, `rs26722`, `rs2287949`, `rs121912621`, `rs375077956`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs2287949

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 5, 33954406 |
| Funkcja (dbSNP) | synonymous_variant, missense_variant, genic_downstream_transcript_variant, coding_sequence_variant |
| ClinVar (dbSNP) | benign,likely-benign |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/2287949) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs2287949) | — |

**Kontekst w pliku `md/SLC45A2.md` (poza sekcją 4):** **Powiązane markery:** rs26722 (E272K, Azja Wschodnia); rs2287949 (synonimiczny, haplotypy); patogenne OCA4: rs121912621 (p.Asp157Asn), rs375077956 (p.Tyr266Ter)

**Skrót HGVS (NCBI):** HGVS=NC_000005.10:g.33954406T>A,NC_000005.10:g.33954406T>C,NC_000005.10:g.33954406T>G,NC_000005.9:g.33954511T>A,NC_000005.9:g.33954511T>C,NC_000005.9:g.33954511T>G,NG_011691.3:g.35287A>T,NG_011691.3:g.35287A>G,NG_011691.3:g.35287A>C,NG_011691.2:g.35270A>T,NG_011691.2:g.35270A>G,N…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs121912621

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 5, 33982329 |
| Funkcja (dbSNP) | coding_sequence_variant, missense_variant |
| ClinVar (dbSNP) | pathogenic |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/121912621) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs121912621) | — |

**Kontekst w pliku `md/SLC45A2.md` (poza sekcją 4):** **Powiązane markery:** rs26722 (E272K, Azja Wschodnia); rs2287949 (synonimiczny, haplotypy); patogenne OCA4: rs121912621 (p.Asp157Asn), rs375077956 (p.Tyr266Ter) **Uwagi o zmienności populacyjnej:** Mutacje OCA4 (np. rs121912621) MAF ~0% w zdrowych kohortach; efekt założyciela w Japonii.

**Skrót HGVS (NCBI):** HGVS=NC_000005.10:g.33982329C>G,NC_000005.10:g.33982329C>T,NC_000005.9:g.33982434C>G,NC_000005.9:g.33982434C>T,NG_011691.3:g.7364G>C,NG_011691.3:g.7364G>A,NG_011691.2:g.7347G>C,NG_011691.2:g.7347G>A,NM_016180.5:c.469G>C,NM_016180.5:c.469G>A,NM_016180.4:c.469G>C,NM_016180.4:c.469G…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs375077956

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 5, 33963781 |
| Funkcja (dbSNP) | synonymous_variant, stop_gained, coding_sequence_variant, intron_variant |
| ClinVar (dbSNP) | likely-benign,pathogenic |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/375077956) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs375077956) | — |

**Kontekst w pliku `md/SLC45A2.md` (poza sekcją 4):** **Powiązane markery:** rs26722 (E272K, Azja Wschodnia); rs2287949 (synonimiczny, haplotypy); patogenne OCA4: rs121912621 (p.Asp157Asn), rs375077956 (p.Tyr266Ter)

**Skrót HGVS (NCBI):** HGVS=NC_000005.10:g.33963781G>A,NC_000005.10:g.33963781G>T,NC_000005.9:g.33963886G>A,NC_000005.9:g.33963886G>T,NG_011691.3:g.25912C>T,NG_011691.3:g.25912C>A,NG_011691.2:g.25895C>T,NG_011691.2:g.25895C>A,NM_016180.5:c.798C>T,NM_016180.5:c.798C>A,NM_016180.4:c.798C>T,NM_016180.4:c.…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## SLC6A4 — Gen depresji

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs4795541**

**W sekcji 4 obecne:** `rs25531`, `rs25532`, `rs1042173`
**W indeksie łącznie:** `rs4795541`, `rs25531`, `rs25532`, `rs1042173`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs4795541

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | SLC |
| Lokalizacja | chr 17, 30237299 |
| Funkcja (dbSNP) | intron_variant, 2KB_upstream_variant, genic_upstream_transcript_variant, upstream_transcript_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: A/G |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/4795541) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs4795541) | — |

**Kontekst w pliku `md/SLC6A4.md` (poza sekcją 4):** **Główny marker:** 5-HTTLPR (rs4795541) + rs25531 (A>G w regionie promotorowym) **Baza referencyjna:** [SNPedia (rs4795541)](https://www.snpedia.com/index.php/Rs4795541) – 5-HTTLPR, VNTR, farmakogenomika SSRI i psychoterapia.

**Skrót HGVS (NCBI):** HGVS=NC_000017.11:g.30237299A>G,NC_000017.10:g.28564317A>G,NG_011747.2:g.3638T>C,NG_055470.1:g.1919A>G · SEQ=[A/G] · LEN=1 · GENE=SLC6A4:6532,LOC105371720:105371720

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---

## ZEB2 — Gen naczyń i Mowata-Wilsona

### 1. rsID bez tabeli wariantów w sekcji 4

- **rs6740731**
- **rs35500812**
- **rs137852981**
- **rs786204815**
- **rs587776604**

**W sekcji 4 obecne:** `rs2252641`, `rs17678683`
**W indeksie łącznie:** `rs2252641`, `rs17678683`, `rs6740731`, `rs35500812`, `rs137852981`, `rs786204815`, `rs587776604`

### 2. Informacje zewnętrzne i kontekst do uzupełnienia tabel

#### rs6740731

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | Z |
| Lokalizacja | chr 2, 144513025 |
| Funkcja (dbSNP) | non_coding_transcript_variant, intron_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: G/A/C/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/6740731) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs6740731) | — |

**Kontekst w pliku `md/ZEB2.md` (poza sekcją 4):** **Powiązane markery:** rs17678683 (CAD, tkanka tłuszczowa); rs6740731, rs35500812; patogenne MOWS: rs137852981 (p.Arg695Ter), rs786204815 (p.Arg343Ter), rs587776604 (p.Met476fs)

**Skrót HGVS (NCBI):** HGVS=NC_000002.12:g.144513025G>A,NC_000002.12:g.144513025G>C,NC_000002.12:g.144513025G>T,NC_000002.11:g.145270592G>A,NC_000002.11:g.145270592G>C,NC_000002.11:g.145270592G>T,NG_016431.1:g.12367C>T,NG_016431.1:g.12367C>G,NG_016431.1:g.12367C>A,NR_033258.2:n.1096C>T,NR_033258.2:n.10…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs35500812

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | TEX |
| Lokalizacja | chr 2, 145073005 |
| Funkcja (dbSNP) | intron_variant, non_coding_transcript_variant |
| ClinVar (dbSNP) | — |
| MAF / allely | allely ref/alt: C/-/CC |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/35500812) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs35500812) | — |

**Kontekst w pliku `md/ZEB2.md` (poza sekcją 4):** **Powiązane markery:** rs17678683 (CAD, tkanka tłuszczowa); rs6740731, rs35500812; patogenne MOWS: rs137852981 (p.Arg695Ter), rs786204815 (p.Arg343Ter), rs587776604 (p.Met476fs)

**Skrót HGVS (NCBI):** HGVS=NC_000002.12:g.145073005del,NC_000002.12:g.145073005dup,NC_000002.11:g.145830572del,NC_000002.11:g.145830572dup,NR_033870.2:n.1067del,NR_033870.2:n.1067dup · SEQ=[C/-/CC] · LEN=2 · GENE=TEX41:401014,LOC100505498:100505498

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs137852981

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | — |
| Lokalizacja | chr 2, 144399104 |
| Funkcja (dbSNP) | genic_downstream_transcript_variant, synonymous_variant, missense_variant, coding_sequence_variant, stop_gained |
| ClinVar (dbSNP) | pathogenic |
| MAF / allely | brak w eSummary |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/137852981) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs137852981) | — |

**Kontekst w pliku `md/ZEB2.md` (poza sekcją 4):** **Powiązane markery:** rs17678683 (CAD, tkanka tłuszczowa); rs6740731, rs35500812; patogenne MOWS: rs137852981 (p.Arg695Ter), rs786204815 (p.Arg343Ter), rs587776604 (p.Met476fs)

**Skrót HGVS (NCBI):** HGVS=NC_000002.12:g.144399104G>A,NC_000002.12:g.144399104G>C,NC_000002.12:g.144399104G>T,NC_000002.11:g.145156671G>A,NC_000002.11:g.145156671G>C,NC_000002.11:g.145156671G>T,NG_016431.1:g.126288C>T,NG_016431.1:g.126288C>G,NG_016431.1:g.126288C>A,NM_014795.4:c.2083C>T,NM_014795.4:c…

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs786204815

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | ZEB |
| Lokalizacja | chr 2, 144400160 |
| Funkcja (dbSNP) | coding_sequence_variant, stop_gained, genic_downstream_transcript_variant |
| ClinVar (dbSNP) | pathogenic |
| Zmiana białkowa (HGVS) | p.Arg343Ter |
| MAF / allely | allely ref/alt: G/A |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/786204815) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs786204815) | — |

**Kontekst w pliku `md/ZEB2.md` (poza sekcją 4):** **Powiązane markery:** rs17678683 (CAD, tkanka tłuszczowa); rs6740731, rs35500812; patogenne MOWS: rs137852981 (p.Arg695Ter), rs786204815 (p.Arg343Ter), rs587776604 (p.Met476fs)

**Skrót HGVS (NCBI):** HGVS=NC_000002.12:g.144400160G>A,NC_000002.11:g.145157727G>A,NG_016431.1:g.125232C>T,NM_014795.4:c.1027C>T,NM_014795.3:c.1027C>T,NM_001171653.2:c.955C>T,NM_001171653.1:c.955C>T,NP_055610.1:p.Arg343Ter,NP_001165124.1:p.Arg319Ter · SEQ=[G/A] · LEN=1 · GENE=ZEB2:9839

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

#### rs587776604

| Pole | Wartość |
| --- | --- |
| Gen (dbSNP) | ZEB |
| Lokalizacja | chr 2, 144399766 |
| Funkcja (dbSNP) | coding_sequence_variant, genic_downstream_transcript_variant, frameshift_variant |
| ClinVar (dbSNP) | pathogenic |
| Zmiana białkowa (HGVS) | p.Met476fs |
| MAF / allely | allely ref/alt: -/T |
| [dbSNP](https://www.ncbi.nlm.nih.gov/snp/587776604) | — |
| [SNPedia](https://www.snpedia.com/index.php/Rs587776604) | — |

**Kontekst w pliku `md/ZEB2.md` (poza sekcją 4):** **Powiązane markery:** rs17678683 (CAD, tkanka tłuszczowa); rs6740731, rs35500812; patogenne MOWS: rs137852981 (p.Arg695Ter), rs786204815 (p.Arg343Ter), rs587776604 (p.Met476fs)

**Skrót HGVS (NCBI):** HGVS=NC_000002.12:g.144399766dup,NC_000002.11:g.145157333dup,NG_016431.1:g.125631dup,NM_014795.4:c.1426dup,NM_014795.3:c.1426dup,NM_001171653.2:c.1354dup,NM_001171653.1:c.1354dup,NP_055610.1:p.Met476fs,NP_001165124.1:p.Met452fs · SEQ=[-/T] · LEN=6 · GENE=ZEB2:9839

**Sugerowana tabela 3-wierszowa:** homozygota referencyjna / heterozygota / homozygota alternatywna — do uzupełnienia na podstawie SNPedia, publikacji z sekcji 8 oraz raportów w `raporty/`.

---
