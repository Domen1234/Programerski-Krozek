# Napiši funkcijo, ki dobi ime in pozdravi človeka -- pozdrav("Domen", "Korenini")
# Izpiše naj: Živjo Domen \n Tvoje ime je dolko x znako, priimek je dolg y znakov

def pozdrav(ime, priimek):
    return "Živjo " + str(ime) + "." +"\n" + "Tvoje ime je dolgo " + str(len(ime)) + " znakov.\n" + "Tvoj priimek je dolg " + str(len(priimek)) + " znakov."


print(pozdrav("Domen", "Korenini"))

# , "Tvoje ime je dolgo ", str(len(ime)), "znakov.\n", "Tvoj priimek je dolg ", str(len(priimek)), "znakov."