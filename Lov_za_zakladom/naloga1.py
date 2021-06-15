import random

def seed():
    random.seed(2021)

def prazna_mreza(w, h):
    return [
        [0 for j in range(w)] for _ in range(h)
    ]

def cell(a):
    if a == 0:
        return "."
    if a == 1:
        return "#"
    if a == 2:
        return "X"
    if a == 3: 
        return "0"

def print_mreza(m):
    rr = "\n".join(
        "".join([cell(x) for x in l]) for l in m
    )
    return rr

def random_mreza(m, p1, p2, p3):
    seed()
    for j in range(len(m)):
        v = m[j]
        for i in range(len(v)):
            r = random.random()
            n = 3
            if r < p1:
                n = 0
            elif r < p2:
                n = 1
            elif r < p3:
                n = 2
            v[i] = n
    return m


p1 = 0.7
p2 = 0.8
p3 = 0.9
mreza0 = prazna_mreza(200, 150)
#print(print_mreza(mreza))
random_mreza(mreza0, p1, p2, p3)
#print(print_mreza(mreza))

mreza = print_mreza(mreza0)
#print(mreza)

##
## 1. Naloga
st_helija = 0
for i in mreza:
    if i == "X":
        st_helija += 1

cena_helija = st_helija * 12

#print(cena_helija)

##
## 2. Naloga
st_kamnov = 0
for i in mreza:
    if i == "#":
        st_kamnov += 1

cena_popravila = st_kamnov * 4
zasluzek = cena_helija - cena_popravila
#print(zasluzek)

##
## 3. Naloga
mreza_list = mreza.split("\n")
seznam_cen = []

for j in range(len(mreza_list)):
    cena = 0
    for i in mreza_list[j]:
        if i == "X":
            cena += 12
        elif i == "#":
            cena = cena - 4
        elif i == "+" or i == "0":
            cena = cena - 6
    seznam_cen.append(cena)


"""
for stolpec in range(200):   #range(len(mreza_list[0]))
    cena = 0
    for i in mreza_list:
        if i[stolpec] == "X":
            cena += 12
        elif i[stolpec] == "#":
            cena -= 4
        elif i[stolpec] == "0" or i[stolpec] == "+":
            cena -= 6
    seznam_cen.append(cena)
"""

print(seznam_cen)
print(max(seznam_cen), seznam_cen.index(max(seznam_cen)))
