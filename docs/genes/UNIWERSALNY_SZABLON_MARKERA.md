[Strona główna](../../README.md) > [genes](00_indeks.md) > [UNIWERSALNY_SZABLON_MARKERA](UNIWERSALNY_SZABLON_MARKERA.md)

---

### 1. Nagłówek i Nazwy
* **Główny symbol genu:** [SYMBOL] (ang. *[NAZWA_ANGIELSKA]*)
* **Pełna nazwa biochemiczna:** [PELNA_NAZWA_PL] (ang. *[PELNA_NAZWA_ANG]*)
* **Nazwy potoczne i medialne:** [NAZWA_1], [NAZWA_2], [NAZWA_3]
* **Synonimy medyczne (opcjonalnie):** [SYNONIM_1], [SYNONIM_2]

### 2. Identyfikator (rsID) i Charakterystyka Wariantu
* **Główny rsID:** [RSID_GLOWNY]
* **Lokalizacja chromosomalna:** [CHROMOSOM_LOKALIZACJA]
* **Typ wariantu:** [SNP/INDEL/VNTR/HAPLOTYP/INNE]
* **Zapis zmiany nukleotydowej (HGVS):** [HGVS_C], [HGVS_G jeśli dotyczy]
* **Orientacja nici i mapowanie alleli:** [PLUS_MINUS_LUB_ODWROCONY_ZAPIS]
* **Powiązane markery / haplotyp (opcjonalnie):** [RSID_1], [RSID_2], [HAPLOTYP]
* **Klasyfikacja bazowa (opcjonalnie):** [ClinVar/PharmVar/dbSNP + status]

### 3. Mechanizm działania
* **Rola biologiczna genu/białka:** [2-4 zdania o funkcji i tkankach docelowych]
* **Wpływ wariantu na szlak:** [2-5 zdań: co zmienia wariant i jaki jest efekt molekularny]
* **Efekt funkcjonalny:** [1-3 zdania: konsekwencja fizjologiczna]

### 4. Tabela Wariantów

**[RSID_GLOWNY] ([OPIS_WARIANTU])**

| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy (kliniczny i funkcjonalny) |
| :--- | :--- | :--- |
| **[GENOTYP_REF]** | [AKTYWNOSC_REF] | [OPIS_REF] |
| **[GENOTYP_HET]** | [AKTYWNOSC_HET] | [OPIS_HET] |
| **[GENOTYP_ALT]** | [AKTYWNOSC_ALT] | [OPIS_ALT] |

*Kolejność wierszy (obowiązkowa): **lewo** = homozygot referencyjny (allel dziki / major wg dbSNP), **środek** = heterozygota, **prawo** = homozygot alternatywny. Gwiazdka ★ **wyłącznie** na wierszu potwierdzonego genotypem właściciela bazy (`raw/ULCEDCBF2693.ai_full.csv`) — nigdy dla „klinicznie istotnego” allelu bez danych osobistych. W HTML ★ = badge „Twój wariant”.*

*Przy wielu SNP w jednym pliku: powtórz blok **rsID** + tabele 3-wierszowe dla każdego markera (nie łącz w jedną tabelę z kolumną „Identyfikator”).*

### 5. Statystyki populacyjne
* **Średnia globalna (ALL):** [CZESTOSC_ALLELU_LUB_GENOTYPU]
* **Europa (NFE):** [DANE]
* **Afryka (AFR):** [DANE]
* **Azja Wschodnia (EAS):** [DANE]
* **Uwagi o zmienności populacyjnej:** [1-2 zdania o niejednoznacznościach i ograniczeniach].

### 6. Wpływ na życie (Zalecenia)
* **[Obszar 1 — np. medycyna / profil ryzyka]:** [Konkretne ryzyko, monitoring, kiedy do specjalisty — na podstawie raportu].
* **[Obszar 2 — np. dieta / suplementacja]:** [Co wspierać, czego unikać; dawki tylko jeśli są w raporcie].
* **[Obszar 3 — np. styl życia / trening]:** [Praktyczne zalecenia z raportu].
* **[Obszar 4 — opcjonalnie farmakologia]:** [Leki, na które gen wpływa — jeśli dotyczy].
* **Ostrzeżenie kliniczne:** Materiał ma charakter informacyjny i nie zastępuje konsultacji lekarskiej.

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

## Reguły ściśle (obowiązkowe dla każdego pliku)
* Używaj zawsze dokładnie tych 8 sekcji i tej samej kolejności.
* W sekcji 2 zawsze podawaj rsID główny, lokalizację i zapis zmiany.
* W sekcji 4 zawsze stosuj 3-wierszową tabelę genotypów (homozygota referencyjna, heterozygota, homozygota wariantu), chyba że marker ma inną biologicznie uzasadnioną strukturę (wtedy opisz dlaczego).
* W sekcji 5 zawsze podawaj minimum 4 populacje: ALL, NFE, AFR, EAS.
* W sekcji 6 podawaj zalecenia ostrożnie, bez języka kategorycznego typu „zawsze”, „nigdy”, jeśli nie ma wysokiej jakości dowodów.
* W sekcji 8 podawaj minimum 3 publikacje z identyfikatorem PMID (jeśli brak — oznacz jawnie „PMID: do uzupełnienia” i nie zgaduj numeru).
* Nie mieszaj orientacji nici: jeśli raportujesz odwrotnie (np. C/T zamiast G/A), oznacz to jawnie w sekcji 2.
* Stosuj jednostki i liczby: %, OR, HR, CI — gdzie to możliwe.
* Jeśli dane są niejednoznaczne, wpisz to wprost („wyniki niespójne między kohortami”).
