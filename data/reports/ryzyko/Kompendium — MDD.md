[Strona główna](../../../00_indeks.md) > [ryzyko](00_indeks.md) > [Kompendium — MDD](Kompendium — MDD.md)

---

# **Architektura genomowa zaburzeń depresyjnych: Kompleksowe mapowanie genów na potrzeby obliczania ryzyka poligenicznego i stratyfikacji biotypów**

Ewolucja zrozumienia genetycznego podłoża epizodów depresji o dużym nasileniu (Major Depressive Disorder \- MDD) przeszła w ostatnich latach fundamentalną transformację, odchodząc od uproszczonych modeli opartych na pojedynczych genach kandydatach w stronę zaawansowanych badań asocjacyjnych całego genomu (GWAS) o zasięgu globalnym.1 MDD jest obecnie definiowane jako zaburzenie o skrajnej poligeniczności, w którym tysiące wariantów genetycznych o małym efekcie jednostkowym kumulują się, tworząc ogólną podatność biologiczną jednostki.3 Najnowsze dane pochodzące z konsorcjum Psychiatric Genomics Consortium (PGC) MDD2025, obejmujące analizę ponad pięciu milionów osób, zidentyfikowały 697 niezależnych asocjacji w 636 loci genetycznych, co stanowi kamień milowy w mapowaniu biologicznych fundamentów depresji.1 Niniejszy raport dostarcza szczegółowej analizy tych markerów, kategoryzując je pod kątem przydatności w obliczaniu poligenicznych wskaźników ryzyka (Polygenic Risk Scores \- PRS) oraz stratyfikacji pacjentów na konkretne biotypy, co jest niezbędne dla rozwoju psychiatrii precyzyjnej.

## **Krajobraz genetyczny MDD w świetle najnowszych badań trans-ancestralnych**

Najbardziej aktualne dowody naukowe wskazują, że MDD charakteryzuje się odziedziczalnością na poziomie 30-50%, mierzoną w badaniach bliźniąt, z czego istotna część przypisana jest wspólnym wariantom genetycznym o charakterze SNP (Single Nucleotide Polymorphisms).2 Przełomowe badanie PGC MDD2025, kierowane przez Marka Adamsa i zespół badawczy z Uniwersytetu w Edynburgu, zintegrowało dane z 29 krajów, obejmując zróżnicowane populacje, co pozwoliło na identyfikację 308 genów o wysokim stopniu pewności (high-confidence genes).1

Asocjacje te nie są rozłożone losowo w genomie, lecz wykazują wyraźne wzbogacenie w regionach kodujących białka gęstości postsynaptycznej oraz mechanizmy klastrowania receptorów.1 Analizy na poziomie pojedynczych komórek (single-cell RNA sequencing) wykazały, że sygnał genetyczny MDD jest szczególnie silny w neuronach pobudzeniowych i hamujących w obrębie przodomózgowia i śródmózgowia, a także w neuronach peptydergicznych i neuronach kolczystych (medium spiny neurons).1 To precyzyjne umiejscowienie sygnału genetycznego pozwala na powiązanie ryzyka genomowego z konkretnymi obwodami neuronalnymi odpowiedzialnymi za regulację nastroju, nagrody i funkcji poznawczych.

### **Kluczowe parametry statystyczne i wydajność PRS**

Obliczanie ryzyka poligenicznego opiera się na sumowaniu efektów poszczególnych alleli ryzyka, ważonych przez ich siłę asocjacji (iloraz szans \- OR lub współczynnik beta) uzyskaną w badaniach GWAS.7

| Parametr statystyczny | Wartość/Opis w PGC MDD2025 | Implikacje kliniczne |
| :---- | :---- | :---- |
| Liczba niezależnych loci | 636 loci (697 asocjacji) | Wskazuje na ogromną złożoność i wielość ścieżek biologicznych.1 |
| Liczba genów "high-confidence" | 308 genów | Cele dla nowych farmakoterapii i precyzyjnej diagnostyki.1 |
| Wariancja wyjaśniana (Liability ![][image1]) | 5,7% \- 5,8% w próbkach europejskich | Poprawa z \<2% w poprzednich latach; rosnąca moc predykcyjna.1 |
| Liczba nowych loci (2025) | 293 nowo zidentyfikowane loci | Rozszerzenie mapy genetycznej o wcześniej nieznane mechanizmy.1 |

Analiza sugeruje, że PRS wytrenowane na danych trans-ancestralnych wykazują lepszą przenaszalność między różnymi grupami etnicznymi, co jest kluczowe dla globalnego zastosowania narzędzi diagnostycznych.1

## **Klasyfikacja genów dla potrzeb stratyfikacji biotypów**

Współczesna psychiatria dąży do zastąpienia opisowej diagnozy opartej na objawach (DSM-5) obiektywnymi biotypami, które odzwierciedlają specyficzne dysfunkcje molekularne.10 Poniżej przedstawiono kompleksowe listy genów podzielone na cztery główne biotypy, przygotowane do integracji z algorytmami analizy genomowej.

### **Biotyp 1: Zapalny i Immunometaboliczny**

Biotyp zapalny dotyczy około 25-30% pacjentów z MDD i charakteryzuje się podwyższonym poziomem markerów stanu zapalnego, takich jak białko C-reaktywne (CRP) oraz cytokiny prozapalne (IL-6, TNF\-![][image2]).11 Pacjenci ci często prezentują objawy neurowegetatywne, takie jak zmęczenie, zaburzenia apetytu i spowolnienie psychomotoryczne, oraz wykazują oporność na standardowe leki z grupy SSRI.12

Genetyczna składowa tego biotypu obejmuje warianty regulujące odpowiedź immunologiczną oraz szlak kynureninowy, który pod wpływem cytokin przekierowuje metabolizm tryptofanu z produkcji serotoniny na produkcję neurotoksycznych metabolitów, takich jak kwas chinolinowy.15

| Gen | Rola w biotypie zapalnym | Kluczowe asocjacje/SNP |
| :---- | :---- | :---- |
| **CRP** | Koduje białko C-reaktywne; marker ogólnoustrojowego zapalenia | rs1205, rs1130864; PRS dla CRP koreluje z BMI i opornością na leczenie.12 |
| **IL6** | Cytokina prozapalna; wpływa na funkcje mózgu i barierę krew-mózg | rs2066992 (wariant T wiąże się z lepszą odpowiedzią na duloksetynę).13 |
| **TNFA** | Czynnik martwicy nowotworu; aktywuje mikroglej i stres oksydacyjny | Podwyższone poziomy korelują z brakiem odpowiedzi na escitalopram.14 |
| **IDO1 / TDO2** | Enzymy szlaku kynureninowego; wyzwalają kaskadę neurotoksyczną | rs35059413 (IDO1), rs3755908 (TDO2); kluczowe dla immunometabolicznego MDD.20 |
| **KMO** | Monooksygenaza kynureninowa; produkuje neurotoksyczne 3-HK | rs1053230; zmiany w ekspresji wiążą się z zaburzeniami poznawczymi w MDD.20 |
| **C4A / C1R** | Elementy układu dopełniacza; zaangażowane w eliminację synaps | Zwiększona liczba kopii C4A jest czynnikiem ryzyka zaburzeń afektywnych i psychoz.23 |
| **BCL11B** | Regulator różnicowania komórek T i funkcji prążkowia | Powiązany z procesami autoimmunologicznymi i dojrzewaniem neuronalnym.24 |

Analiza tych genów pozwala na identyfikację pacjentów, którzy mogą odnieść korzyść z augmentacji leczenia przeciwdepresyjnego lekami przeciwzapalnymi lub interwencji metabolicznych.11

### **Biotyp 2: Poznawczy (Cognitive Biotype)**

Biotyp poznawczy obejmuje około 27% pacjentów i charakteryzuje się deficytami w zakresie funkcji wykonawczych, uwagi i szybkości przetwarzania informacji.25 Deficyty te wynikają z dysfunkcji obwodów kontroli poznawczej, obejmujących grzbietowo-boczną korę przedczołową (dlPFC) i grzbietową część przedniego zakrętu obręczy (dACC).25

Genetyczne podłoże tego biotypu jest silnie powiązane z genami neurorozwojowymi oraz transporterami wpływającymi na homeostazę neuronalną.

| Gen | Mechanizm wpływu na funkcje poznawcze | Implikacje dla analizy |
| :---- | :---- | :---- |
| **ABCB1 (MDR1)** | Transporter glikoproteiny P; chroni mózg przed toksynami i wpływa na transport leków | rs1109866 i rs1109867 modyfikują nasilenie depresji poprzez wpływ na funkcje wykonawcze.27 |
| **ABCB6** | Udział w transporcie metabolicznym w OUN | rs3731885 skorelowany z wynikami testu Wież Hanoi (planowanie).27 |
| **COMT** | Degradacja dopaminy w korze przedczołowej | Val158Met (rs4680) wpływa na elastyczność poznawczą i wydajność pamięci operacyjnej.28 |
| **NEGR1** | Adhezja komórek neuronalnych; zaangażowany we wzrost neurytów | Wspólny czynnik ryzyka dla MDD, inteligencji i osiągnięć edukacyjnych.6 |
| **DCC** | Receptor naprowadzania aksonów; kluczowy dla plastyczności korowej | Wysoki wpływ na architekturę połączeń w obrębie sieci kontroli poznawczej.1 |
| **POU3F2** | Czynnik transkrypcyjny regulujący różnicowanie neuronów | Marker wysokiego ryzyka dla deficytów neurorozwojowych w MDD.1 |

Identyfikacja biotypu poznawczego za pomocą PRS pozwala na wczesne wdrożenie leków prokognitywnych, takich jak guanfacyna, które celują w specyficzne receptory w korze przedczołowej.25

### **Biotyp 3: Lękowy i Dysregulacji Osi HPA (Anxious Biotype)**

Biotyp ten charakteryzuje się nadreaktywnością na stres, wysokim poziomem lęku oraz nieprawidłową odpowiedzią osi podwzgórze-przysadka-nadnercza (HPA).3 Jest on silnie związany z interakcją gen-środowisko, gdzie predyspozycje genetyczne są aktywowane przez traumy z dzieciństwa (ACEs \- Adverse Childhood Experiences).32

Kluczowe geny tego biotypu regulują sprzężenie zwrotne receptora glikokortykoidowego (GR).

| Gen | Funkcja w osi HPA | Kluczowe warianty (rsID) |
| :---- | :---- | :---- |
| **FKBP5** | Ko-chaperon regulujący wrażliwość GR; kluczowy dla zakończenia odpowiedzi stresowej | rs1360780, rs3800373, rs9470080; rs1360780 wiąże się z MDD po traumie poprzez zmiany epigenetyczne.31 |
| **CRHR1** | Receptor czynnika uwalniającego kortykotropinę typu 1 | rs7209436, rs110402, rs242924; warianty te determinują szczytowe wydzielanie kortyzolu w stresie.31 |
| **NR3C1 (GR)** | Receptor glikokortykoidowy; główny element hamowania osi HPA | rs41423247 (BclI), rs6198; modyfikują podatność na zaburzenia lękowe i afektywne.31 |
| **NR3C2 (MR)** | Receptor mineralokortykoidowy; kontroluje bazowy poziom kortyzolu | rs5522; wpływ na stabilność nastroju i reaktywność emocjonalną.35 |
| **SLC6A4** | Transporter serotoniny; moduluje reaktywność ciała migdałowatego | Polimorfizm 5-HTTLPR (S vs L); allel S zwiększa wrażliwość na negatywne bodźce środowiskowe.28 |

W tym biotypie mechanizmy epigenetyczne, takie jak demetylacja *FKBP5*, działają jako molekularna pamięć stresu, co może być wykorzystane do oceny ryzyka nawrotów depresji.33

### **Biotyp 4: Melancholiczny i Somatogenny (Factor F1/F2)**

Najnowsze analizy symptomatyczne oparte na metodzie BIONIC wyodrębniły dwa genetyczne wymiary MDD: czynnik F1 (psychiatryczny/neurorozwojowy) i czynnik F2 (kardiometaboliczny/somatyczny).37 Biotyp melancholiczny wykazuje silne powiązanie z czynnikiem F2, obejmującym zaburzenia rytmu dobowego, anhedonię i podatność metaboliczną.37

| Gen | Obszar wpływu | Znaczenie biologiczne |
| :---- | :---- | :---- |
| **FTO** | Regulacja masy ciała i metabolizmu | Silna korelacja genetyczna między depresją melancholiczną a otyłością i cukrzycą typu 2\.28 |
| **RORB / MEIS1** | Regulacja rytmów dobowych i snu | Wspólne podłoże genetyczne MDD i bezsenności.30 |
| **DRD2** | Receptor dopaminy D2; kluczowy dla systemu nagrody | Związany z anhedonią i obniżoną zdolnością do odczuwania przyjemności (kluczowy objaw melancholii).37 |
| **SLC6A3 (DAT)** | Transporter dopaminy | Wpływa na napęd psychomotoryczny; zmiany w tym genie korelują ze spowolnieniem ruchowym.40 |
| **MC4R** | Receptor melanokortyny 4; kontrola apetytu | Genetyczne powiązanie z nietypowymi objawami depresji (hiperfagia).37 |

Zrozumienie składowej metabolicznej w biotypie melancholicznym pozwala na lepsze zarządzanie chorobami współistniejącymi, które często pogarszają rokowanie w MDD.37

## **Techniczne aspekty obliczania prawdopodobieństwa biotypów w analizie kodu genetycznego**

Aby program analizujący dane genetyczne mógł skutecznie wskazać prawdopodobieństwo występowania każdego z biotypów, musi on operować na znormalizowanych wagach pochodzących z odpowiednich baz GWAS oraz stosować rygorystyczną kontrolę jakości (Quality Control \- QC).

### **Algorytm obliczeniowy i formuła PRS**

Standardowy model addytywny PRS obliczany jest według wzoru:

![][image3]  
gdzie:

* ![][image4] to wynik ryzyka poligenicznego dla osoby ![][image5].7  
* ![][image6] to logarytm ilorazu szans (log-OR) dla allelu efektu wariantu ![][image7] pobrany z bazy PGC MDD2025.7  
* ![][image8] to dawka allelu ryzyka (0, 1 lub 2\) u danej osoby.7  
* ![][image9] to liczba markerów SNP uwzględnionych w modelu po procesie "clumpingu".41

### **Standardowy format danych wejściowych (Base File)**

Programy takie jak PRSice-2 wymagają pliku bazy (Base File) o określonej strukturze kolumnowej, aby poprawnie dopasować dane sumaryczne do danych genotypowych pacjenta.41

| Nazwa kolumny | Wymaganie | Opis |
| :---- | :---- | :---- |
| **SNP** | Obowiązkowe | Identyfikator rsID wariantu (np. rs1360780).7 |
| **CHR** | Obowiązkowe | Numer chromosomu (1-22, X, Y).41 |
| **BP** | Obowiązkowe | Pozycja wariantu w parach zasad (build hg19 lub hg38).41 |
| **A1** | Obowiązkowe | Allel efektu (ten, dla którego podano wagę STAT).41 |
| **A2** | Zalecane | Allel referencyjny (nie-efektu).41 |
| **OR / BETA** | Obowiązkowe | Waga wariantu (Iloraz szans lub współczynnik Beta).41 |
| **P** | Obowiązkowe | Wartość p asocjacji; służy do filtrowania progów istotności.41 |
| **INFO** | Zalecane | Jakość imputacji (zalecane \> 0.8).43 |
| **MAF** | Zalecane | Częstość rzadszego allelu (zalecane \> 0.01).43 |

### **Parametry filtracji dla MDD**

Badania wykazują, że dla MDD optymalna moc predykcyjna PRS jest osiągana nie tylko przy progach rygorystycznych (![][image10]), ale często przy szerszych progach, takich jak ![][image11] lub nawet ![][image12], co wynika z faktu, że wiele wariantów o znaczeniu biologicznym nie osiąga poziomu istotności całogenomowej w pojedynczych badaniach.41

## **Farmakogenetyka i markery odpowiedzi na leczenie**

Integralną częścią raportu dla programu analizującego kod genetyczny musi być moduł farmakogenetyczny (PGx), który ocenia zdolność pacjenta do metabolizowania leków oraz ryzyko wystąpienia działań niepożądanych.19

### **Układ Cytochromu P450**

Warianty w genach CYP determinują, czy pacjent jest wolnym (Poor), pośrednim (Intermediate), czy ultraszybkim (Ultrarapid) metabolizerem danego leku.19

| Gen | Znaczenie kliniczne w MDD | Rekomendacje |
| :---- | :---- | :---- |
| **CYP2D6** | Metabolizuje fluoksetynę, paroksetynę, wenlafaksynę, trójpierścieniowe leki przeciwdepresyjne (TCA) | Wolni metabolizerzy mają wysokie ryzyko toksyczności; ultraszybcy \- braku skuteczności.19 |
| **CYP2C19** | Metabolizuje escitalopram, citalopram, sertralinę | Konieczna korekta dawki u wolnych metabolizerów (często spotykane w populacjach azjatyckich).19 |
| **CYP2B6** | Metabolizuje bupropion i mirtazapinę | Genotyp 6/6 wiąże się ze zwiększoną ekspozycją na lek i lepszą odpowiedzią kliniczną.19 |
| **CYP3A4 / 1A2** | Metabolizm amitryptyliny i nortryptyliny | Wpływa na tempo eliminacji leków starszej generacji.19 |

### **Pozostałe markery farmakodynamiczne**

Oprócz metabolizmu, geny receptorów i transporterów determinują bezpośrednią reakcję tkanki nerwowej na lek.40

* **HTR2A (rs6311, rs6313)**: Polimorfizmy w genie receptora serotoninowego 2A korelują z ryzykiem wystąpienia działań niepożądanych (np. nudności) oraz ogólną odpowiedzią na SSRI.29  
* **ABCB1 (rs2032582)**: Wpływa na aktywność pompy usuwającej leki z mózgu; warianty te mogą decydować o lekooporności poprzez ograniczanie stężenia antydepresantu w synapsach.27  
* **BDNF (rs6265)**: Wariant Val66Met wpływa na plastyczność neuronalną indukowaną przez leki; nosiciele allelu Met mogą wykazywać opóźnioną lub słabszą reakcję na terapię.28

## **Podsumowanie i rekomendacje dla implementacji**

Opracowanie pełnej listy genów związanych z MDD oraz ich wykorzystanie do obliczania prawdopodobieństwa biotypów wymaga zintegrowanego podejścia, łączącego najnowsze dane z GWAS (PGC 2025\) z głęboką wiedzą o szlakach biologicznych.1

### **Kluczowe wnioski dla algorytmów analizy danych:**

1. **Zastosowanie wag z PGC MDD2025**: Jest to obecnie najpotężniejszy zestaw danych sumarycznych, który maksymalizuje wariancję wyjaśnianą w PRS (do \~6%).1  
2. **Partycjonowanie PRS (Pathway-specific PRS)**: Zamiast jednego ogólnego wskaźnika, program powinien generować cztery sub-wskaźniki odpowiadające biotypom: zapalnemu, poznawczemu, lękowemu i melancholicznemu.12  
3. **Integracja z markerami HPA i zapalenia**: Wykorzystanie specyficznych wariantów w genach *FKBP5*, *CRP* i *IDO1* pozwala na przejście od oceny "ryzyka zachorowania" do "charakterystyki biologicznej" depresji u danego pacjenta.12  
4. **Uwzględnienie interakcji ze środowiskiem**: Algorytm powinien uwzględniać status ACEs (traumy z dzieciństwa) jako moderatora wpływu PRS dla biotypu lękowego.32  
5. **Walidacja farmakogenetyczna**: Każdy raport genomowy musi zawierać status metabolizera CYP2D6/CYP2C19, aby zapewnić bezpieczeństwo i skuteczność dobranej farmakoterapii.19

Prezentowane podejście pozwala na stworzenie narzędzia diagnostycznego, które nie tylko identyfikuje osoby zagrożone MDD, ale przede wszystkim wskazuje na najbardziej prawdopodobną ścieżkę patofizjologiczną u konkretnego pacjenta. Umożliwia to przejście od metody "prób i błędów" w leczeniu depresji do psychiatrii precyzyjnej, w której dobór leku (np. przeciwzapalny vs prokognitywny vs standardowy SSRI) jest podyktowany indywidualnym profilem genetycznym biotypu.11

#### **Cytowane prace**

1. PGC MDD2025 \- University of Edinburgh Research Explorer, otwierano: maja 12, 2026, [https://www.research.ed.ac.uk/en/datasets/pgc-mdd2025/](https://www.research.ed.ac.uk/en/datasets/pgc-mdd2025/)  
2. MDD Working Group – PGC \- Psychiatric Genomics Consortium, otwierano: maja 12, 2026, [https://pgc.unc.edu/for-researchers/working-groups/mdd/](https://pgc.unc.edu/for-researchers/working-groups/mdd/)  
3. Genetic and epigenetic factors associated with depression: An updated overview \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9232544/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9232544/)  
4. Precision Psychiatry: Biomarker-Guided Tailored Therapy for Effective Treatment and Prevention in Major Depression \- MRCT Center, otwierano: maja 12, 2026, [https://mrctcenter.org/wp-content/uploads/2024/10/Jones-2021-Precision-Psychiatry\_-Biomarker-Gui.pdf](https://mrctcenter.org/wp-content/uploads/2024/10/Jones-2021-Precision-Psychiatry_-Biomarker-Gui.pdf)  
5. Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies \- WashU Research Profiles, otwierano: maja 12, 2026, [https://profiles.wustl.edu/en/publications/trans-ancestry-genome-wide-study-of-depression-identifies-697-ass/](https://profiles.wustl.edu/en/publications/trans-ancestry-genome-wide-study-of-depression-identifies-697-ass/)  
6. Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies \- University of Bristol Research Portal, otwierano: maja 12, 2026, [https://research-information.bris.ac.uk/en/publications/trans-ancestry-genome-wide-study-of-depression-identifies-697-ass/](https://research-information.bris.ac.uk/en/publications/trans-ancestry-genome-wide-study-of-depression-identifies-697-ass/)  
7. Calculating Polygenic Risk Scores (PRS) in UK Biobank: A Practical Guide for Epidemiologists \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.818574/full](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.818574/full)  
8. A guide to performing Polygenic Risk Score analyses \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7612115/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7612115/)  
9. Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies. \- Oxford Global Health, otwierano: maja 12, 2026, [https://www.globalhealth.ox.ac.uk/publication/2084955](https://www.globalhealth.ox.ac.uk/publication/2084955)  
10. Two Distinct Biotypes in Major Depression Unveiled \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12065012/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12065012/)  
11. Inflamed brain: Targeting immune changes and inflammation for treatment of depression \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8683253/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8683253/)  
12. Genetic inflammatory signature defines depression subtypes and treatment response, otwierano: maja 12, 2026, [https://www.news-medical.net/news/20251021/Genetic-inflammatory-signature-defines-depression-subtypes-and-treatment-response.aspx](https://www.news-medical.net/news/20251021/Genetic-inflammatory-signature-defines-depression-subtypes-and-treatment-response.aspx)  
13. Inflammatory biomarkers in depression: scoping review \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11536280/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11536280/)  
14. Inflammatory and Immune Biomarkers in Mood Disorders: From Mechanistic Pathways to Clinical Translation \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12524191/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12524191/)  
15. The Kynurenine Pathway: A Finger in Every Pie \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6790159/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6790159/)  
16. The Monoamine–Glutamate Continuum of Depression: A Neurobiological Framework for Precision Psychiatry \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/404165793\_The\_Monoamine-Glutamate\_Continuum\_of\_Depression\_A\_Neurobiological\_Framework\_for\_Precision\_Psychiatry](https://www.researchgate.net/publication/404165793_The_Monoamine-Glutamate_Continuum_of_Depression_A_Neurobiological_Framework_for_Precision_Psychiatry)  
17. The kynurenine pathway in major depressive disorder \- University of Wollongong Research Online, otwierano: maja 12, 2026, [https://ro.uow.edu.au/ndownloader/files/52456316/1](https://ro.uow.edu.au/ndownloader/files/52456316/1)  
18. The Central Role of Cytokines in PTSD and Major Depressive Disorder: Mechanisms and Clinical Implications \- SCIEPublish, otwierano: maja 12, 2026, [https://www.sciepublish.com/article/pii/672](https://www.sciepublish.com/article/pii/672)  
19. Pharmacogenetics and the Response to Antidepressants in Major Depressive Disorder, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12472883/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12472883/)  
20. (PDF) Gene Variant Frequencies of IDO1, IDO2, TDO, and KMO in Substance Use Disorder Cohorts \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/385366077\_Gene\_Variant\_Frequencies\_of\_IDO1\_IDO2\_TDO\_and\_KMO\_in\_Substance\_Use\_Disorder\_Cohorts](https://www.researchgate.net/publication/385366077_Gene_Variant_Frequencies_of_IDO1_IDO2_TDO_and_KMO_in_Substance_Use_Disorder_Cohorts)  
21. Gene Variant Frequencies of IDO1, IDO2, TDO, and KMO in Substance Use Disorder Cohorts \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11594152/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11594152/)  
22. The kynurenine pathway in major depressive disorder, bipolar disorder, and schizophrenia: a systematic review and meta-analysis of cerebrospinal fluid studies \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10668321/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10668321/)  
23. Transcriptome Analysis of Post-Mortem Brain Tissue Reveals Up-Regulation of the Complement Cascade in a Subgroup of Schizophreni \- Diva-Portal.org, otwierano: maja 12, 2026, [https://www.diva-portal.org/smash/get/diva2:922690/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:922690/FULLTEXT01.pdf)  
24. L Fahey et al 2018 \- University of Galway, otwierano: maja 12, 2026, [https://www.universityofgalway.ie/media/schoolofpsychology/images/irelatemanuscripts/Jess-Holland-preprint-ALSPAC\_SPPE.docx](https://www.universityofgalway.ie/media/schoolofpsychology/images/irelatemanuscripts/Jess-Holland-preprint-ALSPAC_SPPE.docx)  
25. Leanne Williams \- Stanford Profiles, otwierano: maja 12, 2026, [https://profiles.stanford.edu/leanne-williams](https://profiles.stanford.edu/leanne-williams)  
26. Leonardo TOZZI | MD., Ph.D. | Research profile \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/profile/Leonardo-Tozzi](https://www.researchgate.net/profile/Leonardo-Tozzi)  
27. Interactions between ABC gene polymorphisms and processing speed in predicting depression severity \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11800503/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11800503/)  
28. The Genetic Mosaic of Depression: Linking Polymorphisms to Neuroplasticity and Stress Regulation \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12944579/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12944579/)  
29. Pharmacogenetics of antidepressant drugs: current clinical practice and future directions, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12046622/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12046622/)  
30. Blood transcriptomic analysis reveals a distinct molecular subtype of treatment resistant depression compared to non-treatment resistant depression | Request PDF \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/395372664\_Blood\_transcriptomic\_analysis\_reveals\_a\_distinct\_molecular\_subtype\_of\_treatment\_resistant\_depression\_compared\_to\_non-treatment\_resistant\_depression](https://www.researchgate.net/publication/395372664_Blood_transcriptomic_analysis_reveals_a_distinct_molecular_subtype_of_treatment_resistant_depression_compared_to_non-treatment_resistant_depression)  
31. Genetic Association of FKBP5 and CRHR1 with Cortisol Response to Acute Psychosocial Stress in Healthy Adults \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3628278/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3628278/)  
32. Biotypes of deeply phenotyped depressed patients reflect signatures of adverse childhood experience and depressive cognitive biases | medRxiv, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.1101/2025.07.03.25330801v1.full-text](https://www.medrxiv.org/content/10.1101/2025.07.03.25330801v1.full-text)  
33. View of FKBP5 Gene Variants as Predictors for Antidepressant Response in Individuals with Major Depressive Disorder Who Have Experienced Childhood Trauma. A Systematic Review, otwierano: maja 12, 2026, [https://ijms.info/IJMS/article/view/437/659](https://ijms.info/IJMS/article/view/437/659)  
34. Role of FKBP5 and its genetic mutations in stress-induced psychiatric disorders: an opportunity for drug discovery \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1182345/full](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1182345/full)  
35. HPA Axis in Major Depression: Cortisol, Clinical Symptomatology, and Genetic Variation Predict Cognition \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5313380/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5313380/)  
36. Genetics Factors in Major Depression Disease \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6065213/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6065213/)  
37. Symptom-specific genetics reveal heterogeneity within major depressive disorder \- medRxiv, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.64898/2026.03.24.26349158.full](https://www.medrxiv.org/content/10.64898/2026.03.24.26349158.full)  
38. GWAS Meta-Analysis Reveals Shared Genes and Biological Pathways between Major Depressive Disorder and Insomnia \- MDPI, otwierano: maja 12, 2026, [https://www.mdpi.com/2073-4425/12/10/1506](https://www.mdpi.com/2073-4425/12/10/1506)  
39. Biomarkers of Major Depressive Disorder: Knowing is Half the Battle, otwierano: maja 12, 2026, [https://www.cpn.or.kr/journal/view.html?doi=10.9758/cpn.2021.19.1.12](https://www.cpn.or.kr/journal/view.html?doi=10.9758/cpn.2021.19.1.12)  
40. Pharmacogenetics and the Response to Antidepressants in Major Depressive Disorder, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/395437216\_Pharmacogenetics\_and\_the\_Response\_to\_Antidepressants\_in\_Major\_Depressive\_Disorder](https://www.researchgate.net/publication/395437216_Pharmacogenetics_and_the_Response_to_Antidepressants_in_Major_Depressive_Disorder)  
41. PRSice-2, otwierano: maja 12, 2026, [https://choishingwan.github.io/PRSice/step\_by\_step/](https://choishingwan.github.io/PRSice/step_by_step/)  
42. PRSice \- Jordan Lab Docs, otwierano: maja 12, 2026, [https://jordanlabmanual.biosci.gatech.edu/IntegratedRiskPredictionToolforColorectalCancer/polygenic-risk-scores/prsice/](https://jordanlabmanual.biosci.gatech.edu/IntegratedRiskPredictionToolforColorectalCancer/polygenic-risk-scores/prsice/)  
43. Polygenic risk scores for major depressive disorder and neuroticism as predictors of antidepressant response: Meta-analysis of three treatment cohorts \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6150505/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6150505/)  
44. A harmonized benchmarking framework for implementation-aware evaluation of 46 polygenic risk score tools across binary and continuous phenotypes | bioRxiv, otwierano: maja 12, 2026, [https://www.biorxiv.org/content/10.64898/2026.03.22.713457v1.full-text](https://www.biorxiv.org/content/10.64898/2026.03.22.713457v1.full-text)  
45. GWAS summary statistics for major depression (PGC MDD2025) \- Figshare, otwierano: maja 12, 2026, [https://figshare.com/articles/dataset/GWAS\_summary\_statistics\_for\_major\_depression\_PGC\_MDD2025\_/27061255](https://figshare.com/articles/dataset/GWAS_summary_statistics_for_major_depression_PGC_MDD2025_/27061255)  
46. Pharmacogenetics and the Response to Antidepressants in Major Depressive Disorder, otwierano: maja 12, 2026, [https://www.scilit.com/publications/ef4ccbcac16868fd27eb8376126807a8](https://www.scilit.com/publications/ef4ccbcac16868fd27eb8376126807a8)  
47. Harnessing digital health interventions to address the heterogeneity of depression: a systematic review \- Semantic Scholar, otwierano: maja 12, 2026, [https://pdfs.semanticscholar.org/48d4/b50ec48cacd8e3eec2b7a0acf4d9189e54ab.pdf](https://pdfs.semanticscholar.org/48d4/b50ec48cacd8e3eec2b7a0acf4d9189e54ab.pdf)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAVCAYAAABG1c6oAAABZUlEQVR4Xt2TzytEURTHv0IpY4FiQ1kpSmFFKXYsLGUj1kJ+lA3Z2QhLCylbG4WatayUEiVlxUbKVvkD+H6de9/MvfNMb5qF8qlP8+49b86775zzgP9OLZ2ku3SFNoXhypmjQ7DEa/Q8DFdGjp7SfbfuondJ1DFC7+kn/XK/D/SVvtM87BV1ItFLO911N1ISevTUN9jreJRkFpZ4kdYUxcQSPYn2flBhz+g1bYti7fQmJTZID2hz0V6Cjv5Ij2hdFBugL/SStrq9PrpJG/FLwglY7dTBmHVYbN6tVb8t2gE7/bTbD9hGaf3q6Qzs5Atu3UCPYc3z3vo/ePwoqKsX7voKdqod2lK4NRtp9VM3l2HdHXN7mfH18zXy9NNnFIY4M2n1E1OwGm1E+2UpN396kBJqeDPTQ59QOn/6Qg4RJlylo8kdEcOw6f9A+P2qnh59v2qKEmvW9mBjUxUqwzis01Un+zu+AVvURkbKupHXAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAZCAYAAAAFbs/PAAAA00lEQVR4Xu3QPwuBURTH8SOUyeBvRMpgtymZKCtlNpgMBt6GyGSgpOQVyGhQymI0KatX4AXwvd17uWxW/OpTT+fce8/TEfnnaxJDFUUE3noviWOKGero4oC86SeQNd+SxgZ9+E3NhzGWoif1UDC9zy6oxkD0+Iw5bNPBCWWMEFTFHI6i/19ddtPAWfThmi2qjdzQtAUntjcXZ2MVXE3zPap2Eb3iR1LYoeXUPChhK8/HkgjbA6q5xwRDrNBGBAusRW9LbfMRL6IIiZ7g1tXLdt2/lzsrZiGopgDobwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC4AAAAYCAYAAACFms+HAAAC5UlEQVR4Xu2Xy6tPURTHl1DyyqMI0WWgvPKWV7lFkVKUMlAGMjAQKRIDA2SAQkbEgOQRUcTAqwzEhEIMZHATGZgofwDfT/us32//9tk/53ev3Ev9vvVJd519zm+dtb9rnc2srbba6g2NEp1imRhUxMaK4b6gSsvFK/FD/Cx4J14XsQ/ikBhWrB8tboqv0XrWcA/rn4u90fpUQ8RJcV9sFjvFA7HHwnN5frd0QnwWi5P4bAsvcUUMjeKrLCS6P4qhmeKFuGbl6nE/z9knBkbxyeKlhRfqF8UrRXVuiWdiTHKNH7shvokVUXyXhcR5gVSnLX9tg3hs5d8g2TNiSxKv1FTxVpwTA5JrI8Q9a9wNPHnRgsU6ipjLi5C+KM/l+VzL2eiImJMGq7TGQoW2pxekhaJL3LH61o+z4GWS98Zy+frUWr5z9MZ6K1tihpWfVanDlvc3ieLVN2JuFKeSVDT2N4nMEk/EeQsTIhUN6A39ycIOrLMeJIy8El0WfHasAJ96w0zwxYV2WNihhxbuvSu+iEdiupWr6aIQ/MZ3q78AXLLG3WlJ7u+rYqKFSjm5SjTz93zx0cLobJa4i4mywEKBqHzaD67VYmkadLm/mRKtyP2NhQZHcd+53GTiZSlKTlstVJ0kY9HMWLEzideEv5u9cU45f6MOC7vABGISxaJ3dicxFwnn+uu38tFFBalkK2o2v/2FqHrqV3qCAqXCUnyM0numiOMWfiv+UNU0Tby3/FjLiTWXrexvxMeFLfckGIsHrD6/sdCk2uqgReKpmBfFxottxb8cC2j2mpZY+CzH3c1Zg7NDThyIaF4ayddzPjkq+hdr8DBJ8Ny14qyFxmcnmel8I9jZU2KThanFV5RDViyGAucVxu91K9vur4gdIRES9zk+0uo29OvMbhLL2qAQn/9un136WiRL0hvTC/+6sMpt68HZpa9FwvRUr/j7T4X/L1j4jwVfX5r5vxC+pqkPipXF3w36BedWlyCUIY1HAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAYCAYAAAAoG9cuAAAAuklEQVR4XmNgGGaAFYgjgdgcXQIZuADxZyBuRpdABtxA7ADEvGjixANmIDYAYisGiLswAB8QTwHiDCCeB8TzgZgDWQEjEFcAsSWUD3LwCSAWh6sAAmEgLgBiFiDmAuIVQLyQAc0kZKAAxOeAOB9NHAXYA/EjKI0TVDJATFJAE4cDkBtAbqHcPaA4e86AxT0xQBzCAAntViDeD8RiKCqA4A4QzwViWwaIVT6o0hAwEYh3MECiQh1NjsoAAPgwGIfeUb8NAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAXCAYAAADtNKTnAAABTklEQVR4Xu3TTytFQRjH8Uco5E+RbKhDEbFBblLKQlFsbKTwBhDZkJVCSbFQlD0LspElWdlb2PFm+D49d645Y+457Cz86rM4M3OmmWdmRP7zm1RjDFNoDvp+lEFcYBHzeMBMakROenGGRq9tDdeo89rKpgZH6AzaN3CL+qA9mhGsBm068RX2UBH0RbOJUbEf29CEWbGadHjjykb3e4ACXvBR9I4hb1xmEuyKLVlXoCupxTbOUVUamZF1saMNo0f7hoHit062gwk3wMVtpSXsIPt4knhfKonY5WoI2tvxLLYl3aZu8RBbYjc6lUm8Ythr0xM6xqXYxdNJFtCPO4mclh6tXm+9UKc4wSNWxCbTaC26MC226lSh/XpUolXswcUulv6oT2Iu7Ejk62jz0oN79GFZvH+0HkvuIyfduBErrE5Yyrh8f3BZ0Rq5Ov2xfAIStSfDFCR+YgAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAXCAYAAADHhFVIAAAAjklEQVR4XmNgGOSAG4jTgVgFXQIEMoD4PxDHoUuAgDAQWwMxK7oETsAMxAZAbAFlwwHIiCYgLgLirUBcjyzpAMSFQMwLxKuBeDoDmm4QKAHi00Asjy4BcuVeIG4FYkY0OQYnIH4ExPZArMoAMQUOOhkgjhFigASEA7KkBwPEvnlAnMaAxWgeIOZHFxxUAACehhAoXpfmZQAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAYCAYAAAALQIb7AAAB30lEQVR4Xu2VsUtWURiH39BAUExyEEqlwsp0sTElFRuKqCFwEKRaHGwoCSJxaVAiUSEVwZYGCYpoKCWiBgdxEcKWpoKWaGv0D9Dnxzn389xzP6XrZ4v4wMP33fOee8+573nPuWaHHDSqsANv4jks8+2VeDLpVCrncRF/4jwO4iy+xmZ8hV2F3nvkKD7E33gfK9Jhu4Q/8CueiGK50EDj+AdvRLEEDb7gjSeSi7u4gcN4JIqFzOBQ3JiH07iOq1gfxWKmrMT1eoSbOBYHilBtLuV7QuX9Dv9aiTP+F+pwDb+b20shWrvj5vqEHgs7Qac35iq2hw3JYFL/Q7R5tRWWzG0HFdBn7A/6lOMIdgdtO7bX4rIVHywhSfU3PJUO5UOpempuzXqiWILSqzTH+0uTe4aPLV00Z3DS3BbJFFMDruAXy54M6jxhrlqVlgRNsg9b8YO5ZwjdP+B/P2GLb0/RhB/xF05jr7mH6wbdfA8vF3q7NdEbXMMX/lrobbU0F/Et1vj2DJptI143d9Lr0M2kIUADzOGtOAB38LntfhrlQmupSr2At237wfrVQMrOvnHWXKpUIOEeVRrfY1vQti+oOuMvgAZ5Y7usV6lowJf4AEfNfXD/G1onFdYTvOKvU2wBiAZCRdsbraUAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAYCAYAAAD3Va0xAAABGklEQVR4XmNgGAUDBmyA+BIQ/4fiJUDMgSTPC8TLkOQ/A/EcIOZCUgMHjEDcBcSPgPgBEJuiyEKANxDPYkC1BAMIAPFEIE5lgNjYygAxHBlkAHEImhgG0AHiRiAWB+L9QHwaiOWR5FmAuBuqDi8A2RQHZZcwQMIiCSHNIMwAcTHI5XhBAxAbQNmaQHwNiDcBMR9UzAKIW6BsnAAWPiBbQQDkjalA/BqInaBiINcSHT7IgQsyAGQQyEBQLJEcPjAA8hLIayAv2jIQET4gV4D8boguAQShDJCksA+Iq9HkMAB6+CADMQZIUgDFIMHwATkblNw50SWgAJQULgOxGroEDNgD8S0GRP55AMRuyAqgAJQUQHkPb/iMgqEEAEblLziHqHJZAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAAAYCAYAAAAiR3l8AAAD9klEQVR4Xu2Z2atNURzHfzJknso8XUSETBEiLzIkIh6UMVwkZSbkxTyPGcuDecqQoZAMRUgUQsnDfVAevCh/AN9vv72cc9bZ69y19z7nump/6pNz9z7D2uu71m+tvYmkpKSkpLipCcfD9XAubJB7OqW6MwUODl4PgNtgrczplOpMHbgLdgn+bgQ3wIZ/32ExHL6Fv+DvwI/wXXDsC9wk+kVVTUfR0dhOtKzUhb3hzOB1VcPfnAab2CcC2EflogGsgK1yT3uzCn6GU+FkOC/3dDh74Dc4xDreVzTMC1JgFJQIlpEKyQws+hWOznpPqWkGJ8ED8BN8KeHBdIAP4AzRoEfBp6IlMCr14DHR670C2+eezocj5zp8Dlta5xjaVfgDjrTOxaU2rG8fDKEffASfwPtwtYR3XilhgONgf3hUwgPk+sQJcDJ4bVgHz0mmWgwTnZ1hbofdYQ24AE4UrTaP4UPYQgrAD36Q/AaQpvCuhM/OqHCgLIe3JLNIF4IBbrEPesKOpy5YkluLdpgvByU8wDLRZWiJdZw7SVYMXocvZXC/ZEJvDC9JJZNnrOh6t8g+AQaJljF2Or8sDrzgraLlgMGx83xIEmBXeEq0tNmwAqyEi6U4AbJzWaHsAMeIlkGuZb50gocls1yxfVwTOcmcbJbwGWbSfy9aQqLCxuyFZ2EvidZZhAEyhEPwGXwlejG+G5g+8Lzkhhg3POIK0ATlCtA+Xgi2aSHcAXvCZXBOcDwUs8ZViCZvajIb+0Z0OnMXGIVu8EQgX8eFAd6GnYO/m8M7ou1jED5kh5gkPOIKkAGFBRUnQANz4e+4drx/MevfRdGL5IeMviOdsEM4yzjbOOs4+5ISttlZKjrYWNp9YYiX4W6JHx5xBcilJyyoJAF6Y9Y/dkwSuEviGsfttn2BxcSM9rD12gUHApcJ7rLLck9FwhWgKyjX8aLCCyvWLUL2LOTFJimfLJfc/dpbaFe5csHwNorOvB7wtIRvbHxwBci9A/cQdptMgNyNlgRz//cCtrHOJYXh8bYk7gaGncTOsgNkpWDFYOWojOzwzO9zyYgboitA9h37kJMhm1miy1PBHWQSuMvh0wVeUJT1LgrZtxADxT9I3o/uFP2Mgbvia6I748puaRgenyFyR2f/ZtwQGeBr2NY6zu9fK7m3Wvz94/CI5N9bJ2ao6Ej6KZlHVHz+OT37TUWGJZGzgTN+hPjdC7KD+X5+jm27B29KfgeGwWe88yU/PAN3tmtEHx4XgrOfbeAzYdNX30WDnJ31PgZ3RvQRGB+j7YM3xK+t/xX8v61y8V8XOJL5CGqC6MzxCf5fwbbx1odt5b/Vua0pKSkpKSkpKVXLHzqwvaeSeIB4AAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAAYCAYAAACyVACzAAADR0lEQVR4Xu2Xy6tNURzHv0LJKynvcBVKyCtCZCLkMcLIY6YM1I1IiolHIW/Joww8QuSRRyHPIgwoxEAGN5mZKH8A36/fXnevs/Ze5+5zzr0U+1ufzr1rrbP3Wt/1W7/fOkCpUqVKlfovNIu8IT/Iz4QP5G3S9olsJ73cF/6wupGlZC/ZSkZVdleV5rwG9t0NZEBlN4bBnj2EdIa9axxZlfwd1T7ylUwP2ifAjLtAegZ9Ha3e5CLZDHv3ePKILPYHRTSU3CcrYQufS56Syd6YaaQFaZCIz2SeNyYj7cA18pz0D/o0ySvkG5kT9NWrrqR72JijdeQO6eO1LSOPkZ2nry6wzT+V/O20hZxHGjUTYeY/IffIJmSjL6PR5D2yD5c0UU04L+pqlTZlPbkJ29Vqcu89HLRPgqWGBUG7ryZYapHZvhbBIkcmSfrcmXYXk16s/LQ27KCmwkJVC9SxqEfarV3kMswk5Ye25DYwNEsL1IIVJTHpBOgkhGbNhx01RadUl1k7kB85MucSeQfb0Vo1nOwn58hY0qmyu6qcKTGzwnZfzpSYWa5dzzpNjpBn5BXZiCrJ3eWkFnIUVjmEJvOaHIRVi1qkinUyoZbq5cstLDSliFkyo6hZt8iI5P++5DZs/cqrGblwV9VRBdGRcUQdzpGiRtGjKFI0KaoakaqXUkNoShGzlE6KmJVXaJphgaP0k5HLVxrUiPrBctIhFKgoBRQzJdbuKzSlrXZfLirz8vfvfNVe1wI/urSYeo+g1ASraKEpzqxqm6vcqxwcmuLMUlXUkVO1fQDbaKfYEW69X70gg4K+RiWjdBWpJ7lLLpeeQWU60KZ+ST6dVIgGIn2H1qI1KRB8rYalHKUeRf9LZM3SJuikZa4mY8hHZCfUnvKvDVNQm2nLYRXK5T99V7d5/xqjCNFNvQVpnskbp/x0ghyD3SXFHticnDT2KuwG0HpNmgFz9TvSa75+D65wAzpAWtQ2WCTPRrG7lha4G2b0QpgBD2E/e5wUgWdhP2VUoJy0WLUfhxWLA+Q6GeyN0XjNR/PS2u+SG8GYv6oesB+3yhtFpCgZSZaQmYiU9Ii0Icpx+q4+8zZIz9NzNUbHM29MqVKlSpX61/QLOKaq5QYmDFcAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAACu0lEQVR4Xu2Xy6tOURjGH6HkFsotuRUKCYkQMVDkVsKIIaWcyEiKCSmJkFJM5JJrGSgphQzccinEQAYnmZkofwDP492rs/b77f219/4+Z7R+9eucs9b37b3Wu971rnWARCKRSNRmBX1Pf9M/mZ/ph6ztKz1KR4Qv9DND6FZ6kh6mM/Pdpcyhm+lYOoAOp8votvhDRZyiP+hS1z4fFpQbsIf1JyPpTXoQ9u559AndGH+ohC3oW9jga9gzStFq36PP6TjXpwHcpT/pKtfXlMF0qG8soIc+oKOiNq3oU7SO07MWNh95n+5GhayeRT/RS3SQ69MgNJiibKmLBnIANrAlrs8T3nvOtS+Ebdd1rt2jQCiQtdBDVQ/2+A6ymPbCBq9UbcJ4epzegQVgYL67kLA4PhAL6Dd6yLV7GgXiGIpXXBO/RT/CVqIuU+lpeo3OhRWtqoQJlwXCt3sUCH3mOmx7vKA70WYRQg3opedh1VnqIe/oGTopfLgiquwXM6tWeY8mogLnJ1wnELfp6Ozv6fQN3YuSBQkpqOo8GZbGQR1dVdHDtepafWWBsqET1sC2q59w1UBo7PH4NT4ttIJROLZQH/b7jprovFYNOAsLYqeUTbisvQr6juaqILeg+tCtozHOCr206bYQ02AXPT/hEIh2CzeDvqWXkc8KPUvbTdsmR7g/vKQTXV+nKAg6jpsUShFq1xXkJ6MF+579DKioT0DfO0Kw4kCEraF29eeYTb+g9WXdJD46F6FeQLbDboNhT+u7umXGR/kY+ghW7HXUC/Vp0lOyv4V+1+mhg0AXun/ozv2K/kL+/4sd4QP/AQ34CCwDV6LNMRahAZ+ABXE9LAiPkb8mK3Ou0mewYh/Qcf+Q7qO7YFl/Ac3vQl1nGOy6u8F3lKAs0J7fRJcjWs0K6F2rYUFURtTJxkQikUiIv7dRhQBubzMIAAAAAElFTkSuQmCC>