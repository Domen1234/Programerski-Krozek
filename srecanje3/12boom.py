pogoj = int(input("Vpiši število katero naj bo BOOM. "))
zacetno_st = int(input("Vpiši začetno število. "))
koncno_st = int(input("Vpiši končno število. "))
koraki = int(input("Vpiši na koliko korakov naj stejem. "))

if zacetno_st < koncno_st:
    smer = koraki
else:
    smer = -koraki

for stevilo in range(zacetno_st, koncno_st + smer, smer):
    if stevilo % pogoj == 0:
        print("BOOM!")
    else:
        print(stevilo)
