# Instructions: https://adventofcode.com/2020/day/4

import os.path

input_file = open(os.path.join("AdventOfCode2020", "day4.in"), "r")

podatki = []
podatki_x_oseba = []
valid_passports = 0
passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Dodam vsako osebo posebaj v podatke
for vrstica in input_file:
    if vrstica == "\n":
        podatki.append(podatki_x_oseba.copy())
        podatki_x_oseba.clear()
    else:
        podatki_x_oseba.append(vrstica)
podatki.append(podatki_x_oseba.copy())

# Podatke razdelim po presledku
for oseba in podatki:
    passport_v_vrsticah = []
    for zmesan_podatek in oseba:
        zmesan_podatek = zmesan_podatek.split(" ")
        passport_v_vrsticah.append(zmesan_podatek)
    
    # Dam vska podatek od osebe posebaj v listo passport_osebe
    passport_osebe = []
    for vrstica_passporta in passport_v_vrsticah:
        if len(vrstica_passporta) > 1:
            for en_podatek in vrstica_passporta:
                passport_osebe.append(en_podatek.strip())
        else:
            passport_osebe.append(vrstica_passporta[0].strip())

    # Dodamo listo z kategorijami, ki jih ima passport
    passport_categories = []
    for item in passport_osebe:
        passport_categories.append(item.split(":")[0])

    # Pogledam če imaj passport osebe vse potrebene podatke
    passport_items = 0
    for polje in passport_fields:
        if polje in passport_categories:
            passport_items += 1
    if passport_items == len(passport_fields):
        valid_passports += 1


print(valid_passports)


input_file.close()
