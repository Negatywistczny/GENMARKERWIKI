### 1. Nagłówek i Nazwy
* **Główny symbol genu:** MC4R
* **Pełna nazwa biochemiczna:** Receptor melanokortyny 4; kontrola apetytu (ang. *Melanocortin 4 receptor*)

### 2. Identyfikator (rsID) i Charakterystyka Wariantu
* **Główny rsID:** rs17782313
* **Lokalizacja chromosomalna:** chr18q21.32
* **Powiązane markery:** rs9939609

### 3. Mechanizm działania
* **Rola biologiczna genu/białka:** Zrozumienie składowej metabolicznej w biotypie melancholicznym pozwala na lepsze zarządzanie chorobami współistniejącymi, które często pogarszają rokowanie w MDD.37 ## **Techniczne aspekty obliczania prawdopodobieństwa biotypów w analizie kodu genetycznego** Aby program analizujący dane genetyczne mógł skutecznie wskazać prawdopodobieństwo występowania każdego z biotypów, musi on operować na znormalizowanych wagach pochodzących z odpowiednich baz GWAS oraz stosować rygorystyczną kontrolę jakości (Quality Control \- QC). ### **Algorytm obliczeniowy i formuła PRS** Standardowy model addytywny PRS obliczany jest według wzoru: gdzie: * to wynik ryzyka poligenicznego dla osoby .7 * to logarytm ilorazu szans (log-OR) dla allelu efektu wariantu pobrany z bazy PGC MDD2025.7 * to dawka allelu ryzyka (0, 1 lub 2\) u danej osoby.7 * to liczba markerów SNP uwzględnionych w modelu po procesie "clumpingu".41 ### **Standardowy format danych wejściowych (Base File)** Programy takie jak PRSice-2 wymagają pliku bazy (Base File) o określonej strukturze kolumnowej, aby poprawnie dopasować dane sumaryczne do danych genotypowych pacjenta.

<!-- topic-card -->