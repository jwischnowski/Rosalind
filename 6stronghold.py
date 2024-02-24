input = "rosalind_hamm.txt"
distance = 0

with open('output.txt', 'w') as outfile, open(input, 'r') as infile:
    lines = infile.readlines()
    for count, character in enumerate(lines[0].strip()):
        if character != lines[1].strip()[count]:
            distance += 1
        else:
            continue
    outfile.write(str(distance))