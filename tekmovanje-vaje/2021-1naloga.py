def izenaceno(polje):
    stetje_x = 0
    stetje_o = 0
    zap_x = 0
    zap_o = 0

    for znak in polje:
        if znak == "x":
            stetje_x += 1
            zap_x += 1
            zap_o = 0
        elif znak == "o":
            stetje_o += 1
            zap_o += 1
            zap_x = 0
        else:
            return "Napaka."

        if zap_x == 3:
            return 0 # "Igra ni izenacena. Zmagal je: x"
        elif zap_o == 3:
            return 0 #"Igra ni izenacena. Zmagal je o"
    
    if stetje_x == stetje_o:
        return 1 #"Igra je izenacena."
    else:
        return 0 #"Igra ni izenacena. "

print(izenaceno("xoooxx"))