# Smrekica s Trikotniki
# ......X
# .....XXX
# ....XXXXX
# ...XXXXXXX
# ..XXXXXXXXX
# .....XXX
# ....XXXXX
# ...XXXXXXX
# ..XXXXXXXXX
# .XXXXXXXXXXX
# ....XXXXX
# ...XXXXXXX
# ..XXXXXXXXX
# .XXXXXXXXXXX
# XXXXXXXXXXXXX


deli = 3
vrstice = 5
sirina = 7
znak = "#"
znak_presledek = "."
#velikost = int(input("Vpiši velikost. "))
#znak = input("Vpiši znak s katernim naj naredim trikotnik. ")
#znak_presledek = input("Vpiši znak za presledek. ")


for delec in range(deli):
    for i in range(vrstice):
        prvi_presledek = znak_presledek * (sirina - (i + 1 + delec))
        del_smrekice = znak * (i + 1 + delec)
        drugi_del_smrekice = znak * (i + delec)
        print(prvi_presledek + del_smrekice + drugi_del_smrekice)



"""
for i in range(5):
    prvi_presledek = znak_presledek * (sirina - (i + 1))
    del_smrekice = znak * (i + 1)
    drugi_del_smrekice = znak * i
    print(prvi_presledek + del_smrekice + drugi_del_smrekice)

for j in range(5):
    prvi_presledek = znak_presledek * (sirina - (j + 2))
    del_smrekice = znak * (j + 2)
    drugi_del_smrekice = znak * (j + 1)
    print(prvi_presledek + del_smrekice + drugi_del_smrekice)

for k in range(5):
    prvi_presledek = znak_presledek * (sirina - (k + 3))
    del_smrekice = znak * (k + 3)
    drugi_del_smrekice = znak * (k + 2)
    print(prvi_presledek + del_smrekice + drugi_del_smrekice)
"""