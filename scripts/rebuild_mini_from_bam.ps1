# Pełny rebuild minikart z genotypów BAM.
$ErrorActionPreference = "Stop"
$env:PATH = "C:\Users\kacpe\Documents\GitHub\FASTQ-CONVERTER\tools\bin;C:\msys64\mingw64\bin;" + $env:PATH
Set-Location (Split-Path -Parent $PSScriptRoot)

python scripts/apply_bam_genotypes_to_report.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/count_mini_stars.py
python scripts/audit_mini_cards.py
python scripts/report_lof_gene_status.py
