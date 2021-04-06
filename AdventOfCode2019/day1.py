# Instructions: https://adventofcode.com/2019/day/1

import os.path
import math

input_file = open(os.path.join("AdventOfCode2019", "day1.in"), "r")

"""
### 1. Del:
vsota = 0

def racunanje_goriva(stevilka):
    stevilka = int(stevilka) // 3
    stevilka -= 2
    # Preveri, če je stevilka > 0
    return max(0, stevilka)

for vrstica in input_file:
    odgovor = racunanje_goriva(vrstica)
    vsota += odgovor

print(vsota)
"""

### 2. Del:
masa_goriva = 0

def racunanje_goriva(stevilka):
    stevilka = int(stevilka) // 3
    stevilka -= 2
    # Preveri, če je stevilka > 0
    return max(0, stevilka)


for vrstica in input_file:
    izrac_masa_goriva = racunanje_goriva(vrstica)
    masa_goriva += izrac_masa_goriva
    masa_modula = izrac_masa_goriva
    while masa_modula > 1:
        masa_modula = racunanje_goriva(masa_modula)
        masa_goriva += max(0, masa_modula)

print(masa_goriva)  

input_file.close()
