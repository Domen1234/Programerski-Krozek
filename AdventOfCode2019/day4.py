# instructions: https://adventofcode.com/2019/day/4

import time

puzzle_input = "134792-675810"
prva_st_gesla = int(puzzle_input.split("-")[0])
druga_st_gesla = int(puzzle_input.split("-")[1])

valid_passwords = 0

for geslo in range(prva_st_gesla, druga_st_gesla):
    # Pogledamo ce se ponovi neka stevka v številki
    """
    stevke = set()
    for stevka in str(geslo):
        stevke.add(stevka)
    if len(stevke) < len(str(geslo)):
        ponovi_stevilka = True
    else:
        ponovi_stevilka = False
    """
    stevke = []
    i = 0
    for stevka in str(geslo):
        if i != 0 and stevka == stevke[i - 1]:
            ponovi_stevilka = True
        else:
            ponovi_stevilka = False
        stevke.append(stevka)
        i += 1
    # Pogledamo, če številke naraščajo
    max_stevilka = 0
    for stevka in str(geslo):
        if int(stevka) >= int(max_stevilka):
            max_stevilka = stevka
    if max_stevilka == str(geslo)[-1]:
        narsacajuce = True
    else:
        narsacajuce = False

    # Pogledamo, če geslo zadostuje obema pogojema
    if ponovi_stevilka == True and narsacajuce == True:
        valid_passwords += 1

print(valid_passwords)
