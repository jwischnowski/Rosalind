input = "rosalind_dna.txt"
nucleotides = {}
with open('output.txt', 'w') as outfile, open(input, 'r') as infile:
    sequence = infile.read()
    for nucleotide in sequence:
        if nucleotide not in nucleotides:
            nucleotides[nucleotide] = 1
        else:
            nucleotides[nucleotide] += 1
    outfile.write(f"{nucleotides["A"]} {nucleotides["C"]} {nucleotides["G"]} {nucleotides["T"]}")