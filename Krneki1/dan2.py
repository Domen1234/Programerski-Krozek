"""
# Preprosta trgovina
# Vpišeš koliko denarja imaš in koliko stane izdelek
# program ti napiše koliko denarja ti mora vrniti

denar = float(input("Koliko denarja imaš? "))
izdelek = str(input("Koliko stane izdelek? "))
vracilo = denar - float(izdelek)
print("Vrnit ti moram " + str(vracilo) + " evrov.")
"""

"""
# if stavek:
# if pogoj:
#     kaj se zgodi, če se pogoj izpolne
# else:
#     kaj se zgodi, če se pogoj ne izpolne

# Program te vpraša koliko si star
# če si starejši od 18 let ti napiše: Super lahko delaš izpit za avto
# če pa nisi starejši od 18 let ti pa napiše: Še malo moraš počakati

starost = int(input("Koliko si star? "))
if starost >= 18:
    print("Super lahko delaš izpit za avto.")
else:
    print("Še malo moraš počakati.")

"""

# Program, ki te sprašuje matematične porbleme (z knjižnjico random)
# Program ti postavi nek račun s seštevnjem -> npr.: 5 + 3 = 
# Ti vpišeš odgovor
# Program preveri če je previlno

import random

prva_stevilka = str(random.randint(0, 50))
druga_stevilka = str(random.randint(0, 50))

racun = int(input(prva_stevilka + " + " + druga_stevilka + " = " ))

razultat = int(prva_stevilka) + int(druga_stevilka)

if racun == razultat:
    print("Bravo razultat je pravilen.")
else:
    print("Nič ne znaš. Pravilna rešitev je: " +  str(razultat))