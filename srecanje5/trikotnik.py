# Uporabnik vnese st n
# Izpise trikotnik n * n iz samih X

velikost = 5
znak = "#"
#velikost = int(input("Vpiši velikost. "))
#znak = input("Vpiši znak s katernim naj naredim trikotnik. ")

for vrstica in range(velikost):
    vrstica += 1
    print(znak * (vrstica + 1))
