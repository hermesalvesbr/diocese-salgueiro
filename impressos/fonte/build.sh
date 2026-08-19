#!/usr/bin/env bash
# Regera os dois PDFs de impressão a partir do PDF oficial da encíclica.
# Requer: poppler-utils (pdftohtml), python3, google-chrome.
set -euo pipefail
cd "$(dirname "$0")"
PDF=../../20260515-magnifica-humanitas.pdf
OUT=..

pdftohtml -xml -f 33 -l 51 -i -nodrm "$PDF" ./rec51 >/dev/null
python3 build_texto.py rec51.xml blocos.json
python3 gera_html.py recorte.html
python3 gera_cartoes.py cartoes-out.html

chrome() { google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
           --virtual-time-budget=8000 --print-to-pdf="$1" "file://$PWD/$2" 2>/dev/null; }
chrome "$OUT/enciclica-recorte-cap3-cap4.pdf" recorte.html
chrome "$OUT/cartoes-tres-compromissos.pdf"   cartoes-out.html
chrome "$OUT/como-imprimir.pdf"                comoimprimir.html
chrome "$OUT/guia-do-facilitador.pdf"          guia.html
rm -f rec51.xml recorte.html cartoes-out.html blocos.json
echo "PDFs regerados em $OUT"
