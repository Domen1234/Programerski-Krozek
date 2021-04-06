zacetno_st = int(input("Vpiši število s katerim naj začnem. "))
koncno_st = int(input("Vpiši število s katerim naj končam. "))

# Nastavimo smer, ki jo  bomo potrebovali v rangu
if zacetno_st < koncno_st:
    smer = 1
else:
    smer = -1


for stevilo in range(zacetno_st, koncno_st + smer, smer):
    if stevilo % 3 == 0 and stevilo % 5 != 0:
        print("Fizz")
    elif stevilo % 5 == 0 and stevilo % 3 != 0:
        print("Buzz")
    elif stevilo % 3 == 0 and stevilo % 5 == 0:
        print("Fizz Buzz")
    else:
        print(stevilo)
