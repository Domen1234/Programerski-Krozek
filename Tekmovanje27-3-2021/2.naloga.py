# Program pogleda, če je opravilo iz nekega marsovsa prisotno tudi pri drugih marsovcih, 
# če je potem program poveča spremenljivko opravila za 1 in na koncu primerja število opravil in 
# pove ali so vsa opravila pribljižno enako zastopana

import os.path

vhod = open(os.path.join("Tekmovanje27-3-2021", "marsovci.txt"), "r")

m = vhod.readline(1)

marsovci = []
stetje = 0
for vrstica in vhod:
    if stetje != 0:
        vrstica = vrstica.strip()
        marsovci.append(vrstica.split(" "))
    stetje += 1

opravila = 0
for marsovec in marsovci:
    for opravilo in marsovec:
        for marsovec1 in marsovci:
            if opravilo in marsovec1:
                opravila += 1
                print(opravila)


#print(marsovci)
vhod.close()