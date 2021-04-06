import turtle
import random

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
    izbrana_barva = seznam_barv[random.randrange(0, 7)]

    zelvica.pencolor(izbrana_barva)
    zelvica.fillcolor(izbrana_barva)

    zelvica.forward(dolzina)
    zelvica.right(notranji_kot)
    zelvica.begin_fill()
    zelvica.circle(30)
    zelvica.end_fill()
    
turtle.done()
