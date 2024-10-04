#!/bin/bash

for f in BufferStockTheory BufferStockTheory-Slides BufferStockTheory-NoAppendix; do
    latexmk "$f"
done

cd Appendices

for f in *.tex; do
    latexmk "$f"
done

/Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-make/makePDF-Portable.sh /Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-Latest BufferStockTheory private bib . Resources
/Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-make/makePDF-Portable.sh /Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-Latest BufferStockTheory private bib . Resources
/Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-make/makePDF-Portable.sh /Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-Latest BufferStockTheory private bib . Resources
/Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-make/makePDF-Portable.sh /Volumes/Data/Papers/BufferStockTheory/BufferStockTheory-Latest BufferStockTheory private bib . Resources
