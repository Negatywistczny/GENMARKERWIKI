[Strona główna](../README.md) > [Dokumentacja](00_indeks.md) > [Standardy](STANDARDS.md)

---

# Standardy Inżynieryjne Projektu: GenMarkerWiki

Projekt funkcjonuje w oparciu o model architektoniczny **Single-App** ([`template-single-app`](https://github.com/kacperczeczot/template-single-app)) i bezwzględnie przestrzega reguł zdefiniowanych w centralnej Konstytucji **[`devex-standards`](https://github.com/kacperczeczot/devex-standards)**.

---

## 1. Zgodność ze Standardami Zewnętrznymi

| Standard | Implementacja w Projekcie | Oficjalna Specyfikacja |
| :--- | :--- | :--- |
| **Conventional Commits** | Commity w języku angielskim (`feat:`, `fix:`, `docs:`, `refactor:`) | [conventionalcommits.org](https://www.conventionalcommits.org/pl/v1.0.0/) |
| **Semantic Versioning** | SemVer (`MAJOR.MINOR.PATCH`) | [semver.org](https://semver.org/lang/pl/) |
| **ADR** | Rejestr Decyzji w [`docs/adr/`](adr/README.md) | [adr.github.io](https://adr.github.io/) |
| **EditorConfig** | [`.editorconfig`](../.editorconfig) w root dla spójności IDE | [editorconfig.org](https://editorconfig.org/) |

---

## 2. Bramki Jakościowe i Walidatory

- **Walidacja struktury kart genów:** `node scripts/verify_structure.mjs`
- **Walidacja mapowania tonów i wariantów:** `node scripts/verify-tones.mjs`
- **Audyt spójności Markdown:** `python3 scripts/audit_md_coherence.py`

---

## 3. Źródło Prawdy (SSOT)
👉 **[devex-standards / Architecture Rules](https://github.com/kacperczeczot/devex-standards/blob/main/docs/architecture/RULES.md)**
👉 **[devex-standards / Tooling Rules](https://github.com/kacperczeczot/devex-standards/blob/main/docs/tooling/RULES.md)**
