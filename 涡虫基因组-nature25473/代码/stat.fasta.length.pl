#! /usr/bin/perl -w
use strict;
die "perl  $0 infa > outfile\n" unless @ARGV == 1;
open IN,$ARGV[0] || die;
$/=">";<IN>;$/="\n";
while(<IN>){
        chomp;
        my $id = (split /\s+/,$_)[0];
	$id =~ s/^>//;
        $/=">";chomp(my $fa=<IN>);$/="\n";
        $fa =~ s/\n+//g;
        my $len = length $fa;
	my $len2 = sprintf "%.2f",$len/10**6;
	print join ("\t",$id,$len,$len2),"\n";
}
close IN;
