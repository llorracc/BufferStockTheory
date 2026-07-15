#!/bin/bash
perl -e '
sub run_pdftotext {
    foreach my $file (@ARGV) {
        my $pdf_file = "$file.pdf";
        my $txt_file = "$file.txt";
        
        if (-f $pdf_file) {
            print "Running pdftotext on $pdf_file...\n";
            system("pdftotext", "-nopgbrk", $pdf_file, $txt_file);
            print "Converted $pdf_file to $txt_file\n";
        } else {
            print "PDF file $pdf_file not found\n";
        }
    }
}

run_pdftotext(@ARGV);
' "$@"
