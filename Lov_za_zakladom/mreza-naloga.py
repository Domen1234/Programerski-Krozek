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
mreza = prazna_mreza(200, 150)
#print(print_mreza(mreza))
random_mreza(mreza, p1, p2, p3)
print(print_mreza(mreza))
