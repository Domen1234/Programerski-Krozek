# Tukaj bomo naredili razred Zajec in cel kup stvari, ki zajcem pripada
# 
# Definiraj razred Zajec, ki ima dva podatka: teza: float, starost: int
# __str__: Zajec star X let in tehta Y kg
# __repr__: Zajec(X, Y)
# nahrani(self, teza_hrane): 0.25 teze prejete hrane
# sprehod(self, dolzina_v_km: int): na vsakem km izgubi 1% teže na začetku tega kilometra
#   Zajcu naj se posodobi teža, metoda naj vrne za koliko je shujšal
# ustvarimo 3 nove objekte tipa Zajec 


class Zajec:
    koeficient_hranjenja = 0.25
    koeficient_hujsanja = 0.01
    def __init__(self, starost, teza):
        self.starost = int(starost)
        self.teza = float(teza)
    def __str__(self):
        return "Zajec je star " + str(self.starost) + " let in tehta " + str(self.teza) + " kg"
    def __repr__(self):
        return "Zajec(" + str(self.starost) + "," + str(self.teza) + ")"
    
    def __lt__(self, other): # lt - less than ; self - tist ki je na levi, other - tist ki je na desni
        if self.starost < other.starost:
            return True
        elif self.starost == other.starost:
            return self.teza < other.teza
        else:
            return False

    def nahrani(self, teza_hrane):
        
        self.teza += (Zajec.koeficient_hranjenja * teza_hrane)

    def sprehod(self, dolzina_v_km):
        prejsnja_teza = self.teza
        stetje = 0
        while stetje != dolzina_v_km:
            self.teza -= Zajec.koeficient_hujsanja * self.teza
            stetje += 1
        shujsana_kolicina = prejsnja_teza - self.teza
        return shujsana_kolicina


z1 = Zajec(27, 23)
z2 = Zajec(23, 22)
z3 = Zajec(18, 12)

zajci = [z1, z2, z3]

while True:
    zajci.sort()
    print("Na voljo imas zajce: " + str(zajci))
    dejavnost = input("Kaj bos naredil z zajci (sprehod/nahrani)? ")
    if dejavnost.lower() == "sprehod":
        izbrani = int(input("Napiši index zajca katerega boš poslal na sprehod. "))
        dolzina = int(input("Kako dolg naj bo sprehod? "))
        zajci[izbrani].sprehod(dolzina)
    elif dejavnost.lower() == "nahrani":
        izbrani = int(input("Napiši index zajca katerega boš nahranil. "))
        kolicina = int(input("Koliko hrane mu boš dal? "))
        zajci[izbrani].nahrani(kolicina)
    else:
        print("Napaka.")


#zajci.sort()
#print(zajci)