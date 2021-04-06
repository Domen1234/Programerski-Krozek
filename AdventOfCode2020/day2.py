# Instructions: https://adventofcode.com/2020/day/2
'''
import os.path

input_file = open(os.path.join("AdventOfCode2020", "day2.in"), "r")

odgovor = 0

for vrstica in input_file:
    count = 0

    # Razcepimo vrstico na niz znakov in št. znakov in iskan zna
    razcepljena_vrstica = vrstica.split(":")
    
    # Poiščemo število znakov 
    st_znakov_in_znak = razcepljena_vrstica[0].split(" ")

    # Število potrebnih znakov razdelimo na dva dela, da dobimo minimalno št. znakov in maximalno št znakov
    min_in_max_znakov = st_znakov_in_znak[0].split("-")
    min_znakov = int(min_in_max_znakov[0])
    max_znakov = int(min_in_max_znakov[1])
    
    # Dobimo znak, ki ga iščemo
    iskani_znak = st_znakov_in_znak[1]

    # Poiščemo niz znakov
    niz_znakov = razcepljena_vrstica[1]

    # Preštejemo št. iskanih znakov v nizu znakov
    for crka in niz_znakov:
        if crka == iskani_znak:
            count += 1
    
    # Preverimo, če število znakov ustreza omejitvi št. znakov (min_in_max_znakov)
    if count >= min_znakov and count <= max_znakov:
        odgovor += 1

print(odgovor)


input_file.close()
'''

### DRUGI DEL

import os.path

input_file = open(os.path.join("AdventOfCode2020", "day2.in"), "r")

odgovor = 0


for vrstica in input_file:
    # Razcepimo vrstico na niz znakov in št. znakov in iskan zna
    razcepljena_vrstica = vrstica.split(":")
    
    # Poiščemo število znakov 
    iskani_znaki_in_znak = razcepljena_vrstica[0].split(" ")

    # Število potrebnih znakov razdelimo na dva dela, da dobimo minimalno št. znakov in maximalno št znakov
    prvi_in_drugi_iskain_znak = iskani_znaki_in_znak[0].split("-")
    prvi_iskani_znak = int(prvi_in_drugi_iskain_znak[0])
    drugi_iskani_znak = int(prvi_in_drugi_iskain_znak[1])
    
    # Dobimo znak, ki ga iščemo
    iskani_znak = iskani_znaki_in_znak[1]

    # Poiščemo niz znakov
    niz_znakov = razcepljena_vrstica[1]
    niz_znakov = niz_znakov[1:]

    # Preverimo, če so iskani znaki na mestu kjer morajo biti
    if niz_znakov[prvi_iskani_znak - 1] != iskani_znak and niz_znakov[drugi_iskani_znak - 1] == iskani_znak:
        odgovor += 1
    elif niz_znakov[prvi_iskani_znak - 1] == iskani_znak and niz_znakov[drugi_iskani_znak - 1] != iskani_znak:
        odgovor += 1


print(odgovor)


input_file.close()
