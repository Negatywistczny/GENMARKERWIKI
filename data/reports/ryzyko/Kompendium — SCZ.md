[Strona główna](../../../00_indeks.md) > [ryzyko](00_indeks.md) > [Kompendium — SCZ](Kompendium — SCZ.md)

---

# **Zaawansowana architektura genomowa schizofrenii i ramy obliczeniowe dla predykcji biotypów psychotycznych w oparciu o poligeniczną ocenę ryzyka**

Zrozumienie genetycznego podłoża schizofrenii (SCZ) ewoluowało w ciągu ostatniej dekady od identyfikacji rzadkich wariantów o dużej penetracji do uznania wysoce wielogenowej natury tego zaburzenia, w którym tysiące powszechnych wariantów genetycznych o małym efekcie kumulują się, kształtując indywidualną podatność biologiczną.1 Przełomowe badania asocjacyjne całego genomu (GWAS) przeprowadzone przez Psychiatric Genomics Consortium (PGC), w szczególności trzecia fala analiz (PGC3) opublikowana w 2022 roku, zidentyfikowały rekordową liczbę 287 niezależnych loci genomowych związanych z ryzykiem schizofrenii, co pozwoliło na wyłonienie 120 genów priorytetowych, w większości zaangażowanych w kluczowe funkcje neuronalne i synaptyczne.4 Równolegle, inicjatywy takie jak Bipolar-Schizophrenia Network on Intermediate Phenotypes (B-SNIP) dążą do dekonstrukcji klinicznej heterogeniczności schizofrenii poprzez identyfikację biotypów opartych na markerach biologicznych, takich jak parametry poznawcze, elektrofizjologiczne i okulomotoryczne, które przecinają tradycyjne kategorie diagnostyczne DSM.7 Niniejszy raport stanowi wyczerpujące opracowanie danych genetycznych niezbędnych do obliczania poligenicznego ryzyka (PRS) oraz wskazywania prawdopodobieństwa występowania poszczególnych biotypów w oparciu o najnowsze odkrycia z zakresu genomiki psychiatrycznej i bioinformatyki.

## **Krajobraz genomowy schizofrenii w świetle danych PGC3**

Współczesna analiza genetyczna schizofrenii opiera się na fundamencie statystyk podsumowujących z metaanalizy PGC3, która objęła próbę 76 755 osób ze schizofrenią oraz 243 649 osób z grupy kontrolnej.5 Identyfikacja 287 loci o znaczeniu ogólnogenomowym (![][image1]) umożliwiła precyzyjne mapowanie sygnałów genetycznych na konkretne jednostki funkcjonalne w ośrodkowym układzie nerwowym. Dziedziczność schizofrenii szacowana jest na poziomie 60-80%, z czego znacząca część przypisywana jest wspólnym wariantom genetycznym, co uzasadnia stosowanie modeli PRS w predykcji ryzyka.3

Analizy funkcjonalne przeprowadzone w ramach PGC3, wykorzystujące metody takie jak precyzyjne mapowanie (fine-mapping) oraz Mendlowska randomizacja oparta na danych sumarycznych (SMR), pozwoliły wskazać 120 genów priorytetowych, z których 106 to geny kodujące białka.5 Asocjacje te koncentrują się głównie w neuronach OUN, zarówno pobudzających, jak i hamujących, co sugeruje, że schizofrenia jest przede wszystkim zaburzeniem komunikacji neuronalnej.5

| Symbol genu | Mechanizm biologiczny i funkcja | Znaczenie kliniczne i potencjalne leki |
| :---- | :---- | :---- |
| DRD2 | Receptor dopaminy D2; kluczowy dla sygnalizacji dopaminergicznej | Główny cel tradycyjnych leków przeciwpsychotycznych 4 |
| GRIN2A | Podjednostka receptora NMDA; kluczowa dla plastyczności synaptycznej | Cel dla modulatorów glutaminergicznych (np. iclepertin) 4 |
| CACNA1C | Kanał wapniowy sterowany napięciem (Cav1.2); regulacja prądów wapniowych | Potencjalne zastosowanie blokerów kanału wapniowego (np. werapamil) 4 |
| GABBR2 | Receptor GABA typu B; hamowanie neuronalne w OUN | Cel dla baklofenu; badany w kontekście autyzmu i psychoz 4 |
| PDE4B | Fosfodiesteraza 4B; regulacja poziomów cAMP | Potencjalny cel dla leków prokognitywnych (np. roflumilast) 4 |
| CACNB2 | Pomocnicza podjednostka kanału wapniowego; stabilizacja Cav1.2 | Powiązany z zaburzeniami afektywnymi i lękowymi 4 |
| AKT3 | Kinaza białkowa B; kluczowa dla sygnalizacji przeżycia komórek | Potencjalny cel w onkologii i neuropsychiatrii 4 |
| GRM3 | Metabotropowy receptor glutaminianu 3; autoinhibicja glutaminianu | Cel dla agonistów mGluR2/3 (np. pomaglumetad methionil) 4 |
| ATP2A2 | Pompa wapniowa siateczki (SERCA2); regulacja cytoplazmatycznego wapnia | Locus rs4766428; powiązanie z chorobą Dariera i psychozą 5 |
| HCN1 | Kanał aktywowany hiperpolaryzacją; regulacja rytmu neuronalnego | Przewidywany jako cel dla nowych małych cząsteczek 9 |

Wyliczenie PRS oparte na statystykach PGC3 pozwala na uzyskanie istotnych różnic w odpowiedzialności za schizofrenię. Osoby w najwyższym decylu rozkładu PRS wykazują iloraz szans (OR) wynoszący około 10 w porównaniu do najniższego decyla, co wskazuje na wysoką wartość prognostyczną tej metody w populacjach o podobnym pochodzeniu etnicznym.11

## **Biotypy psychotyczne konsorcjum B-SNIP jako cel predykcji genetycznej**

Tradycyjne diagnozy kliniczne, takie jak schizofrenia (SZ), zaburzenie schizoafektywne (SAD) czy choroba afektywna dwubiegunowa z psychozą (BDP), charakteryzują się ogromnym nakładaniem biologicznym, co utrudnia precyzyjne dopasowanie leczenia.7 Projekt B-SNIP, stosując taksonomię numeryczną na panelu biomarkerów, wyodrębnił trzy biotypy psychozy, które cechują się unikalnymi profilami neurobiologicznymi, niezależnymi od tradycyjnych kategorii DSM.7

Biotypy te zostały zdefiniowane w oparciu o 11 tzw. bio-faktorów, które obejmują sprawność poznawczą (mierzoną testami BACS), kontrolę okulomotoryczną (antysakady) oraz miary elektrofizjologiczne (EEG/ERP), takie jak amplituda odpowiedzi na bodźce słuchowe i aktywność wewnętrzna mózgu.7

| Charakterystyka | Biotyp 1 (BT1) | Biotyp 2 (BT2) | Biotyp 3 (BT3) |
| :---- | :---- | :---- | :---- |
| Status poznawczy | Najcięższe upośledzenie (BACS) | Ciężkie upośledzenie (BACS) | Bliski normie klinicznej 13 |
| Odpowiedź neuronalna | Niska wigoru (ERP); osłabione reakcje na bodźce | Wysoka reaktywność; nadmierna aktywność EEG | Prawidłowa lub bliska normie 8 |
| Kontrola antysakad | Wysoka liczba błędów | Wysoka liczba błędów | Minimalne odchylenia 7 |
| Struktura mózgu | Rozległe redukcje gęstości istoty szarej (GMD) | Umiarkowane redukcje GMD (wyspa, czoło) | Minimalne zmiany strukturalne 17 |
| Rokowanie | Najgorsze wyniki funkcjonalne | Umiarkowane wyniki funkcjonalne | Najlepsze rokowanie kliniczne 16 |

Genetyczna predykcja biotypów wymaga odejścia od ogólnego PRS dla schizofrenii na rzecz modeli uwzględniających specyficzne warianty genetyczne wpływające na powyższe bio-faktory. Chociaż ogólne obciążenie poligeniczne (PRS-SCZ) jest podobne we wszystkich biotypach, to badania transkryptomiczne (TWAS) zidentyfikowały konkretne geny, których ekspresja różnicuje te podgrupy.12

## **Architektura genomowa biotypów: Wyniki TWAS i Mendlowskiej randomizacji**

Najnowsze analizy trans-ancestralne przeprowadzone na próbach B-SNIP zidentyfikowały 12 unikalnych genów i izoform, których genetycznie regulowana ekspresja (GReX) w mózgu jest istotnie powiązana ze specyficznymi biotypami psychotycznymi.12 Siedem z tych genów spełniło rygorystyczne kryteria Mendlowskiej randomizacji (MR), co sugeruje ich przyczynowy charakter w patofizjologii biotypów.12

| Gen / Transkrypt | Biotyp i typ asocjacji | Szlak biologiczny i mechanizm |
| :---- | :---- | :---- |
| TMEM140 | BT1 i BT3 (populacja AFR); mózg dorosły i płodowy | Sygnalizacja adhezyjna; potencjalna rola w rozwoju synaps 12 |
| ARTN | BT1 i BT2 (populacja AFR); mózg płodowy | Koduje arteminę; sygnalizacja RET; rozwój neuronów 12 |
| C1orf115 | BT1 vs BT3; ogólne ryzyko psychozy (populacja ASN) | Nieznana funkcja; potencjalnie kluczowy marker diagnostyczny 12 |
| CYREN | BT3 (populacja ASN); mózg dorosły | Naprawa DNA i ochrona genomu neuronalnego 12 |
| CHRNA5 | BT1; powiązanie z deficytami poznawczymi | Podjednostka receptora nikotynowego; regulacja uwagi 12 |
| GPR151 | BT1; specyficzna asocjacja w populacji EUR | Receptor sierocy; wysoka ekspresja w uzdeczce (habenula) 12 |
| STX16-NPEPL1 | BT1 (populacja EUR); fuzja genowa | Transport wewnątrzkomórkowy i metabolizm peptydów 12 |
| GOLPH3L | BT2 (populacja EUR); mózg dorosły | Funkcja aparatu Golgiego; transport białek błonowych 12 |
| PTPRE | BT3 (populacja EUR); fosfataza tyrozynowa | Sygnalizacja międzykomórkowa i stabilność synaps 12 |

Zidentyfikowane geny wykazują wzbogacenie w szlakach sygnalizacyjnych krytycznych dla rozwoju układu nerwowego, takich jak sygnalizacja RET (Rearranged during Transfection), oddziaływania cząsteczki adhezyjnej NCAM1 oraz szlaki wzrostu neurytów.12 Różnice w profilach genetycznych biotypów sugerują, że Biotyp 1 może wynikać z wczesnych zaburzeń neurorozwojowych wpływających na integralność strukturalną neuronów, podczas gdy Biotyp 2 może być związany z dysregulacją pobudliwości synaptycznej i sygnalizacji wapniowej.12

## **Metodyka obliczeniowa przygotowania danych dla programu analizy kodu genetycznego**

Aby przygotować dane do predykcji prawdopodobieństwa biotypów, program analizujący musi zintegrować statystyki podsumowujące GWAS (plik bazowy) z surowymi danymi genotypowymi pacjenta (plik docelowy). Rekomendowanym standardem oprogramowania jest **PRSice-2**, który oferuje wysoką wydajność obliczeniową i zaawansowane opcje optymalizacji wyników.25

### **Wymagane parametry i struktura danych wejściowych**

Proces obliczania PRS dla biotypów wymaga precyzyjnego sformatowania plików wejściowych, aby uniknąć błędów związanych z odwróceniem nici (strand flip) lub nieprawidłowym przypisaniem alleli ryzyka.27

1. **Plik bazowy (Base File):** Musi zawierać statystyki z PGC3 lub specyficzne wagi biotypowe wyprowadzone z TWAS. Niezbędne kolumny to:  
   * SNP: Identyfikator rsID wariantu genetycznego.  
   * A1: Allel efektywny (allel ryzyka, na który nakładana jest waga).  
   * A2: Allel referencyjny.  
   * OR lub BETA: Wartość ilorazu szans lub logarytmu naturalnego efektu.  
   * P: Wartość istotności statystycznej asocjacji.  
   * INFO i MAF: Służą do filtrowania wariantów o niskiej jakości (zalecane INFO \> 0.8, MAF \> 0.01).27  
2. **Plik docelowy (Target Data):** Surowe genotypy pacjenta w formacie PLINK (.bed,.bim,.fam) lub BGEN. Dane te powinny przejść rygorystyczną kontrolę jakości (QC), obejmującą usunięcie wariantów o wysokim braku danych oraz sprawdzenie heterozygotyczności.27

### **Implementacja analizy biotypów w PRSice-2**

Predykcja biotypów nie polega na jednym wyniku PRS, lecz na profilowaniu ryzyka w obrębie specyficznych szlaków funkcjonalnych przy użyciu modułu **PRSet**.30 Algorytm powinien uwzględniać:

* **Clumping (C):** Usuwanie wariantów w silnym sprzężeniu LD (zalecane parametry: ![][image2], okno 250 kb), aby uniknąć nadmiernej reprezentacji pojedynczych loci.27  
* **Thresholding (T):** Optymalizacja progu P-value. Chociaż w schizofrenii często stosuje się szerokie progi (np. ![][image3] lub ![][image4]), biotypy mogą wymagać bardziej rygorystycznej selekcji loci funkcjonalnych.27  
* **Ancestry Adjustment:** Stosowanie metod post-hoc dopasowania do pochodzenia etnicznego (np. metoda Khery) jest krytyczne dla zminimalizowania inflacji statystycznej wynikającej ze struktury populacji, co jest szczególnie istotne w wielorasowych próbach B-SNIP.12

Przykładowa struktura polecenia dla oprogramowania analizującego prawdopodobieństwo biotypów:

Bash

Rscript PRSice.R \\  
    \--prsice PRSice\_linux \\  
    \--base PGC3\_SCZ\_Weights.txt \\  
    \--target patient\_genotypes \\  
    \--snp SNP \--A1 A1 \--stat OR \--pvalue P \\  
    \--ms-filter Biotype\_Specific\_Genes.txt \\  
    \--clump-kb 250 \--clump-r2 0.1 \--clump-p 1.0 \\  
    \--bar-levels 0.000001,0.00001,0.0001,0.001,0.01,0.05,0.1,0.2,0.3,0.4,0.5 \\  
    \--num-check F \--out SCZ\_Biotype\_Prediction

## **Mechanizmy biologiczne i szlaki synaptyczne w predykcji biotypów**

Mapowanie wariantów genetycznych na szlaki biologiczne pozwala na głębszą interpretację prawdopodobieństwa biotypów. Badania wykazały, że geny schizofrenii są wzbogacone w funkcjach związanych z plastycznością synaptyczną, gospodarką wapniową i sygnalizacją immunologiczną.6

### **Systemy neuroprzekaźnictwa i ich rola w podgrupach**

Analiza asocjacji genetycznych wskazuje na kluczową rolę kilku systemów, których dysfunkcja może być specyficzna dla poszczególnych biotypów:

* **Układ glutaminergiczny i receptory NMDA:** Geny takie jak *GRIN2A* i *GRM3* są kluczowe dla Biotypu 1, charakteryzującego się głębokimi deficytami poznawczymi i niską reaktywnością neuronalną. Osłabienie funkcji receptorów NMDA prowadzi do upośledzenia plastyczności i integracji informacji.4  
* **Sygnalizacja wapniowa:** Loci obejmujące *CACNA1C*, *CACNB2* oraz *ATP2A2* są powiązane z Biotypem 2, w którym dominuje nadpobudliwość neuronalna. Zaburzenia homeostazy wapnia wpływają na uwalnianie neuroprzekaźników i rytmikę pracy mózgu.5  
* **Adhezja neuronalna i rozwój neurytów:** Geny zidentyfikowane w TWAS biotypów (*ARTN*, *TMEM140*) oraz loci takie jak *CNTN4* i *MMP16* wskazują na defekty neurorozwojowe, które mogą determinować strukturę mózgu widoczną w MRI u pacjentów z Biotypem 1\.12

| Szlak biologiczny | Kluczowe geny | Implikacje dla biotypu |
| :---- | :---- | :---- |
| Sygnalizacja RET / NCAM | ARTN, NCAM1, RET | BT1/BT2: Zaburzenia migracji i wzrastania aksonów 12 |
| Gospodarka wapniowa | ATP2A2, CACNA1C, CACNB2 | BT2: Nadreaktywność, zaburzenia hamowania sensorycznego 5 |
| System NMDA / Glutaminian | GRIN2A, GRM3, SLC12A5 | BT1: Deficyty poznawcze, niska amplituda odpowiedzi neuronalnej 4 |
| Kaskada dopełniacza (Układ odpornościowy) | CSMD1, C4A/B | BT1: Nadmierne przycinanie synaptyczne w okresie dojrzewania 9 |
| Sygnalizacja dopaminergiczna | DRD2, AKT3 | Wszystkie biotypy: Podstawowy mechanizm objawów psychotycznych 4 |

Wykorzystanie zasobów takich jak baza **SZDB (A Database for Schizophrenia Genetic Research)** pozwala na integrację danych GWAS z profilami eQTL dla specyficznych typów komórek (np. neuronów glutaminergicznych vs hamujących neuronów GABAergicznych), co znacznie zwiększa precyzję predykcji biotypów na poziomie funkcjonalnym.36

## **Algorytm predykcji biotypów: Od genotypu do prawdopodobieństwa klinicznego**

Ostateczne przygotowanie danych dla programu do analizy kodu genetycznego powinno opierać się na wielowymiarowym modelu punktowym. Prawdopodobieństwo wystąpienia biotypu ![][image5] można zdefiniować jako funkcję sumaryczną wyników cząstkowych z różnych domen genetycznych.

### **Krok 1: Wyliczenie ogólnego PRS-SCZ (Liability Scale)**

Służy jako filtr wstępny potwierdzający genetyczną podatność na psychozę. Wykorzystuje się pełny zestaw 287 loci PGC3.5

### **Krok 2: Profilowanie specyficzne dla biotypów (Biotype-Specific Scores)**

Wprowadzenie wag dla 12 genów i izoform z TWAS B-SNIP.

* **BT1-Score:** Suma wag dla *TMEM140*, *ARTN*, *CHRNA5*, *GPR151*, *STX16*. Wysoki wynik wskazuje na duże prawdopodobieństwo Biotypu 1 (deficyty poznawcze, niska reaktywność).12  
* **BT2-Score:** Suma wag dla *ARTN*, *GOLPH3L*, *CACNA1C*, *ATP2A2*. Wysoki wynik wskazuje na nadaktywność neuronalną i zaburzenia hamowania (Biotyp 2).12  
* **BT3-Score:** Suma wag dla *TMEM140*, *CYREN*, *PTPRE*. Wysoki wynik przy niskim ogólnym obciążeniu innymi genami sugeruje Biotyp 3 (psychoza o łagodniejszym podłożu biologicznym).12

### **Krok 3: Analiza interakcji genetyczno-klinicznych**

Integracja wyników genetycznych z potencjalną odpowiedzią na leczenie. Dane wskazują, że pacjenci z wysokim PRS-SCZ (częściej reprezentujący BT1 i BT2) wykazują większą oporność na standardowe leki (TRS \- Treatment Resistant Schizophrenia).1 Wyliczenie prawdopodobieństwa biotypu pozwala więc na wczesną stratyfikację pacjentów do badań klinicznych nad nowymi cząsteczkami, takimi jak inhibitory transportu glicyny dla BT1 czy blokery kanałów wapniowych dla BT2.4

## **Wnioski dla implementacji systemów medycyny personalizowanej**

Integracja pełnej listy genów związanych ze schizofrenią w ramy obliczeniowe PRSice-2 lub podobnych algorytmów stanowi kluczowy krok w stronę obiektywnej diagnostyki w psychiatrii. Przejście od subiektywnych opisów objawów do predykcji biotypów w oparciu o architekturę genomową pozwala na:

1. Wcześniejszą identyfikację pacjentów o najgorszym rokowaniu (Biotyp 1\) i wdrożenie intensywnej rehabilitacji poznawczej.  
2. Precyzyjne celowanie farmakologiczne w specyficzne szlaki sygnalizacyjne (np. wapniowe vs glutaminergiczne) zależnie od genetycznego profilu biotypowego.  
3. Zminimalizowanie ryzyka błędnych diagnoz w obrębie spektrum schizofrenii i choroby afektywnej dwubiegunowej poprzez skupienie się na wspólnych bio-faktorach.

Wykazane w raportach asocjacje genów takich jak *TMEM140*, *ARTN* czy *CHRNA5* z biotypami psychotycznymi dostarczają biologicznego uzasadnienia dla nowej taksonomii zaburzeń psychicznych, która jest nie tylko spójna statystycznie, ale również zakorzeniona w przyczynowych mechanizmach molekularnych.12 Ostateczny program analizy kodu genetycznego powinien traktować te geny jako priorytetowe markery w procesie przygotowania danych predykcyjnych.

#### **Cytowane prace**

1. Schizophrenia Polygenic Risk Score as a Predictor of Antipsychotic Efficacy in First Episode Psychosis \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6461047/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6461047/)  
2. Genome-wide Association Analysis Identifies 14 New Risk Loci for Schizophrenia \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3827979/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3827979/)  
3. Mapping genomic loci prioritises genes and implicates synaptic biology in schizophrenia, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.1101/2020.09.12.20192922.full](https://www.medrxiv.org/content/10.1101/2020.09.12.20192922.full)  
4. Identifying drug targets for schizophrenia through gene prioritization \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11118622/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11118622/)  
5. otwierano: maja 12, 2026, [https://lirias.kuleuven.be/retrieve/157b1516-6b54-4c30-a496-5748d5672b8c](https://lirias.kuleuven.be/retrieve/157b1516-6b54-4c30-a496-5748d5672b8c)  
6. Mapping genomic loci implicates genes and synaptic biology in schizophrenia \- VU Research Portal, otwierano: maja 12, 2026, [https://research.vu.nl/ws/portalfiles/portal/170337762/Mapping\_genomic\_loci\_implicates\_genes\_and\_synaptic\_biology\_in\_schizophrenia.pdf](https://research.vu.nl/ws/portalfiles/portal/170337762/Mapping_genomic_loci_implicates_genes_and_synaptic_biology_in_schizophrenia.pdf)  
7. Differentiating Biomarker Features and Familial Characteristics of B-SNIP Psychosis Biotypes \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10802686/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10802686/)  
8. Differentiating biomarker features and familial characteristics of B-SNIP psychosis Biotypes, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12354876/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12354876/)  
9. Identifying drug targets for schizophrenia through gene prioritization ..., otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12923709/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12923709/)  
10. Identifying drug targets for schizophrenia through gene prioritization \- medRxiv, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.1101/2024.05.15.24307423v1.full-text](https://www.medrxiv.org/content/10.1101/2024.05.15.24307423v1.full-text)  
11. Polygenic risk score for schizophrenia is more strongly associated with ancestry than with ... \- bioRxiv, otwierano: maja 12, 2026, [https://www.biorxiv.org/content/10.1101/287136v1.full-text](https://www.biorxiv.org/content/10.1101/287136v1.full-text)  
12. Genetic Analysis of Psychosis Biotypes: Shared Ancestry-Adjusted ..., otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11643284/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11643284/)  
13. Psychosis Biotypes: Replication and Validation from the B-SNIP Consortium \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8781330/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8781330/)  
14. Testing Psychosis Phenotypes from B-SNIP for Clinical Application: Biotype Characteristics and Targets | Request PDF \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/340970879\_Testing\_Psychosis\_Phenotypes\_from\_B-SNIP\_for\_Clinical\_Application\_Biotype\_Characteristics\_and\_Targets](https://www.researchgate.net/publication/340970879_Testing_Psychosis_Phenotypes_from_B-SNIP_for_Clinical_Application_Biotype_Characteristics_and_Targets)  
15. Clinical Characterization and Differentiation of B-SNIP Psychosis Biotypes: Algorithmic Diagnostics for Efficient Prescription of Treatments (ADEPT) \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10712427/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10712427/)  
16. Study Details | NCT06740383 | Biomarkers/Biotypes, Course of Early Psychosis and Specialty Services | ClinicalTrials.gov, otwierano: maja 12, 2026, [https://clinicaltrials.gov/study/NCT06740383](https://clinicaltrials.gov/study/NCT06740383)  
17. Brain Structure Biomarkers in the Psychosis Biotypes: Findings From the Bipolar-Schizophrenia Network for Intermediate Phenotypes \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6501573/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6501573/)  
18. (PDF) Supervised machine learning classification of psychosis biotypes based on brain structure: findings from the Bipolar-Schizophrenia network for intermediate phenotypes (B-SNIP) \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/373047244\_Supervised\_machine\_learning\_classification\_of\_psychosis\_biotypes\_based\_on\_brain\_structure\_findings\_from\_the\_Bipolar-Schizophrenia\_network\_for\_intermediate\_phenotypes\_B-SNIP](https://www.researchgate.net/publication/373047244_Supervised_machine_learning_classification_of_psychosis_biotypes_based_on_brain_structure_findings_from_the_Bipolar-Schizophrenia_network_for_intermediate_phenotypes_B-SNIP)  
19. Genetic Analysis of Psychosis Biotypes: Shared Ancestry-Adjusted Polygenic Risk and Unique Genomic Associations | medRxiv, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.1101/2024.12.05.24318404v1](https://www.medrxiv.org/content/10.1101/2024.12.05.24318404v1)  
20. Cindy Wen's research works | University of California, Los Angeles and other places, otwierano: maja 12, 2026, [https://www.researchgate.net/scientific-contributions/Cindy-Wen-2201951478](https://www.researchgate.net/scientific-contributions/Cindy-Wen-2201951478)  
21. Genetic Analysis of Psychosis Biotypes: Shared Ancestry-Adjusted Polygenic Risk and Unique Genomic Associations \- PubMed, otwierano: maja 12, 2026, [https://pubmed.ncbi.nlm.nih.gov/39677452/](https://pubmed.ncbi.nlm.nih.gov/39677452/)  
22. NCAM1 association study of bipolar disorder and schizophrenia: Polymorphisms and alternatively spliced isoforms lead to similarities and differences | Request PDF \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/235771295\_NCAM1\_association\_study\_of\_bipolar\_disorder\_and\_schizophrenia\_Polymorphisms\_and\_alternatively\_spliced\_isoforms\_lead\_to\_similarities\_and\_differences](https://www.researchgate.net/publication/235771295_NCAM1_association_study_of_bipolar_disorder_and_schizophrenia_Polymorphisms_and_alternatively_spliced_isoforms_lead_to_similarities_and_differences)  
23. Genetic analysis of psychosis Biotypes: shared Ancestry-adjusted polygenic risk and unique genomic associations | Request PDF \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/387305126\_Genetic\_analysis\_of\_psychosis\_Biotypes\_shared\_Ancestry-adjusted\_polygenic\_risk\_and\_unique\_genomic\_associations](https://www.researchgate.net/publication/387305126_Genetic_analysis_of_psychosis_Biotypes_shared_Ancestry-adjusted_polygenic_risk_and_unique_genomic_associations)  
24. A review of post-GWAS studies in schizophrenia \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12578940/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12578940/)  
25. PRSice-2: Polygenic Risk Score software for biobank-scale data \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/334476090\_PRSice-2\_Polygenic\_Risk\_Score\_software\_for\_biobank-scale\_data](https://www.researchgate.net/publication/334476090_PRSice-2_Polygenic_Risk_Score_software_for_biobank-scale_data)  
26. PRSice-2: Polygenic Risk Score software for biobank-scale data, otwierano: maja 12, 2026, [https://www.ukbiobank.ac.uk/publications/prsice-2-polygenic-risk-score-software-for-biobank-scale-data/](https://www.ukbiobank.ac.uk/publications/prsice-2-polygenic-risk-score-software-for-biobank-scale-data/)  
27. PRSice-2, otwierano: maja 12, 2026, [https://choishingwan.github.io/PRSice/step\_by\_step/](https://choishingwan.github.io/PRSice/step_by_step/)  
28. Available Commands \- PRSice-2, otwierano: maja 12, 2026, [https://choishingwan.github.io/PRSice/command\_detail/](https://choishingwan.github.io/PRSice/command_detail/)  
29. PRSice-2 \- Basic Tutorial for Polygenic Risk Score Analyses, otwierano: maja 12, 2026, [https://choishingwan.github.io/PRS-Tutorial/prsice/](https://choishingwan.github.io/PRS-Tutorial/prsice/)  
30. Clustering schizophrenia genes by their temporal expression patterns aids functional interpretation genetics-based evidence in favor of the two-hit hypothesis | medRxiv, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.1101/2022.08.25.22279215v1.full-text](https://www.medrxiv.org/content/10.1101/2022.08.25.22279215v1.full-text)  
31. Clustering Schizophrenia Genes by Their Temporal Expression Patterns Aids Functional Interpretation \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10919784/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10919784/)  
32. Polygenic Risk Score for Schizophrenia and Treatment-Resistant Schizophrenia \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5581885/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5581885/)  
33. (PDF) Trans-Ancestry Analysis of Psychosis Biotypes: Shared Polygenic Risk and Unique Genomic Associations \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/378632657\_Trans-Ancestry\_Analysis\_of\_Psychosis\_Biotypes\_Shared\_Polygenic\_Risk\_and\_Unique\_Genomic\_Associations](https://www.researchgate.net/publication/378632657_Trans-Ancestry_Analysis_of_Psychosis_Biotypes_Shared_Polygenic_Risk_and_Unique_Genomic_Associations)  
34. Polygenic Risk Score, Genome-wide Association, and Gene Set Analyses of Cognitive Domain Deficits in Schizophrenia \- eScholarship.org, otwierano: maja 12, 2026, [https://escholarship.org/content/qt03b270n2/qt03b270n2\_noSplash\_52989853881a6922ad52314e574b7b2e.pdf](https://escholarship.org/content/qt03b270n2/qt03b270n2_noSplash_52989853881a6922ad52314e574b7b2e.pdf)  
35. A Sheffield Hallam University thesis, otwierano: maja 12, 2026, [https://shura.shu.ac.uk/35932/1/Slay\_2025\_PhD\_IdentificationOfRare.pdf](https://shura.shu.ac.uk/35932/1/Slay_2025_PhD_IdentificationOfRare.pdf)  
36. SZDB \- Database Commons, otwierano: maja 12, 2026, [https://ngdc.cncb.ac.cn/databasecommons/database/id/4985](https://ngdc.cncb.ac.cn/databasecommons/database/id/4985)  
37. Welcome to SZDB, otwierano: maja 12, 2026, [http://szdb.org/](http://szdb.org/)  
38. Welcome to SZDB 3.0, otwierano: maja 12, 2026, [https://www.szdb.org.cn/](https://www.szdb.org.cn/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAAAYCAYAAAAiR3l8AAAD9klEQVR4Xu2Z2atNURzHfzJknso8XUSETBEiLzIkIh6UMVwkZSbkxTyPGcuDecqQoZAMRUgUQsnDfVAevCh/AN9vv72cc9bZ69y19z7nump/6pNz9z7D2uu71m+tvYmkpKSkpLipCcfD9XAubJB7OqW6MwUODl4PgNtgrczplOpMHbgLdgn+bgQ3wIZ/32ExHL6Fv+DvwI/wXXDsC9wk+kVVTUfR0dhOtKzUhb3hzOB1VcPfnAab2CcC2EflogGsgK1yT3uzCn6GU+FkOC/3dDh74Dc4xDreVzTMC1JgFJQIlpEKyQws+hWOznpPqWkGJ8ED8BN8KeHBdIAP4AzRoEfBp6IlMCr14DHR670C2+eezocj5zp8Dlta5xjaVfgDjrTOxaU2rG8fDKEffASfwPtwtYR3XilhgONgf3hUwgPk+sQJcDJ4bVgHz0mmWgwTnZ1hbofdYQ24AE4UrTaP4UPYQgrAD36Q/AaQpvCuhM/OqHCgLIe3JLNIF4IBbrEPesKOpy5YkluLdpgvByU8wDLRZWiJdZw7SVYMXocvZXC/ZEJvDC9JJZNnrOh6t8g+AQaJljF2Or8sDrzgraLlgMGx83xIEmBXeEq0tNmwAqyEi6U4AbJzWaHsAMeIlkGuZb50gocls1yxfVwTOcmcbJbwGWbSfy9aQqLCxuyFZ2EvidZZhAEyhEPwGXwlejG+G5g+8Lzkhhg3POIK0ATlCtA+Xgi2aSHcAXvCZXBOcDwUs8ZViCZvajIb+0Z0OnMXGIVu8EQgX8eFAd6GnYO/m8M7ou1jED5kh5gkPOIKkAGFBRUnQANz4e+4drx/MevfRdGL5IeMviOdsEM4yzjbOOs4+5ISttlZKjrYWNp9YYiX4W6JHx5xBcilJyyoJAF6Y9Y/dkwSuEviGsfttn2BxcSM9rD12gUHApcJ7rLLck9FwhWgKyjX8aLCCyvWLUL2LOTFJimfLJfc/dpbaFe5csHwNorOvB7wtIRvbHxwBci9A/cQdptMgNyNlgRz//cCtrHOJYXh8bYk7gaGncTOsgNkpWDFYOWojOzwzO9zyYgboitA9h37kJMhm1miy1PBHWQSuMvh0wVeUJT1LgrZtxADxT9I3o/uFP2Mgbvia6I748puaRgenyFyR2f/ZtwQGeBr2NY6zu9fK7m3Wvz94/CI5N9bJ2ao6Ej6KZlHVHz+OT37TUWGJZGzgTN+hPjdC7KD+X5+jm27B29KfgeGwWe88yU/PAN3tmtEHx4XgrOfbeAzYdNX30WDnJ31PgZ3RvQRGB+j7YM3xK+t/xX8v61y8V8XOJL5CGqC6MzxCf5fwbbx1odt5b/Vua0pKSkpKSkpKVXLHzqwvaeSeIB4AAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAAYCAYAAABDX1s+AAACVElEQVR4Xu2XzUsVURiHX0kh0sQKFfsyBFtEi3SjKBJUZBDWIpchIgguIiGScCe1UCJ0IX7QrmjRqsClZNAqQqtFtAhqJ7Ro439Qv5/vnDszx/m4o8PciTsPPNyZc85c57y+5z3nihQUpMUpOA1nYR+s8XdXFyfhQ3gYdsAP8I5vRJUxCH/Ai849M+U1PFIaUWXUwx5Y59w/gS9EM6YSHIXj8Cl8AFv93bEcgrfhWbtjP5yG7+ANuyMjzsB1eFf0H3JNdAl3ewcFwLHM9MdwC/6El3wj9gEzhF94SypTVGvhM/jcuTZwCb+S6Iw1wesXrYcHDgiDMQkHnHsWV+9LZcE5+AXes9pvSrIJ8vnI8VyTjB6XA+HndXHXJrNhTDTl2NYJ7zvtWXIZ/pG9AeF7/YXDVnsYkQFpEC1OU3BTtGDOiT70HraLptlv0T9qZLZkjZl4WEDs9jAiA3IFjohuqdxaF2CT6Lb6DZ53hyaGO8CnBLIOHNt9MhhOJGjiqQZkVDQYXIfbsFd0KXDJXHWu88KEBE881YAYuFQ24Am7I0eETTysPYzYgLCovoGLkm5GNIgW4XJtFj00hcHsZRbbEzcBYZaXQ2xAWCdYL1hL0uQCHEogd7qos0Qb/CiazV743na9a4HHPfdeYgPirR95htn7CK7BRqeN56NVuCTuuYjHgq+iuyZ3SRsG5BfssjsMPLnxOBwW0TzBQLyEK6IZNQ/fiv4iN/Ca8+FOaQLHH6LL8Lu4R4cd+BnOOGNKME253v8XWGeY7lxm/IyqOwUFBQUFleIf24ByBeZQ94cAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAAYCAYAAACyVACzAAADR0lEQVR4Xu2Xy6tNURzHv0LJKynvcBVKyCtCZCLkMcLIY6YM1I1IiolHIW/Joww8QuSRRyHPIgwoxEAGN5mZKH8A36/fXnevs/Ze5+5zzr0U+1ufzr1rrbP3Wt/1W7/fOkCpUqVKlfovNIu8IT/Iz4QP5G3S9olsJ73cF/6wupGlZC/ZSkZVdleV5rwG9t0NZEBlN4bBnj2EdIa9axxZlfwd1T7ylUwP2ifAjLtAegZ9Ha3e5CLZDHv3ePKILPYHRTSU3CcrYQufS56Syd6YaaQFaZCIz2SeNyYj7cA18pz0D/o0ySvkG5kT9NWrrqR72JijdeQO6eO1LSOPkZ2nry6wzT+V/O20hZxHGjUTYeY/IffIJmSjL6PR5D2yD5c0UU04L+pqlTZlPbkJ29Vqcu89HLRPgqWGBUG7ryZYapHZvhbBIkcmSfrcmXYXk16s/LQ27KCmwkJVC9SxqEfarV3kMswk5Ye25DYwNEsL1IIVJTHpBOgkhGbNhx01RadUl1k7kB85MucSeQfb0Vo1nOwn58hY0qmyu6qcKTGzwnZfzpSYWa5dzzpNjpBn5BXZiCrJ3eWkFnIUVjmEJvOaHIRVi1qkinUyoZbq5cstLDSliFkyo6hZt8iI5P++5DZs/cqrGblwV9VRBdGRcUQdzpGiRtGjKFI0KaoakaqXUkNoShGzlE6KmJVXaJphgaP0k5HLVxrUiPrBctIhFKgoBRQzJdbuKzSlrXZfLirz8vfvfNVe1wI/urSYeo+g1ASraKEpzqxqm6vcqxwcmuLMUlXUkVO1fQDbaKfYEW69X70gg4K+RiWjdBWpJ7lLLpeeQWU60KZ+ST6dVIgGIn2H1qI1KRB8rYalHKUeRf9LZM3SJuikZa4mY8hHZCfUnvKvDVNQm2nLYRXK5T99V7d5/xqjCNFNvQVpnskbp/x0ghyD3SXFHticnDT2KuwG0HpNmgFz9TvSa75+D65wAzpAWtQ2WCTPRrG7lha4G2b0QpgBD2E/e5wUgWdhP2VUoJy0WLUfhxWLA+Q6GeyN0XjNR/PS2u+SG8GYv6oesB+3yhtFpCgZSZaQmYiU9Ii0Icpx+q4+8zZIz9NzNUbHM29MqVKlSpX61/QLOKaq5QYmDFcAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAACu0lEQVR4Xu2Xy6tOURjGH6HkFsotuRUKCYkQMVDkVsKIIaWcyEiKCSmJkFJM5JJrGSgphQzccinEQAYnmZkofwDP492rs/b77f219/4+Z7R+9eucs9b37b3Wu971rnWARCKRSNRmBX1Pf9M/mZ/ph6ztKz1KR4Qv9DND6FZ6kh6mM/Pdpcyhm+lYOoAOp8votvhDRZyiP+hS1z4fFpQbsIf1JyPpTXoQ9u559AndGH+ohC3oW9jga9gzStFq36PP6TjXpwHcpT/pKtfXlMF0qG8soIc+oKOiNq3oU7SO07MWNh95n+5GhayeRT/RS3SQ69MgNJiibKmLBnIANrAlrs8T3nvOtS+Ebdd1rt2jQCiQtdBDVQ/2+A6ymPbCBq9UbcJ4epzegQVgYL67kLA4PhAL6Dd6yLV7GgXiGIpXXBO/RT/CVqIuU+lpeo3OhRWtqoQJlwXCt3sUCH3mOmx7vKA70WYRQg3opedh1VnqIe/oGTopfLgiquwXM6tWeY8mogLnJ1wnELfp6Ozv6fQN3YuSBQkpqOo8GZbGQR1dVdHDtepafWWBsqET1sC2q59w1UBo7PH4NT4ttIJROLZQH/b7jprovFYNOAsLYqeUTbisvQr6juaqILeg+tCtozHOCr206bYQ02AXPT/hEIh2CzeDvqWXkc8KPUvbTdsmR7g/vKQTXV+nKAg6jpsUShFq1xXkJ6MF+579DKioT0DfO0Kw4kCEraF29eeYTb+g9WXdJD46F6FeQLbDboNhT+u7umXGR/kY+ghW7HXUC/Vp0lOyv4V+1+mhg0AXun/ozv2K/kL+/4sd4QP/AQ34CCwDV6LNMRahAZ+ABXE9LAiPkb8mK3Ou0mewYh/Qcf+Q7qO7YFl/Ac3vQl1nGOy6u8F3lKAs0J7fRJcjWs0K6F2rYUFURtTJxkQikUiIv7dRhQBubzMIAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAADdUlEQVR4Xu2Yy6tNURzHf0LJKxFCukdKkbxKeZWSUEw8ZoqpECmSDFyPkZQkAxKhEHlEBl4DA69EIQaiblIGJsofwO/jt3/O3uvstc927rnHUedb39y71l7r/tb391qLSAcddNAiDFcODAfbANiEbS3BMuU+aV8hDihXhhN5WKR8pfyh/JnwnfJ1MvZBbLNhviCFGcorytHJ79OUjyS711flC7F9+PmGcoGyX7IGbFQ+L8n7Yn+nLEYqzyvnhBMxHFF+Uc4LxmeKiXJROTQ1Pkh5Rrk6NeaYrfykPBaMs4a/g1BbpCrGVuU15aTUGGsR0r2Jd4k+nLQ0GSuLJVJrfy7w9nXlY+WYYI7FV5XflItT42x+T2q/B7OUH6VWCFARi0CipCsZQ5z03sCFWB6M78kZqwfqxE3Jd1oGU5RvlaeUA4K5Eco7ko0WvHZUedA/ClAkxFjlM7F5vgN7xQRKIyYEEbIhGCsDBMw7XwYrxMJ1UzihmKvsUd6SagUepXwo8SJUJMR8sf08VAcru6VaZxwxIYgcasrfgnTCAePDiTTwbF594OCXlW/E8t7BQSlc7tEQLsRJsQhwkk5PlaeT34sQE6JRYBPpmD5HBl4DepTHlYcTYshLsRSY4B8nwDjyvBKMO1yIJ1LdDyIMVX+tWOEsQrOF8JSM7uf14ZJyomQ9GDOWzdg05tWi1KCNvVfelvh6UEaIcWLdBodVslM1cCHWhRMOrw/bw4kC9EYIQCpyyJ3hRAplhADUjDKt0YXIq4O/gVFha6yH3grBvYFDxuZBWSFwIB2hHgpTw+8PFDDCrCwoqoTj9HAiQZEQtK8T0pyIIHXPikU1B6UNb5P8FlkRszn3MjZVLF/PSbwe5IG6wqaxKIoJ0V+5XuyqzWWsqJW5ELEWDVhPW1+oXKPcLJYmtOQQdAsujNj+B/RywuS7VN8EXF0xsgy804QXG94AD8QO6vt+Fmu1CMffQ3g8l/d2QVi+ZY2vd9vy3hh8z9wOMUfCWK2gSGJzbL5hENZ1b2p9DGrNfjGHEAmxJ7enY1EqNgweSHfF0utfIKwPtNHJYqKEzsFWUoh/+wS0om7JPqlbBR57/BdAl9hT+4Jyt1jap4FtuyT72m06eBofUq4KJ1oADpUuitiSVyQRhhSOpU3TMETME5VgvB3AlYA7Rp+L8F/jF2tSx+4UE9OzAAAAAElFTkSuQmCC>