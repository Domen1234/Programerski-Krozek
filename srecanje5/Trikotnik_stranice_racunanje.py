a = float(input("Vpiši stranico a "))
b = float(input("Vpiši stranico b "))
c = float(input("Vpiši stranico c "))

obseg = a + b + c
s = (a + b + c) / 2
ploscina =  (s * (s - a) * (s - b) * (s - c)) ** 0.5

if a + b > c and a + c > b and b + c > a:
    print("To je trikotnik.")
    print("Obseg je " + str(obseg))
    print("Ploščina je " + str(ploscina))
else:
    print("To ni trikotnik.")

if a > b and a > c:
    print("Stranica a je najdaljša")

if b > a and b > c:
    print("Stranica b je najdaljša")

if c > a and c > b:
    print("Stranica c je najdaljša")
