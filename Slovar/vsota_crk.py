# Napiši funkcijo, kjer človek poda ime in priimek  in vrne vsoto črk
# "A" -> 0, "B" -> 1, ...
# "Č" -> "C", ...

abeceda = "abcdefghijklmnopqrstuvwxyz"
sifra = {}
for crka in abeceda:
    sifra[crka] = ord(crka) - ord("a")
print(sifra)

grde_crke = "čšž"
grde_crke_slovar = {
    "č": "c",
    "š": "s",
    "ž": "z"
}

ime = input("Vpiši svoje ime. ").lower()
vsota = 0

for crka in ime:
    if crka != " ":
        if crka in grde_crke:
            crka = grde_crke_slovar[crka]
        vsota += sifra[crka]

print(vsota)





