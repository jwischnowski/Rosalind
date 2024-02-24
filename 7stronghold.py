input = "rosalind_iprb.txt"

with open('output.txt', 'w') as outfile, open(input, 'r') as infile:
    k, m, n = infile.read().split(" ")
    k, m, n = int(k), int(m), int(n)
    total = k + m + n # Number of individuals
    pool = total - 1 # Number of potential mates

    # Calculate probability of homozygous recessive
    recess_mm = (m/total) * ((m-1) / pool) * .25 
    recess_mn = (m/total) * (n / pool) * .50
    recess_nm = (n/total) * (m / pool) * .50
    recess_nn = (n/total) * ((n-1)/pool) * 1 # Chance of n-n mating resulting in recessive phenotype
    recessive = recess_mm + recess_mn + recess_nn + recess_nm
    dominant = 1 - recessive

    outfile.write(str(dominant))