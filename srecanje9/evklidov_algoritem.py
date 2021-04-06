# Input: 2 naravni števili a in b
# Output: največji skupni delitelj števil a in b

#x = int(input("Vpiši prvo številko. "))
x = 12
#y = int(input("Vpiši drugo številko. "))
y = 4


##### Evklidov algoritem (Največji skupni delitelj)
def gcd(a, b):
    ostanek = a % b

    while ostanek != 0:
        a = b
        b = ostanek
        ostanek = a % b

    return b

##### Največji skupni delitelj v seznamu 
def gcd_seznama(seznam):
    D = gcd(seznam[0], seznam[1])
    for i in range(len(seznam) - 1):
        D = gcd(D, seznam[i + 1])
    return D

##### Najmanjši skupni večkratnik
def lcm(a, b):
    rezultat = (a * b) // gcd(a, b)
    return rezultat

##### Najmanjši skupni večkratnik v seznamu
def lcm_seznam(seznam):
    # Določimo najmanjši
    v = lcm(seznam[0], seznam[1])
    for i in range(len(seznam) - 1):
        v = lcm(seznam[i + 1],v)
    return v


print(gcd(x, y))

print(gcd_seznama([15, 45, 25]))

print(lcm(2, 13))

print(lcm_seznam([2, 3, 13, 6, 21, 35]))
