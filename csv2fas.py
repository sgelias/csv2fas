import csv
import sys

inputPath = sys.argv[1]
outputPath = sys.argv[2]

print(
    "\n"
    "###########    The number of columns vary from 0 to n (the first column is '0').    ###########\n"
    "###########    Please, firt privide the column number that contain fasta names,     ###########\n"
    "###########    and next the column numver that contain the sequence.                ###########\n"
)


colnames = input("Number of column for fasta names: ")
seqnames = input("Number of column for fasta sequences: ")

n = 0

with open(inputPath, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter = ',')
    next(reader)
    with open(outputPath, 'w') as outfas:
        for row in reader:
            n += 1
            seqname = row[colnames]
            dnaseq = row[seqnames]
            outfas.write('>' + seqname + '\n' + dnaseq + '\n')

print("Done.")
