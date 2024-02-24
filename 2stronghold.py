input = "rosalind_rna.txt"
with open('output.txt', 'w') as outfile, open(input, 'r') as infile:
    sequence = infile.read()
    rnasequence = sequence.replace("T", "U")    
    outfile.write(rnasequence)