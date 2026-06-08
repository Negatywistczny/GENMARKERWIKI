# **Architektura Genetyczna ADHD: Kompleksowy Wykaz Genów Ryzyka, Punktacji Poligenicznej (PRS) oraz Neurobiologicznych Biotypów dla Precyzyjnej Analizy Kodu Genetycznego**

## **Genetyczne fundamenty heterogeniczności zespołu nadpobudliwości psychoruchowej**

Zespół nadpobudliwości psychoruchowej z deficytem uwagi (ADHD) stanowi jedno z najpowszechniejszych zaburzeń neurorozwojowych, którego etiologia jest głęboko zakorzeniona w strukturze genomu człowieka. Analizy oparte na badaniach bliźniąt i rodzin konsekwentnie wskazują, że odziedziczalność ADHD oscyluje w granicach 70–80%, co plasuje je wśród najbardziej uwarunkowanych genetycznie schorzeń neuropsychiatrycznych.1 Mimo tak silnego komponentu dziedzicznego, przez dziesięciolecia nauka zmagała się z problemem "brakującej odziedziczalności", gdzie pojedyncze geny kandydaty nie były w stanie wyjaśnić złożoności fenotypu. Dopiero rozwój badań asocjacyjnych całego genomu (GWAS) pozwolił na zrozumienie, że ADHD nie wynika z mutacji w jednym punkcie, lecz jest wynikiem skumulowanego efektu tysięcy wariantów genetycznych o małej sile oddziaływania.4

Współczesna analiza kodu genetycznego w kontekście ADHD musi wykraczać poza proste stwierdzenie ryzyka. Kluczowym wyzwaniem dla programistów i diagnostów jest obecnie dekompozycja tego ryzyka na konkretne ścieżki biologiczne, które prowadzą do powstania różnych biotypów zaburzenia. Heterogeniczność kliniczna ADHD – objawiająca się u jednych pacjentów głównie problemami z koncentracją, u innych gwałtowną impulsywnością, a u jeszcze innych głęboką dysregulacją emocjonalną – znajduje swoje odzwierciedlenie w unikalnych profilach genetycznych i neuroanatomicznych.7 Integracja danych z najnowszych metaanaliz całogenomowych z lat 2023–2026 pozwala na stworzenie zaawansowanych modeli probabilistycznych, które mogą przewidzieć nie tylko samo wystąpienie ADHD, ale także jego konkretną manifestację biologiczną.8

## **Krajobraz loci ryzyka: Analiza metaanalizy Demontis i współpracowników (2023)**

Przełomowym momentem w genetyce ADHD była publikacja wyników metaanalizy przeprowadzonej przez Psychiatric Genomics Consortium (PGC) w 2023 roku. Badanie to, obejmujące imponującą próbę 38 691 osób z diagnozą ADHD oraz 186 843 osób z grupy kontrolnej, pozwoliło na zidentyfikowanie 27 niezależnych loci o znaczeniu całogenomowym, co stanowi ponad dwukrotny wzrost w stosunku do wcześniejszych raportów z 2019 roku.4 Zidentyfikowane warianty nie są rozmieszczone losowo; wykazują one wyraźne zagęszczenie w regionach genomu, które pozostały niezmienione w toku ewolucji człowieka, co podkreśla ich fundamentalne znaczenie dla funkcjonowania ośrodkowego układu nerwowego.5

Analiza tych loci pozwoliła na wyodrębnienie 76 genów wysokiego ryzyka, które wykazują szczególnie silną ekspresję we wczesnych fazach rozwoju mózgu, zwłaszcza w korze przedczołowej i neuronach dopaminergicznych śródmózgowia.4 Dla programów analizujących kod genetyczny te 27 loci stanowi podstawowy zestaw zmiennych wejściowych. Należy zauważyć, że ADHD jest zaburzeniem wybitnie poligenicznym, gdzie około 7000 wariantów genetycznych wyjaśnia 90% odziedziczalności opartej na SNP (Single Nucleotide Polymorphisms).4

| Numer Locus | Najbardziej Prawdopodobny Gen (HGNC) | Funkcja Biologiczna i Kontekst ADHD | Istotność Statystyczna (p-value) |
| :---- | :---- | :---- | :---- |
| 1 | **SORCS3** | Plastyczność synaptyczna, sygnalizacja glutamatergiczna. | 4 |
| 2 | **ST3GAL3** | Glikozylacja białek w mózgu płodowym, rozwój korowy. | 2 |
| 3 | **PTPRF** | Synaptogeneza, selektywna śmierć neuronów. | 2 |
| 4 | **FOXP2** | Neurogeneza, rozwój mowy, komunikacja neuronalna. | 2 |
| 5 | **CDH13** | Adhezja komórkowa, migracja neuronów, plastyczność. | 2 |
| 6 | **ADGRL3** (LPHN3) | Tworzenie synaps glutamatergicznych, wzrost neurytów. | 2 |
| 7 | **DUSP6** | Regulacja sygnalizacji ERK/MAPK, stabilność obwodów. | 5 |
| 8 | **MED8** | Składnik mediatora transkrypcji, stabilna ekspresja. | 15 |
| 9 | **RPS26** | Biogeneza rybosomów, ekspresja w mózgu płodowym. | 15 |
| 10 | **TIE1** | Receptorowa kinaza tyrozynowa, rozwój naczyniowy mózgu. | 12 |

Wykaz ten nie jest zamknięty, jednak geny takie jak *SORCS3* są szczególnie interesujące dla systemów analitycznych, ponieważ ich związek z ADHD został potwierdzony zarówno poprzez analizę rzadkich wariantów skracających białka (PTV), jak i poprzez powszechne warianty SNP.4 Oznacza to, że gen ten może służyć jako stabilny marker w różnych populacjach i dla różnych metod sekwencjonowania.

## **Parametryzacja Punktacji Poligenicznej (PRS) dla Systemów Diagnostycznych**

Aby algorytm mógł wyliczyć prawdopodobieństwo wystąpienia biotypu, musi najpierw prawidłowo obliczyć ogólną punktację poligeniczną (PRS). PRS jest sumą alleli ryzyka niesionych przez daną osobę, z których każdy jest ważony współczynnikiem siły efektu (![][image1] lub ![][image2]) uzyskanym z niezależnego badania GWAS.17 W przypadku ADHD, punktacja ta wyjaśnia obecnie od 0,7% do 4,0% wariancji w diagnozach kategorycznych, co choć wydaje się małą wartością, pozwala na skuteczne różnicowanie grup o ekstremalnie niskim i wysokim ryzyku genetycznym.20

Dla programisty przygotowującego dane, kluczowe są standardy kontroli jakości (QC) oraz wybór odpowiedniego zestawu danych bazowych. Do obliczenia PRS-ADHD zaleca się stosowanie statystyk sumarycznych z metaanalizy Demontis et al. 2023 (PMID: 36702997).9 Proces przygotowania danych powinien obejmować rygorystyczne filtrowanie:

1. **Częstotliwość allelu mniejszego (MAF):** Należy uwzględniać tylko warianty o MAF \> 0,01. Warianty rzadsze mogą wprowadzać szum statystyczny i błędy w imputacji.17  
2. **Jakość imputacji (INFO score):** Próg INFO \> 0,8 zapewnia wysoką pewność co do przewidywanych genotypów wariantów, które nie były bezpośrednio obecne na matrycy mikromacierzy.17  
3. **Równowaga Hardy’ego-Weinberga (HWE):** Wykluczenie wariantów z p \< ![][image3] w celu usunięcia błędów genotypowania.17  
4. **LD Clumping:** Aby uniknąć wielokrotnego liczenia tego samego sygnału genetycznego wynikającego ze sprzężenia loci, należy zastosować procedurę "clumpingu" z parametrami ![][image4] w oknie 250 kb.26

Praktyczne zastosowanie PRS w diagnostyce wykazuje, że osoby z najwyższego decyla punktacji mają od 1,5 do 2 razy wyższe prawdopodobieństwo spełnienia kryteriów diagnostycznych ADHD w porównaniu do średniej populacyjnej.28 Co więcej, wysoki PRS jest silniej skorelowany z uporczywym przebiegiem ADHD, który trwa od dzieciństwa do dorosłości, niż z przypadkami, które ulegają remisji.28

## **Klasyfikacja Biotypów ADHD na podstawie Modelowania Normatywnego i Topologii**

Kluczowym elementem zapytania jest przypisanie genów do konkretnych biotypów. W 2026 roku badania opublikowane w JAMA Psychiatry zrewolucjonizowały sposób patrzenia na heterogeniczność ADHD, odchodząc od kategoryzacji opartej na zachowaniu na rzecz klasyfikacji opartej na topologii sieci mózgowych i sygnaturach molekularnych.7 Zespół badawczy z West China Hospital wykorzystał modelowanie normatywne – proces analogiczny do siatek centylowych wzrostu u dzieci – aby zmierzyć stopień odchylenia struktury mózgu pacjenta z ADHD od wzorca typowego dla wieku i płci.8

W wyniku analizy wyodrębniono trzy stabilne biotypy, które różnią się nie tylko objawami, ale przede wszystkim zaangażowaniem konkretnych układów neuroprzekaźników i regionów mózgu. Dla celów automatyzacji analizy genetycznej, każdy biotyp można powiązać z grupą genów regulatorowych odpowiedzialnych za gęstość receptorów w tych regionach.7

### **Biotyp 1: Profil Ciężki-Mieszany z Dysregulacją Emocjonalną (Severe-Combined)**

Pacjenci z tego biotypu wykazują najbardziej rozległe odchylenia od normy w skali całego mózgu. Zmiany te koncentrują się w obwodach łączących przyśrodkową korę przedczołową (mPFC) z gałką bladą (pallidum) – regionami odpowiedzialnymi za filtrację impulsów i regulację motywacyjną.30 Klinicznie są to osoby o największym nasileniu zarówno nieuwagi, jak i nadpobudliwości, u których dodatkowo występuje silna labilność emocjonalna.30

Sygnatury molekularne biotypu 1 obejmują:

* **Układ Cholinergiczny:** Geny takie jak *CHRNA4* i *CHRNA7* (receptory nikotynowe), które modulują kontrolę motoryczną i uwagę.7  
* **Układ Histaminergiczny:** Wyjątkowe dla tego biotypu zaangażowanie receptora H3 (gen *HRH3*), co sugeruje tło neurozapalne i zaburzenia cyklu sen-czuwanie.7  
* **Złożoność Monaminergiczna:** Jednoczesna dysfunkcja w obrębie transportu serotoniny (geny *SLC6A4, HTR4, HTR1A*) oraz dopaminy (receptor D2, gen *DRD2*).7

Dla programu analitycznego oznacza to, że wysokie skumulowane ryzyko genetyczne w loci tych układów, połączone z ogólnym wysokim PRS-ADHD, wskazuje na najwyższe prawdopodobieństwo wystąpienia biotypu 1\. Pacjenci ci często nie reagują na standardową monoterapię stymulantami, wymagając bardziej złożonych strategii terapeutycznych.8

### **Biotyp 2: Profil Przeważająco Nadpobudliwo-Impulsywny (Hyperactive-Impulsive)**

Biotyp ten charakteryzuje się zmianami zlokalizowanymi w obwodzie kory zakrętu obręczy (ACC) i gałki bladej, co odpowiada za procesy selekcji reakcji i kontroli działania.10 Mózg tych pacjentów ma problem z "hamowaniem" gwałtownych impulsów, co przekłada się na nadruchliwość i głośność.33

Sygnatury molekularne biotypu 2 obejmują:

* **Układ Glutamatergiczny:** Geny receptorów metabotropowych, szczególnie *GRM5*, zaangażowane w sygnalizację w jądrach podstawnych i procesy nagrody.7  
* **Układ Kanabinoidowy:** Rola receptora CB1 (gen *CNR1*), który moduluje uwalnianie innych przekaźników i jest silnie skorelowany z profilami impulsywności.7  
* **Interakcje Serotoninergiczne:** Specyficzne antykorelacje z receptorami *HTR1A* i *HTR2A*.7

W analizie kodu genetycznego, warianty genów układu glutamatergicznego powinny być ważone wyżej przy próbie predykcji biotypu 2\. Istotne jest również uwzględnienie genów plejotropowych, takich jak *MDFIC*, który łączy ryzyko ADHD z zachowaniami antyspołecznymi i opozycyjnymi, często towarzyszącymi temu biotypowi.16

### **Biotyp 3: Profil Przeważająco z Deficytem Uwagi (Inattentive)**

Jest to najbardziej subtelny biotyp pod względem neuroanatomicznym, wykazujący ogniskowe różnice w górnym zakręcie czołowym (SFG) – regionie kluczowym dla podtrzymywania uwagi i filtrowania dystraktorów.30 Pacjenci ci często wydają się być "we własnym świecie", są rozkojarzeni, ale rzadko wykazują nadmierną aktywność ruchową.33

Sygnatury molekularne biotypu 3 obejmują:

* **Układ Serotoninergiczny:** Selektywna antykorelacja z receptorem *HTR2A*.7 Sugeruje to, że ten konkretny receptor może być kluczem do zrozumienia patofizjologii czystego deficytu uwagi.  
* **Układ Noradrenergiczny:** Geny takie jak *SLC6A2* (transporter noradrenaliny) i *ADRA2A* (receptor alfa-2A), które są odpowiedzialne za funkcje wykonawcze i czujność w korze czołowej.2

Algorytmy predykcyjne dla biotypu 3 powinny koncentrować się na wariantach genetycznych wpływających na funkcję kory czołowej oraz na stabilność procesów uwagi. Co istotne, ten biotyp wykazuje wysoką korelację genetyczną z dysleksją i problemami w nauce, co sugeruje zaangażowanie genów takich jak *CNTNAP2*.42

## **Wykaz genów dla algorytmu predykcyjnego (z podziałem na ścieżki biologiczne)**

Dla potrzeb programu analizy genetycznej, geny zostały pogrupowane według systemów funkcjonalnych. Program powinien wyliczać oddzielne "wyniki ścieżkowe" (pathway PRS) dla każdej z poniższych kategorii, co pozwoli na oszacowanie prawdopodobieństwa biotypu.

### **1\. Ścieżka Dopaminergiczna i Nagrody (Głównie Biotypy 1 i 2\)**

Fundamentalna dla procesów motywacji, hamowania i napędu ruchowego.

| Gen (Symbol HGNC) | Funkcja w OUN | Kluczowe Dane dla Programu |
| :---- | :---- | :---- |
| **SLC6A3** (DAT1) | Transporter dopaminy; usuwa DA z synapsy. | Warianty 9R i 10R w regionie 3' UTR; wpływ na odpowiedź na metylofenidat. 45 |
| **DRD4** | Receptor dopaminy D4; kora przedczołowa. | Allel 7-repeat (7R) związany z obniżoną wrażliwością na dopaminę i cieńszą korą czołową. 40 |
| **DRD5** | Receptor dopaminy D5. | Najsilniej związany z ADHD gen receptora w metaanalizach GWAS. 2 |
| **COMT** | Enzym rozkładający dopaminę. | Polimorfizm Val158Met (rs4680); kluczowy dla poziomów dopaminy w PFC. 2 |
| **ANKK1** | Ściśle powiązany z receptorem D2 (*DRD2*). | Wariant TaqIA; modulacja gęstości receptorów D2 w prążkowiu. 37 |
| **DBH** | Beta-hydroksylaza dopaminy. | Konwersja dopaminy do noradrenaliny; polimorfizm rs1611115. 2 |

### **2\. Ścieżka Serotoninergiczna i Emocjonalna (Głównie Biotypy 1 i 3\)**

Kluczowa dla regulacji nastroju, lęku, stabilności emocjonalnej i podtrzymywania uwagi.

| Gen (Symbol HGNC) | Funkcja w OUN | Kluczowe Dane dla Programu |
| :---- | :---- | :---- |
| **HTR1B** | Receptor serotoniny 1B. | Polimorfizmy rs6296 i G861C; silna korelacja z inuatywnością i agresją. 40 |
| **HTR2A** | Receptor serotoniny 2A. | Główny marker molekularny dla Biotypu 3; rola w elastyczności poznawczej. 40 |
| **TPH2** | Synteza serotoniny w mózgu. | Rate-limiting enzyme; wariant rs4570625 wpływający na regulację stresu. 37 |
| **SLC6A4** (5-HTT) | Transporter serotoniny. | Polimorfizm 5-HTTLPR; modulacja stabilności emocjonalnej w Biotypie 1\. 2 |
| **HTR4** | Receptor serotoniny 4\. | Wykazuje korelację przestrzenną z zmianami w Biotypie 1\. 7 |

### **3\. Ścieżka Neurorozwojowa i Adhezji Komórkowej (Wszystkie Biotypy)**

Wpływa na strukturę sieci mózgowych, kierowanie aksonami i synaptogenezę w fazie płodowej.

| Gen (Symbol HGNC) | Rola w Rozwoju | Dowody GWAS / Lokalizacja |
| :---- | :---- | :---- |
| **CDH13** | Kadheryna 13; adhezja i migracja. | Najbardziej powtarzalny gen w GWAS; rola w integracji sieci. 2 |
| **ADGRL3** (LPHN3) | Latrofilina-3; synaptogeneza. | Wariant rs1397547 reguluje rozwój synaps glutamatergicznych. 59 |
| **SORCS3** | Plastyczność synaptyczna. | Wspólny czynnik ryzyka dla ADHD, autyzmu i depresji. 4 |
| **CNTNAP2** | Kontaktyna; adhezja komórkowa. | Związany z ADHD, autyzmem i zaburzeniami mowy. 2 |
| **ASTN2** | Astrotaktyna 2; migracja neuronów. | Wspólny locus dla ADHD i zaburzeń obsesyjno-kompulsyjnych. 41 |
| **ST3GAL3** | Enzym glikozylacji. | Kluczowy gen TWAS dla kory płodowej (pmid: 36702997). 2 |

### **4\. Nowe Geny Ryzyka i Sygnatury Tkankowe (Dane TWAS 2026\)**

Zidentyfikowane poprzez Transcriptome-Wide Association Studies jako geny przyczynowe.

| Gen (Symbol HGNC) | Tkanka o najwyższej istotności | Potencjał Diagnostyczny |
| :---- | :---- | :---- |
| **MPL** | Kora, jądra podstawne, móżdżek. | Nowy, silny gen ryzyka związany z podziałami komórkowymi. 16 |
| **NKX2-2** | Biała materia, jądra podstawne. | Różnicowanie gleju; kluczowe dla integralności strukturalnej mózgu. 16 |
| **PTPRF** | Kora (płodowa i dorosła). | Gen causalny; wpływ na stabilność synaps. 2 |
| **MDFIC** | Jądra podstawne. | Plejotropia z zachowaniami impulsywnymi i agresją. 16 |
| **LSM6** | Kora mózgowa, móżdżek. | Stabilna ekspresja w różnych typach neuronów (excitatory/inhibitory). 15 |

## **Integracja Wielopoziomowa: Algorytm Obliczania Prawdopodobieństwa Biotypu**

Aby program analizy kodu genetycznego mógł wskazać prawdopodobieństwo wystąpienia biotypu, musi operować na macierzy wag. Tradycyjny PRS jest niewystarczający; model musi integrować "wyniki ścieżkowe" (Pathways) oraz dane o ekspresji tkankowej (TWAS).

### **Architektura modelu danych dla programu analitycznego**

Model powinien składać się z trzech warstw obliczeniowych:

**Warstwa 1: Ogólny PRS (Global Vulnerability)** Weryfikacja, czy pacjent w ogóle znajduje się w grupie ryzyka ADHD. Wykorzystanie wszystkich SNP ze statystyk sumarycznych PGC 2023\. Jeśli wynik znajduje się poniżej 20\. centyla, prawdopodobieństwo ADHD jest o 17–19% niższe od populacyjnego; powyżej 80\. centyla – ryzyko rośnie o 35%.62

**Warstwa 2: Modulacja Ścieżkowa (Pathway-Based Scoring)**

Dekompozycja PRS na pod-wyniki istotne dla biotypów:

* **Cholinergic/Histaminergic Score:** Warianty w genach *CHRNA4, CHRNA7, HRH3, DRD2, SLC6A4*. Wysoki wynik wskazuje na **Biotyp 1**.7  
* **Glutamatergic/Cannabinoid Score:** Warianty w genach *GRM1, GRM5, CNR1, GRIN2A*. Wysoki wynik wskazuje na **Biotyp 2**.7  
* **Noradrenergic/SFG-Specific Score:** Warianty w genach *SLC6A2, ADRA2A, HTR2A*. Wysoki wynik wskazuje na **Biotyp 3**.7

**Warstwa 3: Analiza Plejotropii (Comorbidity Matrix)**

ADHD wykazuje wysokie korelacje genetyczne (![][image5]) z innymi zaburzeniami, co program powinien uwzględnić jako modyfikatory prawdopodobieństwa:

* Jeśli wysoki PRS-ADHD współwystępuje z wysokim PRS dla Depresji (MDD) (![][image6]), rośnie prawdopodobieństwo **Biotypu 1** (dysregulacja emocjonalna).63  
* Jeśli wysoki PRS-ADHD współwystępuje z wysokim PRS dla BMI (![][image7]), rośnie prawdopodobieństwo **Biotypu 2** (impulsywność).64  
* Jeśli wysoki PRS-ADHD współwystępuje z niskim wynikiem dla osiągnięć edukacyjnych i IQ, rośnie prawdopodobieństwo **Biotypu 3**.62

### **Formuła wagowa dla biotypu ![][image8]**

Prawdopodobieństwo ![][image9] dla biotypu ![][image10] u osobnika ![][image11] można wyrazić jako funkcję:

![][image12]  
Gdzie:

* ![][image13] to punktacja poligeniczna ograniczona do genów specyficznych dla biotypu ![][image14] (np. histaminergicznych dla B1).7  
* ![][image15] to wynik asocjacji transkryptomu dla tkanki kluczowej dla biotypu (np. jądra podstawne dla B2, kora dla B3).61

## **Genetyka a Odpowiedź na Leczenie: Implikacje dla Psychiatrii Precyzyjnej**

Zastosowanie listy genów do predykcji biotypów ma bezpośrednie znaczenie dla personalizacji farmakoterapii, co powinno być końcowym produktem modułu analitycznego.8 Różnice neurochemiczne między biotypami wyjaśniają, dlaczego "standardowe" leczenie stymulantami (metylofenidat, amfetamina) zawodzi u znaczącej części pacjentów.33

### **Rekomendacje oparte na biotypach genetycznych**

**Predykcje dla Biotypu 1 (Ciężki-Mieszany):** Złożoność tego profilu (dopamina, serotonina, acetylocholina, histamina) sugeruje, że pacjenci ci rzadko reagują optymalnie na monoterapię stymulantami.33 Algorytm powinien wskazać potrzebę rozważenia leków o szerokim spektrum działania lub terapii skojarzonej (np. stymulant \+ lek modulujący nastrój). Wysokie ryzyko w genie *HRH3* może sugerować korzyści z interwencji wpływających na układ histaminowy.7

**Predykcje dla Biotypu 2 (Nadpobudliwy):** Silne powiązanie z układem glutamatergicznym i kanabinoidowym wskazuje na potencjalną skuteczność leków takich jak atomoksetyna (inhibitor reuptake'u noradrenaliny, który wpływa również na korę czołową i jądra podstawne) lub agonistów receptorów alfa-2 adrenergicznych (guanfacyna).7

**Predykcje dla Biotypu 3 (Inuatywny):** Selektywny związek z receptorem *HTR2A* otwiera drogę do stosowania leków modulujących układ serotoninergiczny w celu poprawy koncentracji.7 Geny zaangażowane w transport noradrenaliny (*SLC6A2*) są tu kluczowe, co potwierdza wysoką skuteczność atomoksetyny w tym konkretnym podtypie.2

## **Uwzględnienie różnorodności populacyjnej w analizie kodu genetycznego**

Istotnym ograniczeniem obecnych modeli PRS jest ich pochodzenie głównie z populacji o pochodzeniu europejskim (EUR). Badania z lat 2024–2025 wskazują na istotne różnice w strukturze loci ryzyka między populacjami.67

Analiza kohort latynoamerykańskich (kolumbijskich i meksykańskich) wykazała, że choć istnieje ogólna jednorodność wpływu wariantów genetycznych, to niektóre geny, jak *FOXP2* (rs7458242), wykazują znaczne zróżnicowanie populacyjne (![][image16]).67 Z kolei w populacjach azjatyckich (np. Hongkong) identyfikowane są unikalne loci sugerujące zaangażowanie genów odpornościowych i procesów rozwoju móżdżku w późnym niemowlęctwie.69

Dla programu analizującego kod genetyczny oznacza to konieczność:

1. **Dostosowania wag SNP:** Stosowanie wag specyficznych dla populacji (np. z GWAS dla populacji azjatyckich), jeśli pacjent nie jest pochodzenia europejskiego.69  
2. **Korekty na pochodzenie (Ancestry Correction):** Obowiązkowe uwzględnienie pierwszych 10 głównych składowych (Principal Components, PCs) w celu wyeliminowania artefaktów wynikających ze stratyfikacji populacji.24

## **Zaawansowana analiza funkcjonalna: Od SNP do białka**

Aby program mógł przygotować dane do precyzyjnego wskazania biotypu, musi uwzględniać nie tylko obecność wariantu, ale jego funkcjonalny wpływ na białko. Geny takie jak *ADGRL3* (rs1397547) są doskonałym przykładem – SNP ten jest wariantem synonimicznym, ale znacząco zwiększa transkrypcję genu we wczesnym rozwoju neuronalnym, co prowadzi do dysregulacji neuronów glutamatergicznych.59

Program powinien kategoryzować warianty według ich wpływu:

* **Warianty skracające białko (PTV):** Takie jak te zidentyfikowane w genie *SORCS3*, które mają znacznie większą wagę w modelu niż powszechne SNP.4  
* **eQTL (Expression Quantitative Trait Loci):** Warianty wpływające na poziom ekspresji genów w konkretnych tkankach mózgowych (np. kora płodowa dla genu *ST3GAL3*).15  
* **SMR (Summary-data-based Mendelian Randomization):** Wykorzystanie danych SMR do identyfikacji genów, w których istnieje dowód przyczynowy między poziomem ekspresji a ryzykiem ADHD (np. *LSM6, RPS26*).15

## **Wnioski i wytyczne dla implementacji systemów analizy genetycznej ADHD**

Stworzenie narzędzia do predykcji biotypów ADHD na podstawie kodu genetycznego jest zadaniem wymagającym integracji danych z GWAS, TWAS, transkryptomiki przestrzennej oraz klinicznych korelacji poligenicznych. Przedstawiona analiza pozwala na sformułowanie następujących rekomendacji technicznych:

1. **Baza genowa:** Rdzeń analizy powinny stanowić 27 loci zidentyfikowane w 2023 roku, ze szczególnym uwzględnieniem genów *SORCS3, CDH13, ADGRL3* i *ST3GAL3*.4  
2. **Dekompozycja PRS:** Algorytm musi obliczać sub-wyniki dla układów neurotransmisyjnych (dopamina, serotonina, glutaminian, histamina, acetylocholina), aby zmapować je na 3 biotypy zidentyfikowane w 2026 roku.7  
3. **Model Probabilistyczny Biotypów:**  
   * **P(B1)** rośnie przy wysokim PRS-ADHD \+ wysokim PRS-MDD \+ dysfunkcji w genach *CHRNA4/7* i *HRH3*.7  
   * **P(B2)** rośnie przy zmianach w ścieżce glutamatergicznej (*GRM5*) i kanabinoidowej (*CNR1*).7  
   * **P(B3)** rośnie przy selektywnych zmianach w genach *HTR2A* i *SLC6A2* połączonych z wysoką korelacją z dysleksją.7  
4. **Kontekst neurorozwojowy:** Wyniki genetyczne powinny być interpretowane przez pryzmat genów ekspresji płodowej (np. *LSM6, RPS26*), co pozwala na ocenę trajektorii rozwojowej pacjenta.15

Wdrażając powyższy wykaz i zasady ważenia wariantów, program analizy kodu genetycznego może stać się fundamentem dla psychiatrii precyzyjnej, zastępując subiektywne checklisty obiektywnymi miarami biologicznymi. Pozwala to na skrócenie procesu doboru leków (metoda prób i błędów) i zapewnia pacjentom opiekę dostosowaną do ich unikalnej neurobiologii.8

#### **Cytowane prace**

1. Genomics in ADHD: what's new and what's next? \- APSARD, otwierano: maja 12, 2026, [https://apsard.org/genomics-in-adhd-whats-new-and-whats-next/](https://apsard.org/genomics-in-adhd-whats-new-and-whats-next/)  
2. Attention-deficit hyperactivity disorder associated gene variants and their impact on neuroanatomy, otwierano: maja 12, 2026, [https://www.ijcmph.com/index.php/ijcmph/article/download/14892/8842/73472](https://www.ijcmph.com/index.php/ijcmph/article/download/14892/8842/73472)  
3. The Role of ADHD Associated Genes in Neurodevelopment | Request PDF \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/324125896\_The\_Role\_of\_ADHD\_Associated\_Genes\_in\_Neurodevelopment](https://www.researchgate.net/publication/324125896_The_Role_of_ADHD_Associated_Genes_in_Neurodevelopment)  
4. Genome-wide analyses of ADHD identify 27 risk loci, refine the genetic architecture and implicate several cognitive domains, otwierano: maja 12, 2026, [https://diposit.ub.edu/bitstreams/81db12ba-52d2-4cd3-a344-8614c1a6b0b2/download](https://diposit.ub.edu/bitstreams/81db12ba-52d2-4cd3-a344-8614c1a6b0b2/download)  
5. Study reveals strongest links yet between genes and ADHD risk | Broad Institute, otwierano: maja 12, 2026, [https://www.broadinstitute.org/news/study-reveals-strongest-links-yet-between-genes-and-adhd-risk](https://www.broadinstitute.org/news/study-reveals-strongest-links-yet-between-genes-and-adhd-risk)  
6. The First Robust Genetic Markers for ADHD Are Reported, otwierano: maja 12, 2026, [https://bbrfoundation.org/content/first-robust-genetic-markers-adhd-are-reported](https://bbrfoundation.org/content/first-robust-genetic-markers-adhd-are-reported)  
7. Mapping ADHD Heterogeneity and Biotypes by Topological Deviations in Morphometric Similarity Networks \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12936971/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12936971/)  
8. ADHD Isn't One Condition—Brain Scans Suggest Three Types, otwierano: maja 12, 2026, [https://www.technologynetworks.com/proteomics/news/adhd-isnt-one-conditionbrain-scans-suggest-three-types-410256](https://www.technologynetworks.com/proteomics/news/adhd-isnt-one-conditionbrain-scans-suggest-three-types-410256)  
9. Genome-wide analyses of ADHD identify 27 risk loci, refine the genetic architecture and implicate several cognitive domains. | Broad Institute, otwierano: maja 12, 2026, [https://www.broadinstitute.org/publications/broad1332711](https://www.broadinstitute.org/publications/broad1332711)  
10. Mapping ADHD Heterogeneity and Biotypes by Topological Deviations in Morphometric Similarity Networks \- PubMed, otwierano: maja 12, 2026, [https://pubmed.ncbi.nlm.nih.gov/41739459/](https://pubmed.ncbi.nlm.nih.gov/41739459/)  
11. Transcriptome profiling of dopaminergic neurons derived from an ADHD induced pluripotent stem cell (iPSC) model | bioRxiv, otwierano: maja 12, 2026, [https://www.biorxiv.org/content/10.1101/2024.09.22.614376v1.full-text](https://www.biorxiv.org/content/10.1101/2024.09.22.614376v1.full-text)  
12. Unraveling ADHD: genes, co-occurring traits, and developmental dynamics, otwierano: maja 12, 2026, [https://www.life-science-alliance.org/content/8/5/e202403029](https://www.life-science-alliance.org/content/8/5/e202403029)  
13. Pathway Analysis in Attention Deficit Hyperactivity Disorder: An Ensemble Approach \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4983253/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4983253/)  
14. ADGRL3 genomic variation implicated in neurogenesis and ADHD links functional effects to the incretin polypeptide GIP \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9508192/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9508192/)  
15. Integrative multi-omics data from early development to identify the genes and cell types underlying attention-deficit/hyperactivity disorder \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12312303/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12312303/)  
16. Multi-tissue transcriptome-wide association study identifies 29 risk genes associated with attention-deficit/hyperactivity disorder | medRxiv, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.64898/2026.02.16.26346287v1.full-text](https://www.medrxiv.org/content/10.64898/2026.02.16.26346287v1.full-text)  
17. Polygenic Risk Score (PRS) Tutorial, otwierano: maja 12, 2026, [https://odap-ico.github.io/PRS\_tutorial/](https://odap-ico.github.io/PRS_tutorial/)  
18. PRSice-2, otwierano: maja 12, 2026, [https://choishingwan.github.io/PRSice/step\_by\_step/](https://choishingwan.github.io/PRSice/step_by_step/)  
19. Psychiatric Polygenic Risk Scores as Predictor for Attention Deficit/Hyperactivity Disorder and Autism Spectrum Disorder in a Clinical Child and Adolescent Sample \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7355275/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7355275/)  
20. Associations of Polygenic Risk for Attention-Deficit/Hyperactivity Disorder with General and Specific Dimensions of Childhood Psychological Problems and Facets of Impulsivity \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10001434/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10001434/)  
21. Genome-wide analyses of ADHD identify 27 risk loci, refine the genetic architecture and implicate several cognitive domains \- Aarhus University \- Pure, otwierano: maja 12, 2026, [https://pure.au.dk/portal/en/publications/genome-wide-analyses-of-adhd-identify-27-risk-loci-refine-the-gen/](https://pure.au.dk/portal/en/publications/genome-wide-analyses-of-adhd-identify-27-risk-loci-refine-the-gen/)  
22. Genome-wide analyses of ADHD identify 27 risk loci, refine the ..., otwierano: maja 12, 2026, [https://pubmed.ncbi.nlm.nih.gov/36702997/](https://pubmed.ncbi.nlm.nih.gov/36702997/)  
23. CBC-UCONN/Polygenic-Risk-Score-Analysis \- GitHub, otwierano: maja 12, 2026, [https://github.com/CBC-UCONN/Polygenic-Risk-Score-Analysis](https://github.com/CBC-UCONN/Polygenic-Risk-Score-Analysis)  
24. Using polygenic scores in combination with symptom rating scales to identify attention-deficit/hyperactivity disorder \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11210094/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11210094/)  
25. PRSice-2 \- Basic Tutorial for Polygenic Risk Score Analyses, otwierano: maja 12, 2026, [https://choishingwan.github.io/PRS-Tutorial/prsice/](https://choishingwan.github.io/PRS-Tutorial/prsice/)  
26. Calculating Polygenic Risk Scores (PRS) in UK Biobank: A Practical Guide for Epidemiologists \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.818574/full](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.818574/full)  
27. Polygenic risk scores \- GWASTutorial \- GitHub Pages, otwierano: maja 12, 2026, [https://cloufield.github.io/GWASTutorial/10\_PRS/](https://cloufield.github.io/GWASTutorial/10_PRS/)  
28. Polygenic Risk and the Course of Attention-Deficit/Hyperactivity Disorder From Childhood to Young Adulthood: Findings From a Nationally Representative Cohort \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8417462/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8417462/)  
29. Polygenic Risk and the Course of Attention-Deficit/Hyperactivity Disorder From Childhood to Young Adulthood \- University of Edinburgh Research Explorer, otwierano: maja 12, 2026, [https://www.research.ed.ac.uk/files/303493495/1\_s2.0\_S0890856721000010\_main.pdf](https://www.research.ed.ac.uk/files/303493495/1_s2.0_S0890856721000010_main.pdf)  
30. Finding Order in the Complexity of ADHD: A Brain Imaging Study Identifies Three Neurobiological Subtypes, otwierano: maja 12, 2026, [https://www.adhdevidence.org/blog/finding-order-in-the-complexity-of-adhd-a-brain-imaging-study-identifies-three-neurobiological-subtypes](https://www.adhdevidence.org/blog/finding-order-in-the-complexity-of-adhd-a-brain-imaging-study-identifies-three-neurobiological-subtypes)  
31. Brain Imaging Study Reveals ADHD Biotypes \- Technology Networks, otwierano: maja 12, 2026, [https://www.technologynetworks.com/neuroscience/articles/is-adhd-actually-three-different-brain-conditions-410657](https://www.technologynetworks.com/neuroscience/articles/is-adhd-actually-three-different-brain-conditions-410657)  
32. There might be 3 different types of ADHD, new brain study suggests | National Geographic, otwierano: maja 12, 2026, [https://www.nationalgeographic.com/health/article/adhd-brain-study-three-subtypes](https://www.nationalgeographic.com/health/article/adhd-brain-study-three-subtypes)  
33. 3 Types of ADHD: What 2026 Brain Research Found \- LifeStance Health, otwierano: maja 12, 2026, [https://lifestance.com/blog/3-types-of-adhd-2026-brain-scan-research/](https://lifestance.com/blog/3-types-of-adhd-2026-brain-scan-research/)  
34. 3 Different Types of ADHD Identified in New Study. What to Know \- Healthline, otwierano: maja 12, 2026, [https://www.healthline.com/health-news/three-different-types-adhd-study](https://www.healthline.com/health-news/three-different-types-adhd-study)  
35. Mapping ADHD Heterogeneity and Biotypes by Topological Deviations in Morphometric Similarity Networks | Scilit, otwierano: maja 12, 2026, [https://www.scilit.com/publications/5e2e3fcb57b6baea97f8a840ec6b8e5d](https://www.scilit.com/publications/5e2e3fcb57b6baea97f8a840ec6b8e5d)  
36. We Could Be Missing A Key Detail About ADHD: New Data Suggests There Are 3 Distinct Types \- IFLScience, otwierano: maja 12, 2026, [https://www.iflscience.com/we-could-be-missing-a-key-detail-about-adhd-new-data-suggests-there-are-3-distinct-types-82725](https://www.iflscience.com/we-could-be-missing-a-key-detail-about-adhd-new-data-suggests-there-are-3-distinct-types-82725)  
37. Attention-deficit/hyperactive disorder updates \- Frontiers, otwierano: maja 12, 2026, [https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2022.925049/full](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2022.925049/full)  
38. Genetic Insights Into ADHD Biology \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5999780/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5999780/)  
39. Understanding the Different Types of ADHD: What Parents Should Know, otwierano: maja 12, 2026, [https://www.brownhealth.org/be-well/understanding-different-types-adhd-what-parents-should-know](https://www.brownhealth.org/be-well/understanding-different-types-adhd-what-parents-should-know)  
40. The Genetics of ADHD: A review of polymorphisms in neurotransmitter system genes \- Rollins Scholarship Onlin, otwierano: maja 12, 2026, [https://scholarship.rollins.edu/cgi/viewcontent.cgi?article=1000\&context=olin\_excellence](https://scholarship.rollins.edu/cgi/viewcontent.cgi?article=1000&context=olin_excellence)  
41. Hot gene list \- ADHDgene Database, otwierano: maja 12, 2026, [http://adhd.psych.ac.cn/topGene.do](http://adhd.psych.ac.cn/topGene.do)  
42. Associative gene networks reveal novel candidates important for ADHD and dyslexia comorbidity \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10478365/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10478365/)  
43. Fundamental Elements in Autism: From Neurogenesis and Neurite Growth to Synaptic Plasticity \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5701944/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5701944/)  
44. Hyperactivity and inattention (ADHD): Genetics | Encyclopedia on Early Childhood Development, otwierano: maja 12, 2026, [https://www.child-encyclopedia.com/hyperactivity-and-inattention-adhd/according-experts/adhd-and-genetics](https://www.child-encyclopedia.com/hyperactivity-and-inattention-adhd/according-experts/adhd-and-genetics)  
45. Understanding ADHD: 2.1.3 Candidate genes and dopamine | OpenLearn \- Open University, otwierano: maja 12, 2026, [https://www.open.edu/openlearn/health-sports-psychology/understanding-adhd/content-section-2.1.3](https://www.open.edu/openlearn/health-sports-psychology/understanding-adhd/content-section-2.1.3)  
46. Dopamine genes and attention-deficit hyperactivity disorder: a review \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC161723/](https://pmc.ncbi.nlm.nih.gov/articles/PMC161723/)  
47. ADHD gene traced \- UChicago Medicine, otwierano: maja 12, 2026, [https://www.uchicagomedicine.org/forefront/news/adhd-gene-traced](https://www.uchicagomedicine.org/forefront/news/adhd-gene-traced)  
48. An Overview on the Genetics of ADHD \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC2854824/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2854824/)  
49. Molecular Genetics of Attention Deficit Hyperactivity Disorder \- PMC \- NIH, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC2847260/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2847260/)  
50. Common and Unique Genetic Background between Attention-Deficit/Hyperactivity Disorder and Excessive Body Weight \- MDPI, otwierano: maja 12, 2026, [https://www.mdpi.com/2073-4425/12/9/1407](https://www.mdpi.com/2073-4425/12/9/1407)  
51. Attention deficit hyperactivity disorder (ADHD) and genetics | Health and Medicine | Research Starters \- EBSCO, otwierano: maja 12, 2026, [https://www.ebsco.com/research-starters/health-and-medicine/attention-deficit-hyperactivity-disorder-adhd-and-genetics](https://www.ebsco.com/research-starters/health-and-medicine/attention-deficit-hyperactivity-disorder-adhd-and-genetics)  
52. Genetic Influences on ADHD Symptom Dimensions: Examination of A Priori Candidates, Gene-based Tests, Genome-wide Variation, and SNP Heritability \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5690554/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5690554/)  
53. The 5-HT2A serotonin receptor in executive function: Implications for neuropsychiatric and neurodegenerative diseases | Request PDF \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/295098907\_The\_5-HT2A\_serotonin\_receptor\_in\_executive\_function\_Implications\_for\_neuropsychiatric\_and\_neurodegenerative\_diseases](https://www.researchgate.net/publication/295098907_The_5-HT2A_serotonin_receptor_in_executive_function_Implications_for_neuropsychiatric_and_neurodegenerative_diseases)  
54. Exploration of 19 serotoninergic candidate genes in adults and children with attention-deficit/hyperactivity disorder identifies \- Universitat de Barcelona, otwierano: maja 12, 2026, [https://www.ub.edu/geneticaclasses/brucormand/pdfs/44.pdf](https://www.ub.edu/geneticaclasses/brucormand/pdfs/44.pdf)  
55. Understanding Adult ADHD Through Genetics \- Neurobiologix, otwierano: maja 12, 2026, [https://neurobiologix.com/blogs/blogs/understanding-adult-adhd-through-genetics](https://neurobiologix.com/blogs/blogs/understanding-adult-adhd-through-genetics)  
56. Literature Genes List \- ADHDgene Database, otwierano: maja 12, 2026, [http://adhd.psych.ac.cn/LiteratureGene.do](http://adhd.psych.ac.cn/LiteratureGene.do)  
57. Gene group: 5-hydroxytryptamine receptors (HTR), otwierano: maja 12, 2026, [https://www.genenames.org/data/genegroup/\#\!/group/171](https://www.genenames.org/data/genegroup/#!/group/171)  
58. Impact of the ADHD-susceptibility gene CDH13 on development and function of brain networks \- PubMed, otwierano: maja 12, 2026, [https://pubmed.ncbi.nlm.nih.gov/22795700/](https://pubmed.ncbi.nlm.nih.gov/22795700/)  
59. Expression profile of the ADHD risk gene ADGRL3 during human neurodevelopment and the effects of genetic variation | bioRxiv, otwierano: maja 12, 2026, [https://www.biorxiv.org/content/10.1101/2025.01.29.635411v1.full-text](https://www.biorxiv.org/content/10.1101/2025.01.29.635411v1.full-text)  
60. Expression profile of the ADHD risk gene ADGRL3 during human neurodevelopment and the effects of genetic variation \- bioRxiv, otwierano: maja 12, 2026, [https://www.biorxiv.org/content/10.1101/2025.01.29.635411v1.full.pdf](https://www.biorxiv.org/content/10.1101/2025.01.29.635411v1.full.pdf)  
61. Multi-tissue transcriptome-wide association study identifies 29 risk genes associated with attention \- medRxiv, otwierano: maja 12, 2026, [https://www.medrxiv.org/content/10.64898/2026.02.16.26346287v1.full.pdf](https://www.medrxiv.org/content/10.64898/2026.02.16.26346287v1.full.pdf)  
62. The positive end of the polygenic score distribution for ADHD: a low risk or a protective factor? | Psychological Medicine, otwierano: maja 12, 2026, [https://www.cambridge.org/core/journals/psychological-medicine/article/positive-end-of-the-polygenic-score-distribution-for-adhd-a-low-risk-or-a-protective-factor/57B77249FD800E9299F0301DA745B603](https://www.cambridge.org/core/journals/psychological-medicine/article/positive-end-of-the-polygenic-score-distribution-for-adhd-a-low-risk-or-a-protective-factor/57B77249FD800E9299F0301DA745B603)  
63. Investigating regions of shared genetic variation in attention deficit/hyperactivity disorder and major depressive disorder: a GWAS meta-analysis \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8016853/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8016853/)  
64. Association of Polygenic Risk for Attention-Deficit/Hyperactivity Disorder With Co-occurring Traits and Disorders \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6278881/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6278881/)  
65. ADHD Inattention and Hyperactivity-Impulsivity: Neural Pathways \- ADDitude, otwierano: maja 12, 2026, [https://www.additudemag.com/adhd-inattention-hyperactivity-impulsivity-neural-pathways/](https://www.additudemag.com/adhd-inattention-hyperactivity-impulsivity-neural-pathways/)  
66. Identification of biotypes in Attention-Deficit/Hyperactivity Disorder, a report from a randomized, controlled trial \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9148272/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9148272/)  
67. Exploring the relationship between admixture and genetic susceptibility to attention deficit hyperactivity disorder in two Latin American cohorts \- PMC, otwierano: maja 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11269173/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11269173/)  
68. Exploring the relationship between admixture and genetic susceptibility to attention deficit hyperactivity disorder in two Latin American cohorts \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/380394350\_Exploring\_the\_relationship\_between\_admixture\_and\_genetic\_susceptibility\_to\_attention\_deficit\_hyperactivity\_disorder\_in\_two\_Latin\_American\_cohorts](https://www.researchgate.net/publication/380394350_Exploring_the_relationship_between_admixture_and_genetic_susceptibility_to_attention_deficit_hyperactivity_disorder_in_two_Latin_American_cohorts)  
69. (PDF) Common and rare variant analyses implicate late-infancy cerebellar development and immune genes in ADHD \- ResearchGate, otwierano: maja 12, 2026, [https://www.researchgate.net/publication/392865206\_Common\_and\_rare\_variant\_analyses\_implicate\_late-infancy\_cerebellar\_development\_and\_immune\_genes\_in\_ADHD](https://www.researchgate.net/publication/392865206_Common_and_rare_variant_analyses_implicate_late-infancy_cerebellar_development_and_immune_genes_in_ADHD)  
70. A Genome-Wide Association Meta-Analysis of Attention-Deficit/ Hyperactivity Disorder Symptoms in Population-Based Paediatric Cohorts \- e-Repositori UPF, otwierano: maja 12, 2026, [https://repositori.upf.edu/bitstreams/8528f85b-77ae-47f2-ac63-e9aede30591d/download](https://repositori.upf.edu/bitstreams/8528f85b-77ae-47f2-ac63-e9aede30591d/download)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAYCAYAAABwZEQ3AAACSUlEQVR4Xu2V26tNURTGP6HcQhzkTskTdZwnl6KkCIlSygPxIKHjdEpykhJ5EEmSeBEvlAdRlCSUa4oiSlEnKQ/+CH7fHmueNfc6l9pbkdpf/dp7jTnnWGOOMeZcUkstNa9hMAkmVAf+trrhG/yCI5Wxf6JV8APWVQca1Ha4ochy0zoAb2Fexd6IRsG1Av9vSsnJLRhXGWtEM+CN/rDU0+El9MACWA/T6maUmgprYTmMLGzegOdvgu+wpZiXxpP8vET1a/vJ/fITXsFh2AlPYUM2x0HehYuKl3XBZUVWt8FpeAG9cAFOwHwvLLQCHsJe2A134BOsyebU5H5x827MbOdVlm0RvIdOxRVgtSlK6wxYQ/VLB7yDzZnNpfwC7ZlNI+CK+veLg3Gm5sBVRS/MLcYcwCnYpzK4wfrFPu3bWR2f2c/AI5ic2fr6xWlNmgj34DmshM+Ke+i1wulRxY5SIJZL7Tn+zZVaIA8y+T+neh81p05X3h8L4YOiP1YrnLmUQ+mgBr4avM7r8yBddm9wR2arycF4x3nt3GC9sEzR/V8VJ6iq0TBcZb/chDGKk+LszVQE4xc7gKStCp/27T7q61X3wRNYWjzPhsewX5FC19mlqfaCHTlzvmldd9c/zXGW9yjWO7MfVW7W/n1S3Y+z4KSiEjV5wS64D2cVgTgz3nHSYnigOMo+wg7uOIwtxu3jEDyDS8X/dI/49xjcVhwKHwZnwtW4rjLoOjnVA11USQ5uSkEeaC5/8Qf76tvuLKYX+335c0st/d/6DahzZZXwd7VEAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAYCAYAAADtaU2/AAAB8ElEQVR4Xu2VzSuFURDGRygKiUI+r5IspFhISuwo2VmztZCVjWyUCAsfyUbJQkkpC7GSJB8pIUQRJdkpG38Az3PPPe65855XKVbuU7/ozHnPzJkzM1ckqf+uPNAGukA1SE2w/rJSQDPYAiugO8YqOAD18a1fygTz4Bl8xOD/l+AdXIBxUGI/0EoHw+BYgg5omwK3oE7ZrGrBHVgEac46HW6CfVDmrEfFgyfADWhQNium+xqMicmMVqeY2/ZpA9QvIbZe8Bb7G6ZcsA12Qb6yUaPgBTSpdQbJp6DjHtdQCc7AHihwDUrW8QkoVLYssC7+oCrAqZjzi13DoJhohtxFjyLgXPyO7TPo96XTNTHFWuWsf0X6Clpdg0e0c98GyFa2DjEVfCjmPO55FBMovwu0IiPnDRgto/5OfENmhhnS8r1vOTgCyyDDWY/KOvalz1WpmD6+AjXKZrNGJ7pG5sS0GFstQSwEFsR3jlmVA2JSGWgHCX9fW4xMd8RZj4obFySYJlfsaw4ODhD2u1ZY/9qAQi/FScSDZyR4cIuY0TcinncSkw0OFF/gjeBJ4o5Z4ZOizuGIZEWy7O185qzeEeNcTyp+PAvuJXE+L0m84nPEtNKDmPOmJaRzWPJMD3+N2kGRBB3+VMwgL8UzOaiSSupv9QnfcmZ1l5X0LwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE4AAAAXCAYAAAClK3kiAAACh0lEQVR4Xu2XzasOURzHv/KShZcouYhIcVMKi5uklERIURYWIkUkJZSbZEUpJC95LYlYSBFLVhailI2ykKWy8Efw/fo903PmzDlznzmTuQvnU59uz8w89znzeWbOnAfIZDLdMpFuoiu97QvoCTpKl3v7/nuO04f0I93ibJ/f276IzqD36LCzP0Om0ecoh9tNrzuvj9EzzusgqrzL39gxU+keOtPf0WM6PUQv0ZN0bnl3I0LhzqMa7j6d5Gz7yzJ6gD6jP1F+U1fMojvpNfoVdvuEgiykb+heWGDNT+/oGvegBoTC6fz9cDpGx5ZQuG10hH7C+IXbSlfT2wiH0zd+BdVvX7fRE1hIsQ52NYa8CDvfglbhCjRQDbhJOJ2wjKGn1hCd4O+oQZ8fCreYfoadiMt2+p2u8rYPQiicHhp+uJuoOYeUcEvpA9gt5DOZnqJHUfOhAWLhNtBfqIbTSf+GTepNCYXbSG+hf1VrztvX310lJZzQGugpyvFSo4lYuCJQLJy/fSw0P96AXa2vYGPV7a6xX4DF2gy72rQsiZIaTrjx2kQTsXAKEwqUGq4OjXs2nQObbmppE04onp7Ml5EeTcTCHUE40L8I14i24XSlaT54D5vIU4mFiwWKbe+MNuEU7RzsShumjxB+YAxCLNxa+gPVQEU4PV3HhdRwbrTi9tRaKTVeLNw8+gF2VbtoEv+C8vqsU4pwtWsWD0U7Sw+j+p7UeAqnhbh+bLvo/4/S1+g/5fT5d1FePnSG1kcaqH5u6ZKX3+hbusI5LsR6ehDVaAVL6Gk6xd/hoafXC9jnFmPQeDSu/c5xCvaY3oEtJ67Sl6hGzgTQ8kC/Enb0/o65XMhkMpnM4PwBL8mFRXdvj4EAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAAYCAYAAACoaOA9AAACrUlEQVR4Xu2YzasOYRjGL6HE8RFJx0ek2JBEoSOR7xIWLIWUUkREkliQSD6TfOx8LGRBqbM5oawshIUslKWysPEfcF3dz5x35jkz7zwzY16Lmat+vfM+z7xznuea+77nngO0alW3ZpEz5DIZIKOS083VTHKSjCPzyTuyK3FGg7WFfCOL3XdF0DMyfviMBmsCWUnGuu8XySNYJP0PTSQHyVVygsxIThfWErLOHyyj2eQ12epP9EhzyBDZA7s5G2Fpvix+UoCWk8NkkPwmR5LTxaXIuUB24N8XZF07L03HkGvkoTuOpDR/imKRLHNULjaR76hojhZ/jKxx31WY4wssK6XIcfKKrPDmfM0jnzByI9tgG1zqjYdIv+lqjhao8FTKSPrcjE4uK0oOwJzW2AJy1I2Xla5ziTyHmTI6OZ2qteQXRm5E6/pDdnvjIepqTh+ssJ0iH2DF9grs5LdkLllNfsIWEKEoKiNd7zp5QhahmMGRCf5GssZD1NWc9WQv7DGtx/VNMgX2qP5CFnZOrSRF2wOHjstIG0gzoTZz9sOMUd7+IKtgd1NptcEdl5V+q+hQlChaFDVVdAjpJtRmTiSl0xsyzZ+ooOmwmnIL1XsRKcuErPEQ5ZqjgvyC3EG1SElTPHpuo3xKSYpqRbe/kcgcRX9R5ZqjuqL6otpTp2SMepQyxVjqJ+9hUR6X1u3Xx8mOPOWaE683vVD8Ma5mLNQknXca1hNNcmPqv+6Tu+j0XboJn2FP37w6F5mT+fTVG7da8qn+RM3S3zsHS2k1lyG9jkx5TO7BerMb5CXsPweRdKz9qCdSyqVpH/kIe3WI2pOvsLWoVg5LbXdffKDH0outXiRDa4ZM1B3f7j6zTNX7lwxs5Ukpdh75adVIqUc7i/B61hgpanaiU7Rbteqh/gJhd3XAv6wFawAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAXCAYAAADtNKTnAAABA0lEQVR4Xu3TMUvDUBSG4a9gwUFBKlIoFjcnh+Ik6CSlSxcHuzp07iLo4FxaVAQHN6G7iJSORdE/4Ojk3h/iezjBcKMhydIpHzyEcC7k3HNvpDJllpx1tLEdvduzg/rvioys4RaX+MQQ1xjgAzvx0vQc4wx7+MY9NvCEL+zGS7NjHbxjM1nIG5vJFA+oJGq5Yy1b67attKzK6xP00ArLUhcLHCQLUaoY40Te6Ui+/SAXeEUtWYhiH5nJB76CR5wGK+St2lGn5U7xl23wzyp4apYr+b2xHOFF3lWhNOVbuMFc/8yjSGyodg3+zCMrh3jDFvbl96kRrMgR+wnP5SfYl1/MID/DqB+1pveqggAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAYCAYAAABtGnqsAAADfElEQVR4Xu2Y26tNURTGP7kk9wi5Hw94QLm8KOSE3Mndg0KehJQiiVAuuRUSSYgocj3JLXIpEYkXeVBKSXnwovwBfN8Ze7XnnnvOtc9eOJusX31xxpyWNb855hhzHSAnJycnJ+c/YxC1ldpPLaDalg5nYgbsmWn0o45T3f2Bf4lZ1CNqONWB2kRdpDq5k6qkP/WMOuIPOLSmDlEvqJ7e2D9DX+optdCJdaFuUyudWDXImIPUd6QbOIf6jBoZ2LmgNFpQbfygh4z7QI1wYvp3R6krsIysFhmznXqFuIHKUJWLs4gY2JGaDNthoT+nIDCxSnpTDdSPgh5T42GL9tHcRX7QYyfKDRRa+BuqzotXIjFmMMyYkIHKUBk8CjZeZqB2TQ/ZCNsFveReai2s1gwoTq0KFfbDsI1pCTNtKHWTOkX1KU5tHFtNzXViIbSAmIGheBoyZhs1GmZIzEDV3FWwdwwaOJFaRg2j3sMKperKJeotbHeyUEct8YMwM+fDnq1jp827R51AeiPQRmt+yKgsBrrGxAxU1z2A4nsFDVwBM28mrEiOgT1UR3hS4e9Z0H/ayw86tKemUutgC5exabSDbWrIqGoN9I0JGehmaELQwAQd3YdUN3/gF5D52oQLsMWn3dm6UmP9oEfMqFg8RCtqC0qNCRk4DcUMTYgaqCZyHdbNsmZcCL3AHWoprIOep54g3Ei0eM1LYzPCRmlhqt9qRJXQJVhrfenoNfWN+lT4eTm1w5sjaVzzNF8Xap2KRlTnVJNUC2MoczR+GtYt/UX49IDd7HUUXIZQd6kzsNKh3VT5uEENdOaFUFZ8oSY4Mb3XuYKS7FY5kFGxbPcJZWCIaAa69S+ETNgD65LKnN2wI5+GzFEdDaGFLYZl41fqGszYSuiY36I2ODGZruyb58SUyboYH4Md2Uooc/WMtBOouMaDma4Xug97wRAyuAHWnfVCJ1H6NdCcjKSeU2uo2bCvENU0N9PVnD7CPs/KssVBR1BHUUczuau+gx1hF/2seDJH80uOsDIi7RavT50k49RkLiP79eZ3oA5eD/sFQHL599GadsFKSc1R8dbFWoyjrsKy8W9GHwC6hjTlCP9xdG/Ssd0Hu/RWqn+1Rk1E5tV78ZqTFNJa1b+moro3HfGG0KzocvsAdi3QB7XuUGVdKCeOdnM9rFPrd266dOcU+AlUHKbD69ph6wAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAYCAYAAABtGnqsAAAD9UlEQVR4Xu2Y66tVVRTFh/jELCUxyQoNfAQqaJ9CCyXDygp8C1oqgiAqRlCIJH3pLYKFBBEViWLiG/GVr25EUShBREEg+EXwgx/9A2r87tz7nnX23fvccx/cq3gGDO49a6+z91pjzTnm3EdqoYUWWmihhfsMU8yd5i5zmTmi/nJTGGwuND/O+Jqq7/OguVHxvDezz/csXjWvmDPNUeZ283vzoXRSFxhqfmC+bT5pvm5eNy+ZTyTzwHPmz+ZKc7y52fxa1WLf1XhcsZnlydgY84y5IRnrCs+bh8xHk7EV5h1ztzkkG3vKvGYuzj4/Yv5i/qYQs98wOmMjDDKHFQcLQDgiZVYyxvf2mkcUEdkMtpr/KcTKMcG8qhAIoRCR65fNsdkcnsUaVmfXO0BOv6A4YcBf/KG3KrOok4rFwh8VKcFCimAuUdAI76uzgOBz8w9zUmG8CrPNH8w3kjH2SmTl0TVRIehX5nBznPmwStbOqWGO7yi+wCI/UZwSXsONegI84jPFwWDYPHi6eUrhIY/VprZfw1vyVKkCQlUJWDbeHTxj3jS/Uax9nnnb/E6hzybzC/OE4rA7gB+sNWeY/5p7FL6CR/xlTq1N7RYmmauKgwoxlyruTdqxuPPml2pcCDho5pcJ1VsBKSrs+x/z6WzsRUXWpPdlHgIfVGIX6xXivaI4AU6CiCCFF2T/9wSIkZp0EQ8oFrlNsUCEbYSRikMtE6q3AlLZsQCiLkcu4D7VV1wyk8hM57aD1E0Nsy+A+BzCAcXmG/Vs+Mvc4mABVUJVjTcDIu6cwhdTYD1UZe6dIi9A/O0AReS4opr1NOLKgG+cNdcoqtd+s03lhYTNM68RdqhcKDaJf9d5UxNAPDyNXhBQWSlkdAy5pTUlID6HJ+GFVSByuI4H8JDiJoqgFdip8I0U0xQn/q1ikVQ87CPdSBVeMm+pPn1YF2mWphp2QNWsinZAw0yFTRtnsg9PJqCwIAoec9KWpTSFU/8rAyJ8pKiSRM6HipRvBMTBR8vAxujs2xSLOaYQtiuQ5qcVbxA5EJ3oW5KMEcmkH1Wzrl/LwKHxzL/N3xP+qShm+XfWmT+p1t6VFhHAgi4oFlgGBD6pqM7cnFNJ3wb6E3jVr+YWxfsrbyHvqj7SKQA3FE1xWS+bp2EZsYkcFDqqMxlDR8GBoFPxda89IuoULWC3ahFHmB9Wz9ubvgAbm28uUi06imBPvO9iJb0BGTdZcVhz1NmSmgKnkpvms+ZRRTTezZhovqfyFO535Ib7qaLp7cr/BhoUEcSbXxgfcBDOtDoD5X/NAt97WZ1bpQEBze1FRVtA30S/2N1+674Gp/mWolLzm9s9/WtsX+N/CbGxHxiVbZYAAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAABFUlEQVR4Xu2TsUoDURBFb9DCQisRQVBCEPsUClY2gpbiB9j4CxamFhtBJPgFgtj4ATaKlaiICgoWgmAjKWwEPyCecXaf7Jg1jUWKHDgs7H379s3MrtTn35nDa/zEduYz3uIHtvAAp/MHytjCF6yH+zW8wHOcCFliGI/xDEdDZjTlJ1uKQU4V73APK8Uobf6Ks8Xoh2V5D9ZiACvyPmzjYMgSDfkbFnE8cxI38B5XcSBfHMmP+CAvYSdzV96TTRxJqztQVXn9U/IJnOBYyBJ/1W/YBCy38jpSNn9jCA/xHRdC9k23+c/Lm3skX/uLGXzEfRXrt47bkZ/wVD6RArbzlfxbty/M5nwj/yfs+oaXuC4vo0/P8QUHKzcYJfPaIwAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAYCAYAAAAlBadpAAAA3klEQVR4Xu3SPwtBURzG8TMYDMhEklWZZFCUsnoP3oDNe2CTkmw2C0oZlJcgFgoxmAw2i/IC+N4/p65fF7cMlvvUZznPOaf761yl/PyUEja442E7YGuvndBAWB9wSxsXFMR6VlkXDRESnRnj1ikWiInOODDBFWXRmUljjz4Cootirty/ykxFWfPVZEHyOGOGyGtlpancbzY2j7FDTnRm9Exn9NCydbFGB0m9WUbPO0IKcYegY59r9Lx1WXiJMe/bZ/gU/b5LJET3NRkcMVAe5tMpYoWbev2fq85Nfv6dJ5xHLCD/+2t8AAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAYCAYAAAD+vg1LAAABdUlEQVR4Xu2UsStFYRjGX6EMbilJKbrdZDAxUCwURSbJbGEwsRhYDGQhSWaDEslgYyGTkFCUQSmLDBblD+B5vN93Ot+be4/rmORXv273e84993zPec8R+efP0A7P4Rt8d97DS/gKn+EGbPQ/KJZ5+ABbzXoOnsBjWGeyRCrhLjyC1SYjq6I76bNBEll4BVdgSRhFf/oI28IomX7RjkdsAAZFe16AZSZLZEb0inphrbMeTsFrOARL/cHfxW/1RrSKReeyaOfTMBMdXQRZyd9vg+hEHMAakxHezE676CnUL+FEMGdNcdg3K+w26xH55pdUwE34ArtMVpCk+e0Qvalbosd6+NAswUlYHluPaIK3cE3CfjkB3PodPBSdEA+fvjH3uQ+bY9nnlZyJvgv4RHFOL0TfGfx8gqdwVLSOOBxF7o7V7cCqME4Pb/ZXk5QKnownHbZBWljFHmyxQVp4wm35pX55E9fhBJyD42H8c9jrAJyFPe57wAd4mUK4E2A06wAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAXCAYAAADHhFVIAAAAjklEQVR4XmNgGOSAG4jTgVgFXQIEMoD4PxDHoUuAgDAQWwMxK7oETsAMxAZAbAFlwwHIiCYgLgLirUBcjyzpAMSFQMwLxKuBeDoDmm4QKAHi00Asjy4BcuVeIG4FYkY0OQYnIH4ExPZArMoAMQUOOhkgjhFigASEA7KkBwPEvnlAnMaAxWgeIOZHFxxUAACehhAoXpfmZQAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,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>

[image13]: <data:image/png;base64,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>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAYCAYAAAAoG9cuAAAAuklEQVR4XmNgGGaAFYgjgdgcXQIZuADxZyBuRpdABtxA7ADEvGjixANmIDYAYisGiLswAB8QTwHiDCCeB8TzgZgDWQEjEFcAsSWUD3LwCSAWh6sAAmEgLgBiFiDmAuIVQLyQAc0kZKAAxOeAOB9NHAXYA/EjKI0TVDJATFJAE4cDkBtAbqHcPaA4e86AxT0xQBzCAAntViDeD8RiKCqA4A4QzwViWwaIVT6o0hAwEYh3MECiQh1NjsoAAPgwGIfeUb8NAAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHQAAAAYCAYAAAArrNkGAAAFsElEQVR4Xu2Z14tlRRDGPzEgmDPmUYy4ihlFdGcNuOiawIQRRNQHA8ZFRUVdc85iABUDKuackMUVFQwP4oOiIOKbIIJ/gNaPOuWt26fPnbOwruPM/eBj51af26dvV9VX1b3SGGOMMcYYY4wxG7CS8UzjzuVABSsatzIeZtyu+bxCY+PvGY39jZ8av+jJucbtjUuMfyV+YNzUuGvzXNj/NL5kXFeOhY0txm5o7FNhX+PPxsMLewkc+KHxXuOxxluNLxoXGa9Lz81IELVs6EPGLZrP4Hbjb8YDm89E9X7Gz4y7NTZwj/F342SyAea5z/iThp8PHGJ8zLhOOdCB1eVOIQjOLcYydpEH52RhP06+zvmFfcZhQ+PDxg2SbW3jW3LnbZzsbCpO2iTZLpdv8qHJBsKhvxr3KcZWlgfRDoV9FE43vit/F++sAUl+QD53BGaANb8tz94ZDeTz7MI2x/i98RH5JgVw9PXGNZKNbGGTSxncw/hjM1Y6e9J4jtqb3oXNjI8aD5bPiSrUMGH82nhBYQcbyb9HUM5oHGncprBRd2rSRg08VcOOOE3tZ1c13mK8qxnLDmVDb9SwIowC77pKHjDUZhxaBlogxhfLm58M1rRTYZs1oH7WpLIGnFU6lM6SbjSyN48RLLAvcNJtcpkmyz6X19Japq1pfF2DZuxLeRPEHH3VYMahq352IRxKEACy+Kbm39LZ1DEyt+aMGsiqu+WNDgiHsj7WWQNHmo81cCr8w3hWfmiagYYTBRqlWnuqX4K1MJWslYjno66dLM9QkJ1Nhlyodvc5CkcbL9YguyLYcCrOHQWylXLygvxo9JFxvTS+ijzrMw5ouLxxktp9BljfeIY8AdgD+o7dh57oga762YUcAHSQZCCZBebKjz44m472CvULEkC0cpbMmRb8Vu1uledrRyDW8rSGgyC64byJ2OieJ5NteWBLecDHnmXMkXfsoWg8e7Pqz1ZBFNDI9K2fYELeWXJxQL2iuw2EszkWXan+xxTWcZ787FiC4GBO5s4g+7vWzHeyTHNUe03toPgvQAb27SkIujvU/u2dWNr6CaKu/SLvRnPzEQ7lQH9pMTYK1ExqZy0ScQ4SyhEmQAQ/K1eEEtTyNzVQHErC48Zv5MFL58tvoO5fpmEZxn6N8QkNS3Fp53fNMz6lwbUk/QJSGorEbzlGrmR8l5LA2J1qX7ywBr7Ls2VnjuxysuiFpa2fgGjnZuYrtY8K4exP5GfJPkA6nzceVQ40uEQuu1kuJ+QqgYOyQ2g2zjc+J9/AABvCeRrgjBPlG/eqcfPGjgO4MpyQ35ChMtTdmp3vHiE//7I+kN/BuwmiBc1negwCkvP8/Rq+qAHHy+ckCClhGfzumLcKzqDvGL/TcJ36Qd4tTpXeZAfHiFrNxaFke006S5BJyHbc8dKZ5kgk+/IaGX9PHkTz5TVxkXzN1EIy8Q15cOYGikDFFhchfN5aPgfOiUCmgaKGv2w8QQO5rtkJQgKWDEX2CRJuyeId/I4lckexT5GhrIu9K9e3rTwYmaOUYxzadbGyTMAC9jKuVg7Ix6ipNelclqBZiPejGPxosiDfTQdwCJ1vrp+sk0xBEjOQQqSf4CZARtkJfJQAB5fvwAH0ELW1PKl6x87YK2on1L/u0P8byKBn5HKHchAMbDwXEjvKb8LYzPc1kHVkG2ejIjU7wEZG4TQcTtnYWy6tSGRWMByItKNuSDHdbIkcIBlkbO1qc9aCThuZwxkHNTYkDgfQFOFcFOVquURyIXGtXAG67AAHkW2nyK82keSF8vrI2INyZ+BYOvhQLeajnJRApukJyqxmztwQjiHfzLIM1GxrVWygy05DFs1XOR81kcwvLzP478lopAI4EWeW9ZO5sVNWxpimwOmc32mq6JoXyzOQGlx2v/Pkd+RjTHMgyUgxTiVbKQdkcwbPXKS6MvyDvwFmLxfN3jN1twAAAABJRU5ErkJggg==>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAYCAYAAAB+zTpYAAADs0lEQVR4Xu2Y2atOURiHX5nnKUTmkDJEUiIcEiFChiJckSRu3HBBpgwpJEMilGQIpVDiQhIyhSgiN+7cKH8Av+e8ezn7rPMN+xxHZ8v3q6fz7bXXHtY7rXcfs4oqqqiiiir6TzRD/BA/y/BJjEmuyZuaiXFil9gr5ov2tWaUVwdxSCwWfUSviM41U6vVUawRB8Sm5LikjoivYkI03lysFC/EsOhcHtRC7BRbzA0zWFwT90S/1LxywohPrG5gBXBe0GTxUCw1v269OC3apObUUhdxSzwSPaNzqLs4b36zvAmnvxUXzaMQEYWxUcqJ7LxjHpFpzor7VuOs4eK5WJAcYy/shnOK2mek+CBOmUcEIu3aJb8x8D6rWUCeNFS8EndFt2RsrrmBD4ZJGTRLrIrGWor9oio5xjbcE4NjE4SdcOjy5HxBBY+vS40RGdvMb0D9oa7xO4/i/YLzecc94pu5obOK9faOxjA46R/WPUA8Mw/E1qKHuVPL2gWvpOsvdXer1fVo3sVCp4l35sFBBDZUo83raqfU2FRzx50zLx8E5DFxw7z+F1Sov9/NN7KP5tH8WYxNzWsMDRK3xdN6sKj6yvJi8cx/bb74kMINEY45IRZG45SRuKNi7hmrvQfUEhO5IF1/SZdLlv0lifi28WATKWTfe3OjN0TjxWOr2zUFA7PhpzuGDeaRXfB5of4yKShdf7MIT9ND5kVkHhlIq0adrI9CDSerye60wjcDLW1a2C62YbW4GYaJ+1/CPnQQWUQNz1KviS4WHDfxpSiYdimNMG/H+BvEdbRNDfk4ImvpEq5a3WeHbiuzgcv1v7F48e3mRX6KGGXuoJfm/eKy3zMLi6+rmWJePYjTNBaLZXHpRYeyR38crg/OLfoxkCgYMV0yg9jwbhY4V7REFKq/xcSLsXkMFJPESdHKfAFXLHu9bmyxuDdiempsiXkq07uHda1Ixtj1S601dApxlAatFg9E3+S44CbHTegY6BzwPtDaXBBdw6RIGJCadt08UkN9ooYftez1urFFVGE0NmWMSOtEJ3Q8ORfEBvXFPFvJxGIqVmeDyEKy9o65HXg2Hzn1+SwvKjaPw+YLYDGI+pel/v5N4dz+Yk5CiK5YZOFuK10OiUgytJQTeN4Q8xI20f6s364WXyt4iShAG807B6L4srnhacypr3nWAPPuqFSJaBLheV6M/x6tFTvMU4XxE2KzeWr+sSf/otjkWENVNJ4r8c0f78K8eMdoLI8i5Wdb0+0VFVX0j+gX/2W6eSgmuHsAAAAASUVORK5CYII=>