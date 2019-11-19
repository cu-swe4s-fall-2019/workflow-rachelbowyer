import sys
import gzip
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify for gene dist")
    parser.add_argument('file_name', type=str, help='specify input .gz file')
    parser.add_argument('gene_name', type=str, help='specify gene name')
    parser.add_argument('out_file_name', type=str, help='specify output file')
    args = parser.parse_args()

file_name = args.file_name
gene_name = args.gene_name
out_file_name = args.out_file_name

o = open(out_file_name, 'w')

version = None
dim = None
header = None

f = gzip.open(file_name, 'rt')

names = []
for l in f:
    A = l.rstrip().split('\t')
    if version is None:
        version = A
        continue
    if dim is None:
        dim = A
        continue
    if header is None:
        header = A
        continue
    names.append(A[1])
    if A[1] == gene_name:
        for i in range(2, len(header)):
            o.write(header[i] + ' ' + A[i] + '\n')
            
try:
    names.index(gene_name)
except ValueError:
    raise

f.close()
o.close()
