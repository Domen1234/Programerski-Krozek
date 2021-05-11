# [a_0, a_1, a_2, ..., a_{n-1}] <- seznam n elementov
# <= - ni simetrična, anti simetrična a R b; b R a => a =b
# < - ni simetrična (not a < b) && (not b < a) => a = b
# tranzitivnost: a R b; b R c => a R c


# B: za vsaka par (i, j); i < j => B[i] <= B[j] ---> Dovolj je da preverim samo ozaporedna stevila, zaredi tranzitivnosti
# Kako bi preverili ali je seznam urejen
# Napiši funcijo je_urejen(sez): ki dobi seznam števil, urejene po <=; vrne True ali False
# Prazni seznami so urejeni

import time
import random

seznam = [3, 6, 2, 1, 7]
seznam1 = [1, 4, 6, 8, 3, 2, 6, 8, 4]
seznam2 = [4, 6, 8, 3, 2, 4, 6, 7]
seznam3 = [1, 4, 6, 8, 5, 4, 3, 6, 9, 3]
seznam4 = [3, 3, 8, 6, 4, 6, 8, 6, 4, 3]


def je_urejen(seznam):
    if len(seznam) == 0 or len(seznam) == 1:
        return True	
    for i in range(len(seznam)):
        if i == 0:
            continue
        if seznam[i] < seznam[i - 1]:
            return False
    return True

#print(je_urejen(seznam))


#
# Insertion sort

def insertion_sort(seznam):
    urejen_sez = [seznam.pop()]
    while True:
        x = seznam.pop()
        for i in range(len(urejen_sez)):           
            if x > urejen_sez[len(urejen_sez) - 1 - i]:
                urejen_sez.insert(len(urejen_sez) - i, x)
                break
            elif x < urejen_sez[i]:
                urejen_sez.insert(i, x)
                break
  
        if len(seznam) == 0:
            return urejen_sez
            

#print(insertion_sort(seznam4))


#
# Selection sort

def najmanjsi(seznam):
    trenutni = seznam[0]
    for i in seznam:
        if i < trenutni:
            trenutni = i
    return seznam.index(trenutni)


def selection_sort(seznam):
    sortiran = []
    while len(seznam) != 0:
        sortiran.append(seznam.pop(najmanjsi(seznam)))
    return sortiran


#print(selection_sort(seznam))


#
# Merge sort

seznam5 = [1, 2, 8, 30]
seznam6 = [2.3, 4, 5, 13, 19 ,28, 29]


def merge_star(seznam1, seznam2):
    sortiran = []
    l_sez1 = len(seznam1)
    l_sez2 = len(seznam2)
    while len(seznam1) != 0 and len(seznam2) != 0:
        if seznam1[0] <= seznam2[0]:
            sortiran.append(seznam1.pop(0))
            l_sez1 -= 1
        else:
            sortiran.append(seznam2.pop(0))
            l_sez2 -= 1
        
    if l_sez1 < l_sez2:
        while len(seznam2) != 0:
            sortiran.append(seznam2.pop(0))
    else:
        while len(seznam1) != 0:
            sortiran.append(seznam1.pop(0))

    return sortiran


#print(merge_star(seznam5, seznam6))


def merge(seznam1, seznam2):
    sortiran = []
    l_sez1 = len(seznam1)
    l_sez2 = len(seznam2)
    i1 = 0
    i2= 0
    while True:
        if seznam1[i1] <= seznam2[i2]:
            sortiran.append(seznam1[i1])
            l_sez1 -= 1
            i1 += 1
        else:
            sortiran.append(seznam2[i2])
            l_sez2 -= 1
            i2 += 1
        
        if i1 == len(seznam1) or i2 == len(seznam2):
            break
    
    sortiran += seznam2[i2:]
    sortiran += seznam1[i1:]

    return sortiran

#print(merge(seznam5, seznam6))
        


#
# Sortiranje dolgega seznama
# dolg seznam razbiješ na sezname dolžina 1
# te sezname dolžina 1 po dva mergas skupaj dokler ne dobis enega velikega


seznam = [3, 6, 2, 1, 7, 4, 5, 9, 8, 12, 3]


def urejenje_z_zlivanje(seznam):
    cas = time.time()
    nov = []
    for i in seznam:
        nov.append([i])

    while len(nov) != 1:
        nov1 = []
        for i in range(0, len(nov), 2): # 2 na koncu je po koliko skače (step)
            if i + 1 >= len(nov):
                nov1.append(nov[i])
            else:
                nov1.append(merge(nov[i], nov[i + 1]))
        nov = nov1
        #print(nov)

    return nov[0], time.time() - cas


#print(urejenje_z_zlivanje(seznam))


dolzine = [10, 100, 1000, 10000, 100000, 1000000]
sez = []
for i in dolzine:
    for krneki in range(i):
        sez.append(random.randint(0, 1000000))
    cas = time.time()
    urejenje_z_zlivanje(sez)
    print(i, time.time() - cas)


