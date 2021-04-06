import os.path
"""
class Uporabnik:
    def __init__(self, odgovori):
        self.odgovori = odgovori

class Skupina:
    def __init__(self, uporabniki):
        self.uporabniki = uporabniki

    def dolzina_razlicnih(self):
        print(len(self.uporabniki))

        do_sedaj = set()

        for uporabnik in self.uporabniki:
            mnozica_odg = set(uporabnik.odgovori)
            do_sedaj = do_sedaj.union(mnozica_odg)  # Lahko napisemo do_sedaj |= mnozica_odg
        return len(do_sedaj)


vhod = open(os.path.join("AdventOfCode2020", "day6.in"), "r").read()

skupine = []

skupine_vrstic = vhod.split("\n\n")

for skupina in skupine_vrstic:
    uporabniki = []
    besede_uporabnikov = skupina.split("\n")
    for beseda in besede_uporabnikov:
        uporabniki.append(Uporabnik(beseda))


    skupina = Skupina(uporabniki)
    skupine.append(skupina)

vsota = 0

for skupina in skupine:
    vsota += skupina.dolzina_razlicnih()

print("Končna vsota je: " + str(vsota))

"""
### DRUGI DEL

class Uporabnik:
    def __init__(self, odgovori):
        self.odgovori = odgovori

class Skupina:
    def __init__(self, uporabniki):
        self.uporabniki = uporabniki

    def dolzina_razlicnih(self):
        #print(len(self.uporabniki))

        do_sedaj = set()

        for uporabnik in self.uporabniki:
            mnozica_odg = set(uporabnik.odgovori)
            do_sedaj = do_sedaj.union(mnozica_odg)  # Lahko napisemo do_sedaj |= mnozica_odg
        return len(do_sedaj)

    def dolzina_enakih(self):
        #print(len(self.uporabniki))

        do_sedaj = set(self.uporabniki[0].odgovori)

        for uporabnik in self.uporabniki:
            mnozica_odg = set(uporabnik.odgovori)
            do_sedaj = do_sedaj.intersection(mnozica_odg)  # Lahko napisemo do_sedaj |= mnozica_odg
        return len(do_sedaj)


vhod = open(os.path.join("AdventOfCode2020", "day6.in"), "r").read()

skupine = []

skupine_vrstic = vhod.split("\n\n")

for skupina in skupine_vrstic:
    uporabniki = []
    besede_uporabnikov = skupina.split("\n")
    for beseda in besede_uporabnikov:
        uporabniki.append(Uporabnik(beseda))


    skupina = Skupina(uporabniki)
    skupine.append(skupina)

vsota = 0
vsota2 = 0

for skupina in skupine:
    vsota += skupina.dolzina_razlicnih()
    vsota2 += skupina.dolzina_enakih()


print("Končna vsota je: ", vsota, "Rezultat naloge 2: ", vsota2)




