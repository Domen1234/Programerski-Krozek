velikost = 5
znak = "#"
#velikost = int(input("Vpiši velikost. "))
#znak = input("Vpiši znak s katernim naj naredim trikotnik. ")

for i in range(velikost):
    print(znak * (i + 1))

for c in range(velikost):
    print(znak * (velikost - (c + 1)))
