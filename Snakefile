GENES = ["SDHB", "MEN1","KCNH2","MSH2","MYL2","BRCA2"]
TISSUES = ["Brain","Heart","Blood","Skin"]

rule all:
    input:
        '-'.join(TISSUES) + '_' + '-'.join(GENES) +'.png'

rule gene_data:
    output:
        "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
    shell:
        "wget https://github.com/swe4s/lectures/raw/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"

rule sample_tissue_data:
    output:
        "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"
    shell:
        "wget https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"

rule gene_sample_counts:
    input:
        "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
    output:
        expand("{gene}_counts.txt", gene=GENES)
    shell:
        "for gene in {GENES}; do " \
        + "python get_gene_counts.py {input} $gene $gene\_counts.txt; done"

rule tissue_samples:
    input:
        "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"
    output:
        expand("{tissue}_samples.txt", tissue=TISSUES)
    shell:
        "for tissue in {TISSUES}; do " \
        + "python get_tissue_samples.py {input} $tissue $tissue\_samples.txt; done"

rule box:
    input:
        expand('{gene}_counts.txt', gene=GENES),
        expand("{tissue}_samples.txt", tissue=TISSUES)
    output:
        '-'.join(TISSUES) + '_' + '-'.join(GENES) +'.png'
    shell:
        'python box.py -tissues ' + ' '.join(TISSUES) + ' -genes ' + ' '.join(GENES) + ' -out_name {output}'
