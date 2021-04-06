# Preberes vrstico v inputu
# vrstico razdeliš na ukaz in stevilko
# Pogledaš kater ukaz

# acc - neki spremenljivkli dodas vrednost
# jmp -  gres pa na vrstico k je za vecja od trenutne
# nop - pass

# Stroj mora vedeti:
#   - vrednost
#   - v kateri vrstici je
#   - vse vrstice, ki jih je ze izvedel
#   - seznam ukazov
"""
### PRVI DEL
import os.path

input_file = open(os.path.join("AdventOfCode2020", "day8.in"), "r")


class Ukaz:
    def __init__(self, tip_ukaza, stevilka):
        self.tip_ukaza = tip_ukaza
        self.stevilka = stevilka
    def __str__(self):
        return self.tip_ukaza + " " + str(self.stevilka)
    def __repr__(self):
        return self.tip_ukaza + " " + str(self.stevilka)



class Machine:
    def __init__(self, ukazi):
        self.ukazi = ukazi
        self.akumulator = 0 # To je tisto kar se spreminja
        self.line = 0 # Index ukaza na katerem smo

    def naredi_korak(self):
        trenutni = self.ukazi[self.line]
        if trenutni.tip_ukaza == "acc":
            self.akumulator += trenutni.stevilka
            self.line += 1
        elif trenutni.tip_ukaza == "jmp":
            self.line += trenutni.stevilka
        elif trenutni.tip_ukaza == "nop":
            self.line += 1

        
# Preberemo ukaze
ukazi = []

for vrstica in input_file:
    splitana_vrstica = vrstica.split(" ")
    trenutni_ukaz = Ukaz(splitana_vrstica[0], int(splitana_vrstica[1]))
    ukazi.append(trenutni_ukaz)


stroj = Machine(ukazi)
opravljene_vrstice = []

while True:
    opravljene_vrstice.append(stroj.line)
    stroj.naredi_korak()
    if stroj.line in opravljene_vrstice:
        print("Vrstica se je ponovila")
        print("Akumulator je: ", stroj.akumulator)
        break


input_file.close()
"""

### DRUGI DEL
import os.path

input_file = open(os.path.join("AdventOfCode2020", "day8.in"), "r")


class Ukaz:
    def __init__(self, tip_ukaza, stevilka):
        self.tip_ukaza = tip_ukaza
        self.stevilka = stevilka
    def __str__(self):
        return self.tip_ukaza + " " + str(self.stevilka)
    def __repr__(self):
        return self.tip_ukaza + " " + str(self.stevilka)



class Machine:
    def __init__(self, ukazi):
        self.ukazi = ukazi
        self.akumulator = 0 # To je tisto kar se spreminja
        self.line = 0 # Index ukaza na katerem smo
    
    def naredi_korak(self):
        trenutni = self.ukazi[self.line]
        if trenutni.tip_ukaza == "acc":
            self.akumulator += trenutni.stevilka
            self.line += 1
        elif trenutni.tip_ukaza == "jmp":
            self.line += trenutni.stevilka
        elif trenutni.tip_ukaza == "nop":
            self.line += 1
    
    def pozeni(self):
        #Naj vrne ali se zacikla ali pa se izvede do konca
        opravljene_vrstice = []
        
        while True:
            opravljene_vrstice.append(self.line)
            self.naredi_korak()
            if self.line in opravljene_vrstice:
                self.line = 0
                self.akumulator = 0
                return False

            if self.line >= len(ukazi):
                self.line = 0
                return True




# Preberemo ukaze
ukazi = []

for vrstica in input_file:
    splitana_vrstica = vrstica.split(" ")
    trenutni_ukaz = Ukaz(splitana_vrstica[0], int(splitana_vrstica[1]))
    ukazi.append(trenutni_ukaz)


stroj = Machine(ukazi)
ze_popravljeni_ukazi = []


for ukaz in ukazi:
    print(stroj.akumulator)
    originalen_tip = ukaz.tip_ukaza

    if ukaz.tip_ukaza == "nop":
        ukaz.tip_ukaza = "jmp"
        ze_popravljeni_ukazi.append(stroj.line)

    elif ukaz.tip_ukaza == "jmp":
        ukaz.tip_ukaza = "nop"
        ze_popravljeni_ukazi.append(stroj.line)


    if stroj.pozeni() == True:
        print("Prisel si do konca. Akumulator je: ", stroj.akumulator)
        break
    else:
        print("False")

    ukaz.tip_ukaza = originalen_tip


input_file.close()
