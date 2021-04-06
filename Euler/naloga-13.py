import os.path

input_file = open(os.path.join("Euler", "naloga-13.in"), "r")

vsota = 0

for vrstica in input_file:
    vsota += int(vrstica)

vsota = str(vsota)
print(vsota[0:10])

input_file.close()
