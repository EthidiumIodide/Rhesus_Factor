__author__ = 'ivazirabad'
vcfFile = open("U:/PD/150526/Run3-V0_S1_L001_R1_001_Output/Run3-V0_S1_L001_R1_001/Run3-V0_S1_L001_R1_001_Mutation_Report1.vcf")
txtFile = open("C:/Users/ivazirabad/Desktop/file.vcf", 'w')

for line in vcfFile:
    splitLine = line.split("\t")
    if not line.startswith("#"):
        print(splitLine[6])
        if not splitLine[6] == 'SGflt':\
            txtFile.write(line)
    else: txtFile.write(line)
