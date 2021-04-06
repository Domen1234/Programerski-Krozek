#
# Sifriranje in desifriranje


def zasifriraj(sifra, beseda):
    zasifrirano = ""
    for i in beseda:
        if i in sifra:
            i = sifra[i]
        zasifrirano += i
    return zasifrirano

def obratna_sifra(sifra):
    obratna_sifra = {}
    for i in sifra:
        vrednost = sifra[i]
        obratna_sifra[vrednost] = i
    return obratna_sifra

def desifriraj(sifra, beseda):
    desifrirano = ""
    for i in beseda:
        i = obratna_sifra(sifra)[i]
        desifrirano += i
    return desifrirano


def preveri_sifro(sifra):
    abeceda = "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"
    if len(abeceda) != len(sifra):
        return False
    for i in abeceda:
        if i not in sifra or i not in obratna_sifra(sifra):
            return False
    return True



nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
              'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
              'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
              'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
              'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}


fake_sifra = {'Č': 'A', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
              'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
              'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
              'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
              'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'X': 'D'}              

beseda = "KRNEKI"
zasifrirana_beseda = "ILŠVIB"

print(zasifriraj(nasa_sifra, beseda))
print(desifriraj(nasa_sifra, zasifrirana_beseda))
print(preveri_sifro(fake_sifra))
