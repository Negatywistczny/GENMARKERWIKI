[Strona główna](../../README.md) > [Dokumentacja](../README.md) > [ADR](README.md) > [ADR 0001](0001-markdown-and-static-html-viewer.md)

---

# ADR 0001: Przechowywanie Kart Genów w Markdownie i Przeglądarka Vanilla JS

* **Status:** Zaakceptowany
* **Data:** 2026-06-05
* **Autorzy:** Kacper Czeczot

---

## Kontekst
Projekt wymagał stworzenia czytelnej, łatwej w edycji i przeszukiwaniu bazy wiedzy o polimorfizmach genetycznych SNP z możliwością generowania raportów osobistych oraz podglądu w przeglądarce i druku do PDF.

## Decyzja
1. **Markdown jako SSOT:** Każdy gen posiada dedykowaną kartę w formacie Markdown z 8 ścisłymi sekcjami.
2. **Vanilla JS / CSS Viewer w `public/`:** Lekka, bezserwerowa przeglądarka kart HTML (`public/index.html`, `public/html/gene.html`) z filtrami kategorii, wyszukiwarką rsID i widokiem druku.
3. **Skrypty automatyzacji w `scripts/`:** Skrypty Node.js i Pythona do weryfikacji struktury (`verify_structure.mjs`), spójności tonów (`verify-tones.mjs`) oraz generowania raportów.

## Konsekwencje
### Pozytywne:
- Karty są czytelne zarówno w edytorze kodu/Obsidianie, jak i w przeglądarce.
- Brak ciężkich zależności runtime — strona działa bezpośrednio z dysku lub GitHub Pages.
