import os.path

input_file = open(os.path.join("srecanje7", "podatki.txt"), "r")
output_file = open(os.path.join("srecanje7", "podatki_v_letih.txt"), "w")

#input_file = open("podatki.txt", "r")
#output_file = open("podatki_v_letih.txt", "w")

for line in input_file:
    podatki = line.split(",")
    
    output_vrstica = podatki[0] + ", " + str(int(podatki[1]) / 12) + "\n"
    output_file.write(output_vrstica)

    print(podatki[0])

input_file.close()
output_file.close()
