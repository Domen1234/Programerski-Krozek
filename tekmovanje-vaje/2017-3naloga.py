zaloga = ["", "", "", "", "", ""]


zaloga[0] = int(input("Zaloga sendvicev st. 1: "))
zaloga[1] = int(input("Zaloga sendvicev st. 2: "))
zaloga[2] = int(input("Zaloga sendvicev st. 3: "))
zaloga[3] = int(input("Zaloga sendvicev st. 4: "))
zaloga[4] = int(input("Zaloga sendvicev st. 5: "))
zaloga[5] = int(input("Zaloga sendvicev st. 6: "))
"""
zaloga[0] = 1
zaloga[1] = 1
zaloga[2] = 1
zaloga[3] = 1
zaloga[4] = 1
zaloga[5] = 1
"""

izbrani_sendvic = [0, 0, 0, 0, 0, 0]

while True:
    zahtevani_sendvic = int(input("Pozdravljeni, kateri sendvic zelite? "))

    if zahtevani_sendvic == 0:
        # Napisemo kateri so najbolj kupljani sendvici
        max_sendvic = 0
        popularn_sendvici = ""
        index = 0
        for sendvic in izbrani_sendvic:
            if sendvic >= max_sendvic:
                max_sendvic = sendvic
                popularn_sendvici += str(index + 1) + " "
            index += 1

        print("Najbolj popularen je sendvic st. ", popularn_sendvici)

        # Napisemo katerih sendvicev je zmanjkalo
        zmanjkanih_sendvicev = ""
        index = 0
        for sendvic in zaloga:
            if sendvic == 0:
                zmanjkanih_sendvicev += str(index + 1) + " "
            index += 1
        print("Zmanjkalo je sendvičev st. ", zmanjkanih_sendvicev)
        
        break

    # Preverimo, če je sendvic na zalogi in ga odštejemo od zaloge
    if zaloga[zahtevani_sendvic - 1] != 0:
        zaloga[zahtevani_sendvic -1] -= 1
        izbrani_sendvic[zahtevani_sendvic -1] += 1
        print("Izvolite sendvic st. ", zahtevani_sendvic, " Dober tek!")
    else:
        print("Sendvicev tipa ", zahtevani_sendvic, "nam je zal zmanjkalo. Vec srece prihodnjic!")

