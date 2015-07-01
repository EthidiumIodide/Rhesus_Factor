#!/usr/bin/python
__author__ = 'ivazirabad'
txtFile = open('M:/samtools_input.txt')
outputFile = open('M:\low_qual_probes_on_chr1.bed', 'w')

for line in txtFile:
    splitLine = line.split("\t")
    chrom = splitLine[1].split(":")[0]
    start = splitLine[1].split(":")[1].split("-")[0]
    end = splitLine[1].split(":")[1].split("-")[1].rstrip()
    outputFile.write(chrom+"\t"+start+"\t"+end+"\t"+splitLine[0]+"\t"+'0'+"\n")
outputFile.close()