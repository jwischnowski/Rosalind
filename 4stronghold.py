months = 33
offspring = 3
adults = 0
babies = 1
babygrowup = 0
for i in range(months-1):
    babygrowup = babies #Count rabbits that will mature this generation but won't produce offspring
    babies += adults * offspring #Baby rabbits are born from mature adults
    adults += babygrowup #Baby rabbits mature into adults, adding to adults and subtracting from babies
    babies -= babygrowup
    total = adults + babies #Add adults and babies
print(total)