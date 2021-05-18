
def najdi(sez, x):
    # Sprejme seznam 'sez' in element 'x' in vrne tak 'i', da velja sez[i] = x ali -1, če tak i ne obstaja
    for i in range(len(sez)):
        if sez[i] == x:
            return i
    return -1


def najdi_pametno_1(sez, x):
    # Sprejme urejen seznam 'sez' in element 'x' in vrne tak 'i', da velja sez[i] = x ali -1, če tak 'i' ne obstaja
    # Iščemo bolj pametno in nehamo, ko vemo, da elementa 'x' gotovo ne bo v seznamu
    for i in range(len(sez)):
        if sez[i] == x:
            return i
        elif sez[i] > x:
            return -1
    return -1

#seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
#print(najdi_pametno_1(seznam, 13))


"""
       0  1  2  3  4  5  6  7   8   9   10  11   12
sez = [1, 3, 4, 5, 7, 8, 9, 10, 16, 24, 50, 100], dolzine: 12
ISCEM: x = 16
bisekcija(sez, x, 0, 12)
1. KORAK: (12 + 0) // 2 = 6
2. Primerjam 9 < 16 -> True
3. KORAK: return bisekcija(sez, x, 6, 12)
    bisekcija(sez, x, 6, 12)
    1. KORAK: (6 + 12) // 2 = 9
    2. KORAK sez[9] = 24, primerjam 24 < 16 -> False
    3. KORAK return bisekcija(sez, x, 6+1, 9)

bisekcija (sez, x, zacetek, konec)
    if zacetek + 1 == konec
"""

def bisekcija(sez, x, levi, desni):
    sredina = (levi + desni) // 2
    #print(sez[levi : desni])
    if sez[sredina] == x:
        return sredina
    elif desni == levi:
        return -1
    elif sez[sredina] > x:
        return bisekcija(sez, x, levi, sredina)
    elif sez[sredina] < x:
        return bisekcija(sez, x, sredina + 1, desni)


seznam1 = [1, 3, 4, 5, 7, 8, 9, 10, 16, 24, 50, 100]
x = 17
#print(bisekcija(seznam1, x, 0, len(seznam1)))


## TEST
seznam2 = range(1, 100)

for i in seznam2:
    print(bisekcija(seznam2, i, 0, len(seznam2)) == i - 1)
