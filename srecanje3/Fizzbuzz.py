# DN
# Uporabnik vnese številko
# Če je st deljivo s 3 naj izpise Fizz
# Če je st deljivo s 5 naj izpise Buzz
# Če je st deljivo obema naj izpise Fizz Buzz
# Drugace naj izpise samo to število

zacetno_st = int(input("Vpiši število s katerim naj začnem. "))
koncno_st = int(input("Vpiši število s katerim naj končam. "))


print("Začetek.")
for stevilo in range(zacetno_st, koncno_st + 1, 4):  # Če dodamo na konec 4 bo skakal stevila po 4

    if stevilo % 3 == 0 and stevilo % 5 != 0:
        print("Fizz")
    elif stevilo % 5 == 0 and stevilo % 3 != 0:
        print("Buzz")
    elif stevilo % 3 == 0 and stevilo % 5 == 0:
        print("Fizz Buzz")
    else:
        print(stevilo)
print("Konec.")
