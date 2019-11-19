import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def boxplot(L, nameset, group_col_name, gene_name, out_file_name):
    """generates boxplot of data"""
    fig = plt.figure(figsize=(10, 3), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.boxplot(L)
    ax.set_xticklabels(nameset, rotation=90)
    ax.set_xlabel(group_col_name)
    ax.set_title(gene_name)
    ax.set_ylabel('Gene Read Counts')

    plt.savefig(out_file_name, bbox_inches='tight')
    plt.close()

    return out_file_name


def binary_search(key, D):
    """does a binary search"""
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify for gene dist")
    parser.add_argument('-tissues', '--tissues', nargs='+', default=[])
    parser.add_argument('-genes', '--genes', nargs='+', default=[])
    parser.add_argument('-out_name', '--out_name',nargs='+', default=[])
    args = parser.parse_args()
    
    tissues = args.tissues
    genes = args.genes
    out_file = args.out_name
    
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
        fig = plt.figure(figsize=(10, 3), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.boxplot(wanted_counts)
        ax.set_xticklabels(genes)
        ax.set_ylabel('Counts')
        ax.set_title(tissue)

        plt.savefig(str(tissue)+'.png',bbox_inches='tight')

                        
        
        
#     counts = []
#     for i in range(len(genes)):
#         gene = genes[i]
#         tissue = tissues[i]

#         sample_to_count_map = {}

#         f = open(gene + '_counts.txt')
#         for l in f:
#             A = l.rstrip().split()
#             sample_to_count_map[A[0]] = int(A[1])

#         f.close()

#         count = []

#         f = open(tissue + '_samples.txt')
#         for l in f:
#             sample = l.rstrip()
#             if sample in sample_to_count_map:
#                 count.append(sample_to_count_map[sample])
#         f.close()

#         counts.append(count)
        
#         fig = plt.figure(figsize=(3,3),dpi=300)
#         fig, ax = plt.subplots(len(tissues),1)
#         for i in range(len(tissues)):
# #             print(i)
# #             print(counts[i])
#             ax[1].boxplot(counts[i])
# #             ax = fig.add_subplot(len(counts),1,i)
# #             ax.boxplot([1,2,3,4])
# # #             ax.boxplot(counts[i])
# # #             ax.spines['top'].set_visible(False)
# # #             ax.spines['right'].set_visible(False)
# # #             ax.set_title(genes[i] + ' ' + tissues[i])
        
#         plt.savefig(out_file[0],bbox_inches='tight')