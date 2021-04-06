vnos_uporabnika = int(input("Vnesi število ur v dnevu!"))
vnos_dni = int(input("Vnesi število dni v mesecu!"))
vnos_ur = int(input("Vnesi sekund ur v uri!"))
vnos_milisek = int(input("Vnesi število milisekund v sekundi!"))

st_dni = vnos_dni
st_ur = st_dni * vnos_uporabnika
st_sek = st_ur * vnos_ur
milisek = st_sek * vnos_milisek

max_milisek = int(input("Koliko je največje število milisekund v mesecu?"))

zacetni_pozdrav = "Stevilo milisekund v mesecu je:"

print(zacetni_pozdrav)
print(milisek)

if milisek > max_milisek:
    print("Delaš nadure")
    print("Pazi, da ne boš prveč utrujen")
else:
    print("Delaš premalo")
    print("Nisi dovolj delaven")

print("Adijo")
