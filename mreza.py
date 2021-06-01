from math import trunc
import random
random.seed(1234)
primer_mreza = [
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 0]
]

def prazna_mreza(w, h):
    prazna_mreza = []
    for i in range(h):
        prazna_mreza.append([])
        for j in range(w):
            prazna_mreza[i].append(0)
    return prazna_mreza

def izpisi_mrezo(mreza):
    # vsako vrsrstico posebaj, brez vejic in oklepajev
    # namesto 0 damo piko
    # namesto 1 damo #
    skupaj = ""
    for vrstica in mreza:
        spremenjena = ""
        for znak in vrstica:
            if znak == 0:
                spremenjena += "."
            elif znak == 1:
                spremenjena += "#"
            else:
                spremenjena += str(znak)
        spremenjena += "\n"
        skupaj += spremenjena
        #print(spremenjena)
    return skupaj
        

def nakljucno_napolni1(mreza, p):
    nova_mreza = []
    stetje = 0
    for vrstica in mreza:
        nova_mreza.append([])
        for znak in vrstica:
            r = random.random()
            if r < p:
                nova_mreza[stetje].append(1)
            else:
                nova_mreza[stetje].append(0)
        stetje += 1
    return nova_mreza

def nakljucno_napolni(mreza, p):
    stetje = 0
    for vrstica in mreza:
        for i in range(len(vrstica)):
            r = random.random()
            if r < p:
                mreza[stetje][i] = 0
            else:
                mreza[stetje][i] = 1
        stetje += 1
    return mreza

def flood_fill(mreza, i, j, simbol = -1):
    # Za vsakega soseda naredi naslednje:
    # preveri kaj je: 
    #   če je 1 -> nič (je previsoko)
    #   če je 0 -> 
    #       nastavim soseda na -1
    #       flood_fill(mreza, sosed_i, sosed_j, simbol)
    #   če je < 0 -> pustim, ker je to že poplavljeno
    # 
    #print(mreza)
    if mreza[i][j] == 0:
        mreza[i][j] = simbol
    if i > 0:
        if mreza[i - 1][j] == 0:
            mreza[i - 1][j] = simbol
            flood_fill(mreza, i - 1, j, simbol)
    if i < len(mreza) - 1:
        if mreza[i + 1][j] == 0:
            mreza[i + 1][j] = simbol
            flood_fill(mreza, i + 1, j, simbol)
    if j > 0:
        if mreza[i][j - 1] == 0:
            mreza[i][j - 1] = simbol
            flood_fill(mreza, i, j - 1, simbol)
    if j < len(mreza) - 1:
        if mreza[i][j + 1] == 0:
            mreza[i][j + 1] = simbol
            flood_fill(mreza, i, j + 1, simbol)
    return mreza

def poisci_prvo_0(mreza):
    stetje_i = 0
    for vrstica in mreza:
        stetje_j = 0
        for element in vrstica:
            if element == 0:
                return stetje_i, stetje_j
            stetje_j += 1
        stetje_i += 1
    return 0

mreza = [
    [1, 0, 0, 1, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 1], 
    [0, 1, 0, 0, 0], 
    [1, 0, 1, 0, 1]
    ]

def stevilo_bazenov(mreza):
    stetje_bazenov = 0
    while poisci_prvo_0(mreza) != 0:
        mreza = flood_fill(mreza, poisci_prvo_0(mreza)[0], poisci_prvo_0(mreza)[1])
        stetje_bazenov += 1
    return stetje_bazenov








#print(prazna_mreza(5, 5))
#print(izpisi_mrezo([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
#print(nakljucno_napolni([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 0.5))
#print(izpisi_mrezo(nakljucno_napolni(prazna_mreza(100, 100), 0.5)))
#print(flood_fill([[1, 0, 0, 1, 1], [1, 1, 0, 1, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]], 2, 2))
#print(izpisi_mrezo([[1, 0, 0, 1, 1], [1, 1, 0, 1, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]))
#print(izpisi_mrezo([[1, -1, -1, 1, 1], [1, 1, -1, 1, 0], [-1, 1, -1, 1, 1], [-1, -1, -1, -1, -1], [1, -1, 1, -1, 1]]))
#print(poisci_prvo_0([[1, -1, -1, 1, 1], [1, 1, -1, 1, 0], [-1, 1, -1, 1, 1], [-1, -1, -1, -1, -1], [1, -1, 1, -1, 1]]))
print(stevilo_bazenov(mreza))
