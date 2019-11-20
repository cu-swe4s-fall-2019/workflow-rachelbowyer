#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#test that wrong tissue group name doesn't work
run gene_name_test python get_gene_counts.py GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt Bloody poop.txt
assert_exit_code 1

#test that wrong files name doesn't work
run gene_file_test python get_gene_counts.py poop.gz Bloody poop.txt
assert_exit_code 1


#test that the output file is created
rm file.txt
run file_creation_test python get_gene_counts.py GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt Blood file.txt
test -f file.txt
