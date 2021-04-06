import os.path

ime = "HAHAHA"
skupna_starost = 0

output_file = open(os.path.join("srecanje7", "podatki.txt"), "r")

while ime != "":
    ime = input("Kako ti je ime?")

    if ime == "":
        break

    starost_v_mesecih = int(input("Koliko si star(v mesecih)? "))
    skupna_starost += starost_v_mesecih

    output_vrstica = ime + ", " + str(starost_v_mesecih) + "\n"

    output_file.write(output_vrstica)

    print("Pozdravljen " + ime, ". Star si ", str(starost_v_mesecih / 12)) 

print("Skupaj so stari", str(skupna_starost / 12), "let")

output_file.close()
