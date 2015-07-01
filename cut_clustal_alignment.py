__author__ = 'ivazirabad'
# This does something

clustal_aln_first = open("M:/hi/first/final_first_align_RHCE_truncated.aln")
clustal_aln_second = open("M:/hi/second/second_half_RHD_RHCE_align_RHCE.aln")
seq_name = []
seq = []

# initialize the values
for x in range(0,8):
    seq.append('')
    seq_name.append('')

for x, line in enumerate(clustal_aln_first):
    y = x % 8
    print("hello", x, y,sep="\t")
    seq_name[y] = line.split("\t")[0]
    seq[y] = seq[y]+line.split("\t")[1]

for x in range(0,8):
    clustal_print = open("M:/hi/RHCE/merged_"+seq_name[x]+"_RHCE_Complete.txt",'w')
    clustal_print.write(">"+seq_name[x]+"\n"+seq[x])
    clustal_print.close()