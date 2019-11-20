#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#test that wrong gene name doesn't work
run argparse_error python box.py -tissue Blood -genes SDHB -out_file poop.png
assert_exit_code 2

#test that the output file is created
rm poop.png
run argparse_error python box.py -tissue Blood -genes SDHB -out_name poop.png
test -f poop.png
