# -*- mode: sh; sh-shell: bash; -*-
# Google 'latexmk latexmkrc' for explanation of this config file
# or see https://mg.readthedocs.io/latexmk.html
# 
# latexmk at unix command line will compile the paper
system("[[ -e economics.bib         ]] && rm -f economics.bib"        );
system("[[ -e BufferStockTheory.bib ]] && rm -f BufferStockTheory.bib");
#$bibtex = 'bibtool -x %B.aux -o %B.bbl ';
$do_cd = 1;
$clean_ext = "bbl nav out snm dvi idv mk4 css cfg tmp xref 4tc out aux log fls fdb_latexmk synctex.gz toc svg png html 4ct ps out.ps upa upb lg yml css out snm bib\-save*";
$bibtex_use=2;
$pdf_mode = 1;
$rc_report = 1;
#@default_files = ('BufferStockTheory','BufferStockTheory-NoAppendix','BufferStockTheory-Slides','Introduction','Tables-All');
@default_files = ('BufferStockTheory','BufferStockTheory-NoAppendix','Appendices-All-Referenced','BufferStockTheory-Slides','Introduction');
#@default_files = ('BufferStockTheory');
$ENV{'BIBINPUTS'} = './@resources/texlive/texmf-local/bibtex/bst:' . ($ENV{'BIBINPUTS'} || '');
$pdflatex="pdflatex -interaction=nonstopmode %O %S";
$aux_out_dir_report = 1;
$silent  = 0;
$bibtex_use_original_exit_codes = 0;
system("\@resources/shell/bibtool_extract-used-refs-from-system-bib-and-add-refs.sh . BufferStockTheory");

