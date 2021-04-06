nepodvojeno = []
beseda = input("Vpiši besedo. ")

for i in range(len(beseda)):
    if i <= len(beseda) - 2 and beseda[i] != beseda[i + 1]:
        nepodvojeno.append(beseda[i])
nepodvojeno.append(beseda[i])
print("Beseda brez podvojenih črk je: " + str(nepodvojeno))
