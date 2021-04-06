koda = "2345678"

def kljuc(koda):
    koda = int(koda)
    koda = str(koda)
    if "0" in koda or "9" in koda:
        return "V koda je številka 0 ali 9."

    prejsnji = koda[0]
    for i in koda:
        if int(prejsnji) - int(i) > 5 or int(prejsnji) - int(i) < -5:
            return "Ni vredu.", int(prejsnji) - int(i), i
        prejsnji = i

    prejsnji = 0
    for i in koda:
        if i == prejsnji:
            return "Znaka se podvojita. ", i, prejsnji
        prejsnji = i

    ponavljajoce_st = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0}
    for i in koda:
        ponavljajoce_st[i] += 1

    print(ponavljajoce_st)
    for i in ponavljajoce_st.values():
        if i > 2:
            return "Stevilka se je preveckrat ponovila."
    
    return "Vse je OK."
    

print(kljuc(koda))
