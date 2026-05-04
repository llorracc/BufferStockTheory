#!/bin/bash
perl -e '
sub run_pdftotext {
    foreach my $file (@ARGV) {
        my $pdf_file = "$file.pdf";
        my $txt_file = "$file.txt";
        
        if (-f $pdf_file) {
            print "Running pdftotext on $pdf_file...\n";
            system("/usr/local/bin/pdftotext", "-nopgbrk", $pdf_file, $txt_file);
            print "Converted $pdf_file to $txt_file\n";
        } else {
            print "PDF file $pdf_file not found\n";
        }
    }
}

run_pdftotext(@ARGV);
' "$@"

# Clean up auxiliary files after successful compilation (but preserve cross-ref files)
echo "Cleaning up auxiliary files (preserving cross-reference and bibliography files)..."
# Custom cleanup that excludes .xref, .bbl, and other files needed for cross-compilation
find . -name "*.aux" -delete 2>/dev/null || true
find . -name "*.log" -delete 2>/dev/null || true
find . -name "*.fls" -delete 2>/dev/null || true
find . -name "*.fdb_latexmk" -delete 2>/dev/null || true
find . -name "*.synctex.gz" -delete 2>/dev/null || true
# find . -name "*.out" -delete 2>/dev/null || true  # Preserve .out files for hyperlinks
find . -name "*.toc" -delete 2>/dev/null || true
find . -name "*.nav" -delete 2>/dev/null || true
find . -name "*.snm" -delete 2>/dev/null || true
echo "Selective cleanup complete (preserved .xref, .bbl files for cross-compilation)."
