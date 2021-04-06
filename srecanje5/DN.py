# Uporabnik naj vpise številko
# Izpiši vsoto njegovih števk

# x = 1357
# x % 10 -> 7
# x // 10 -> 135

stevilo = int(input("Vpiši številko. "))
vsota = 0

if stevilo < 0:
    stevilo = stevilo * -1  # ali stevilo = abs(stevilo)

while stevilo != 0:
    print("Število:" + str(stevilo))
    zadja_stevla = stevilo % 10
    vsota += zadja_stevla
    stevilo = stevilo // 10  # // deli celo st in ne dobimo decimalk
print("Vsota števk je " + str(vsota))
