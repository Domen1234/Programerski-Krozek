# instructions: https://adventofcode.com/2020/day/3

import os.path

input_file = open(os.path.join("AdventOfCode2020", "day3.in"), "r")

"""
### Prvi del:
trenutna_pozicija = 0
st_dreves = 0


for vrstica in input_file:
    vrstica = vrstica.strip()
    if vrstica[trenutna_pozicija] == "#":
        st_dreves += 1
    trenutna_pozicija += 3
    trenutna_pozicija = trenutna_pozicija % len(vrstica)
    print(trenutna_pozicija)

print(st_dreves)
"""

### Drugi del:
skupno_st_drves = 1
nacini_premikanja = ["11", "31", "51", "71", "12"]  # 11 -> right 1, down 1; 12 -> right 1, down 2


for nacin_premikanja in nacini_premikanja:
    # Preverimo cecl dokument za vsak nacin premikanja
    st_dreves = 0
    zap_st_vrstice = 0
    trenutna_pozicija = 0
    for vrstica in input_file:
        zap_st_vrstice += 1
        # Preverimo, če preskakujemo po 2 vrstici in potem vsako 2 preskočimo
        if nacin_premikanja[1] == "2":
            if zap_st_vrstice % 2 == 0:
                pass
        vrstica = vrstica.strip()
        # Pogledamo, če je na trenutni lokaciji drevo
        if vrstica[trenutna_pozicija] == "#":
            st_dreves += 1
        trenutna_pozicija += int(nacin_premikanja[0])
        trenutna_pozicija = trenutna_pozicija % len(vrstica)
    print(st_dreves)
    if st_dreves > 0:
        skupno_st_drves *= st_dreves

print(skupno_st_drves)

input_file.close()
