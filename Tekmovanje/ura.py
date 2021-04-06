"""
25 ur v dnevu
45 minute v uri
80 sekund v minuti

12 mesecev(enako dolgi kot na Zemlji)
lahko 4 prestopni meseci v lletu
dodaten dan v aprilu, če je leto dedljivo s 3
dodatna dva dveva v septembu, če je leto deljivo s 5
dodatni 3 dnevi v juniju in novembru, če je leto deljivo s 7, ne pa s 3 ali/in 5
"""

def st_dod_dni(leto, mesec):
    dod_dnevi = 0
    if mesec == 1:
        dod_dnevi += 3
    if mesec == 2:
        dod_dnevi += 0
    if mesec == 3:
        dod_dnevi += 3
    if mesec == 4:
        dod_dnevi += 2
    if mesec == 5:
        dod_dnevi += 3
    if mesec == 6:
        dod_dnevi += 2
    if mesec == 7:
        dod_dnevi += 3
    if mesec == 8:
        dod_dnevi += 3
    if mesec == 9:
        dod_dnevi += 2
    if mesec == 10:
        dod_dnevi += 3
    if mesec == 11:
        dod_dnevi += 2
    if mesec == 12:
        dod_dnevi += 3
    
    if vhod_leto % 3 == 0 and mesec == 4:
        dod_dnevi += 1
    if vhod_leto % 5 == 0 and mesec == 9:
        dod_dnevi += 2
    if vhod_leto % 7 == 0 and (vhod_leto % 3 != 0 or vhod_leto % 5 != 0) and mesec == 6:
        dod_dnevi += 3
    if vhod_leto % 7 == 0 and (vhod_leto % 3 != 0 or vhod_leto % 5 != 0) and mesec == 11:
        dod_dnevi += 3

    return dod_dnevi


zac_sekunda = 00
zac_minuta = 00
zac_ura = 15
zac_dan = 21
zac_mesec = 1
zac_leto = 2021

#vhod = input("vnesi datum. ")

#vhod = "2021/02/01 14:00:00"
vhod = "2035/02/28 24:44:79"

vhod_datum = vhod.split(" ")[0]
vhod_leto = int(vhod_datum.split("/")[0])
vhod_mesec = int(vhod_datum.split("/")[1])
vhod_dan = int(vhod_datum.split("/")[2])

vhod_cas = vhod.split(" ")[1]
vhod_ure = int(vhod_cas.split(":")[0])
vhod_minute = int(vhod_cas.split(":")[1])
vhod_sekunde = int(vhod_cas.split(":")[2])


counter = 0

while True:
    # Preverjanje
    if zac_leto == vhod_leto and zac_mesec == vhod_mesec and zac_dan == vhod_dan and zac_ura == vhod_ure and zac_minuta == vhod_minute and zac_sekunda == vhod_sekunde:
        print(counter)
        break
    #print(zac_leto, zac_mesec)
    zac_sekunda += 1
    counter += 1
    if zac_sekunda == 80:
        zac_sekunda = 0
        zac_minuta += 1
        if zac_minuta == 45:
            zac_minuta = 0
            zac_ura += 1
            if zac_ura == 25:
                zac_ura = 0
                zac_dan += 1
                st_dni_v_mesecu = 28 + st_dod_dni(zac_leto, zac_mesec)
                if zac_dan > st_dni_v_mesecu:
                    zac_dan = 1
                    print("Obrnil sem mesec", zac_leto, zac_mesec)
                    zac_mesec += 1
                    if zac_mesec > 12:
                        zac_mesec = 1
                        zac_leto += 1


