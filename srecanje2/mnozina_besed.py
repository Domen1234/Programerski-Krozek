ime = input("Povej svoje ime. ")
st_bonbonov = int(input("Koliko bonbonov imaš? "))

beseda = "bonbon"

# Določimo pripono glede na sklon in števnik
if st_bonbonov % 100 == 1:
    pripona = ""
elif st_bonbonov % 100 == 2:
    pripona = "a"
elif st_bonbonov % 100 == 3:
    pripona = "e"
elif st_bonbonov % 100 == 4:
    pripona = "e"
else:
    pripona = "ov"

# Izpišemo vse skupaj s pripono 
print(ime + " ima " + str(st_bonbonov) + " " + beseda + pripona)
