import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify for gene dist")
    parser.add_argument('-tissues', '--tissues', nargs='+', default=[])
    parser.add_argument('-genes', '--genes', nargs='+', default=[])
    parser.add_argument('-out_name', '--out_name', nargs='+', default=[])
    args = parser.parse_args()

    tissues = args.tissues
    genes = args.genes
    out_file = args.out_name

    fig, ax = plt.subplots(len(tissues), 1, figsize=(10, 9), squeeze=False)

    j = 0

    for tissue in tissues:
        wanted_counts = []
        f = open(tissue + '_samples.txt')

        IDs = []
        for l in f:
            A = l.rstrip().split()
            IDs.append(A[0])
        f.close()

        for gene in genes:

            one_gene_list = []

            ff = open(gene + '_counts.txt')

            gene_IDs = []
            gene_counts = []

            for l in ff:
                A = l.rstrip().split()
                gene_IDs.append(A[0])
                gene_counts.append(int(A[1]))
            ff.close()

            for ID in IDs:
                for i in range(len(gene_IDs)):
                    if ID == gene_IDs[i]:
                        one_gene_list.append(gene_counts[i])

            wanted_counts.append(one_gene_list)
            print(gene)

        print(tissue)
        ax[j, 0].boxplot(wanted_counts)
        ax[j, 0].set_xticklabels(genes)
        ax[j, 0].set_ylabel('Counts')
        ax[j, 0].set_title(tissue)

        j = j + 1

    plt.xlabel('Gene')
    plt.savefig(str(out_file[0]), bbox_inches='tight')
