#!/usr/bin/python
__author__ = 'Yusef-PC'
import re
rhd_align = open("M:/hi/rhd_rhce_first.aln")
align_output = open("M:/hi/first/final_first_align.aln",'w')

alignment_name_list = []
alignment_seq_list = []

for line in rhd_align:
    if line.startswith(">"):
        alignment_name_list.append(line[1:])

current_position_1_RHD_5Prime = 0
current_position_1_RHCE_5Prime = 1
current_position_2_RHD = 0
current_position_2_RHCE = 0
current_position_RHCE = 1
current_position_RHD = 0
current_position_RHCE_exon_10 = 0
current_position_RHD_exon_10 = 0
absolute_position = 1

start_1_RHD_5Prime = 25585274
start_1_RHCE_5Prime = 25761683
start_2_RHD = 25594500
start_2_RHCE = 25751820
start_RHD = 25272393
start_RHCE = 25360659
start_RHCE_exon_10 = 25689044
start_RHD_exon_10 = 25655389

RHD_seq = []
RHCE_seq = []
RHD_5prime_seq = []
RHCE_5prime_seq = []
Two_RHD_seq = []
Two_RHCE_seq = []
RHCE_exon_10_seq = []
RHD_exon_10_seq = []

for RHD,RHCE,Two_RHD,Two_RHCE,Prime5_RHCE,Prime5_RHD,RHD_exon10,RHCE_exon10 in zip(open("M:/hi/first/NG_007494.1_RHD_First-Half.fa"),
                                                            open("M:/hi/first/NG_009208.3_RHCE_First-Half.fa"),
                                                            open("M:/hi/first/2_RHD.fa"),
                                                            open("M:/hi/first/2_RHCE.fa"),
                                                            open("M:/hi/first/1_RHCE_5Prime.fa"),
                                                            open("M:/hi/first/1_RHD_5Prime.fa"),
                                                            open("M:/hi/first/4_RHD_exon10.fa"),
                                                            open("M:/hi/first/4_RHCE_exon10.fa"),):
    if not RHD.startswith(">"):
        RHD_seq = list(RHD)
        RHCE_seq = list(RHCE)
        RHD_5prime_seq = list(Prime5_RHD)
        RHCE_5prime_seq = list(Prime5_RHCE)
        Two_RHD_seq = list(Two_RHD)
        Two_RHCE_seq = list(Two_RHCE)
        RHD_exon_10_seq = list(RHD_exon10)
        RHCE_exon_10_seq = list(RHCE_exon10)

        for RHD_char,RHCE_char,RHD_5prime_char,RHCE_5prime_char,Two_RHD_char,Two_RHCE_char,RHD_exon_10_char, RHCE_exon_10_char in zip(RHD_seq, RHCE_seq, RHD_5prime_seq, RHCE_5prime_seq, Two_RHD_seq, Two_RHCE_seq, RHD_exon_10_seq, RHCE_exon_10_seq):
            if absolute_position % 80 == 0:
                align_output.write("RHD\t"+re.sub('[\'\[\], ]', '', str(RHD_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_RHD)+"\t"+str(start_RHD)+"\n"+
                                   "RHCE\t"+re.sub('[\'\[\], ]', '', str(RHCE_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_RHCE)+"\t"+str(start_RHCE)+"\n"+
                                   "2_RHD\t"+re.sub('[\'\[\], ]', '', str(Two_RHD_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_2_RHD)+"\t"+str(start_2_RHD)+"\n"+
                                   "2_RHCE\t"+re.sub('[\'\[\], ]', '', str(Two_RHCE_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_2_RHCE)+"\t"+str(start_2_RHCE)+"\n"+
                                   "1_RHD_5Prime\t"+re.sub('[\'\[\], ]', '', str(RHD_5prime_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_1_RHD_5Prime)+"\t"+str(start_1_RHD_5Prime)+"\n"+
                                   "1_RHCE_5Prime\t"+re.sub('[\'\[\], ]', '', str(RHCE_5prime_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_1_RHCE_5Prime)+"\t"+str(start_1_RHCE_5Prime)+"\n"+
                                   "4_RHD_Exon10\t"+re.sub('[\'\[\], ]', '', str(RHD_exon_10_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_RHD_exon_10)+"\t"+str(start_RHD_exon_10)+"\n"+
                                   "4_RHCE_Exon10\t"+re.sub('[\'\[\], ]', '', str(RHCE_exon_10_seq[absolute_position-79:absolute_position]))+"\t"+str(current_position_RHCE_exon_10)+"\t"+str(start_RHCE_exon_10)+"\n\n")
            if RHD_char != "-":
                current_position_RHD += 1
                start_RHD += 1
            if RHCE_char != "-":
                current_position_RHCE += 1
                start_RHCE -= 1
            if RHD_5prime_char != "-":
                current_position_1_RHD_5Prime += 1
                start_1_RHD_5Prime += 1
            if RHCE_5prime_char != "-":
                current_position_1_RHCE_5Prime += 1
                start_1_RHCE_5Prime -= 1
            if Two_RHD_char != "-":
                current_position_2_RHD += 1
                start_2_RHD += 1
            if Two_RHCE_char != "-":
                current_position_2_RHCE += 1
                start_2_RHCE -= 1
            if RHD_exon_10_char != "-":
                current_position_RHD_exon_10 += 1
                start_RHD_exon_10 += 1
            if RHCE_exon_10_char != "-":
                current_position_RHCE_exon_10 += 1
                start_RHCE_exon_10 -= 1
            absolute_position += 1