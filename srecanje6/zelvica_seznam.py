import turtle

window = turtle.Screen()
zelvica = turtle.Turtle()

#n = int(input("Vnesi število kotov. "))
n = 12
#dolzina = int(input("Vnesi dolžino stranice. "))
dolzina = 100
notranji_kot = 360 / n

zelvica.pencolor("#ff00ff")

seznam_barv = ["green", "red", "blue", "orange", "pink", "black", "brown"]

print(seznam_barv[3])

for stranica in range(n):
#    if stranica % 2 == 0:
#        zelvica.pendown()
#    else:
#        zelvica.penup()

    zelvica.pencolor(seznam_barv[stranica % len(seznam_barv)])
    zelvica.forward(dolzina)
    zelvica.right(notranji_kot)

for stranica in range(n):
    zelvica.pencolor(seznam_barv[stranica % len(seznam_barv)])
    zelvica.forward(dolzina)
    zelvica.left(notranji_kot)

turtle.done()
