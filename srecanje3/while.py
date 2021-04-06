stevilo = int(input("Vpiši število."))
napake = 0

while stevilo > 3:
    napake += 1
    print(stevilo)
    print("Tole pa ni manjše od 3. ")
    stevilo = int(input("Vpiši število."))
print("Bravo vpisal si število, ki je manjša od 3.")
print("Zmotil si se" + str(napake) + "krat.")

