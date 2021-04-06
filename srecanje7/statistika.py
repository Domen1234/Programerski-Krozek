import os.path

# Naredimo seznam za starost in za imena
input_file = open(os.path.join("srecanje7", "podatki_v_letih.txt"), "r")

imena = []
starosti = []

for line in input_file:
    podatki = line.split(",")
    
    imena.append(podatki[0])
    starosti.append(float(podatki[1]))

input_file.close()


# Iščemo minimum (in drugega najmlajšega) po seznamu starosti
trenutni_min = starosti[0]
index_najmlajsega = 0
trenutni_drugi_minimum = starosti[0]
index_drugega_najmlajsega = 0

for i in range(0, len(starosti)):
    if starosti[i] < trenutni_min:
        trenutni_drugi_minimum = trenutni_min
        index_drugega_najmlajsega = index_najmlajsega
        trenutni_min = starosti[i]
        index_najmlajsega = i

print("Najmlajši je star: ", trenutni_min, "let.")
print("Najmlajšemu je ime: ", imena[index_najmlajsega])
print("Drugi najmlajši je star: ", trenutni_drugi_minimum, "let.")
print("Drugemu najmlajšemu je ime: ", imena[index_drugega_najmlajsega])


# Iščemo maximum (in drugega najstarejšega) po seznamu starosti
trenutni_max = starosti[0]
index_najstarejsega = 0
trenutni_drugi_max = starosti[0]
index_drugega_naj = 0

for j in range(0, len(starosti)):
    if starosti[j] > trenutni_max:
        trenutni_drugi_max = trenutni_max
        index_drugega_naj = index_najstarejsega
        trenutni_max = starosti[j]
        index_najstarejsega = j

print("Najstarejši je star: ", trenutni_max, "let.")
print("Najstarejšemu je ime: ", imena[index_najstarejsega])
print("Drugi najstarejši je star: ", trenutni_drugi_max, "let.")
print("Drugemu najstarejšemu je ime: ", imena[index_drugega_naj])


# Izračunamo vsoto
vsota = 0

for st in starosti:
    vsota += st

print("Skupna starost je: ", vsota)


# Izračunamo povprečje
povprecje = vsota / len(starosti)
print("Povprečna starost je: ", povprecje)


# Izpišemo vse ki so starejši(ali enako) od povprečja
strarejsi_od_povprecja = []

for k in range(len(starosti)):
    if starosti[k] >= povprecje:
        strarejsi_od_povprecja.append(imena[k])

print("Starejsi(ali enaki) od povprecja so: ", strarejsi_od_povprecja)


# Izpišemo vse ki so mlajši(ali enako) od povprečja
mlajsi_od_povprecja = []

for l in range(len(starosti)):
    if starosti[l] <= povprecje:
        mlajsi_od_povprecja.append(imena[l])

print("Mlajši(ali enaki) od povprečja so: ", mlajsi_od_povprecja)


# Izpišemo drugega najmlajšega / najstarejšega

    # preveri da dela pri [1,2,3,4,5] [2,1,3,4,5,6]
