"""
vnos_uporabnika = "2, 4, 1, 3, 4"

def najvecji_kupcek(niz_kupckuv):
    kupcki = niz_kupckuv.split(", ")
    izbrani = []

    while True:
        najvecji = max(kupcki)
        izbrani.append(najvecji)
        najvecji_index = kupcki.index(najvecji)
        
        kupcki[najvecji_index - 1] = 0
        kupcki[najvecji_index] = 0
        kupcki[najvecji_index + 1] = 0


        #if len(kupcki) == najvecji_index:
            #kupcki.pop(najvecji_index + 1)
        #kupcki.pop(najvecji_index)
        #if najvecji_index != 0:
            #kupcki.pop(najvecji_index - 1)
        if len(kupcki) == 1:
            return "Konec. Izbral sem kupčke: ", izbrani , "Ostal je :", kupcki


print(najvecji_kupcek(vnos_uporabnika))
"""

# 4, 7, 3, 9, 2, 4, 1, 3, 4
# 7 9 4 4
from functools import lru_cache

kovanci = [2, 4, 1, 3, 4] * 7
dolzina = len(kovanci)

@lru_cache(maxsize=None)
def najvec_kovancev(index_zacetka):
    ostanek = dolzina - index_zacetka
    if ostanek == 1:
        return kovanci[index_zacetka]
    elif ostanek == 2:
        return max(kovanci[-1], kovanci[-2])

    # Izberemo ali ne izberemo kovanca na index_zacetka
    # Izberemo
    izberemo = kovanci[index_zacetka] + najvec_kovancev(index_zacetka + 2)

    # Ne izberemo
    ne_izberemo = najvec_kovancev(index_zacetka + 1) 
    
    return max(izberemo, ne_izberemo)

import time
t = time.time()


print(najvec_kovancev(0))

print(time.time() - t)
