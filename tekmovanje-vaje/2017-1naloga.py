#"""
def zaokrozevanje(vhod):
    celi_del_vhoda = int(vhod)
    decimalen_vhod = abs(vhod - celi_del_vhoda)

    if vhod >= -0.5 and vhod < 0:
        odgovor = "-0"
        return odgovor

    if decimalen_vhod < 0.5:
        odgovor = celi_del_vhoda
    elif decimalen_vhod > 0.5:
        if vhod > 0:
            odgovor = celi_del_vhoda + 1
        else:
            odgovor = celi_del_vhoda - 1
    elif decimalen_vhod == 0.5:
        if vhod > 0:
            odgovor = celi_del_vhoda + 1
        else:
            odgovor = celi_del_vhoda

    return odgovor

#print(zaokrozevanje(-4.467), zaokrozevanje(-0.01), zaokrozevanje(-0.6), zaokrozevanje(4.467), zaokrozevanje(0.01), zaokrozevanje(0.6))
print(zaokrozevanje(-1.5))


"""


# zaokrožimo tako, da se x.5 zavkroži navzgor, ostalo pa na najbližjo celo št.
#
#odgovor je lahko 
#včasih C
#včasih C + 1
#včasih C - 1

def obrezi(stevilka):
    stevilka = int(stevilka)
    return stevilka

def zaokrozi(x):
    c = obrezi(x)
    if (x - c) >= 0.5:
        c += 1
    elif (x - c) <= -0.5:
        c -= 1
    if c == 0 and x <= 0:
        return -0.0
    return c

"""