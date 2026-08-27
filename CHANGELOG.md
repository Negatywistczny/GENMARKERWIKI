# Dziennik Zmian (Changelog)

Wszystkie istotne zmiany w projekcie są dokumentowane w tym pliku zgodnie ze standardem [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/) oraz [Semantic Versioning](https://semver.org/lang/pl/).

---

## [Unreleased]

### Added
- Dostosowanie repozytorium do standardów inżynieryjnych DevEx (Single-App).
- Struktura dokumentacji `docs/` z certyfikatem `docs/STANDARDS.md` i rejestrem `docs/adr/`.
- Pliki konfiguracyjne: `.editorconfig`, `.cursorrules`, `.agents/rules/project.md`, `.github/pull_request_template.md`.

### Changed
- Reorganizacja struktury do Kanonu Root:
  - `md/` ➡️ `docs/genes/`
  - `md-mini/` ➡️ `docs/genes-mini/`
  - `raporty/` ➡️ `data/reports/`
  - `html/` + `index.html` ➡️ `public/`
- Zaktualizowanie ścieżek wejściowych i wyjściowych we wszystkich skryptach w `scripts/`.
- Wdrożenie nawigacji Breadcrumbs.

---

## [1.0.0] - 2026-06-14

### Added
- Baza 50 pełnych kart genów oraz ponad 240 minikart WGS.
- Bezserwerowa przeglądarka internetowa kart HTML/JS z wyszukiwarką rsID i widokiem druku.
- Skrypty automatyzacji walidacji strukturalnej i spójności tonów wariantów.
