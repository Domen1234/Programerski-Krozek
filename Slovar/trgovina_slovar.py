"""
slovar = {}

while True:
    kljuc = int(input("Vpiši kluč. "))
    if kljuc < 0:
        print(slovar)
        break
    ime = input("Vpiši ime. ")
    slovar[kljuc] = ime
"""

# To je zaloga
trgovina = {
    "mleko": 10,
    "jajca": 15,
    "kruh": 7
}

while True:
    ukaz = input("Vpiši ukaz. ")
    if ukaz == "kupi":
        izdelek = input("Kateri izdelek boš kupil? ")
        kolicina = int(input("Koliko jih boš kupil?"))
        trgovina[izdelek] -= kolicina
        print("Imamo jih še: ", trgovina[izdelek])
    elif ukaz == "dodaj":
        izdelek = input("Kateri izdelek bi dodal? ")
        kolicina = int(input("Koliko jih boš dodal?"))
        trgovina[izdelek] += kolicina
        print("Imamo jih še: ", trgovina[izdelek])
    elif ukaz == "zaloga":
        for i in trgovina:
            print(trgovina[i], i)
    elif ukaz == "izhod":
        print("Adijo. ")
        break
    else:
        print("Ne razumem.")




