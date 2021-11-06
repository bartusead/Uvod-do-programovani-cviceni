from turtle import forward, left, right, penup, pendown, setpos, speed, exitonclick, circle, title
from math import sqrt

z = 100
speed(0)
for _ in range(3):
    for _ in range(3):
        for _ in range(4):
            forward(z)
            left(90)
        forward(z)
    left(180)
    penup()
    forward(3*z)
    left(90)
    forward(z)
    left(90)
    pendown()

penup()                 # Nakreslí mřížku
##############################################################################################################
print("Vítejte u piškvorek!")
print("Hráči postupně vybírají pole a - i podle následujícího vzoru:")
print("a | b | c\n---------\nd | e | f\n---------\ng | h | i")

for i in range(1, 10):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
        print("Hraje hráč 1")
    elif i == 2 or i == 4 or i == 6 or i == 8:
        print("Hraje hráč 2")
    kod1 = input("Zadej kód čtverce:")

    while kod1 != "a" and kod1 != "b" and kod1 != "c" and kod1 != "d" and kod1 != "e" and kod1 != "f" and kod1 != "g" and kod1 != "h" and kod1 != "i":
        print("Musíš zadat platný kód čtverce, tedy a, b, c, d, e, f, g, h, nebo i")
        kod1 = input("Zadej kód čtverce:")  # Vylučuje nesprávný vstup od hráče

    if kod1 == "a":
        setpos(50,0)
    elif kod1 == "b":
        setpos(150,0)
    elif kod1 == "c":
        setpos(250,0)
    elif kod1 == "d":
        setpos(50,-100)
    elif kod1 == "e":
        setpos(150,-100)
    elif kod1 == "f":
        setpos(250,-100)
    elif kod1 == "g":
        setpos(50,-200)
    elif kod1 == "h":
        setpos(150,-200)
    elif kod1 == "i":
        setpos(250,-200)
                                        # Po výběru čtverce umístí kurzor (ocas želvy) do příslušného pole
    pendown()
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
        circle(50)
        penup()
    elif i == 2 or i == 4 or i == 6 or i == 8:
        pendown()
        forward(z/2)
        left(135)
        forward(sqrt(2*(z**2)))
        left(135)
        forward(z)
        left(135)
        forward(sqrt(2*(z**2)))
        right(45)
        penup()
                                        # Nakreslí kružnici nebo křížek do příslušného pole
                                    
print("Konec hry!")
exitonclick()