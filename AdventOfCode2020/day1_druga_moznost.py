import os.path

input_file = open(os.path.join("AdventOfCode", "day1.in"), "r")

stevilke = []

# Damo številke iz day1.in v listo
for vrstica in input_file:
    stevilke.append(int(vrstica))

# Listo razvrstimo po velikosti
stevilke.sort()

input_file.close()


#stevilke = [1, 2, 3, 4, 5]
prva_st = stevilke[0]
druga_st = stevilke[len(stevilke) - 1]
index_prve = 0
index_druge = len(stevilke) - 1

while prva_st + druga_st != 2020:
    if index_prve >= index_druge:
        print("V tej listi ni teh dveh števil")
        break
    vsota = prva_st + druga_st
    if vsota > 2020:
        druga_st = stevilke[index_druge - 1]
        index_druge -= 1
    else:
        prva_st = stevilke[index_prve + 1]
        index_prve += 1


print("Števili: ", prva_st, druga_st)
print("Vsota: ", prva_st + druga_st)

### DRUGI DEL NALOGE


"""
for index_tretje in range(len(stevilke)):
    prva_st = stevilke[0]
    index_prve = 0
    druga_st = stevilke[len(stevilke) - 1]
    index_druge = len(stevilke) - 1
    tretja_st = stevilke[index_tretje]
    while prva_st + druga_st + tretja_st != 2020:
        if index_prve >= index_druge:
            #print("V tej listi ni teh števil")
            break
        vsota = prva_st + druga_st + tretja_st
        if vsota > 2020:
            druga_st = stevilke[index_druge - 1]
            index_druge -= 1
        else:
            prva_st = stevilke[index_prve + 1]
            index_prve += 1


print("Števili: ", prva_st, druga_st, tretja_st)
print("Vsota: ", prva_st + druga_st + tretja_st)

"""