#!/usr/bin/env bash
# Setup OptiType + CNVkit + ExpansionHunter w WSL/Ubuntu.
set -euo pipefail

FASTQ_ROOT="${FASTQ_ROOT:-/mnt/c/Users/kacpe/Documents/GitHub/FASTQ-CONVERTER}"
GENMARKER_ROOT="${GENMARKER_ROOT:-/mnt/c/Users/kacpe/Documents/GitHub/GENMARKERWIKI}"
# Conda na dysku Linux (nie /mnt/c — case-insensitive psuje instalacje).
WORK="${WSL_BIO_WORK:-${HOME}/wsl_bio}"
CONDA="${WORK}/miniconda3"
echo "[wsl_bio] apt update..."
sudo apt-get update -qq
sudo apt-get install -y -qq wget bzip2 samtools tabix git build-essential

mkdir -p "$WORK"
cd "$WORK"

if [[ ! -x "${CONDA}/bin/conda" ]]; then
  echo "[wsl_bio] Miniconda..."
  wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
  bash miniconda.sh -b -p "$CONDA"
fi
# shellcheck disable=SC1091
source "${CONDA}/bin/activate"
conda config --set channel_priority strict
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main 2>/dev/null || true
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r 2>/dev/null || true
echo "[wsl_bio] conda env bio..."
if ! conda env list | grep -q "^bio "; then
  conda create -y -n bio python=3.11
fi
conda activate bio

pip install -q --upgrade pip
pip install -q cnvkit optitype-pipeline 2>/dev/null || pip install -q cnvkit 2>/dev/null || true

# OptiType v1.5+ (CLI: optitype, nie OptiTypePipeline.py)
if [[ ! -d "${WORK}/OptiType/.git" ]]; then
  git clone --depth 1 https://github.com/FRED-2/OptiType.git "${WORK}/OptiType"
fi
pip install -q "${WORK}/OptiType" 2>/dev/null || true

# ExpansionHunter (binarka Linux)
EH_VER="v5.0.0"
EH_DIR="${WORK}/ExpansionHunter-${EH_VER}-linux_x86_64"
if [[ ! -x "${EH_DIR}/bin/ExpansionHunter" ]]; then
  echo "[wsl_bio] ExpansionHunter ${EH_VER}..."
  wget -q "https://github.com/Illumina/ExpansionHunter/releases/download/${EH_VER}/ExpansionHunter-${EH_VER}-linux_x86_64.tar.gz" -O eh.tar.gz
  tar -xzf eh.tar.gz -C "$WORK"
fi
export PATH="${EH_DIR}/bin:${PATH}"

# Zapis PATH do pliku env
cat > "${WORK}/env.sh" <<EOF
export FASTQ_ROOT="${FASTQ_ROOT}"
export GENMARKER_ROOT="${GENMARKER_ROOT}"
export PATH="${EH_DIR}/bin:\${PATH}"
source "${CONDA}/bin/activate"
conda activate bio
EOF

echo "[wsl_bio] Weryfikacja narzedzi:"
command -v samtools && samtools --version | head -1
command -v cnvkit.py && cnvkit.py version 2>/dev/null | head -1 || echo "cnvkit: brak"
command -v ExpansionHunter && ExpansionHunter --version 2>&1 | head -1 || echo "ExpansionHunter: brak"
command -v optitype && optitype --help 2>&1 | head -1 || echo "optitype: brak"

echo "[wsl_bio] Setup zakonczony -> ${WORK}/env.sh"
