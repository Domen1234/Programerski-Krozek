import turtle

window = turtle.Screen()
zelvica = turtle.Turtle()

#n = int(input("Vnesi število kotov. "))
n = 9
#dolzina = int(input("Vnesi dolžino stranice. "))
dolzina = 100
notranji_kot = 360 / n

zelvica.pencolor("#ff00ff")
barva = 000000
#barva += 111111


for stranica in range(n):
    if stranica % 2 == 0:
        zelvica.pendown()
    else:
        zelvica.penup()
    zelvica.pencolor("#" + str(barva).zfill(6))
    barva += 111111
    zelvica.forward(dolzina)
    zelvica.right(notranji_kot)


turtle.done()
