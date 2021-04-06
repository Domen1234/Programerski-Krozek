vhod = "-----*-*"
trenutno_stevilo = 1
stevilke = []
stevilke_int = []

for i in vhod:
    if i == "*":
        stevilke.append(str(trenutno_stevilo))
        stevilke_int.append(trenutno_stevilo)
    elif i == "-":
        trenutno_stevilo += 1

stetje = 0
odgovor = " + ".join(stevilke)
"""
for i in stevilke:
    stetje += 1
    odgovor += str(i)
    if stetje == len(stevilke):
        odgovor += " = "
    else:
        odgovor += " + "
"""
odgovor +=" = " + str(sum(stevilke_int))

print(odgovor)
