---
name: Reguły Domenowe GenMarkerWiki
description: Standardy tworzenia i edycji kart polimorfizmów genetycznych SNP oraz raportów.
---

# Reguły Domenowe: GenMarkerWiki

Projekt stanowi ustandaryzowaną bazę wiedzy o polimorfizmach genetycznych SNP o udokumentowanym wpływie fenotypowym.

---

## 1. Wymogi dla Kart Genów (`docs/genes/`)
- Język: polski (precyzyjna terminologia biochemiczna i medyczna).
- Tabela wariantów (`### 4. Tabela Wariantów`) musi stosować nagłówek:
  `| Genotyp | Aktywność / ekspresja | Wpływ fenotypowy (kliniczny i funkcjonalny) |`
- Każda zmiana struktury kart musi przejść test: `node scripts/verify_structure.mjs`.

---

## 2. Standardy DevEx
Projekt bezwzględnie dziedziczy zasady czystości root i wzorce inżynieryjne z:
👉 **[devex-standards](https://github.com/kacperczeczot/devex-standards)**
