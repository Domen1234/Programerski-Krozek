import os.path

input_file = open(os.path.join("AdventOfCode2020", "day1.in"), "r")

stevilke = []

# Damo številke iz day1.in v listo
for vrstica in input_file:
    stevilke.append(int(vrstica))

input_file.close()

for index_prva in range(len(stevilke)):
    prva_stevilka = stevilke[index_prva]
    for index_druge in range(index_prva + 1, len(stevilke)):
        druga_stevilka = stevilke[index_druge]
        if prva_stevilka + druga_stevilka == 2020:
            print(prva_stevilka, druga_stevilka)
            print("Zmnožek teh dve številk je: ", prva_stevilka * druga_stevilka)
        for index_tretja in range(index_druge +1, len(stevilke)):
            tretja_stevilka = stevilke[index_tretja]
            if prva_stevilka + druga_stevilka + tretja_stevilka == 2020:
                print(prva_stevilka, druga_stevilka, tretja_stevilka)
                print("Zmnožek teh treh številk je: ", prva_stevilka * druga_stevilka * tretja_stevilka)


