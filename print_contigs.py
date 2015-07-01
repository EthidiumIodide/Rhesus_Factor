__author__ = 'ivazirabad'
import os,re

directory = 'M:/hi/RHCE'
start_RHD = 25761683

for file in os.listdir(directory):
    contigs = []
    fileOpened = open(directory + '/' + file)
    currentSample = ''
    for line in fileOpened:
        if line.startswith(">"):
            currentSample = line.rstrip()[1:]
        else: # line is the sequence
            p = re.compile("-\w+-")
            for contig_number,m in enumerate(p.finditer(line)):
                print("chr1\t"+str(start_RHD-m.end()+1)+"\t"+str(+start_RHD-m.start()+1)+"\t"+currentSample+'\t0\t+')