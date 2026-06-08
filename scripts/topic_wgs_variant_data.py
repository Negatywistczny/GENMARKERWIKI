#!/usr/bin/env python3
"""Ręcznie opracowane tabele wariantów §4 dla kart tematycznych z potwierdzonym WGS/BAM."""

from __future__ import annotations


def _r(gt: str, activity: str, impact: str, tone: str, star: bool = False) -> dict:
    return {
        "genotype": gt,
        "activity": activity,
        "impact": impact,
        "tone": tone,
        "star": star,
    }


def _tbl(heading: str, wgs_gt: str, rows: list[dict]) -> dict:
    return {"heading": heading, "wgs_gt": wgs_gt, "rows": rows}


VARIANT_TABLES: dict[str, list[dict]] = {
    "ADGRL3": [
        _tbl(
            "rs1397547 (eQTL LPHN3, synaptogeneza glutaminergiczna)",
            "CC",
            [
                _r("TT", "Niższa ekspresja LPHN3", "Allel referencyjny; słabsza modulacja tworzenia synaps glutaminergicznych w korze — typowy profil bez eQTL ryzyka ADHD.", "positive"),
                _r("CT", "Pośrednia ekspresja", "Heterozygota eQTL; umiarkowany wpływ na plastyczność synaptyczną i ryzyko ADHD w kohortach latynoskich.", "neutral"),
                _r("CC", "Wyższa ekspresja LPHN3", "Homozygota allelu eQTL powiązanego z ADHD; wzmocniona synaptogeneza glutaminergiczna i wyższy wkład w neurorozwojowy PRS.", "negative", star=True),
            ],
        ),
        _tbl(
            "rs6551665 (intron ADGRL3, tag GWAS)",
            "GG",
            [
                _r("GG", "Allel major GWAS", "Typowy haplotyp locus 4q13.1; brak obciążenia tag-SNP w metaanalizie PGC ADHD 2023.", "positive", star=True),
                _r("AG", "Pośredni tag", "Heterozygota; niewielki wkład poligeniczny bez silnego efektu fenotypowego w izolacji.", "neutral"),
                _r("AA", "Allel alternatywny", "Homozygota alternatywna; możliwy niewielki wzrost wkładu PRS ADHD w modelach ścieżkowych adhezji.", "negative"),
            ],
        ),
    ],
    "ASTN2": [
        _tbl(
            "rs6470054 (ASTN2, migracja neuronów / locus ADHD–OCD)",
            "GA",
            [
                _r("GG", "Allel referencyjny", "Brak obciążenia wspólnym locus ASTN2 dla ADHD i OCD; typowa migracja neuronów w rozwoju korowym.", "positive"),
                _r("GA", "Heterozygota ryzyka", "Pośredni wkład w neurorozwojowy PRS; korelacja z cieńszą korą w badaniach obrazowych ADHD.", "neutral", star=True),
                _r("AA", "Homozygota alternatywna", "Silniejszy sygnał GWAS w locus 9q22; wyższe ryzyko współwystępowania ADHD z cechami kompulsywnymi.", "negative"),
            ],
        ),
        _tbl(
            "rs1857050 (ASTN2, stabilność białka)",
            "TT",
            [
                _r("TT", "Ekspresja referencyjna", "Homozygota referencyjna ASTN2; prawidłowe prowadzenie aksonów w korze i móżdżu.", "positive", star=True),
                _r("CT", "Pośrednia", "Heterozygota; umiarkowany wpływ na plastyczność obwodów fronto-cerebellar.", "neutral"),
                _r("CC", "Alternatywna", "Homozygota alternatywna; potencjalnie obniżona stabilność astrotaktyny 2 w rozwoju OUN.", "negative"),
            ],
        ),
    ],
    "CHRNA4": [
        _tbl(
            "rs1044396 (CHRNA4, α4 nAChR — modulacja dopaminy)",
            "GG",
            [
                _r("GG", "Standardowa α4", "Homozygota referencyjna; typowa modulacja uwalniania dopaminy przez układ cholinergiczny — profil Biotypu 1 bez nadreaktywności nAChR.", "positive", star=True),
                _r("AG", "Pośrednia α4", "Heterozygota; umiarkowana wrażliwość na nikotynę i lekka tendencja do impulsywności motorycznej.", "neutral"),
                _r("AA", "Obniżona funkcja α4", "Homozygota alternatywna; słabsza kontrola motoryczna i wyższa skłonność do poszukiwania stymulacji (RDS) w modelach cholinergicznych.", "negative"),
            ],
        ),
        _tbl(
            "rs2273502 (CHRNA4, ekspresja w korze)",
            "TT",
            [
                _r("CC", "Niższa ekspresja", "Homozygota referencyjna; mniejsza ekspresja CHRNA4 w korze przedczołowej.", "positive"),
                _r("CT", "Pośrednia", "Heterozygota; profil pośredni pod względem uwagi cholinergicznej.", "neutral"),
                _r("TT", "Wyższa ekspresja α4", "Homozygota alternatywna; wzmocniona sygnatura cholinergiczna Biotypu 1 (ciężki-mieszany) w modelu scoringu molekularnego.", "negative", star=True),
            ],
        ),
    ],
    "CHRNA7": [
        _tbl(
            "rs2064070 (CHRNA7, α7 nAChR — uwaga i P50)",
            "TT",
            [
                _r("CC", "Standardowy α7", "Homozygota referencyjna; prawidłowa modulacja P50 i filtrowania bodźców sensorycznych.", "positive"),
                _r("CT", "Pośredni α7", "Heterozygota; umiarkowane ryzyko deficytu uwagi w testach neurofizjologicznych.", "neutral"),
                _r("TT", "Obniżona funkcja α7", "Homozygota alternatywna; osłabiony układ cholinergiczny α7 powiązany z deficytem uwagi i skłonnością do przeciążenia sensorycznego (Biotyp 1).", "negative", star=True),
            ],
        ),
        _tbl(
            "rs6494223 (CHRNA7, tag locus 15q13)",
            "CC",
            [
                _r("CC", "Allel referencyjny", "Typowy haplotyp CHRNA7; brak dodatkowego obciążenia tag-SNP w PRS ADHD.", "positive", star=True),
                _r("CT", "Heterozygota", "Pośredni wkład poligeniczny w locus 15q13.3.", "neutral"),
                _r("TT", "Alternatywna", "Homozygota alternatywna; potencjalnie wyższy wkład w neurorozwojowy score cholinergiczny.", "negative"),
            ],
        ),
    ],
    "CNR1": [
        _tbl(
            "rs2023239 (CNR1, CB1 — ekspresja receptora)",
            "TT",
            [
                _r("TT", "Ekspresja referencyjna CB1", "Homozygota referencyjna; typowa gęstość CB1 w jądrach podstawnych — profil impulsywności bez nadreaktywności endokannabinoidowej.", "positive", star=True),
                _r("CT", "Pośrednia CB1", "Heterozygota; umiarkowana modulacja sygnalizacji endokannabinoidowej w obwodach nagrody.", "neutral"),
                _r("CC", "Obniżona ekspresja CB1", "Homozygota alternatywna; zmieniona regulacja apetytu i impulsywności — skłonność do Biotypu 2 (nadpobudliwy).", "negative"),
            ],
        ),
        _tbl(
            "rs806368 (CNR1, intron — zależność od kannabinoidów)",
            "TC",
            [
                _r("TT", "Allel referencyjny", "Homozygota referencyjna; niższe ryzyko zaburzeń używania kannabinoidów w metaanalizach.", "positive"),
                _r("TC", "Heterozygota", "Pośrednia wrażliwość CB1; umiarkowane powiązanie z impulsywnością i reaktywnością na stres.", "neutral", star=True),
                _r("CC", "Alternatywna", "Homozygota alternatywna; wyższe ryzyko uzależnienia od konopi i nasilenie objawów ADHD w kohortach europejskich.", "negative"),
            ],
        ),
    ],
    "DRD4": [
        _tbl(
            "rs1800955 (−521C>T, promotor DRD4)",
            "TC",
            [
                _r("CC", "Niższa ekspresja D4", "Homozygota −521C; niższa transkrypcja DRD4 w korze — mniejsza skłonność do poszukiwania nowości.", "positive"),
                _r("CT", "Pośrednia ekspresja D4", "Heterozygota −521C/T; umiarkowana ekspresja receptora D4 i pośredni profil poszukiwania nagrody.", "neutral", star=True),
                _r("TT", "Wyższa ekspresja D4", "Homozygota −521T; zwiększona ekspresja promotora DRD4 — wyższa reaktywność dopaminergiczna i skłonność do impulsywności (Biotyp 1–2).", "negative"),
            ],
        ),
        _tbl(
            "rs3758653 (synonimiczny SNP DRD4, nie VNTR 7R)",
            "TT",
            [
                _r("TT", "Haplotyp referencyjny", "Homozygota referencyjna rs3758653; brak tagowania allelu 7-repeat VNTR — typowa gęstość D4 w korze przedczołowej.", "positive", star=True),
                _r("CT", "Heterozygota", "Pośredni haplotyp; brak silnego powiązania z 7R — profil dopaminergiczny bez ekstremalnej hiporeaktywności.", "neutral"),
                _r("CC", "Alternatywna", "Homozygota alternatywna; możliwe powiązanie z wariantami DRD4 o zmienionej wrażliwości na dopaminę w badaniach asocjacyjnych.", "negative"),
            ],
        ),
    ],
    "DRD5": [
        _tbl(
            "rs1800762 (DRD5, −616C>G promotor)",
            "CC",
            [
                _r("CC", "Ekspresja referencyjna D5", "Homozygota −616C; typowa ekspresja DRD5 — najsilniejszy gen receptora dopaminowego w GWAS ADHD bez nadregulacji.", "positive", star=True),
                _r("CG", "Pośrednia D5", "Heterozygota; umiarkowany wkład w dopaminergiczny PRS ADHD.", "neutral"),
                _r("GG", "Wyższa ekspresja D5", "Homozygota −616G; zwiększona ekspresja DRD5 powiązana z wyższym ryzykiem ADHD w metaanalizach PGC.", "negative"),
            ],
        ),
        _tbl(
            "rs10033951 (DRD5, intron)",
            "CT",
            [
                _r("CC", "Allel referencyjny", "Homozygota referencyjna; niższy wkład tag-SNP w PRS dopaminergiczny.", "positive"),
                _r("CT", "Heterozygota", "Pośredni wkład w receptor D5; korelacja z cechami nieuwagi w podtypach ADHD.", "neutral", star=True),
                _r("TT", "Alternatywna", "Homozygota alternatywna; wzmocniony sygnał GWAS w locus 4p16.1 dla DRD5.", "negative"),
            ],
        ),
    ],
    "FOXP2": [
        _tbl(
            "rs2396753 (FOXP2, rozwój mowy)",
            "CA",
            [
                _r("CC", "Allel referencyjny", "Homozygota referencyjna FOXP2; typowy rozwój obwodów mowy i płynność językowa.", "positive"),
                _r("CA", "Heterozygota GWAS", "Pośredni wkład w neurorozwojowy PRS; możliwy wpływ na późny rozwój mowy i koordynację motoryczną w ADHD.", "neutral", star=True),
                _r("AA", "Alternatywna", "Homozygota alternatywna; wyższy wkład FOXP2 w ryzyko współwystępowania ADHD z trudnościami językowymi.", "negative"),
            ],
        ),
        _tbl(
            "rs7782412 (FOXP2, tag locus 7q31)",
            "TC",
            [
                _r("TT", "Referencyjny", "Homozygota referencyjna; brak dodatkowego obciążenia tag-SNP.", "positive"),
                _r("TC", "Heterozygota", "Pośredni haplotyp FOXP2; umiarkowany wpływ na rozwój korowy i komunikację.", "neutral", star=True),
                _r("CC", "Alternatywna", "Homozygota alternatywna; potencjalnie wyższy wkład w neurorozwojowy score mowy.", "negative"),
            ],
        ),
    ],
    "GRM5": [
        _tbl(
            "rs362990 (GRM5, mGluR5 — glutaminian/nagroda)",
            "TT",
            [
                _r("CC", "Niższa aktywność mGluR5", "Homozygota referencyjna; mniejsza modulacja glutaminergiczna w jądrach podstawnych.", "positive"),
                _r("CT", "Pośrednia mGluR5", "Heterozygota; umiarkowany wpływ na impulsywność i poszukiwanie nagrody.", "neutral"),
                _r("TT", "Wyższa aktywność mGluR5", "Homozygota alternatywna; wzmocniona sygnatura glutaminergiczna Biotypu 2 — wyższa reaktywność obwodów nagrody.", "negative", star=True),
            ],
        ),
        _tbl(
            "rs362584 (GRM5, ekspresja w striatum)",
            "AA",
            [
                _r("GG", "Ekspresja referencyjna", "Homozygota referencyjna GRM5; typowa ekspresja mGluR5 w striatum.", "positive"),
                _r("AG", "Pośrednia", "Heterozygota; profil pośredni w modelu glutaminergic/cannabinoid score.", "neutral"),
                _r("AA", "Allel alternatywny", "Homozygota alternatywna; wyższy wkład w Biotyp 2 (nadpobudliwy) w klasyfikacji molekularnej ADHD.", "negative", star=True),
            ],
        ),
    ],
    "HRH3": [
        _tbl(
            "rs3743419 (HRH3, autoreceptor histaminowy H3)",
            "GG",
            [
                _r("CC", "Standardowy H3", "Homozygota referencyjna; prawidłowa modulacja histaminy w OUN i rytmie dobowym.", "positive"),
                _r("CG", "Pośredni H3", "Heterozygota; umiarkowane ryzyko zaburzeń snu i uwagi w Biotypie 1.", "neutral"),
                _r("GG", "Obniżona funkcja H3", "Homozygota alternatywna; osłabiona hamująca rola H3 — tendencja do nadmiernej histaminy synaptycznej i deficytu uwagi (sygnatura Biotypu 1).", "negative", star=True),
            ],
        ),
        _tbl(
            "rs16840066 (HRH3, tag ekspresji)",
            "AA",
            [
                _r("AA", "Ekspresja referencyjna", "Homozygota referencyjna; typowa ekspresja HRH3 bez neurozapalnej sygnatury.", "positive", star=True),
                _r("AG", "Pośrednia", "Heterozygota; umiarkowany wpływ na modulację czujności.", "neutral"),
                _r("GG", "Alternatywna", "Homozygota alternatywna; potencjalnie wyższy wkład w cholinergic/histaminergic score ADHD.", "negative"),
            ],
        ),
    ],
    "HTR1B": [
        _tbl(
            "rs6296 (G861C, HTR1B autoreceptor)",
            "CC",
            [
                _r("CC", "G861/G861 (referencja)", "Homozygota G861; typowa autoregulacja serotoniny 1B — mniejsza skłonność do agresji impulsywnej i inuatywności.", "positive", star=True),
                _r("CG", "G861/C861", "Heterozygota G861C; pośredni profil serotoninergiczny z umiarkowaną impulsywnością.", "neutral"),
                _r("GG", "C861/C861", "Homozygota alternatywna; wzmocniona autoregulacja 5-HT1B powiązana z agresją, inuatywnością i Biotypem 1 (emocjonalnym).", "negative"),
            ],
        ),
        _tbl(
            "rs6297 (3′UTR HTR1B)",
            "TT",
            [
                _r("CC", "Referencyjny UTR", "Homozygota referencyjna; stabilna ekspresja HTR1B postsynaptycznie.", "positive"),
                _r("CT", "Pośredni UTR", "Heterozygota; umiarkowany wpływ na regulację nastroju i impulsywność.", "neutral"),
                _r("TT", "Alternatywny UTR", "Homozygota alternatywna; zmieniona stabilność mRNA HTR1B — wyższe ryzyko cech ADHD emocjonalnych w badaniach asocjacyjnych.", "negative", star=True),
            ],
        ),
    ],
    "HTR2A": [
        _tbl(
            "rs6311 (−1438G>A, promotor HTR2A)",
            "CT",
            [
                _r("CC", "Niższa ekspresja 5-HT2A", "Homozygota −1438G; niższa transkrypcja HTR2A — mniejsze ryzyko działań niepożądanych SSRI, słabszy marker Biotypu 3.", "positive"),
                _r("CT", "Pośrednia ekspresja 5-HT2A", "Heterozygota −1438G/A; umiarkowana ekspresja receptora 2A — pośrednia odpowiedź na SSRI i profil uwagi (CPIC).", "neutral", star=True),
                _r("TT", "Wyższa ekspresja 5-HT2A", "Homozygota −1438A; zwiększona ekspresja 5-HT2A — wyższe ryzyko nudności przy SSRI i silniejsza sygnatura Biotypu 3 (inuatywny).", "negative"),
            ],
        ),
        _tbl(
            "rs6313 (T102C, HTR2A — linkage z H452Y)",
            "GA",
            [
                _r("GG", "Allel T102 (referencja)", "Homozygota T102; typowa gęstość receptorów 5-HT2A w korze — profil bez obniżonej odpowiedzi na leki serotoninergiczne.", "positive"),
                _r("GA", "Heterozygota T102/C102", "Pośrednia gęstość 5-HT2A; umiarkowane ryzyko słabszej odpowiedzi na SSRI i deficytu elastyczności poznawczej.", "neutral", star=True),
                _r("AA", "Homozygota C102", "Homozygota C102; obniżona gęstość 5-HT2A w badaniach post-mortem — wyższe ryzyko oporności na SSRI i nasilony Biotyp 3.", "negative"),
            ],
        ),
    ],
    "HTR4": [
        _tbl(
            "rs2013162 (HTR4, receptor 5-HT4)",
            "CC",
            [
                _r("CC", "Ekspresja referencyjna 5-HT4", "Homozygota referencyjna; typowa modulacja nastroju i neurogenezy hipokampalnej — profil Biotypu 1 bez nadregulacji serotoninergicznej.", "positive", star=True),
                _r("CT", "Pośrednia 5-HT4", "Heterozygota; umiarkowany wpływ na stabilność emocjonalną i uwagę.", "neutral"),
                _r("TT", "Alternatywna 5-HT4", "Homozygota alternatywna; zmieniona ekspresja HTR4 powiązana z wyższym wkładem w PRS ADHD emocjonalnego.", "negative"),
            ],
        ),
        _tbl(
            "rs6440851 (HTR4, tag locus 5q32)",
            "CC",
            [
                _r("TT", "Referencyjny tag", "Homozygota referencyjna tag-SNP; niższy wkład poligeniczny.", "positive"),
                _r("CT", "Heterozygota", "Pośredni haplotyp HTR4.", "neutral"),
                _r("CC", "Alternatywny tag", "Homozygota alternatywna; wzmocniona korelacja przestrzenna ze zmianami mózgu w Biotypie 1 (Kompendium ADHD).", "negative", star=True),
            ],
        ),
    ],
    "LSM6": [
        _tbl(
            "rs13107325 (LSM6, TWAS kora/móżdżek)",
            "CT",
            [
                _r("CC", "Allel referencyjny", "Homozygota referencyjna LSM6; typowa ekspresja w neuronach pobudzających i hamujących bez TWAS ryzyka.", "positive"),
                _r("CT", "Heterozygota TWAS", "Pośredni wkład genotypu przyczynowego TWAS 2026 w neurorozwojowy PRS ADHD.", "neutral", star=True),
                _r("TT", "Alternatywna TWAS", "Homozygota alternatywna; wyższy wkład LSM6 w ryzyko ADHD w analizach transkryptomicznych (kora, móżdżek).", "negative"),
            ],
        ),
    ],
    "MDFIC": [
        _tbl(
            "rs10246939 (MDFIC, jądra podstawne — impulsywność)",
            "CC",
            [
                _r("TT", "Referencyjny MDFIC", "Homozygota referencyjna; typowa regulacja transkrypcji w jądrach podstawnych.", "positive"),
                _r("CT", "Heterozygota", "Pośredni wkład TWAS; umiarkowana plejotropia z impulsywnością.", "neutral"),
                _r("CC", "Alternatywna TWAS", "Homozygota alternatywna; gen przyczynowy TWAS powiązany z impulsywnością i agresją (Biotyp 2) w jądrach podstawnych.", "negative", star=True),
            ],
        ),
    ],
    "MED8": [
        _tbl(
            "rs2797285 (locus 1p34.2 — MED8/TWAS)",
            "GG",
            [
                _r("AA", "Referencyjny haplotyp", "Homozygota referencyjna locus 1p34.2; niższy wkład GWAS bez nadregulacji mediatora transkrypcji.", "positive"),
                _r("AG", "Heterozygota", "Pośredni wkład poligeniczny w regionie MED8/RPS26/TIE1.", "neutral"),
                _r("GG", "Alternatywna GWAS", "Homozygota alternatywna rs2797285; wzmocniony sygnał metaanalizy PGC ADHD 2023 w locus 1p34.2.", "negative", star=True),
            ],
        ),
    ],
    "MPL": [
        _tbl(
            "rs139606423 (MPL, TWAS — podziały komórkowe OUN)",
            "CC",
            [
                _r("TT", "Referencyjny MPL", "Homozygota referencyjna; typowa ekspresja trombopoetyny w OUN bez TWAS ryzyka.", "positive"),
                _r("CT", "Heterozygota TWAS", "Pośredni wkład nowego genu ryzyka TWAS 2026 w kora, jądra podstawne i móżdżek.", "neutral"),
                _r("CC", "Alternatywna TWAS", "Homozygota alternatywna; gen przyczynowy MPL powiązany z podziałami komórkowymi i neurorozwojowym PRS ADHD.", "negative", star=True),
            ],
        ),
    ],
    "NKX2-2": [
        _tbl(
            "rs16969968 (NKX2-2, różnicowanie oligodendrocytów)",
            "GA",
            [
                _r("GG", "Referencyjny NKX2-2", "Homozygota referencyjna; prawidłowe różnicowanie gleju i integralność białej materii.", "positive"),
                _r("GA", "Heterozygota TWAS", "Pośredni wkład TWAS w białą materię i jądra podstawne — umiarkowane ryzyko neurorozwojowe.", "neutral", star=True),
                _r("AA", "Alternatywna TWAS", "Homozygota alternatywna; wzmocniony sygnał TWAS NKX2-2 dla ADHD — potencjalny wpływ na mielinizację obwodów uwagi.", "negative"),
            ],
        ),
    ],
    "PTPRF": [
        _tbl(
            "rs10996110 (PTPRF, synaptogeneza / TWAS kora)",
            "GG",
            [
                _r("GG", "Allel referencyjny GWAS", "Homozygota referencyjna lead-SNP PTPRF; typowa stabilność synaps w korze płodowej i dorosłej.", "positive", star=True),
                _r("AG", "Heterozygota", "Pośredni wkład genotypu causal TWAS; umiarkowany wpływ na selektywną śmierć neuronów.", "neutral"),
                _r("AA", "Alternatywna GWAS", "Homozygota alternatywna; wyższy wkład PTPRF w neurorozwojowy PRS i ryzyko destabilizacji synaps.", "negative"),
            ],
        ),
    ],
    "RPS26": [
        _tbl(
            "rs3760707 (RPS26, biogeneza rybosomów — mózg płodowy)",
            "TT",
            [
                _r("TT", "Ekspresja referencyjna", "Homozygota referencyjna RPS26; prawidłowa biogeneza rybosomów w mózgu płodowym — typowy profil GWAS 2023.", "positive", star=True),
                _r("CT", "Heterozygota", "Pośredni wkład locus 12q13.2 w pan-biotypowy PRS ADHD.", "neutral"),
                _r("CC", "Alternatywna GWAS", "Homozygota alternatywna; potencjalnie wyższe ryzyko zaburzeń ekspresji białek synaptycznych w rozwoju.", "negative"),
            ],
        ),
    ],
    "SLC6A2": [
        _tbl(
            "rs3785157 (SLC6A2/NET, transport noradrenaliny)",
            "TT",
            [
                _r("CC", "Wyższa ekspresja NET", "Homozygota referencyjna; skuteczniejsze wychwytywanie noradrenaliny — lepsza kontrola wykonawcza, niższe ryzyko Biotypu 3.", "positive"),
                _r("CT", "Pośrednia NET", "Heterozygota; umiarkowana dostępność noradrenaliny w korze czołowej.", "neutral"),
                _r("TT", "Obniżona ekspresja NET", "Homozygota alternatywna; słabsze wychwytywanie noradrenaliny — deficyt funkcji wykonawczych, wysoka odpowiedź na atomoksetynę (Biotyp 3).", "negative", star=True),
            ],
        ),
        _tbl(
            "rs5569 (SLC6A2, promotor NET)",
            "AA",
            [
                _r("GG", "Standardowy promotor", "Homozygota referencyjna; typowa transkrypcja NET bez epistazy z ADRA2A.", "positive"),
                _r("AG", "Pośredni promotor", "Heterozygota; umiarkowane ryzyko błędów prowokacyjnych (commission errors) w interakcji z ADRA2A.", "neutral"),
                _r("AA", "Obniżona ekspresja NET", "Homozygota alternatywna rs5569; obniżona ekspresja transportera — wzmocniona sygnatura noradrenergiczna Biotypu 3 i słabsze hamowanie impulsów.", "negative", star=True),
            ],
        ),
    ],
    "SORCS3": [
        _tbl(
            "rs139885610 (SORCS3, lead GWAS 2023)",
            "GG",
            [
                _r("GG", "Allel referencyjny lead-SNP", "Homozygota referencyjna rs139885610; najsilniejszy hit GWAS bez alternatywnego allelu ryzyka — typowa plastyczność synaptyczna SORCS3.", "positive", star=True),
                _r("AG", "Heterozygota", "Pośredni wkład SORCS3 w pan-biotypowy PRS; wspólny czynnik ryzyka ADHD, ASD i MDD.", "neutral"),
                _r("AA", "Alternatywna GWAS", "Homozygota alternatywna; wyższy wkład w glutamatergic synaptic plasticity score.", "negative"),
            ],
        ),
        _tbl(
            "rs56163402 (SORCS3, tag locus 10q25)",
            "GG",
            [
                _r("AA", "Referencyjny tag", "Homozygota referencyjna tag-SNP; niższy wkład poligeniczny w SORCS3.", "positive"),
                _r("AG", "Heterozygota", "Pośredni haplotyp locus 10q25.1.", "neutral"),
                _r("GG", "Alternatywny tag GWAS", "Homozygota alternatywna rs56163402; wzmocniony sygnał asocjacji z ADHD w metaanalizie PGC 2023.", "negative", star=True),
            ],
        ),
    ],
    "TIE1": [
        _tbl(
            "rs2797285 (locus 1p34.2 — TIE1, rozwój naczyniowy OUN)",
            "GG",
            [
                _r("AA", "Referencyjny haplotyp", "Homozygota referencyjna; typowy rozwój naczyniowy mózgu bez GWAS obciążenia TIE1.", "positive"),
                _r("AG", "Heterozygota", "Pośredni wkład wspólnego locus 1p34.2 (MED8/RPS26/TIE1).", "neutral"),
                _r("GG", "Alternatywna GWAS", "Homozygota alternatywna rs2797285; wyższy wkład w neurorozwojowy PRS — wspólny wariant z MED8 w tym samym locus.", "negative", star=True),
            ],
        ),
    ],
}
