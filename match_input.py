#!/usr/bin/python
import operator
__author__ = 'ivazirabad'
matchingFile = open('M:/match_input.txt')

name_count_dict = {}
for line in matchingFile:
    splitLine = line.split("\t")
    if splitLine[3] in name_count_dict:
        name_count_dict[splitLine[3]] += 1
    else: name_count_dict[splitLine[3]] = 1
sorted_x = sorted(name_count_dict.items(), key=operator.itemgetter(1))
for key, value in sorted_x:
    print(key, value,sep="\t")