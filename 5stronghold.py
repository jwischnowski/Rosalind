import re

input = "rosalind_gc.txt"
GC_dict = {}

with open('output.txt', 'w') as outfile, open(input, 'r') as infile:
    lines = infile.read()
    sequences = lines.replace("\n", "").split(">")
    for sequence in sequences: #Create a dictionary with GC ratios as keys and IDs as values
        try:
            bases = re.search("Rosalind_([0-9]+)(.+)", sequence)[2]
        except TypeError:
            continue
        GC_ratio = ((bases.count("C") + bases.count("G")) / len(bases)) * 100
        GC_dict[GC_ratio] = re.search("(Rosalind_[0-9]+)(.+)", sequence)[1]
    ratios = sorted(GC_dict)
    ratios.reverse()
    outfile.write(f"{GC_dict[ratios[0]]}\n{ratios[0]:.6f}")