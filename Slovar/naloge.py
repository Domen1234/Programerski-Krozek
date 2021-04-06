# Družinski piknik. Zanima nas kaj bodo jedli gosti.
# 
# Goste predstavimo s slovarjem: ime -> najljubsa jed

# 1. Naloga: iz slovarja gostov vrni seznam vseh gostov s finkcijo imena_gostov(slovar)
# 2. Združi slovarja s funcijo zdruzi(slovar1, slovar2).
# Vrni združen slovar, kjer se podvojene vrednosti vzamejo iz slovar1
# 3. Naloga Izlušči. Vrni kolicino potrebnga materiala v seznamu

def imena_gostov(slovar):
    seznam_imen = []
    for i in slovar:
        seznam_imen.append(i)
    return seznam_imen

def zdruzi(slovar1, slovar2):
    nov_slovar = slovar1.copy()
    for i in slovar2:
        if i not in nov_slovar:
            nov_slovar[i] = slovar2[i]
    return nov_slovar

def izlusci(slovar3):
    jedi = {}
    for i in slovar3:
        if slovar3[i] not in jedi:
            jedi[slovar3[i]] = 1
        else:
            jedi[slovar3[i]] += 1
    return jedi


gosti1 = {
    "Filip": "Musaka",
    "Miha": "Cevapcici",
    "Luka": "Jota",
    "Janez": "Cevapcici",
    "Jaka": "Musaka",
    "Tine": "Cevapcici",
    "Maks": "Cevapcici"
}

gosti2 = {
    "Rok": "Musaka",
    "Miha": "Cevapcici",
    "Ana": "Musaka",
    "Filip": "Cevapcici",
    "Timotej": "Musaka",
    "Zoja": "Cevapcici"
}

print(imena_gostov(gosti1))
print(imena_gostov(gosti1) ==  ["Filip", "Miha", "Luka", "Janez", "Jaka", "Tine", "Maks"])
print(zdruzi(gosti1, gosti2))
print(zdruzi(gosti1, gosti2) == {"Filip": "Musaka", "Miha": "Cevapcici", "Luka": "Jota", "Janez": "Cevapcici", "Jaka": "Musaka", "Tine": "Cevapcici", "Maks": "Cevapcici", 
"Rok": "Musaka", "Ana": "Musaka", "Timotej": "Musaka", "Zoja": "Cevapcici"})
print(izlusci(gosti1))
print(izlusci(gosti1) == {"Musaka": 2, "Cevapcici": 4, "Jota": 1})

