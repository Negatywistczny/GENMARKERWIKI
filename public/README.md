[Strona główna](../README.md) > [public](00_indeks.md)

---

# `public/` (Statyczna Przeglądarka Webowa)

* **Status:** ⚪ `[OPCJONALNY]`

Katalog zawiera bezserwerową, statyczną aplikację internetową do przeglądania i drukowania kart genów:

- [`index.html`](index.html) — strona główna z indeksem markerów, filtrami kategorii i listą rsID.
- `html/gene.html` — dynamiczny widok pojedynczej karty genu (np. `gene.html?gene=COMT`).
- `html/print.html` — widok zoptymalizowany do wydruku i generowania PDF.
- `html/style.css` — arkusz stylów interfejsu.
- `html/app.js` — logika renderowania i interpretacji wariantów.
