# Uruchom gleboka analize BAM w WSL (HLA, VNTR, CNV) i wstrzyknij do raportu.
param(
    [switch]$ApplyOnly
)

$ErrorActionPreference = "Stop"
$Root = "C:\Users\kacpe\Documents\GitHub\GENMARKERWIKI"
$Runner = "/mnt/c/Users/kacpe/Documents/GitHub/GENMARKERWIKI/scripts/wsl_deep_genomics.sh"

if (-not $ApplyOnly) {
    Write-Host "[wsl] Uruchamianie analizy (moze trwac godziny)..." -ForegroundColor Cyan
    wsl.exe -e bash -lc "chmod +x '$Runner' && bash '$Runner'"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Blad WSL. Jesli WSL nie jest zainstalowany, uruchom jako Admin:" -ForegroundColor Red
        Write-Host "  .\scripts\install_wsl_bio.ps1" -ForegroundColor Yellow
        exit 1
    }
}

Set-Location $Root
python scripts/apply_bam_genotypes_to_report.py
python scripts/count_mini_stars.py
