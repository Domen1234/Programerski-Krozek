class Produkt:
    # Cena mora biti na enoto kolicine
    def __init__(self, cena, kolicina, ime, masa, je_hrana):
        self.cena = cena
        self.kolicina = kolicina
        self.ime = ime
        self.masa = masa
        self.je_hrana = je_hrana

    def skupna_masa(self):
        return self.masa * self.kolicina

    def izrac_stopnjo_davka(self):
        # DDV na hrano je 9%
        # DDV na pijaco je 22.5%

        if self.je_hrana == "Hrana":
            return 0.09
        else:
            return 0.225

    def skupna_vrednost(self):
        return self.cena * (1 + self.izrac_stopnjo_davka())
    
    def skupna_vrednost_zaloge(self):
        return self.cena * self.kolicina * (1 + self.izrac_stopnjo_davka())

class Trgovina:
    def __init__(self, zaloga):
        # [
        #   (sifra1, produkt1),
        #   (sifra2, produkt2)
        # ]
        # [jabolko, hruske, banane, kruh, mleko, voda, riz] -> [(1, jabolko), (2, hruske), ...]
        
        zacetna_sifra = 0
        zaloga_trgovine = [] # Sem notr dajemo (sofra, produkt)
        
        for pr in zaloga:
            zacetna_sifra += 1
            zaloga_trgovine.append([zacetna_sifra, pr])

        self.zaloga = zaloga_trgovine
    
    def skupna_masa(self):
        skupaj = 0
        for izdelek in self.zaloga:
            skupaj += Produkt.skupna_masa(izdelek[1])

        return skupaj
    
    def skupna_vrednost(self):
        skupaj = 0
        for izdelek in self.zaloga:
            skupaj += Produkt.skupna_vrednost(izdelek[1])

        return skupaj
    
    def skupno_stevilo_izdelkov(self):
        skupaj = 0
        for izdelek in self.zaloga:
            skupaj += izdelek[1].kolicina

        return skupaj

    def stevilo_razlicnih_izdelkov(self):
        skupaj = 0
        for izdelek in self.zaloga:
            pr = izdelek[1]
            if pr.kolicina > 0:
                skupaj += 1
    
        return skupaj

    def izdelek_z_naj_ceno(self):
        najvecji = self.zaloga[0][1]
        for izdelek in self.zaloga:
            if izdelek[1].cena > najvecji.cena:
                najvecji = izdelek[1]

        return najvecji.ime
    """
    def masa_hrane(self):
        skupaj = 0
        for izdelek in self.zaloga:
            pr = izdelek[0]
            if pr.je_hrana == "Hrana":
                skupaj += Produkt.skupna_masa(pr)
        
        return skupaj

    def masa_pijace(self):
        skupaj = 0
        for izdelek in self.zaloga:
            pr = izdelek[0]
            if pr.je_hrana == "Pijaca":
                skupaj += Produkt.skupna_masa(pr)
        
        return skupaj
    """

    def kupi(self, id_izdelka, sprememba_kolicine):
        for izdelek in self.zaloga:
            pr = izdelek[1]
            if izdelek[0] == id_izdelka:
                pr.kolicina -= sprememba_kolicine
                print(pr.kolicina)

        return True


jabolko = Produkt(1.2, 12, "Jabolko", 5.0, "Hrana") # Jabolka so v zaboju po 5 kg, ki stane 1.2 €, imao 12 zabojev
hruske = Produkt(1.3, 8, "Hruske", 4.0, "Hrana")
banane = Produkt(2.0, 4, "Banane", 3.0, "Hrana")
kruh = Produkt(1.0, 1, "Kruh", 1.0, "Hrana")
mleko = Produkt(1.5, 10, "Mleko", 1.2, "Pijaca")
voda = Produkt(0.3, 14, "Voda", 1.0, "Pijaca")
riz = Produkt(0.5, 3, "Riz", 2.0, "Hrana")

produkti = [jabolko, hruske, banane, kruh, mleko, voda, riz]

trgovina_objekt = Trgovina(produkti)

print("Skupna masa: ", trgovina_objekt.skupna_masa())
print("Skupna vrednost: ", trgovina_objekt.skupna_vrednost())
print("Skupno stevilo izdelkov: ", trgovina_objekt.skupno_stevilo_izdelkov())
print("Izdelek z najvišjo ceno: ", trgovina_objekt.izdelek_z_naj_ceno())

while True:
    zahteva = int(input("Vpiši ID izdelka, ki ga želiš kupit. "))
    if zahteva == 0:
        print("Koncal si z nakupom.")
        break
    elif zahteva > len(produkti):
        print("Ta izdelek ne obstaja.")
    else:
        st_kupljenih_izdelkov = int(input("Koliko teh izdelkov zelis kupiti? "))
        trgovina_objekt.kupi(zahteva, st_kupljenih_izdelkov)


























































"""
def skupna_masa_trgovine(seznam_izdelkov):
    skupaj = 0
    for izdelek in seznam_izdelkov:
        skupaj += Produkt.skupna_masa(izdelek)
    return skupaj

def vrednost_cele_trgovine(seznam_izdelkov):
    skupaj = 0
    for izdelek in seznam_izdelkov:
        skupaj += Produkt.skupna_vrednost_zaloge(izdelek)
    return skupaj

def skupno_stevilo_izdelkov(seznam_izdelkov):
    st_izdelkov = 0
    for izdelek in seznam_izdelkov:
        st_izdelkov += izdelek.kolicina
    return st_izdelkov

def izdelek_z_naj_ceno(seznam_izdelkov):
    najvecji = seznam_izdelkov[0]
    for izdelek in seznam_izdelkov:
        if izdelek.cena > najvecji.cena:
            najvecji = izdelek
    return najvecji.ime

print("Skupna masa je: ", skupna_masa_trgovine(produkti))
print("Skupna vrednost je: ", vrednost_cele_trgovine(produkti))
print("vrednost cele trgovine je: ", vrednost_cele_trgovine(produkti))
print("Število vseh izdelkov je: ", skupno_stevilo_izdelkov(produkti))
print("Izdelek z največjo ceno je: ", izdelek_z_naj_ceno(produkti))
"""

