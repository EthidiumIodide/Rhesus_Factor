#!/usr/bin/python
__author__ = 'ivazirabad'

import sys
import re
txtFile = open('M:/create_bed.txt')
outputFile = open('M:\low_qual_probe.bed', 'w')

for line in txtFile:
    splitLine = line.split("\t")
    if splitLine[13].isdigit():
        coord = "chr"+splitLine[13]+"\t"+splitLine[15]+"\t"+splitLine[16]+"\t"+splitLine[8]+'\t0\t'+splitLine[7]
        outputFile.write(coord+"\n")