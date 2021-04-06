# Collatovo zapodeje
# Če je stevilo deljivo z 2, potem ga deljimo z 2
# Če ni deljivo z 2, potem ga množim s 3 in prištejem 1
# x -> x //  2 (Če je deljiv z 2)
# x -> 3 * x + 1 (Če ni deljiv z 2)
# Končam, ko je x == 1
#  100 -> 50 -> 25 -> 76 -> 38 -> 19 -> .... -> 1
# Uporabnik naj vpiše številko, program pa izpiše vse člene od številke do 1
"""
stevilo = int(input("Vpiši število."))
list = []
st_clenov = 0

list.append(stevilo)
while stevilo != 1:
    if stevilo % 2 == 0:
        stevilo /= 2
        list.append(int(stevilo))
    else:
        stevilo *= 3
        stevilo += 1
        list.append(int(stevilo))
    st_clenov += 1
print(list)
print("Število členov je " + str(st_clenov))
"""



stevilo = int(input("Vpiši število."))
zacetno_st = stevilo
st_clenov = 0

while stevilo != 1:
    print(int(stevilo))
    st_clenov += 1
    if stevilo % 2 == 0:
        stevilo /= 2
    else:
        stevilo *= 3
        stevilo += 1

print("Število členov je " + str(st_clenov))
print("Zaporedje se zacne z " + str(zacetno_st))
