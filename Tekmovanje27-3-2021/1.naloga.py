# Najprej spremenim geslo v listo tako da je vska znak v geslu svoj element
# Potem pa grem po vrti in vsak znak posebaj spremenim v veliko črko, razen če je številka potem pa samo preskočim,
# ker ne mormo spremeniti številke v velik znak
# dodam piko tako, da je za vsak znak, ki ga spremenim v velikega pika na vsakem mestu in potem to izpišem



geslo = "eipe9thu"

def MoznaGesla(geslo):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    stevilke = "0123456789"
    geslo_seznam = []
    for i in geslo:
        geslo_seznam.append(i)

    stetje = 0
    for znak in geslo_seznam:
        if znak in abeceda:
            znak = znak.upper()
            geslo_seznam[stetje] = znak
        elif str(znak) in stevilke:
            stetje += 1
            continue
        dodaj_piko(geslo_seznam)
        geslo_seznam[stetje] = geslo_seznam[stetje].lower()
        stetje += 1


def dodaj_piko(geslo_seznam):
    dolzina = len(geslo_seznam)
    for i in range(dolzina + 1):
        if i != 0:
            geslo_seznam.remove(".")
        geslo_seznam.insert(dolzina - i, ".")
        spremeni_seznam_v_niz(geslo_seznam)
    geslo_seznam.remove(".")

def spremeni_seznam_v_niz(seznam):
    niz = ""
    for i in seznam:
        niz += i
    print(niz)

print(MoznaGesla(geslo))
