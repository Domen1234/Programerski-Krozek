velikost = 5
znak = "#"
znak_presledek = "."
#velikost = int(input("Vpiši velikost. "))
#znak = input("Vpiši znak s katernim naj naredim trikotnik. ")
#znak_presledek = input("Vpiši znak za presledek. ")

for i in range(velikost):
    print((znak_presledek * (velikost - (i + 1))) + (znak * (i + 1)) + (znak * i))
