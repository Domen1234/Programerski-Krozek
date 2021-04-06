ime = input("Kako ti je ime?")
ime_sefa = "Boris"

if ime.lower() == ime_sefa.lower():
    print("O pozdravljen sefe!")
    print("Ti si: " + ime.title())  # Da dobimo prvo črko veliko, lahko damo ime.capitalize ali.title
else:
    print("Pozdravljen %s!" %ime)
    print("Adijo %s!" %ime)
# lahko tudi tako: print("Adijo " + ime + "!")
