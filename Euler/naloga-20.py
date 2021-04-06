vnos = 10

def funkcija(vnos):
    zmnozek = 1
    for krneki in range(vnos):
        krneki += 1 # Samo zato, da mi ne tezi da ne uporabim
        zmnozek *= vnos
        vnos -= 1
    return zmnozek

print("Zmnozek je: ", funkcija(vnos))

vsota = 0
for i in str(funkcija(vnos)):
    vsota += int(i)

print("Vsota stevk v zmnozku je: ", vsota)


