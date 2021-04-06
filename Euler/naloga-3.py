vnos = 600851475143

def je_prastevilo(stevilka):
    if stevilka > 1:
        for i in range(2, stevilka):
            if stevilka % i == 0:
                return False #"Ni prastevilo."
        return True #"Je prastevilo."
    else:
        return False #"Ni prastevilo."

i = 0
seznam_faktorjev = []
while True:
    i += 1
    if je_prastevilo(i) and vnos % i == 0:
        vnos = vnos / i
        seznam_faktorjev.append(i)
    if i > vnos:
        print("Končano. ")
        break

print("Prafaktorji tega števila so: ", seznam_faktorjev)
print("Največji prafaktor tega števila je: ", max(seznam_faktorjev)) #seznam_faktorjev[-1]
