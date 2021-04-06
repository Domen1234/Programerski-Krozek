
"""
geslo = "eipe9thu"

def MoznaGesla(geslo):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    geslo_seznam = []
    for i in geslo:
        geslo_seznam.append(i)

    stetje = 0
    for znak in geslo_seznam:
        if znak in abeceda:
            znak = znak.upper()
            geslo_seznam[stetje] = znak
        dodaj_piko(geslo_seznam)
        geslo_seznam[stetje - 1] = geslo_seznam[stetje - 1].lower()
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
"""










"""
geslo = "eipe9thu"

def MoznaGesla(geslo):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    geslo_seznam = []
    for i in geslo:
        geslo_seznam.append(i)

    seznam = geslo_seznam.copy()
    stetje = 0
    for znak in seznam:
        if znak in abeceda:
            znak = znak.upper()
            geslo_seznam[stetje] = znak
        geslo_seznam[stetje - 1] = geslo_seznam[stetje - 1].lower()
        #print(geslo_seznam)
        dodaj_piko(geslo_seznam)
        stetje += 1


def dodaj_piko(geslo_seznam):
    
    geslo_seznam = []
    for i in geslo:
        geslo_seznam.append(i)


    dolzina = len(geslo_seznam)
    for i in range(dolzina + 1):
        if i != 0:
            geslo_seznam.remove(".")
        geslo_seznam.insert(dolzina - i, ".")
        print(geslo_seznam)
    geslo_seznam.remove(".")



print(MoznaGesla(geslo))
#print(dodaj_piko(geslo))
"""

"""
geslo = "eipe9thu"

def MoznaGesla(geslo):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    geslo_seznam = []
    for i in geslo:
        geslo_seznam.append(i)

    seznam = geslo_seznam.copy()
    stetje = 0
    for znak in seznam:
        if znak in abeceda:
            znak = znak.upper()
            geslo_seznam[stetje] = znak
        geslo_seznam[stetje - 1] = geslo_seznam[stetje - 1].lower()
        #print(geslo_seznam)
        dodaj_piko(geslo_seznam)
        stetje += 1


def dodaj_piko(geslo_seznam):
    
    geslo_seznam = []
    for i in geslo:
        geslo_seznam.append(i)
    

    dolzina = len(geslo_seznam)
    for i in range(dolzina + 1):
        if i != 0:
            geslo_seznam.remove(".")
        geslo_seznam.insert(dolzina - i, ".")
        #print(geslo_seznam)
        spremeni_seznam_v_niz(geslo_seznam)
    geslo_seznam.remove(".")

def spremeni_seznam_v_niz(seznam):
    niz = ""
    for i in seznam:
        niz += i
    print(niz)

print(MoznaGesla(geslo))
#print(dodaj_piko(geslo))
#print(spremeni_seznam_v_niz(['E', 'i', 'p', 'e', '9', 't', 'h', 'u', '.']))

"""