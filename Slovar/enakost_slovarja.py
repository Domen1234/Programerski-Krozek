#
# Funkicija ki preveri ce sta dva slovarja enaka

slovar123 = {1: "sdad", 2: "dsfoidsfh"}
slovar1234 = {2: "dsfoidsfh",1: "sdad"}   #{2: "sdafgdgd",1: "dsfoihjghjfdsfh"}

def preveri(slovar1, slovar2):
    if len(slovar1) != len(slovar2):
        return False
    for i in slovar1:
        if i not in slovar2 or slovar1[i] != slovar2[i]:
            return False
    return True


print(preveri(slovar123, slovar1234))