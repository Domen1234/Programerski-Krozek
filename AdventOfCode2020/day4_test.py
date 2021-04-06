# Instructions: https://adventofcode.com/2020/day/4

import os.path

input_file = open(os.path.join("AdventOfCode2020", "day4.in"), "r")

podatki = []
podatki_x_oseba = []
valid_passports = 0
passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Dodam vsako osebo posebaj v podatke [OK]
for vrstica in input_file:
    if vrstica == "\n":
        podatki.append(podatki_x_oseba.copy())
        podatki_x_oseba.clear()
        #print(podatki[-1])
    else:
        podatki_x_oseba.append(vrstica)
podatki.append(podatki_x_oseba.copy())
    

# Podatke razdelim po presledku
for oseba in podatki:
    podatki_osebe = []
    flag_pass_ok = False
    # Za vsak item v listi podatki_za_osebe pogledas samo del pred :
    id_list = []
    for string_blob in oseba:
        #podatki_osebe.append(i.split(" "))
        # Dobis listo stringov "id:vrednost"
        podatki_osebe = string_blob.split(" ")
        for znak in podatki_osebe:
            id_x = znak.split(":")[0]
            id_list.append(id_x)
    #
    # Zdaj precekiram, ce so notri vsa polje, ki morajo biti v passportu
    for id_item in passport_fields:
        if id_item not in id_list:
            #print("This passport is missing item: %s" % id_item)
            flag_pass_ok = False
            break
        else:
            flag_pass_ok = True
            pass
    if flag_pass_ok == True:
        valid_passports += 1


"""
        print("[OK] - %s/n%s" % (oseba, id_list))
    else:
        print("[NOT] - %s/n%s" % (oseba, id_list))


    #
    # Dam vska podatek od osebe posebaj v listo passport_osebe
    passport_osebe = []

    for trenutni_podatek in podatki_osebe:
        if len(trenutni_podatek) > 1:
            for en_podatek in trenutni_podatek:
                passport_osebe.append(en_podatek.strip())
        else:
            passport_osebe.append(trenutni_podatek[0].strip())

    # Pogledam če imaj passport osebe vse potrebene podatke
    passport_items = 0
    for polje in passport_osebe:
        for stetje in range(len(passport_fields)):
            if passport_fields[stetje] in polje:
                passport_items += 1
                #print("Cointains item: ",passport_fields[stetje], " Passport items: ", passport_items)
        if passport_items >= 7:
            valid_passports += 1
    passport_items = 0
"""


print(valid_passports)
print(id_list)

input_file.close()