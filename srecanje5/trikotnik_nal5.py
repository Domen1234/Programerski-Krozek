velikost = 5
debelina = 3
znak = "#"
znak_presledek = "."
#velikost = int(input("Vpiši velikost. "))
#debelina = int(input("Vpiši debelino trkotnika. "))
#znak = input("Vpiši znak s katernim naj naredim trikotnik. ")
#znak_presledek = input("Vpiši znak za presledek. ")

stranica = znak * debelina

for i in range(velikost):
    prvi_presledek = znak_presledek * (velikost - (i + 1))
    vmesni_presledek = (znak_presledek * (i + 1)) + (znak_presledek * i)
    print(prvi_presledek + stranica + vmesni_presledek +stranica)

