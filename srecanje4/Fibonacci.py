# 0  1  1  2  3  5  8  13 ...
# a  b->c
#    a  b->c

max_velikost = 1000

predzadnji = 1
zadnji = 2

while zadnji < max_velikost:
    naslednji = zadnji + predzadnji
    predzadnji = zadnji
    zadnji = naslednji
    print(naslednji)

