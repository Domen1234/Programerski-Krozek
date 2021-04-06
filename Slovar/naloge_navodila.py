# Naloge s slovarji
# Družinski piknik. Zanima nas, kaaj bodo jedli gostje
# 
# Goste predstavimo s slovarjem: ime -> najljubšo jed

gosti = {"Filip": "musaka", "Miha": "Cevapcici"} 

# 1. Naloga: iz slovarja gostov vrni seznam vseh gostov
def imena_gostov(s):
    return ["Filip", "Luka"]
    # Vrne seznam imen gostov

s1 = {"Filip": "musaka", "Luka": "Jota"}
s2 = {"Filip": "", "Miha": ""}
print(imena_gostov(s1)== ["Filip", "Luka"])
print(imena_gostov(s1)== ["Filip", "Luka"])

# 2. Naloga: Združi slovarja
def zdruzi(s1, s2):
    # Vrnite združen slovar, 
    # kjer se podvojene vrednosti vzamejo iz s1
    pass

# 3. Naloga Izlušči
# Dobimo slovar kaj gostje jedo in ljudi, ki so potrdili udeležbo
# Naredi nakupovalni seznam
# izlusci(gosti, ["Miha", "Filip", "Luka"]) 
#       -> {"musaka": 1, "Cevapcici": 1}
def izlusci(slovar, seznam_imen):
    pass # Vrne kolicino potrebnega materiala