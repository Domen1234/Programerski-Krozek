# CEZARJEVA ŠIFRA

"""
k = 2
A -> C
B -> D
"""

def zasifriraj(beseda, k):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    sifra_obratna = {}
    for crka in abeceda:
        sifra_obratna[ord(crka) - ord("a")] = crka

    grde_crke = "čšž"
    grde_crke_slovar = {
        "č": "c",
        "š": "s",
        "ž": "z"
    }

    posebni_znaki = " ,.-_:;!"

    odgovor = ""
    for crka in beseda:
        if crka not in posebni_znaki:
            if crka in grde_crke:
                crka = grde_crke_slovar[crka]
            stevilka = ord(crka) - ord("a")
            stevilka += k
            odgovor += sifra_obratna[stevilka % len(sifra_obratna)]
        else:
            odgovor += crka

    return odgovor

def desifriraj(beseda, k):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    sifra_obratna = {}
    for crka in abeceda:
        sifra_obratna[ord(crka) - ord("a")] = crka

    grde_crke = "čšž"
    grde_crke_slovar = {
        "č": "c",
        "š": "s",
        "ž": "z"
    }

    posebni_znaki = " ,.-_:;!"

    odgovor = ""
    for crka in beseda:
        if crka not in posebni_znaki:
            if crka in grde_crke:
                crka = grde_crke_slovar[crka]
            stevilka = ord(crka) - ord("a")
            stevilka -= k
            odgovor += sifra_obratna[stevilka % len(sifra_obratna)]
        else:
            odgovor += crka

    return odgovor


print(zasifriraj("krneki bla bla bla.", 2))
print(desifriraj("mtpgmk dnc dnc dnc.", 2))
