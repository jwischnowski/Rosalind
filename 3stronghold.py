input = "rosalind_revc.txt"
newsequence = ""
with open('output.txt', 'w') as outfile, open(input, 'r') as infile:
    sequence = infile.read()
    for base in sequence:
        if base == "A":
            newsequence = "T" + newsequence
        elif base == "T":
            newsequence = "A" + newsequence
        elif base == "C":
            newsequence = "G" + newsequence
        elif base == "G":
            newsequence = "C" + newsequence  
    outfile.write(str(newsequence))