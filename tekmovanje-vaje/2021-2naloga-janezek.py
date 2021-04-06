from functools import lru_cache
"""
import sys
f = open("tekmovanje-vaje/janezek.in")

nizi = f.readlines().split(",")

stevilke = []
for c in nizi:
    stevilke.append(int(c))
print(stevilke)
"""

stevilke = [1,2,4,6,3,2,5,7,3,1,2,4,5,3,2,3,4,5,6,5,4,3,2,3,4,5,6,12,123,546,34523,45,1,1,1,1,1,1,7,8,9,0,1,2,3,4,5]

zapomnjeno = {}

#@lru_cache(maxsize=None)
def maksimum(mesto_janezka):
    if mesto_janezka in zapomnjeno:
        return zapomnjeno[mesto_janezka]
    if len(stevilke) - 1 == mesto_janezka:
        return stevilke[mesto_janezka]
    if mesto_janezka >= len(stevilke):
        return 0
    #Izberemo
    prva_moznost = stevilke[mesto_janezka] + maksimum(mesto_janezka + 2)
    # Ne izberemo
    druga_moznost = maksimum(mesto_janezka + 1)

    rez = max(prva_moznost, druga_moznost)

    zapomnjeno[mesto_janezka] = rez

    return rez




print(maksimum(0))

#f.close()
