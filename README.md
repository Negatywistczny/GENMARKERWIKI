[Strona główna](README.md)

---

# GenMarkerWiki — Baza Wiedzy o Markerach Genetycznych

> Baza wiedzy, generator raportów i interaktywna przeglądarka polimorfizmów genetycznych (SNP) o znaczeniu funkcjonalnym, behawioralnym i metabolicznym.

---

## 1. Dokumentacja i Standardy

Projekt funkcjonuje w oparciu o model **Single-App** ([`template-single-app`](https://github.com/kacperczeczot/template-single-app)) i przestrzega standardów inżynieryjnych ekosystemu:

| Dokument / Sekcja | Opis |
| :--- | :--- |
| [Standardy Projektu (`docs/STANDARDS.md`)](docs/STANDARDS.md) | Deklaracja zgodności ze standardami DevEx i procedury testów |
| [Baza Dokumentacji (`docs/README.md`)](docs/README.md) | Centralny hub dokumentacyjny projektu |
| [Karty Genów (`docs/genes/`)](docs/genes/README.md) | Pełny katalog 50 kart markerów SNP z podziałem na kategorie |
| [Minikarty WGS (`docs/genes-mini/`)](docs/genes-mini/README.md) | Ponad 240 zwięzłych kart markerów WGS |
| [Rejestr Decyzji ADR (`docs/adr/`)](docs/adr/README.md) | Rejestr Decyzji Architektonicznych projektu |
| [Globalne Standardy DevEx (`devex-standards`)](https://github.com/kacperczeczot/devex-standards) | Nadrzędna Konstytucja inżynieryjna ekosystemu |
| [Reguły AI Projektu (`.agents/rules/project.md`)](.agents/rules/project.md) | Instrukcje domenowe dla asystentów AI |

---

## 2. Mapa Repozytorium

* 📁 [**`docs/`**](docs/README.md) — Dokumentacja techniczna, karty genów w formacie Markdown i rejestr ADR.
* 📁 [**`public/`**](public/README.md) — Statyczna przeglądarka internetowa (`index.html`, widok druku i karty).
* 📁 [**`data/`**](data/README.md) — Surowe pliki wejściowe (`raw/`) oraz generowane raporty (`reports/`).
* 📁 [**`scripts/`**](scripts/README.md) — Skrypty walidacyjne Node.js i generatory raportów w Pythonie.

---

## 3. Szybki Start i Weryfikacja

### Weryfikacja spójności kart:
```bash
# Sprawdzenie obecności 8 sekcji w kartach genów
node scripts/verify_structure.mjs

# Sprawdzenie mapowania tonów w przeglądarce
node scripts/verify-tones.mjs

# Audyt spójności Markdown i list JS
python3 scripts/audit_md_coherence.py
```

### Otwarcie przeglądarki:
Otwórz plik `public/index.html` bezpośrednio w dowolnej przeglądarce internetowej.
