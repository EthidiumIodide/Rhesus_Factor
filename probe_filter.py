#!/usr/bin/python
__author__ = 'ivazirabad'

import sys
import re
txtFile = open('M:/probe_category_track.txt')
outputFile = open('M:\samtools_input.txt', 'w')

if len(sys.argv) == 1:
    print("Please enter LQ, MQ, or HQ")
    sys.exit(2)
else:
    for line in txtFile:
        splitLine = re.split(' |\t', line)  # very powerful, splits on spaces and tabs
        if splitLine[0] == sys.argv[1]:  # only search for low quality files
            probeName = splitLine[2]
            coord = splitLine[3]+":"+splitLine[4]+"-"+splitLine[5]
            outputFile.write(probeName+"\t"+coord)