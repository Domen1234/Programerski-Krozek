import time
import random

crke = ("a", "s", "d", "f", "j", "k", "l", " ")
st_pravilnih = 0
st_vseh = 0


while True:
    izbrana_crka = crke[random.randint(0,len(crke) - 1)]
    vnos = input("Vpiši črko " + izbrana_crka + ": ")
    if vnos == izbrana_crka:
        st_pravilnih += 1
    elif vnos.lower() == "konec":
        print("Pravilno si vpisal ", st_pravilnih, " črk, od ", st_vseh)
    else:
        print("Napačno.")
    st_vseh += 1





