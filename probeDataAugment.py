#!/usr/bin/python
__author__ = 'ivazirabad'
import os

directory = 'C:/Users/ivazirabad/Documents/Cytosure/csv'

for file in os.listdir(directory):
    fileOpened = open(directory + '/' + file)
    fileAugmented = open('C:/Users/ivazirabad/Documents/Cytosure/augmented/' + file, 'w')
    headerLine = fileOpened.readline().split(",")
    for i in range(6, 10):
        print(file)
        headerLine[i] = headerLine[i].rstrip() + "_" + file[:-8]
    fileAugmented.write(",".join(headerLine) + '\n')
    for line in fileOpened:
        if "Probe" not in line:
            fileAugmented.write(line)
    fileOpened.close()
    fileAugmented.close()