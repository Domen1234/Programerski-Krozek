moj_slovar = {       # {kljuc: vrednost} Kljuli se ne smejo ponavljat
    1: "Miha",
    2: "Luka",
    3: "Anja",
    4: "Mateja",
    17: "Katarina"

}

print(moj_slovar[17])
print(moj_slovar[4])

moj_slovar[-3] = "Janez"  # Dodamo novo stvar
print(moj_slovar[-3])

moj_slovar[4] = "Francka"  # Popravimo item v slovarju
print(moj_slovar[4]) 

print(14 in moj_slovar)    # Preverimo če je nekaj v slovarju

print(moj_slovar)



for k in moj_slovar:
    print(k, moj_slovar[k])
