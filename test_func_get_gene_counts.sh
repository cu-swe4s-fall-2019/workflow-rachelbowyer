#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#test that if N is too big insert_..pairs.py doesn't work
run gene_name_test python get_gene_counts.py GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz ABCD poop.txt
assert_exit_code 1


#test that the output file is created
rm poop.txt
run gene_name_test python get_gene_counts.py GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz ABCD poop.txt
test -f poop.txt
