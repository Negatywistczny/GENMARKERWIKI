### 1. Nagłówek i Nazwy
* **Główny symbol genu:** [SYMBOL] (ang. *[NAZWA_ANGIELSKA]*)
* **Pełna nazwa biochemiczna:** [PELNA_NAZWA_PL] (ang. *[PELNA_NAZWA_ANG]*)
* **Nazwy potoczne i medialne:** [NAZWA_1], [NAZWA_2], [NAZWA_3]
* **Synonimy medyczne (opcjonalnie):** [SYNONIM_1], [SYNONIM_2]

### 2. Identyfikator (rsID) i Charakterystyka Wariantu
* **Główny rsID:** [RSID_GLOWNY]
* **Lokalizacja chromosomalna:** [CHROMOSOM_LOKALIZACJA]
* **Typ wariantu:** [SNP/INDEL/VNTR/HAPLOTYP/INNE]
* **Zapis zmiany nukleotydowej (HGVS):** [HGVS_C], [HGVS_G jesli dotyczy]
* **Orientacja nici i mapowanie alleli:** [PLUS_MINUS_LUB_ODWROCONY_ZAPIS]
* **Powiązane markery / haplotyp (opcjonalnie):** [RSID_1], [RSID_2], [HAPLOTYP]
* **Klasyfikacja bazowa (opcjonalnie):** [ClinVar/PharmVar/dbSNP + status]

### 3. Mechanizm działania
* **Rola biologiczna genu/białka:** [2-4 zdania o funkcji i tkankach docelowych]
* **Wpływ wariantu na szlak:** [2-5 zdań: co zmienia wariant i jaki jest efekt molekularny]
* **Efekt funkcjonalny:** [1-3 zdania: konsekwencja fizjologiczna]

### 4. Tabela Wariantow
| Genotyp / Uklad alleli | Nazewnictwo (np. Val/Met) | Aktywnosc / ekspresja | Wplyw fenotypowy (kliniczny i funkcjonalny) |
| :--- | :--- | :--- | :--- |
| **[GENOTYP_1]** | [NAZEWNICTWO_1] | [AKTYWNOSC_1] | [OPIS_1] |
| **[GENOTYP_2]** | [NAZEWNICTWO_2] | [AKTYWNOSC_2] | [OPIS_2] |
| **[GENOTYP_3]** | [NAZEWNICTWO_3] | [AKTYWNOSC_3] | [OPIS_3] |

### 5. Statystyki populacyjne
* **Średnia globalna (ALL):** [CZESTOSC_ALLELU_LUB_GENOTYPU]
* **Europa (NFE):** [DANE]
* **Afryka (AFR):** [DANE]
* **Azja Wschodnia (EAS):** [DANE]
* **Uwagi o zmiennosci populacyjnej:** [1-2 zdania o niejednoznacznosciach i ograniczeniach].

### 6. Wpływ na życie (Zalecenia)
* **Medycyna / profil ryzyka:** [KONKRETNE_RYZYKO + co monitorowac].
* **Dieta i suplementacja:** [CO_WLACZYC / CZEGO_UNIKAC].
* **Styl życia i trening:** [ZALECENIA_PRAKTYCZNE].
* **Farmakologia (jeśli dotyczy):** [INTERAKCJE_Z_LEKAMI].
* **Ostrzeżenie kliniczne:** [KIEDY_KONIECZNA_KONSULTACJA_LEKARSKA].

### 7. Ciekawostki
* [CIEKAWOSTKA_1 - 1 zdanie].
* [CIEKAWOSTKA_2 - 1 zdanie].
* [CIEKAWOSTKA_3 - 1 zdanie].

### 8. Źródła (Referencje)
* **PMID: [NUMER]** ([Autor et al., ROK]) – [Krótki opis znaczenia publikacji].
* **PMID: [NUMER]** ([Autor et al., ROK]) – [Krótki opis znaczenia publikacji].
* **PMID: [NUMER]** ([Autor et al., ROK]) – [Krótki opis znaczenia publikacji].
* **Baza referencyjna:** [SNPedia (rs[NUMER])](https://www.snpedia.com/index.php/Rs[NUMER]) – [Zakres adnotacji: częstości, fenotypy, haplotypy].

---

## Reguly scisle (obowiazkowe dla kazdego pliku)
* Uzywaj zawsze dokladnie tych 8 sekcji i tej samej kolejnosci.
* W sekcji 2 zawsze podawaj rsID glowny, lokalizacje i zapis zmiany.
* W sekcji 4 zawsze stosuj 3-wierszowa tabele genotypow (homozygota referencyjna, heterozygota, homozygota wariantu), chyba ze marker ma inna biologicznie uzasadniona strukture (wtedy opisz dlaczego).
* W sekcji 5 zawsze podawaj minimum 4 populacje: ALL, NFE, AFR, EAS.
* W sekcji 6 podawaj zalecenia ostroznie, bez jezyka kategorycznego typu "zawsze", "nigdy", jesli nie ma wysokiej jakosci dowodow.
* W sekcji 8 podawaj minimum 3 publikacje z identyfikatorem PMID (jesli brak - oznacz jawnie "PMID: do uzupełnienia" i nie zgaduj numeru).
* Nie mieszaj orientacji nici: jesli raportujesz odwrotnie (np. C/T zamiast G/A), oznacz to jawnie w sekcji 2.
* Stosuj jednostki i liczby: %, OR, HR, CI - gdzie to mozliwe.
* Jesli dane sa niejednoznaczne, wpisz to wprost ("wyniki niespojne miedzy kohortami").
