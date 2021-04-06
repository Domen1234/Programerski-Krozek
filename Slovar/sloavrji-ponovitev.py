slovar = {1: "Ena", 2: "Dva", 3: "Tri"}

neki = slovar[1]
drugo = slovar[3]
print(neki, drugo)

slovar[15] = "Petnajst"
slovar[1] = "Enaaaaaaa"
print(slovar)


for k in slovar:
    print(k, slovar[k])

# Drugacen nacin
for k, v in slovar.items():
    print(k, v)

# Preverimo če je v slovarju
print(3 in slovar)
print(99 in slovar)


# 
print(slovar.items())
print(list(slovar.keys()))
print(list(slovar.values()))


