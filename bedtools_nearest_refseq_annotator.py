#!/usr/bin/python
__author__ = 'ivazirabad'
refseq_2_symbol = {}
refseq_ref = open('C:/Users/ivazirabad/Downloads/hsa_ref_seq_gene_symbol/hsa_gene_symbol_ref_seq.txt')
annotate_this_file = open('C:/Users/ivazirabad/Desktop/refseq.txt')
annotated = open('C:/Users/ivazirabad/Desktop/refseq2.txt','w')
for line in refseq_ref:
    splitLine = line.split("\t")
    refseq_2_symbol[splitLine[1]] = splitLine[0]
for line in annotate_this_file:
    splitLine = line.split("\t")
    symbol = str(refseq_2_symbol.get(splitLine[0]))
    annotated.write(symbol+"\n")
annotate_this_file.close()