[Strona główna](../README.md) > [scripts](00_indeks.md)

---

# `scripts/` (Skrypty Narzędziowe i Walidatory)

* **Status:** ⚪ `[OPCJONALNY]`

Katalog zawiera skrypty Node.js, Python i powłoki (Bash/PowerShell) do automatyzacji bioinformatycznej, walidacji jakościowej oraz generowania raportów:

| Skrypt | Środowisko | Opis |
| :--- | :--- | :--- |
| [`verify_structure.mjs`](verify_structure.mjs) | Node.js | Waliduje obecność i kolejność 8 sekcji we wszystkich kartach genów |
| [`verify-tones.mjs`](verify-tones.mjs) | Node.js | Sprawdza mapowanie tonów kolorystycznych i wariantów w `public/html/` |
| [`audit_md_coherence.py`](audit_md_coherence.py) | Python 3 | Weryfikuje spójność kart Markdown, minikart oraz list genów w JS |
| [`generate_personal_report.py`](generate_personal_report.py) | Python 3 | Generuje kompleksowy raport genetyczny na podstawie surowych danych WGS |
| [`report_html.py`](report_html.py) | Python 3 | Konwertuje wygenerowany raport Markdown do formatu HTML |
