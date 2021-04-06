import os.path

input_file = open(os.path.join("Euler", "naloga-8.in"), "r")

# Spremenimo inpu v strnig
stevilka = ""
for neki in input_file:
    stevilka += neki.strip()

# Input spremenimo v list z vsako stevko posebaj
seznam = []
for krneki in stevilka:
    seznam.append(krneki)


trenutnih_trinajst = []
naj_zmnozek = 0
for stevka in seznam:
    if len(trenutnih_trinajst) < 13:
        trenutnih_trinajst.append(int(stevka))
    else:
        trenutnih_trinajst.pop(0)
        trenutnih_trinajst.append(int(stevka))
    
    zmnozek = 1
    for i in trenutnih_trinajst:
        zmnozek = zmnozek * i
    
    if zmnozek > naj_zmnozek:
        naj_zmnozek = zmnozek
    

print(naj_zmnozek)

input_file.close()