# +
# -
# *
# /
# **  -> potence 3 ** 2 = 9
# //  -> celoštevilsko deljenje
# 10 // 3 => 3
# %   -> ostanek pri deljenju
# 10 % 3 => 1 ostanek pri deljenju je 1 (mod)
# !=  -> ni enkao

stevilo = int(input("Vpiši število. "))

if stevilo % 2 != 0:
    print("Število je liho")
else:
    print("Število je sodo")
