[Strona główna](../../../00_indeks.md) > [ryzyko](00_indeks.md) > [Kompendium — ASD](Kompendium — ASD.md)

---

# **Architektura genetyczna i molekularna stratyfikacja zaburzeń spektrum autyzmu: Kompendium dla systemów analizy genomowej i predykcji biotypów**

Zaburzenia spektrum autyzmu (ASD) stanowią jedną z najbardziej złożonych i heterogennych grup dysfunkcji neurorozwojowych, których etiologia opiera się na wielowarstwowych interakcjach między rzadkimi wariantami o wysokiej penetracji a powszechnymi wariantami genetycznymi o małym efekcie.1 Współczesna nauka odeszła od postrzegania autyzmu jako pojedynczej jednostki chorobowej na rzecz koncepcji „autyzmów”, co wymusza stosowanie zaawansowanych narzędzi bioinformatycznych do stratyfikacji pacjentów na tzw. biotypy.3 Dziedziczność ASD szacowana jest na poziomie od 70% do 90%, co czyni to zaburzenie idealnym kandydatem do precyzyjnej diagnostyki molekularnej.5 Niniejszy raport stanowi wyczerpujące opracowanie danych genetycznych niezbędnych do implementacji w systemach analizy kodu genetycznego, mających na celu wyliczenie prawdopodobieństwa wystąpienia określonych biotypów klinicznych.

## **Ewolucja krajobrazu genetycznego ASD: Od rzadkich mutacji do ryzyka poligenowego**

Krajobraz genetyczny autyzmu jest charakteryzowany przez współistnienie różnych klas wariantów. Z jednej strony mamy rzadkie mutacje punktowe i warianty liczby kopii (CNV), które często prowadzą do autyzmu syndromicznego.8 Z drugiej strony, u większości pacjentów (ok. 75-80%) nie udaje się zidentyfikować pojedynczej przyczyny genetycznej, co sugeruje model poligeniczny, w którym setki lub tysiące wariantów powszechnych (SNP) kumulują się, przekraczając próg diagnostyczny.10

Fundamentem dla współczesnych programów analizy genetycznej jest baza SFARI Gene, która w 2026 roku obejmuje ponad 1277 genów sklasyfikowanych pod kątem siły dowodów naukowych wiążących je z autyzmem.12 Geny te są dzielone na kategorie: Kategoria 1 (wysoka pewność), Kategoria 2 (silny kandydat) oraz Kategoria S (syndromiczne).14 Implementacja tych list w systemach analitycznych pozwala na natychmiastową identyfikację pacjentów z grupy wysokiego ryzyka molekularnego.

### **Wysokoprzepustowe zestawienie genów o wysokiej pewności (Kategoria 1\)**

Geny kategorii 1 to te, dla których zidentyfikowano liczne mutacje *de novo* typu loss-of-function (LoF) u pacjentów z ASD.14 Są one kluczowe dla biotypu „szeroko obciążonego” (Broadly Affected), charakteryzującego się ciężkim przebiegiem klinicznym.

| Symbol HGNC | Pełna nazwa genu | Lokalizacja | Główny mechanizm patofizjologiczny |
| :---- | :---- | :---- | :---- |
| ADNP | Activity-dependent neuroprotector homeobox | 20q13.13 | Remodelowanie chromatyny, rozwój mózgu 15 |
| ANK2 | Ankyrin 2, neuronal | 4q25-q27 | Organizacja synaps, transport pęcherzyków 14 |
| ARID1B | AT-rich interaction domain 1B | 6q25.3 | Kompleks SWI/SNF, transkrypcja 15 |
| CHD8 | Chromodomain helicase DNA binding protein 8 | 14q11.2 | Remodelowanie chromatyny, makrocefalia 9 |
| DYRK1A | Dual specificity tyrosine phosphorylation kinase 1A | 21q22.13 | Proliferacja neuronów, neurogeneza 17 |
| FMR1 | Fragile X messenger ribonucleoprotein 1 | Xq27.3 | Translacja mRNA w synapsach (Zespół łamliwego X) 17 |
| GRIN2B | Glutamate receptor ionotropic, NMDA 2B | 12p13.1 | Neurotransmisja glutaminianergiczna 17 |
| SCN2A | Sodium voltage-gated channel alpha subunit 2 | 2q24.3 | Funkcja kanałów sodowych, pobudliwość 17 |
| SHANK3 | SH3 and multiple ankyrin repeat domains 3 | 22q13.33 | Gęstość postsynaptyczna, rusztowanie białkowe 17 |
| SYNGAP1 | Synaptic Ras GTPase activating protein 1 | 6p21.32 | Plastyczność synaptyczna, sygnałowanie Ras 8 |

14

## **Stratyfikacja na biotypy: Nowy paradygmat diagnostyki personocentrycznej**

Tradycyjna diagnostyka ASD opiera się na obserwacji zachowania, jednak najnowsze badania, w tym te opublikowane w lipcu 2025 roku w *Nature Genetics*, wprowadzają podział na cztery genetycznie i fenotypowo odrębne biotypy.3 Każdy z nich wymaga innego podejścia terapeutycznego i ma odmienne podłoże molekularne.

### **Biotyp 1: Klasa Społeczno-Behawioralna (Social/Behavioral)**

Ten biotyp charakteryzuje się znaczącymi deficytami w komunikacji społecznej i obecnością zachowań stereotypowych, ale – co istotne – przy zachowaniu prawidłowego tempa rozwoju kamieni milowych (mowy, motoryki).3

* **Profil genetyczny:** Osoby te wykazują wyższe poligeniczne wskaźniki ryzyka (PRS) dla ADHD oraz najwyższe PRS dla depresji.3 Mutacje dotyczą genów neuronalnych, których szczyt ekspresji przypada na okres postnatalny (po urodzeniu).3  
* **Markery molekularne:** Wzbogacenie w warianty genów związanych z aktywnością mikrotubul, organizacją chromatyny oraz procesami naprawy DNA.3

### **Biotyp 2: Klasa Mieszana z Opóźnieniem Rozwoju (Mixed ASD with DD)**

Biotyp ten definiowany jest przez silne opóźnienie rozwoju (Developmental Delay \- DD), pomimo mniej wyraźnych deficytów społecznych w porównaniu z klasą pierwszą.3

* **Profil genetyczny:** Silniejszy komponent dziedziczny. Zwiększona obecność rzadkich wariantów dziedzicznych oraz mutacji typu loss-of-function (LoF) wpływających na geny kory przedczołowej.3  
* **Markery molekularne:** Geny tej klasy są aktywne głównie w fazie płodowej (fetal life) i wczesnym okresie noworodkowym, co wyjaśnia wczesny wiek diagnozy.3 Zakłócenia dotyczą potencjałów czynnościowych neuronów i depolaryzacji błonowej.3

### **Biotyp 3: Klasa Szeroko Obciążona (Broadly Affected)**

Jest to najbardziej dotkliwa postać ASD, charakteryzująca się wysokimi wynikami we wszystkich siedmiu rdzennych cechach zaburzenia, w tym niepełnosprawnością intelektualną, lękiem i samookaleczeniami.3

* **Profil genetyczny:** Najwyższe obciążenie szkodliwymi mutacjami *de novo* (nowo powstałymi). Najniższe wskaźniki PRS dla IQ (co koreluje z upośledzeniem poznawczym).3  
* **Markery molekularne:** Silne wzbogacenie w mutacje genów docelowych dla białka FMRP oraz genów o wysokim ograniczeniu ewolucyjnym (highly constrained genes).3 Dysregulacja genów występuje na wszystkich etapach rozwoju i we wszystkich typach komórek mózgowych.3

### **Biotyp 4: Klasa Umiarkowanych Wyzwań (Moderate Challenges)**

Osoby te wykazują najniższe nasilenie cech autystycznych, choć nadal znajdują się w obrębie spektrum klinicznego.3

* **Profil genetyczny:** Wzbogacenie w warianty genów o niższym ograniczeniu ewolucyjnym, co sugeruje mniejszy wpływ na kluczowe sieci neuronalne.3

## **Obliczanie poligenowego wskaźnika ryzyka (PRS): Metodologia i kluczowe warianty SNP**

Podczas gdy rzadkie mutacje wyjaśniają od 10% do 20% przypadków ASD, pozostała część herytabilności jest przypisywana wariantom powszechnym (Single Nucleotide Polymorphisms \- SNP).8 Poligeniczny wskaźnik ryzyka (PRS) pozwala na ocenę sumarycznego obciążenia genetycznego danego osobnika.

Obliczenie PRS opiera się na sumie ważonej liczby alleli ryzyka posiadanych przez pacjenta. Matematycznie model ten wyraża się wzorem:

![][image1]  
Gdzie ![][image2] to liczba włączonych markerów SNP, ![][image3] to waga (współczynnik logarytmiczny ilorazu szans) dla danego wariantu pochodząca z badań GWAS (Genome-Wide Association Studies), a ![][image4] to liczba kopii allelu ryzyka (0, 1 lub 2).21

### **Kluczowe loci SNP dla analizy ryzyka ASD (Grove et al., 2019 i nowsze)**

Większość współczesnych kalkulatorów PRS bazuje na danych z Psychiatric Genetics Consortium (PGC), obejmujących 18 381 przypadków i 27 969 kontroli.23

| rsID (Marker) | Chromosom | Allel efektu | Gen priorytetowy | Funkcja i znaczenie |
| :---- | :---- | :---- | :---- | :---- |
| rs910805 | 20 | A | XRN2 / NKX2-4 | Najsilniejszy sygnał GWAS; rola w transkrypcji 26 |
| rs10099100 | 8 | C | MSRA / SOX7 | Związek z rozwojem układu nerwowego 26 |
| rs13177031 | 5 | A | ZSWIM6 | Rola w tworzeniu połączeń neuronalnych 28 |
| rs142920272 | 17 | G | MAPT / CRHR1 | Region h2 (inwersja); wpływ na stabilność mikrotubul 27 |
| rs13188074 | 5 | T | KCNN2 | Kanały potasowe; pobudliwość synaptyczna 27 |
| rs78495856 | 7 | T | THSD7A | Adhezja komórkowa w mózgu 28 |
| rs71190156 | 20 | T | MACROD2 | Rozwój poznawczy i mowa 27 |

26

Zastosowanie tych wariantów w programie analitycznym pozwala nie tylko na ocenę ogólnego ryzyka ASD, ale również na korelację z cechami takimi jak osiągnięcia edukacyjne czy funkcje wykonawcze, co jest istotne dla biotypu Social/Behavioral.23

## **Biotyp metaboliczny: Zaburzenia cyklu folianowego i mitochondriów**

Szacuje się, że u około 30% osób z ASD występują mierzalne nieprawidłowości metaboliczne, które mogą być wtórne do zmian genetycznych.8 Identyfikacja "biotypu metabolicznego" ma kluczowe znaczenie, ponieważ jest to jedna z nielicznych grup, w których możliwe jest celowane leczenie suplementacyjne (np. kwasem folinowym).30

### **Szlak metaboliczny folianów i homocysteiny**

Polimorfizmy w genach tego szlaku wpływają na procesy metylacji DNA, co ma bezpośrednie przełożenie na epigenetyczną regulację rozwoju mózgu.30

| Gen | Wariant SNP | Enzym | Konsekwencje genetyczne |
| :---- | :---- | :---- | :---- |
| MTHFR | rs1801133 (C677T) | Reduktaza metylenotetrahydrofolianu | Spadek aktywności enzymu o 30-70%; wzrost homocysteiny 30 |
| MTHFR | rs1801131 (A1298C) | Reduktaza metylenotetrahydrofolianu | Zaburzenia syntezy neurotransmiterów (BH4) 30 |
| DHFR | rs70991108 (19bp ins/del) | Reduktaza dihydrofolianu | Zaburzenia remetylacji; korelacja z symptomami ASD 30 |
| MTRR | rs1801394 (A66G) | Reduktaza syntazy metioninowej | Synergia z MTHFR; zwiększone ryzyko ASD 31 |
| CBS | rs876657421 | Syntaza cystationiny-beta | Klasyczna homocystynuria z fenotypem autystycznym 30 |

30

### **Dysfunkcja mitochondrialna i geny jądrowe**

Zaburzenia energetyczne są istotnym elementem patofizjologii biotypów z silnym opóźnieniem rozwoju. Analiza powinna obejmować zarówno warianty w mitochondrialnym DNA (mtDNA), jak i genach jądrowych kodujących białka mitochondrialne.8

* **Geny jądrowe (Inborn Errors of Metabolism \- IEM):** PAH (Fenyloketonuria), BCKDK (Deficyt kinazy dehydrogenazy alfa-ketokwasów), SLC6A19 (Choroba Hartnupa).8  
* **Geny mtDNA:** Warianty w genach MT-ATP6, MT-ND1, MT-ND5, które odpowiadają za łańcuch oddechowy i produkcję ATP w neuronach.35

Wykrycie tych wariantów pozwala na zaklasyfikowanie pacjenta do biotypu o podłożu metabolicznym, co często wiąże się z objawami takimi jak regresja rozwoju, padaczka oraz specyficzne zmiany w profilu aminokwasowym krwi.8

## **Biotyp immunologiczny: Układ HLA, cytokiny i mikroglej**

Jednym z najbardziej dynamicznie rozwijających się obszarów badań nad ASD jest rola układu odpornościowego. "Biotyp immunologiczny" charakteryzuje się przewlekłym stanem zapalnym układu nerwowego i dysfunkcją bariery krew-mózg.34

### **Kompleks HLA (Human Leukocyte Antigen)**

Geny HLA na chromosomie 6p21 regulują nie tylko odpowiedź odpornościową, ale także eliminację synaps (synaptic pruning) w rozwijającym się mózgu.37

| Gen HLA | Wariant / Allele | Implikacje kliniczne w ASD |
| :---- | :---- | :---- |
| HLA-B | rs1050502 (p.A93G) | Stwierdzany u ok. 44% pacjentów w grupach badawczych 38 |
| HLA-DQB1 | p.S229N | Korelacja z nadwrażliwością pokarmową i dysbiotycznym profilem jelit 38 |
| HLA-DRB1 | Allel HLA-DR4 | Związek z obecnością matczynych autoprzeciwciał (MAR-ASD) 34 |
| MICA | Polimorfizmy klasy I | Aktywacja wrodzonej odpowiedzi odpornościowej w mózgu 39 |

34

### **Szlaki sygnałowe cytokin**

W tym biotypie kluczowe są geny kontrolujące produkcję mediatorów zapalnych, które mogą przekraczać barierę łożyskową lub być produkowane *in situ* przez mikroglej.40

* **MET Receptor Kinase:** Jeden z najważniejszych genów łączących układ immunologiczny, pokarmowy i nerwowy. Polimorfizmy w promotorze MET zmniejszają jego ekspresję, co osłabia stabilność synaps i zwiększa podatność na zapalenie jelit.37  
* **IL-6 i IL-17A:** Geny te są kluczowe dla mechanizmu matczynej aktywacji immunologicznej (MIA). Podwyższona ekspresja IL-6 u płodu prowadzi do nadmiernej aktywacji mikrogleju i nieprawidłowego wzorca migracji neuronów.40  
* **TNF-α:** Marker chronicznej aktywacji odpornościowej, często skorelowany z ciężkością objawów behawioralnych w klasie Broadly Affected.40

## **Katalog rzadkich wariantów i zespołów syndromicznych (Kategoria S)**

Dla systemów analizy genetycznej niezbędna jest lista genów syndromicznych, które pozwalają na natychmiastowe wskazanie etiologii molekularnej (tzw. "genotype-first approach").19

| Symbol HGNC | Zespół kliniczny | Główne objawy poza ASD |
| :---- | :---- | :---- |
| MECP2 | Zespół Retta | Regresja mowy, stereotypie rąk, u płci żeńskiej 9 |
| TSC1 / TSC2 | Stwardnienie guzowate | Guzy hamartomatyczne, padaczka, znamiona skórne 8 |
| PTEN | Zespół Cowden / Makrocefalia | Makrocefalia, polipy, ryzyko nowotworów 43 |
| UBE3A | Zespół Angelmana | Ataksja, brak mowy, napady śmiechu 8 |
| TCF4 | Zespół Pitta-Hopkinsa | Głębokie opóźnienie rozwoju, hiperwentylacja 18 |
| KMT2D | Zespół Kabuki | Specyficzna dysmorfia twarzy, wady serca 18 |

8

Zidentyfikowanie mutacji w tych genach pozwala na precyzyjne określenie prawdopodobieństwa wystąpienia biotypu o wysokim obciążeniu poznawczym i medycznym.3

## **Implementacja bioinformatyczna: Przygotowanie danych do analizy biotypów**

Aby program analityczny mógł skutecznie szacować prawdopodobieństwo wystąpienia każdego z biotypów, dane wejściowe muszą być ustrukturyzowane w odpowiedni sposób, łącząc analizę rzadkich wariantów (WES/WGS) z analizą poligenową (SNP array).

### **Kroki procesowe dla algorytmu analizy:**

1. **Ekstrakcja wariantów rzadkich (VCF):** Skanowanie pod kątem mutacji LoF (nonsensowne, przesunięcie ramki odczytu, miejsca splicingowe) w genach SFARI 1 i S. Wykrycie takiej mutacji silnie przesuwa prawdopodobieństwo w stronę biotypu **Broadly Affected**.3  
2. **Kalkulacja PRS (PLINK/PRSice):** Wyliczenie PRS dla ASD, ADHD, IQ i depresji. Wysokie PRS dla ADHD przy braku rzadkich mutacji wskazuje na biotyp **Social/Behavioral**.3  
3. **Analiza metaboliczna i mitochondrialna:** Sprawdzenie polimorfizmów w genach MTHFR, DHFR oraz rzadkich wariantów w genach jądrowych IEM (np. PAH, CBS). Wykrycie szkodliwych wariantów w tych genach sugeruje biotyp **Metaboliczny/Mixed ASD**.30  
4. **Skanowanie immunologiczne:** Analiza alleli HLA i wariantów w promotorach cytokin (np. MET). Wyniki te wskazują na biotyp **Immunologiczny**.37

### **Specyfikacja techniczna list genowych (Standardy kontroli jakości):**

Dla wiarygodnej analizy system musi stosować następujące filtry kontroli jakości (QC) 22:

* **Minor Allele Frequency (MAF):** \> 1% dla markerów PRS; \< 0.1% dla wariantów rzadkich.  
* **Hardy-Weinberg Equilibrium (HWE):** ![][image5] (wykluczenie błędów genotypowania).  
* **Imputation Info Score:** \> 0.8 (zapewnienie wysokiej jakości danych uzupełnianych statystycznie).  
* **Linkage Disequilibrium (LD) Clumping:** Zmniejszenie redundancji sygnału SNP w oknie 250-500 kb przy ![][image6].46

## **Funkcjonalna konwergencja genów: Synapsa a Chromatyna**

Program analityczny powinien również raportować, w jakich domenach funkcjonalnych dochodzi do największej liczby uszkodzeń. Większość genów ASD zbiega się w dwóch głównych procesach biologicznych, co ma kluczowe znaczenie dla zrozumienia mechanizmu zaburzenia u danego pacjenta.9

### **Grupa I: Geny stabilności i plastyczności synaptycznej**

Geny te odpowiadają za komunikację międzykomórkową i "okablowanie" mózgu.

| Domena funkcjonalna | Kluczowe geny | Rola w ASD |
| :---- | :---- | :---- |
| Adhezja synaptyczna | NRXN1, NLGN3, CNTNAP2 | Tworzenie fizycznych połączeń między neuronami 17 |
| Białka rusztowania | SHANK3, SYNGAP1, DLG4 | Organizacja receptorów w synapsie 20 |
| Kanały jonowe | SCN2A, CACNA1A, KCNQ2 | Przewodnictwo elektryczne i pobudliwość 17 |
| Neurotransmisja | GRIN2B, GABRB3, SLC6A4 | Równowaga między pobudzeniem a hamowaniem 17 |

9

### **Grupa II: Geny regulacji epigenetycznej i transkrypcyjnej**

Te geny kontrolują, jak i kiedy inne geny są odczytywane podczas rozwoju płodowego.

| Mechanizm | Kluczowe geny | Rola w ASD |
| :---- | :---- | :---- |
| Remodelowanie chromatyny | CHD8, ARID1B, SMARCA4 | Zmiana dostępności DNA dla czynników transkrypcyjnych 17 |
| Metylacja DNA / Histonów | MECP2, KMT2A, NSD1 | Trwałe wyciszanie lub aktywacja regionów genomu 18 |
| Regulacja transkrypcji | ADNP, POGZ, FOXP1 | Bezpośrednia kontrola ekspresji genów neuronalnych 14 |
| Ubikwitynacja | UBE3A, HERC1, FBXO11 | Degradacja białek i kontrola cyklu komórkowego 9 |

20

Podział ten jest skorelowany z czasem wystąpienia dysfunkcji. Geny chromatynowe są aktywne głównie w okresie prenatalnym (biotypy z opóźnieniem rozwoju), podczas gdy geny synaptyczne wykazują aktywność przez całe życie (biotypy społeczne).3

## **Warianty liczby kopii (CNV) jako krytyczne czynniki ryzyka**

Algorytm nie może pomijać strukturalnych zmian genomu. Wiele biotypów Broadly Affected wynika z dużych delecji lub duplikacji, które obejmują wiele genów jednocześnie.2

| Region CNV | Typ zmiany | Powiązany fenotyp i biotyp |
| :---- | :---- | :---- |
| 16p11.2 | Delecja / Duplikacja | Częste ASD, zaburzenia BMI, niepełnosprawność intelektualna 2 |
| 15q11-13 | Duplikacja (matczyna) | Zespół idic(15), ciężki autyzm, padaczka 2 |
| 22q11.2 | Delecja | Zespół DiGeorge'a; wysokie ryzyko ASD i schizofrenii 8 |
| 1q21.1 | Delecja / Duplikacja | Mikrocefalia / Makrocefalia, opóźnienie rozwoju 10 |
| 7q11.23 | Duplikacja | Silne deficyty mowy i lęk społeczny 2 |

2

Implementacja detekcji CNV w programie analizy kodu genetycznego pozwala na wyjaśnienie etiologii u pacjentów, u których analiza SNP i WES nie dała jednoznacznych rezultatów.1

## **Interakcja genotypu ze środowiskiem: Czynniki modyfikujące**

Ostateczny fenotyp (biotyp) pacjenta jest wynikiem interakcji predyspozycji genetycznej z czynnikami zewnętrznymi, co systemy analityczne mogą modelować jako dodatkowe zmienne.1

1. **Teoria "Two-Hit" (dwóch uderzeń):** Sugeruje, że pacjenci z jednym dużym czynnikiem ryzyka (np. CNV 16p11.2) mogą mieć łagodny fenotyp, dopóki nie wystąpi u nich drugie "uderzenie" w postaci wysokiego PRS-ASD lub szkodliwego czynnika środowiskowego.1  
2. **Ochronny efekt płci żeńskiej (Female Protective Effect):** Kobiety z autyzmem wykazują średnio większe obciążenie rzadkimi mutacjami szkodliwymi niż mężczyźni z tymi samymi objawami, co sugeruje, że ich mózgi posiadają wyższy próg odporności na zmiany genetyczne.1  
3. **Wiek diagnozy a genetyka:** Biotypy Mixed ASD i Broadly Affected są diagnozowane znacznie wcześniej (często przed 2\. rokiem życia) ze względu na wyraźne opóźnienia neurorozwojowe, co wiąże się z mutacjami w genach aktywnych prenatalnie.3

## **Podsumowanie i rekomendacje dla implementacji systemowej**

Integracja pełnej listy genów związanych z ASD oraz markerów SNP w jednym systemie analitycznym pozwala na przejście od diagnostyki opisowej do molekularnej. System taki powinien generować raport prawdopodobieństwa biotypów w oparciu o hierarchiczną analizę danych:

* **Prawdopodobieństwo Biotypu 3 (Broadly Affected):** Wysokie, jeśli wykryto mutacje LoF w genach SFARI 1, cele FMRP lub patogenne CNV (np. 15q11-13).  
* **Prawdopodobieństwo Biotypu 2 (Mixed ASD with DD):** Wysokie, jeśli wykryto rzadkie warianty dziedziczne w genach kory przedczołowej lub warianty metaboliczne (szlak folianowy).  
* **Prawdopodobieństwo Biotypu 1 (Social/Behavioral):** Wysokie, jeśli PRS dla ASD i ADHD znajduje się w górnym decylu populacji, przy jednoczesnym braku rzadkich mutacji o wysokiej penetracji.  
* **Prawdopodobieństwo Biotypu Immunologicznego/Metabolicznego:** Dodatkowe flagi przy wykryciu specyficznych wariantów w kompleksie HLA, receptorze MET lub genach mitochondrialnych.

Tak skonstruowane narzędzie bioinformatyczne stanowi fundament dla medycyny precyzyjnej w psychiatrii, umożliwiając nie tylko diagnozę, ale także prognozowanie współchorobowości i personalizację interwencji terapeutycznych.3 Krajobraz genetyczny ASD w 2026 roku jest dowodem na to, że zrozumienie "kodu" autyzmu wymaga holistycznego spojrzenia na genom, od pojedynczego nukleotydu po złożone struktury chromatyne i interakcje poligeniczne.

#### **Cytowane prace**

1. Autism Spectrum Disorder: Genetic Mechanisms and Inheritance Patterns \- MDPI, otwierano: maja 12, 2026, [https://www.mdpi.com/2073-4425/16/5/478](https://www.mdpi.com/2073-4425/16/5/478)  
2. Biomarkers in Autism \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4129499/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4129499/)  
3. Person-focused approach explains distinct autism genetic subtypes, otwierano: maja 12, 2026, [https://www.news-medical.net/news/20250715/Person-focused-approach-explains-distinct-autism-genetic-subtypes.aspx](https://www.news-medical.net/news/20250715/Person-focused-approach-explains-distinct-autism-genetic-subtypes.aspx)  
4. Major autism study uncovers biologically distinct subtypes, paving the way for precision diagnosis and care \- Princeton University, otwierano: maja 12, 2026, [https://www.princeton.edu/news/2025/07/09/major-autism-study-uncovers-biologically-distinct-subtypes-paving-way-precision](https://www.princeton.edu/news/2025/07/09/major-autism-study-uncovers-biologically-distinct-subtypes-paving-way-precision)  
5. Three decades of ASD genetics: building a foundation for neurobiological understanding and treatment \- Oxford Academic, otwierano: maja 12, 2026, [https://academic.oup.com/hmg/article/30/20/R236/6329032](https://academic.oup.com/hmg/article/30/20/R236/6329032)  
6. Unraveling the Genetic and Molecular Architecture of Autism Spectrum Disorder: Implications for Clinical Genetics and Genomic Diagnostics \- MDPI, otwierano: maja 12, 2026, [https://www.mdpi.com/1422-0067/27/7/3278](https://www.mdpi.com/1422-0067/27/7/3278)  
7. (PDF) De Novo Variants Predominate in Autism Spectrum Disorder \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/395890916\_De\_Novo\_Variants\_Predominate\_in\_Autism\_Spectrum\_Disorder](https://www.researchgate.net/publication/395890916_De_Novo_Variants_Predominate_in_Autism_Spectrum_Disorder)  
8. Biochemical, Genetic and Clinical Diagnostic Approaches to Autism ..., otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10138025/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10138025/)  
9. Genetic Causes and Modifiers of Autism Spectrum Disorder \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2019.00385/full](https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2019.00385/full)  
10. The genetic landscape of autism spectrum disorder in the Middle Eastern population, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1363849/full](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1363849/full)  
11. 'Polygenic risk scores' for autism, explained | The Transmitter, otwierano: maja 12, 2026, [https://www.thetransmitter.org/spectrum/polygenic-risk-scores-for-autism-explained/](https://www.thetransmitter.org/spectrum/polygenic-risk-scores-for-autism-explained/)  
12. SFARI Gene, otwierano: maja 12, 2026, [https://www.sfari.org/resource/sfari-gene/](https://www.sfari.org/resource/sfari-gene/)  
13. Human Gene Module \- SFARI Gene, otwierano: maja 12, 2026, [https://gene.sfari.org/database/human-gene/](https://gene.sfari.org/database/human-gene/)  
14. Category 1 \- SFARI Gene, otwierano: maja 12, 2026, [https://gene.sfari.org/database/gene-scoring/category-1/](https://gene.sfari.org/database/gene-scoring/category-1/)  
15. Gene Scoring Module \- SFARI Gene, otwierano: maja 12, 2026, [https://gene.sfari.org/database/gene-scoring/](https://gene.sfari.org/database/gene-scoring/)  
16. SFARI genes and where to find them; modelling Autism Spectrum Disorder specific gene expression dysregulation with RNA-seq data \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9203566/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9203566/)  
17. SFARI Gene Category 1 Autism Candidates Details | Gemma, otwierano: maja 12, 2026, [https://gemma.msl.ubc.ca/geneSet/showGeneSet.html?id=303](https://gemma.msl.ubc.ca/geneSet/showGeneSet.html?id=303)  
18. Integrated gene analyses of de novo variants from 46,612 trios with ..., otwierano: maja 12, 2026, [https://www.pnas.org/doi/10.1073/pnas.2203491119](https://www.pnas.org/doi/10.1073/pnas.2203491119)  
19. Syndromic autism spectrum disorders: moving from a clinically defined to a molecularly defined approach \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5789213/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5789213/)  
20. Resolving the synaptic vs. developmental dichotomy of Autism risk genes \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7101276/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7101276/)  
21. Calculating Polygenic Risk Scores (PRS) in UK Biobank: A Practical Guide for Epidemiologists \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.818574/full](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.818574/full)  
22. Polygenic Risk Score (PRS) Tutorial, otwierano: maja 12, 2026, [https://odap-ico.github.io/PRS\_tutorial/](https://odap-ico.github.io/PRS_tutorial/)  
23. Well-being spectrum traits are associated with polygenic scores for autism \- UK Biobank, otwierano: maja 12, 2026, [https://www.ukbiobank.ac.uk/publications/well-being-spectrum-traits-are-associated-with-polygenic-scores-for-autism/](https://www.ukbiobank.ac.uk/publications/well-being-spectrum-traits-are-associated-with-polygenic-scores-for-autism/)  
24. PGS000327 / Autism spectrum disorder (Polygenic Score) \- PGS Catalog, otwierano: maja 12, 2026, [https://www.pgscatalog.org/score/PGS000327/](https://www.pgscatalog.org/score/PGS000327/)  
25. A Systematic Review and Meta-Analysis: Research Using the Autism Polygenic Score, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.1101/2024.03.08.24303918v1.full-text](https://www.medrxiv.org/content/10.1101/2024.03.08.24303918v1.full-text)  
26. Novel Gene-Based Analysis of ASD GWAS: Insight Into the Biological Role of Associated Genes \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2019.00733/full](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2019.00733/full)  
27. Novel Gene-Based Analysis of ASD GWAS: Insight Into the Biological Role of Associated Genes \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6696953/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6696953/)  
28. Estimating the Prevalence and Genetic Risk Mechanisms of ARFID in a Large Autism Cohort, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8221394/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8221394/)  
29. Neural correlates of polygenic risk score for autism spectrum disorders in general population, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7475696/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7475696/)  
30. Genetics and Epigenetics of One-Carbon Metabolism Pathway in Autism Spectrum Disorder: A Sex-Specific Brain Epigenome? \- MDPI, otwierano: maja 12, 2026, [https://www.mdpi.com/2073-4425/12/5/782](https://www.mdpi.com/2073-4425/12/5/782)  
31. Association of folate metabolism gene polymorphisms with autism susceptibility and symptom severity in the Chinese population \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12531928/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12531928/)  
32. Biochemical profile of children with autism spectrum disorders associated with genetic deficiency of the folate cycle \- Biochimica Clinica, otwierano: maja 12, 2026, [https://biochimicaclinica.it/wp-content/uploads/2023/03/pag132\_58\_22\_Maltsev.pdf](https://biochimicaclinica.it/wp-content/uploads/2023/03/pag132_58_22_Maltsev.pdf)  
33. Inborn Errors of Metabolism Associated With Autism Spectrum Disorders: Approaches to Intervention \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.673600/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.673600/full)  
34. Re-emerging concepts of immune dysregulation in autism spectrum disorders \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.1006612/full](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.1006612/full)  
35. Mitochondrial genome \- HUGO Gene Nomenclature Committee (HGNC), otwierano: maja 12, 2026, [https://www.genenames.org/data/genegroup/\#\!/group/1972](https://www.genenames.org/data/genegroup/#!/group/1972)  
36. Blood Test Could Help Diagnose Kids with Autism \- Global Genes, otwierano: maja 12, 2026, [https://globalgenes.org/blog/blood-test-could-help-diagnose-kids-with-autism/](https://globalgenes.org/blog/blood-test-could-help-diagnose-kids-with-autism/)  
37. Immune contributions to cause and effect in autism spectrum disorder \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5650493/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5650493/)  
38. Identifying Rare Genetic Variants of Immune Mediators as Risk Factors for Autism Spectrum Disorder \- MDPI, otwierano: maja 12, 2026, [https://www.mdpi.com/2073-4425/13/6/1098](https://www.mdpi.com/2073-4425/13/6/1098)  
39. HLA Immune Function Genes in Autism \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3420779/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3420779/)  
40. Natural Anti-Inflammatory Agents for Autism Spectrum Disorders \- Encyclopedia.pub, otwierano: maja 12, 2026, [https://encyclopedia.pub/entry/40417](https://encyclopedia.pub/entry/40417)  
41. Neuroimmune mechanisms in autism etiology \- untangling a complex problem using human cellular models \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11044813/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044813/)  
42. Autism Spectrum Disorder: A Neuro-Immunometabolic Hypothesis of the Developmental Origins \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10375982/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10375982/)  
43. Advanced Search \- SFARI Gene, otwierano: maja 12, 2026, [https://gene.sfari.org/search/](https://gene.sfari.org/search/)  
44. (PDF) Psychiatric Polygenic Risk Scores as Predictor for Attention Deficit/Hyperactivity Disorder and Autism Spectrum Disorder in a Clinical Child and Adolescent Sample \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/334686136\_Psychiatric\_Polygenic\_Risk\_Scores\_as\_Predictor\_for\_Attention\_DeficitHyperactivity\_Disorder\_and\_Autism\_Spectrum\_Disorder\_in\_a\_Clinical\_Child\_and\_Adolescent\_Sample](https://www.researchgate.net/publication/334686136_Psychiatric_Polygenic_Risk_Scores_as_Predictor_for_Attention_DeficitHyperactivity_Disorder_and_Autism_Spectrum_Disorder_in_a_Clinical_Child_and_Adolescent_Sample)  
45. Association of Whole-Person Eigen-Polygenic Risk Scores with Alzheimer's Disease, otwierano: maja 12, 2026, [https://www.biorxiv.org/content/10.1101/2022.09.13.507735.full](https://www.biorxiv.org/content/10.1101/2022.09.13.507735.full)  
46. A review of methods and software for polygenic risk score analysis \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12453730/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12453730/)  
47. Building a PRS Pipeline from Scratch | by Michael Anekson \- Medium, otwierano: maja 12, 2026, [https://medium.com/@michaelanekson/building-a-prs-pipeline-from-scratch-35073f4df054](https://medium.com/@michaelanekson/building-a-prs-pipeline-from-scratch-35073f4df054)  
48. Identification of Neurotransmission and Synaptic Biological Processes Disrupted in Autism Spectrum Disorder Using Interaction Networks and Community Detection Analysis \- MDPI, otwierano: maja 12, 2026, [https://www.mdpi.com/2227-9059/11/11/2971](https://www.mdpi.com/2227-9059/11/11/2971)  
49. The emerging role of chromatin remodelers in neurodevelopmental disorders: a developmental perspective \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8004494/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8004494/)  
50. A Machine Learning Approach to Predicting Autism Risk Genes: Validation of Known Genes and Discovery of New Candidates \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2020.500064/full](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2020.500064/full)  
51. 2024 Autism Science Review, otwierano: maja 12, 2026, [https://autismsciencefoundation.org/year-end-summary-2024/](https://autismsciencefoundation.org/year-end-summary-2024/)  
52. An alternative method of SNP inclusion to develop a generalized polygenic risk score analysis across Alzheimer's disease cohorts \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11285631/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11285631/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAA4CAYAAABAFaTtAAAFyklEQVR4Xu3d26ttVR0H8F9UElnZhSyK8Bh0Lykh7UIX6GKUCUJi0JVQCCvxwZLQiu53olIyo4skWQRFUj0kYkFmEQUlCEW9RBC9Cf0BNr6MOVtjz7OXrbXP3md7jp8P/FhrzjHWXGvNpx+/McYcVQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHDcPK3FHS0eMh3/tMU1LU75Xw8AAA7da1tcOb1/x9gAAMDhe0T16trvWlzY4uKdzQAAHLanT69XtbipxcuGNgAA7gfePb2mynZdi4cNbQAAAAAAAAAAAAAAwANAFhfcO0Ue4bEu5j5zZOWohQgAAMfJ2dWTsPe0eNCibTdJ1P7R4pPLBgAADs5/WtxdPXnbxDktfrU8CQBwonh29QQoVatUohLfafGMqf2vU9s9U9u/WrxkaptdXX3/zstb/KLFLTub992TajXc+dBF2zoPrvUVuc+2eGOLr9fm11vncdV/13OXDQAAx+L5Lb48HGfngLtanD4dv7fFeavmuqH6FlCRbaE+OLTFbYvjg5Ah0bnSdtaibRtvH96/oPq9OFY/q/XJIQDAniwTtie0+O10PpYJW/qmKhXpmwQuuwzMcnzQMjft29WrWd9ftG3qUS0+Phy/q8Xjh+O9+tvyBADAsVombBdVr17NVaIxYcvQ4j9r59BhhkmTOP2yxfuH88fD/N3nLxs2kATtNbUaXs3/3KsvtXhTi2/UzgrjZS3eNrXNW2hFqnBvrtXw8aktPlW9cpnPf286H6n8pYqZ6/xpOJ/Ppv8VZRUsAJz0krD9pMWZ1Stmy3lcY8KWPrtVtJLcJdG7ucUfFm0XLI73U6pk+T3bzGebfaJWic5cVYzn1GrId5TE6ZLlyep95/65l/Mw6xuq35NZfmOkzxerDzm/dDqXxHO+xl9qdY38vtun9/H76Vyqi2dUv0YSvTm5fvn0OlvONwQATlBJIH5YfT7abpZDonPiEUmSxvlaeT+2RypDBylz2PKdWUCxjbHilYUMSYbinbX7b07/by7OJXm6scWR6TiVtNzP5fmY70uGXfP+zy1eXL3vH2vVN0Oq83D0C2s1bPvw6tfMgoYkdXnm3DW16pth6XE+YY5fORwDACewvSRsj5zepzL1rKEt5sQnklCkCrabrMxcF68e+v0/T6nth0STzKRiNvtC9ZWuGZr8fK3/zUtjZe7R1Yc68/rUFnfMnZpntvhYi7e2+Pd0LslVErBcI98f+exXp9fc49z3+Xe+rsUrpuO/T+dmGar+dIsPTMf5/vyPbauOAMD9UKpS8zywPMJjKXOmMp/tnurJQnymxYeqDw8+scX7WtzZ4uIWX6lVgvGY6pWrI9PxQbi+xYeXJzfwouoP0/1W9WT1ydP5JDoZ1k3CtKnnVf/fl1ZPvHLNyH//UYtbq89li9ybPPrkc9O5OaFKn/kaP6/VNeI30/GvazWEm+/MY0gyj+2j1RPQJHS5H5HHi+S7tvkfAMBJJMOer68+3DYnEEk8UhlbzplKkreucnes8p1JfPZSRcqCgzitjv78lYvjTcyPQMm9me9JPLZ69WuU4+Vq1PyG+Rr5zHiNOFJ92HSUa4zXvrZ2zr3LPLhxuBoAYFeZHH8QMgSaStWmlolTFhzsJv2uqj637LBlzlyqm5HqWiqb9+UHtRoSTYXtx0MbAMBRPlJ9iC8rGPdbtqTadFuqyDBjhmwfKLIwIvPlxkUVAABHObd60rYcbtwP21TW8oiOVKmuWzacxDJc/aoyHAoAHILxmWvbxO21mh8GAMABOqf6IoNt4y35MAAAAAAAAAAAAOyT7CiQLZ3WyarQPAPuvvoAAHBAsq3UJnuNZo9UCRsAwCG4qMXXqu9ccFP1vUDHyDPgQsIGAHBIzpgi8ny1JGVjzPtwStgAAA5Jnqt2eR29QfroshbfbXHDsgEAgONj3MgdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgI38F3684MDADuJCAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAYCAYAAAD3Va0xAAABGklEQVR4XmNgGAUDBmyA+BIQ/4fiJUDMgSTPC8TLkOQ/A/EcIOZCUgMHjEDcBcSPgPgBEJuiyEKANxDPYkC1BAMIAPFEIE5lgNjYygAxHBlkAHEImhgG0AHiRiAWB+L9QHwaiOWR5FmAuBuqDi8A2RQHZZcwQMIiCSHNIMwAcTHI5XhBAxAbQNmaQHwNiDcBMR9UzAKIW6BsnAAWPiBbQQDkjalA/BqInaBiINcSHT7IgQsyAGQQyEBQLJEcPjAA8hLIayAv2jIQET4gV4D8boguAQShDJCksA+Iq9HkMAB6+CADMQZIUgDFIMHwATkblNw50SWgAJQULgOxGroEDNgD8S0GRP55AMRuyAqgAJQUQHkPb/iMgqEEAEblLziHqHJZAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAXCAYAAADtNKTnAAABTklEQVR4Xu3TTytFQRjH8Uco5E+RbKhDEbFBblLKQlFsbKTwBhDZkJVCSbFQlD0LspElWdlb2PFm+D49d645Y+457Cz86rM4M3OmmWdmRP7zm1RjDFNoDvp+lEFcYBHzeMBMakROenGGRq9tDdeo89rKpgZH6AzaN3CL+qA9mhGsBm068RX2UBH0RbOJUbEf29CEWbGadHjjykb3e4ACXvBR9I4hb1xmEuyKLVlXoCupxTbOUVUamZF1saMNo0f7hoHit062gwk3wMVtpSXsIPt4knhfKonY5WoI2tvxLLYl3aZu8RBbYjc6lUm8Ythr0xM6xqXYxdNJFtCPO4mclh6tXm+9UKc4wSNWxCbTaC26MC226lSh/XpUolXswcUulv6oT2Iu7Ejk62jz0oN79GFZvH+0HkvuIyfduBErrE5Yyrh8f3BZ0Rq5Ov2xfAIStSfDFCR+YgAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAAAYCAYAAABHqosDAAAEFElEQVR4Xu2X66tVVRTFp6igYr5SQ/GR4KNSQQVBVPAkglEKBiqiJRhR4hv0S4oJPgItEYkSCgyFSIzMJ74RCVFRCxMFoeAigR/82B9Q43fnnu611z2KXj944ZwBg3vOWuusveZYc455t1kTTTTRxMtFT3GA2DmfaFRMF1vE/8RDYo/KbINjsHhD/CyfaHRMMc+ad7Lxhscq8Y44Op9oNGCwiDBbHCh+J/5sbsApOonDxHfFqWLX6nQrnmUNYxPtyfMp+pmfa6T53vUQ+/HMIdlcu4EgZ8WN4ofF5wfitnSR+cGOiV+Kc8XN4mlxaLKGA34hflOsWS9+L3ZL1kwTz4vLxY/M97wnzkrWAH7DM5ifL+4Sz4mnxL7FGp63QvxN/Fh8Xzws1or5doOgLotrrLyNReK/VvUXbuO2uNLKda+IR8QdydhM8ajYR+xiLtBF8dVifpL4hziv+A4w+L/ECckYASPESfOMAWTyJfGAuWjsz7MRhQwNIDaitxtxcLrP8GQ89xfKibJKD5mOpyXHb1vMM4+1bxUEsf642KsYA19ZVTxQEx+aBxl4XfxdXFt8r5mv2VB8R8y3xR+tbRZ/YN5pU/Q33z+3i9bAEQA/QSTA39xfZoiPrG3rJhACStfWzA/L/0DwJ/MDgHr7kFmUxh4rsy4uLDd/So292QcgKJlNJl8R94lLzDM5BYKw9rVsfJx5xrURBkPj8EuTsUHiVav6C1lAQHGgAC39HytvLDDCvOQumO8faV1vHw5336pniBJFMIQLICjZTaCUEiV1zdoG/MJAGBRPTS+CfU+cLH5qHljuAdzuVvFP8Q3zg2Ky+BWvESCyIYJGGERAjACm+re5h+E7c6wsua+tzKIYC39hnPk0WwN02O7FZ+LZb9UYKa3F5pUxNhl/jDfN0zVMlrrnFSBEWGd+u3y+a26sgZp5vSMgwBgxQUoiOtB48w5HBgF+zz4hcBg/t06L3W5eOiF6BE2gNAcuMfwF0IFumXtPgGfTXReaX9ACc7Eps3jnYw5BuKidxVgFHADzoQXuNvcDAqUEMLAt5uqybpl5Gu81v4FfxDFWgjVkFxlCN2HdCfPWHGCvz8Vfi/kfzA99XTwofmJlhnBJZMRN8/MQWF6G7LdJPGP+TNZg7PFMWjplxmWRmQD/GmUuEvvHeF1wK+lbNA/EWPO3am6DB+WpmyLW9M4nEjBHxwoR+E36vR7wF7wPD8zBeZ50LrotF5F2XUB8jKf20KGBOPz3utrKkiR7yAQ6VXTPZwX+Rsbgl2n2IggVkpp7hwZeReulvMkispeuR0vGoJ8XtO9vzT0qhAYh2NOytEOBg9IxyBDMF4HwuhdpybT/1BZ4Ruo7DQ9KiS5I6+Z9Kv9PuGFB1lGWlFX6+lHB/2cyuruXqi4DAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAAYCAYAAAC2odCOAAAC5ElEQVR4Xu2XyetOURjHv0LJnDFluAukpAyRWLBQZEgypAwLWeiXaUEyLKQMGRY2QimyIENKycawEjJsxEJspGyVP4Dv13Pv79577nvc4T2Kut/69L7vOee9w/c+z3OeC7Rq1SqsBpDN5AhZRvrkp1sNJRfJPDKNPCRRdkErYBs5DoueUWQTLLL+C/Ulq8lEdyKWbmQtOQ1Lkyn56UoaSG6S/WQ72UVG5lb8g9KNLyXHyGvyiczMrTApRW6QA2QwmUGekJXZRRU0hjyDGaVj6ji3yOjsom6lmwoZmjrWErKQ7IPfpJ3kARmeGVtHnsJuXJpKTsIirRML4rUySceTxpLnsOIdTBHsiR4mI/JTXUsX3skkGSODzjvjs8hH1LvBJN2yJr0gW3tXxBoCe3rj49+DyGLYxakulEkFbzq5Ts6RSfnpxvKZpAh5h6JJWqf1B53xMili98TfZdJjMjedtvA+QXaTN7CIuAwLXX0qLPv3ri6XiuelmCaFNCufSYkZPpPc8TJNIFfIIlgB74HTJ2liL9KncxZpjVH4fojX1JWiSVF1l8xBs+bMZ5IK+08UzWhqkqRAUH0a5k5IG8lsWB5/Q96Q+eQr2ZEZqyuFryK1iVk+k1QafqBoRjcmVZLyWFV9XGZMxUtPbEVmrIlU0E+Re/D3PJ3kM8lnhm88iJIKrxrULx7Tp34rBZWKTaQoUiervqNuFEk+kyLyFkUzEpOSIhxUEeykyTYoqaa8gkVAYlxV6b9nyFXYrlfXnEQ+k9Q83ibXkO/RVCq+xJ/BpXqkHNdWKOmm1Mk+glX+KvobbYBM+gzbQFytJy+Rnie55vuwzjm4VI+0i+kE2rrvwFJN6VImXZxSSSml1Krynz9JqX+BvIfVQ/Ed1p4cTZf93o0U5TrvcphB6m/0WhFcbuiqyGqsqrTTHEL4bruK9IAmk1WwV4w6/VwtRSjWo1aOtsDq0QZ4GqlW+bfiNc5cq1atgukXcgGE13m/LusAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAAYCAYAAABDX1s+AAAClklEQVR4Xu2Xz4tOURzGH6HEkAiN3yk2LPwoM5EUQgkLltKklIXINJKFEk0kPxMz7JhZyIKyFMrKAjMLWSizUxY2/gOep+858973uPe99z33ndfivU99eu8959wf53m/53u+F6hUqVVaRi6Sa2QbmVbf3VlaSgbILLKGvCdH6kZ0mPaRb2SDO1ekPCOzJ0d0mOaQHjLTnV8lT2AR8z80l5wkN0g/WVLfnavp5DBZGXbEaDl5Q/aHHW3SCvKaHIP9IXtgS3hzclCKNFaRfoV8It/JxroREVKE6IaH0PqkqnvnLcEZ5CZ57I69tIRH0ThivXnbYfmwtCF64bNkhztXck2+VKwU/ufIK7I16Au1moyR00H7ATQ3QV3fcLxeSu5pOUj63Yva2lQ0nICFnNrWkjOuPVa6zyB5DjNC6zpPO8kv/GuI3usPORq0Z6mhIV2w5HSefIQlzOuwi96RVbAw+wl7qEfREiPd7xYZIevRnKl+4lmGhO1ZamjILnIctqVqa71D5sO21S9kXW1oKSmqHjl0HCNNJG3iLTWkD2aG1uEP0gv717RkdrvjWOlaRYGiQVGh6CijU0ifeEsN8dJSeUsWhh0ltAiWI+6i+VohTVkTz2rPUq4hSqovyH2Ui4g0JaPkHuKXi6ToVRSHE/eGKMqLKNcQ5QnlC+WSqZTMUA0Rk1ClbvIBFs1J6b3DfLeYLEicJ5VrSDJ/tEPJLXcLihujcRdgNcs816b6aJg8QK0ukvHjsF0zLW/JkAmyKezwUuWmcjjL0amSnncJtlxV8BWpRWTEUzIEq51uk5ewL3IvHWs+2im9caqCH5KvqJUOv8lnctmNmZTK2q6wsY3Sx6M+1ormABmncD/ofosYWalSpUqV2q2/3wJy5i4tWQEAAAAASUVORK5CYII=>