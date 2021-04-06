a = int(input("Vpiši Število za 1. kateto: "))
b = int(input("Vpiši Število za 2.kateto: "))

if a <= 0 or b <= 0:
    print("To ni mogoce.")
else:
    c = (a**2 + b**2) ** 0.5
    print("Hipotenuza je " + str(c))
