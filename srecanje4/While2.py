# Preprosta trgovina
# Koliko različnih izdelkov si kupil
# Kaj si kupil
# Koliko kosov
# Koliko stane en kos

# Skupaj si zapravil: ______€


skupno_st_kosov = 0
skupna_cena = 0.0 # Float

while True:
    ime = input("Kaj si kupil? ")
    st_kosov = int(input("Koliko kosov tega izdelka si kupil? "))
    cena_kosa = float(input("Koliko stane en kos tega izdelka? "))
    if st_kosov == 0:
        print("Končal si z nakupom")
        break

    skupno_st_kosov += st_kosov
    skupna_cena += cena_kosa

print("Skupaj si zapravil: " + str(skupna_cena) + "€")
print("Skupaj si nakupil: " + str(skupno_st_kosov) + " izdelkov.")

