predzadnji = 0
zadnji = 1
vsota = 0
naslednji = 0

while naslednji < 4000000:
    naslednji = zadnji + predzadnji
    predzadnji = zadnji
    zadnji = naslednji
    if naslednji % 2 == 0 and naslednji < 4000000:
        vsota += naslednji
print(vsota)
