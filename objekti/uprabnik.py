# Naredili bomo objekt User
# V tem objektu bomo shranili vse podatke o tem userju
# Hočemo vedeti: Ime, letnica_rojstva, priimek

class User:
    # Te stvari podamo ob kreiranju objekta User
    def __init__(self, ime, priimek, letnica_rojstva):
        self.ime = ime
        self.priimek = priimek
        self.letnica_rojstva = letnica_rojstva
        self.starost = 2020 - letnica_rojstva
        self.polno_ime = self.priimek + ", " + self.ime

    # Poklioče se, ko printamo objekt, vrne lep niz, ki predstavlja uporabnika
    def __str__(self):
        return "Jaz sem " + self.ime + " " + self.priimek + " Rojen: " + str(self.letnica_rojstva) + " star " + str(self.starost)



domen = User("Domen", "Korenini", 2004)
filip = User("Filip", "Koprivec", 1995)
arja = User("Arja Ela", "Hvala", 2006)
matija = User("Matija", "Ihan Švingelj", 2004)
nejc = User("Nejc", "Petrič", 2005)

vsi_uporabniki = [filip, arja, nejc, domen, matija]

# Izpiši polno ime najstarejšega v seznamu vsi_uporabniki
max_starost = 0

for oseba in vsi_uporabniki:
    if oseba.starost > max_starost:
        max_starost = oseba.starost
        najstarejsi = oseba.polno_ime
print("Najstarejši je: ", najstarejsi, oseba)

min_starost = 10000

for oseba in vsi_uporabniki:
    if oseba.starost < min_starost:
        min_starost = oseba.starost
        najmlajsi = oseba.polno_ime
print("Najmlajši je: ", najmlajsi, oseba)





