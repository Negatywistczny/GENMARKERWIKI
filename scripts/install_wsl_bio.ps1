#Requires -RunAsAdministrator
<#
.SYNOPSIS
  Instaluje WSL2 + Ubuntu i uruchamia setup narzedzi bio (OptiType, CNVkit, ExpansionHunter).

.Użycie (PowerShell jako Administrator):
  Set-ExecutionPolicy -Scope Process Bypass
  .\scripts\install_wsl_bio.ps1
  # Po restarcie (jesli wymagany):
  .\scripts\install_wsl_bio.ps1 -SkipWslInstall
#>
param(
    [switch]$SkipWslInstall
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Fastq = "C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER"
$SetupSh = Join-Path $PSScriptRoot "wsl_bio_setup.sh"

function Test-WslReady {
    try {
        $v = wsl.exe --status 2>&1 | Out-String
        return $v -notmatch "nie zainstalowano" -and $v -notmatch "not installed"
    } catch { return $false }
}

if (-not $SkipWslInstall) {
    Write-Host "[1/4] Wlaczanie funkcji WSL i Virtual Machine Platform..." -ForegroundColor Cyan
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart | Out-Null
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart | Out-Null

    Write-Host "[2/4] Instalacja WSL2 (moze wymagac restartu)..." -ForegroundColor Cyan
    wsl.exe --install --no-distribution
    wsl.exe --set-default-version 2

    if (-not (wsl.exe -l -q 2>$null | Select-String "Ubuntu")) {
        Write-Host "[3/4] Pobieranie Ubuntu..." -ForegroundColor Cyan
        wsl.exe --install -d Ubuntu --no-launch
    }
} else {
    Write-Host "[skip] Pomijam instalacje WSL (-SkipWslInstall)" -ForegroundColor Yellow
}

if (-not (Test-WslReady)) {
    Write-Host ""
    Write-Host "WSL wymaga restartu Windows. Po restarcie uruchom:" -ForegroundColor Yellow
    Write-Host "  .\scripts\install_wsl_bio.ps1 -SkipWslInstall" -ForegroundColor White
    exit 0
}

Write-Host "[4/4] Kopiowanie setup do WSL i uruchamianie..." -ForegroundColor Cyan
$WslSetup = "/mnt/c/Users/kacpe/Documents/GitHub/GENMARKERWIKI/scripts/wsl_bio_setup.sh"
wsl.exe -e bash -lc "chmod +x '$WslSetup' && FASTQ_ROOT='$Fastq' GENMARKER_ROOT='$Root' bash '$WslSetup'"

Write-Host ""
Write-Host "Gotowe. Uruchom pipeline:" -ForegroundColor Green
Write-Host "  .\scripts\run_wsl_deep_genomics.ps1" -ForegroundColor White
