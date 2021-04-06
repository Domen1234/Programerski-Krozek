# Stevilo s najdaljšo Collatz verigo

konec = 10 ** 6
najdaljsa_variga = -1
st_z_max_vrigo = -1

for stevilo in range(1, konec):
    zacetno_stevilo = stevilo
    st_clenov = 0
    while stevilo != 1:
        st_clenov += 1
        if stevilo % 2 == 0:
            stevilo = stevilo // 2
        else:
            stevilo = stevilo * 3 + 1
    if najdaljsa_variga < st_clenov:
        najdaljsa_variga = st_clenov
        st_z_max_vrigo = zacetno_stevilo
#    print(str(zacetno_stevilo) + ":" + str(st_clenov))
print("Najdaljšo verigo ima ", str(st_z_max_vrigo), ", ki je dolga", str(st_clenov))
