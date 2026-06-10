#!/usr/bin/env bash
# HLA (OptiType), DAT1 VNTR (ExpansionHunter), CNV (CNVkit) -> CSV dla GENMARKERWIKI.
set -euo pipefail

FASTQ_ROOT="${FASTQ_ROOT:-/mnt/c/Users/kacpe/Documents/GitHub/FASTQ-CONVERTER}"
GENMARKER_ROOT="${GENMARKER_ROOT:-/mnt/c/Users/kacpe/Documents/GitHub/GENMARKERWIKI}"
WORK="${WSL_BIO_WORK:-${HOME}/wsl_bio}"
OUT_CSV="${GENMARKER_ROOT}/scripts/data/wsl_deep_genotypes.csv"
BAM="${FASTQ_ROOT}/BAM/F25A910000190-04_HOMnzpvR_ULCEDCBF2693_ULCEDCBF2693.bam"
REF="${FASTQ_ROOT}/.work/hg38.fa"
EH_VARIANTS="${WORK}/ExpansionHunter-v5.0.0-linux_x86_64/variant_catalog/grch38/variant_catalog.json"

[[ -f "${WORK}/env.sh" ]] && source "${WORK}/env.sh"
mkdir -p "${WORK}/optitype" "${WORK}/eh" "${WORK}/cnv" "$(dirname "$OUT_CSV")"

echo "[deep] BAM: $BAM"
[[ -f "$BAM" ]] || { echo "Brak BAM"; exit 1; }

: > "${OUT_CSV}.tmp"
write_row() {
  # GENE,PRIMARY_RSID,GENOTYPE,SOURCE,NOTES
  echo "$1,$2,$3,$4,$(echo "$5" | tr ',' ';')" >> "${OUT_CSV}.tmp"
}

# --- OptiType HLA (v1.5+ CLI) ---
if command -v optitype &>/dev/null; then
  echo "[deep] OptiType HLA (moze potrwac na pelnym BAM)..."
  mkdir -p "${WORK}/optitype/in" "${WORK}/optitype/out"
  ln -sf "$BAM" "${WORK}/optitype/in/sample.bam" 2>/dev/null || cp -l "$BAM" "${WORK}/optitype/in/sample.bam" 2>/dev/null || true
  optitype run -i "${WORK}/optitype/in" -o "${WORK}/optitype/out" --dna 2>&1 | tail -5 || true
  RES=$(ls -1 "${WORK}/optitype/out"/*_result.tsv 2>/dev/null | head -1 || true)
  if [[ -n "$RES" && -f "$RES" ]]; then
    HLA_B=$(awk -F'\t' 'NR==2{print $2}' "$RES" 2>/dev/null || true)
    HLA_C=$(awk -F'\t' 'NR==2{print $3}' "$RES" 2>/dev/null || true)
    [[ -n "$HLA_B" ]] && write_row "HLA-B" "OptiType" "$HLA_B" "wsl+optitype" "class I"
    [[ -n "$HLA_C" ]] && write_row "HLA-DQB1" "OptiType" "$HLA_C" "wsl+optitype" "proxy class II block"
  fi
else
  echo "[deep] OptiType niedostepny — pomijam HLA"
fi

DAT1_CATALOG="${GENMARKER_ROOT}/scripts/data/eh_dat1_catalog.json"

# --- ExpansionHunter DAT1 (tylko SLC6A3) ---
if command -v ExpansionHunter &>/dev/null && [[ -f "$REF" ]] && [[ -f "$DAT1_CATALOG" ]]; then
  echo "[deep] ExpansionHunter DAT1 (SLC6A3)..."
  ExpansionHunter \
    --reads "$BAM" \
    --reference "$REF" \
    --variant-catalog "$DAT1_CATALOG" \
    --output-prefix "${WORK}/eh/DAT1" 2>&1 | tail -3 || true
  EH_JSON="${WORK}/eh/DAT1.json"
  if [[ -f "$EH_JSON" ]]; then
    REPEAT=$(python3 <<PY
import json
d=json.load(open("${EH_JSON}"))
for locus in d.get("LocusResults", {}).values():
    for vid, v in locus.get("VariantResults", {}).items():
        g = v.get("Genotype", "")
        rep = v.get("RepeatUnit", "")
        if g:
            print(f"{g} ({vid})")
            break
PY
)
    [[ -n "$REPEAT" ]] && write_row "SLC6A3" "DAT1-VNTR" "$REPEAT" "wsl+eh" "ExpansionHunter SLC6A3"
  fi
else
  echo "[deep] ExpansionHunter niedostepny — pomijam VNTR"
fi

# --- CNV: samtools depth (pojedyncza probka, bez referencji kohorty) ---
if command -v samtools &>/dev/null; then
  echo "[deep] CNV depth scan..."
  while IFS=$'\t' read -r chrom start end gene; do
    [[ "$chrom" == chr* ]] || chrom="chr${chrom#chr}"
    mid=$(( (start + end) / 2 ))
    depth=$(samtools depth -a -r "${chrom}:${mid}-${mid}" "$BAM" 2>/dev/null | awk '{print $3}' | head -1)
    depth=${depth:-0}
    if (( depth < 4 )); then gt="deletion"
    elif (( depth > 45 )); then gt="duplication"
    else gt="diploid"; fi
    write_row "$gene" "depth-scan" "$gt" "wsl+depth" "depth=${depth}x at ${chrom}:${mid}"
  done <<'BED'
chr14	21385194	21456126	CHD8
chr10	87862638	87971930	PTEN
chr21	37365573	37526358	DYRK1A
chr13	42271470	42323283	AKAP11
chr12	49018975	49060794	KMT2D
chr6	31981991	32005247	C4A
BED
fi

# --- CNVkit (opcjonalnie, wymaga kohorty) ---
if false && command -v cnvkit.py &>/dev/null && [[ -f "$REF" ]]; then
  echo "[deep] CNVkit (batch target geny)..."
  TARGETS="${WORK}/cnv_targets.bed"
  cat > "$TARGETS" <<'BED'
chr14	21385194	21456126	CHD8
chr10	87862638	87971930	PTEN
chr21	37365573	37526358	DYRK1A
chr13	42271470	42323283	AKAP11
chr12	49018975	49060794	KMT2D
BED
  cnvkit.py batch "$BAM" -f "$REF" -t "$TARGETS" -d "${WORK}/cnv" --processes 4 --method amplicon 2>&1 | tail -10 || true
  for seg in "${WORK}/cnv"/*.cns; do
    [[ -f "$seg" ]] || continue
    python3 - "$seg" <<'PY'
import csv,sys
path=sys.argv[1]
with open(path) as f:
    for row in csv.DictReader(f, delimiter='\t'):
        gene=row.get('gene','')
        if not gene: continue
        log2=float(row.get('log2',0))
        if abs(log2)<0.3: gt='diploid'
        elif log2>0.3: gt='duplication'
        else: gt='deletion'
        print(f"{gene},CNVkit,{gt},wsl+cnvkit,log2={log2}")
PY
  done | while IFS= read -r line; do echo "$line" >> "${OUT_CSV}.tmp"; done
else
  echo "[deep] CNVkit niedostepny — pomijam CNV"
fi

if [[ -s "${OUT_CSV}.tmp" ]]; then
  echo "GENE,PRIMARY_RSID,ALL_RSIDS,GENOTYPE,SOURCE,NOTES" > "$OUT_CSV"
  while IFS= read -r line; do
    IFS=',' read -r g rs gt src notes <<< "$line"
    echo "${g},${rs},,${gt},${src},${notes}" >> "$OUT_CSV"
  done < "${OUT_CSV}.tmp"
  echo "[deep] Zapisano -> $OUT_CSV"
  # merge do missing_mini_wgs_from_bam.csv
  python3 "${GENMARKER_ROOT}/scripts/merge_wsl_deep_to_missing.py" "$OUT_CSV"
else
  echo "[deep] Brak nowych wynikow (narzedzia niegotowe lub analiza pusta)"
fi

rm -f "${OUT_CSV}.tmp"
