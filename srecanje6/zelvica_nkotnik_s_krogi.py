import turtle
import random

window = turtle.Screen()
zelvica = turtle.Turtle()

#n = int(input("Vnesi število kotov. "))
n = 12
#dolzina = int(input("Vnesi dolžino stranice. "))
dolzina = 10
notranji_kot = 360 / n

zelvica.pencolor("#ff00ff")

seznam_barv = ["green", "red", "blue", "orange", "pink", "black", "brown"]

print(seznam_barv[3])

for stranica in range(n):
    # Naredimo random barvo
    izbrana_barva = seznam_barv[random.randrange(0, 7)]

    zelvica.pencolor(izbrana_barva)
    zelvica.fillcolor(izbrana_barva)

    # Nariše stranico
    zelvica.forward(dolzina)
    
    # Nariše povezavo s krogom
    zelvica.right(notranji_kot / 2)
    zelvica.left(90)
    zelvica.forward(40)
    zelvica.right(90)
    
    # Nariše krog
    zelvica.begin_fill()
    zelvica.circle(30)
    zelvica.end_fill()
    
    # Gre nazaj na lik
    zelvica.left(90)
    zelvica.forward(-40)
    zelvica.left(notranji_kot / 2)
    zelvica.right(90)

    # Se obrne, da nadaljuje z risanjem lika
    zelvica.right(notranji_kot)
turtle.done()
