from turtle import forward, left, right, penup, pendown, setpos, speed, exitonclick, circle, title
from math import sqrt

z = 100
speed(0)
for _ in range(2):
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

for _ in range(3):
        for _ in range(4):
            forward(z)
            left(90)
        forward(z)
penup()                 # Nakreslí mřížku
##############################################################################################################
print("Vítejte u piškvorek!")
print("Hráči postupně vybírají pole a - i podle následujícího vzoru:")
print("a | b | c\n---------\nd | e | f\n---------\ng | h | i")

for _ in range(4):

    print("Hraje hráč 1")

    kód1 = input("Zadej kód čtverce:")

    while kód1 != "a" and kód1 != "b" and kód1 != "c" and kód1 != "d" and kód1 != "e" and kód1 != "f" and kód1 != "g" and kód1 != "h" and kód1 != "i":
        print("Musíš zadat platný kód čtverce, tedy a, b, c, d, e, f, g, h, nebo i")
        kód1 = input("Zadej kód čtverce:")  # Vylučuje nesprávný vstup od hráče 1

    if kód1 == "a":
        setpos(50,0)
    elif kód1 == "b":
        setpos(150,0)
    elif kód1 == "c":
        setpos(250,0)
    elif kód1 == "d":
        setpos(50,-100)
    elif kód1 == "e":
        setpos(150,-100)
    elif kód1 == "f":
        setpos(250,-100)
    elif kód1 == "g":
        setpos(50,-200)
    elif kód1 == "h":
        setpos(150,-200)
    elif kód1 == "i":
        setpos(250,-200)
                                        # Po výběru čtverce umístí kurzor (ocas želvy) do příslušného pole
    pendown()
    circle(50)
    penup()
                                        # Nakreslí kružnici do příslušného pole
    print("Hraje hráč 2")
    kód2 = input("Zadej kód čtverce:")

    while kód2 != "a" and kód2 != "b" and kód2 != "c" and kód2 != "d" and kód2 != "e" and kód2 != "f" and kód2 != "g" and kód2 != "h" and kód2 != "i":
        print("Musíš zadat platný kód čtverce, tedy a, b, c, d, e, f, g, h, nebo i")
        kód2 = input("Zadej kód čtverce:")
                                        # Vylučuje nesprávný vstup od hráče 2
    if kód2 == "a":
        setpos(50,0)
    elif kód2 == "b":
        setpos(150,0)
    elif kód2 == "c":
        setpos(250,0)
    elif kód2 == "d":
        setpos(50,-100)
    elif kód2 == "e":
        setpos(150,-100)
    elif kód2 == "f":
        setpos(250,-100)
    elif kód2 == "g":
        setpos(50,-200)
    elif kód2 == "h":
        setpos(150,-200)
    elif kód2 == "i":
        setpos(250,-200)
                                        # Po výběru čtverce umístí kurzor (ocas želvy) do příslušného pole

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
                                        # Nakreslí křížek do příslušného pole
print("Hraje hráč 1")
kód1 = input("Zadej kód čtverce:")
while kód1 != "a" and kód1 != "b" and kód1 != "c" and kód1 != "d" and kód1 != "e" and kód1 != "f" and kód1 != "g" and kód1 != "h" and kód1 != "i":
    print("Musíš zadat platný kód čtverce, tedy a, b, c, d, e, f, g, h, nebo i")
    kód1 = input("Zadej kód čtverce:")

if kód1 == "a":
    setpos(50,0)
elif kód1 == "b":
    setpos(150,0)
elif kód1 == "c":
    setpos(250,0)
elif kód1 == "d":
    setpos(50,-100)
elif kód1 == "e":
    setpos(150,-100)
elif kód1 == "f":
    setpos(250,-100)
elif kód1 == "g":
    setpos(50,-200)
elif kód1 == "h":
    setpos(150,-200)
elif kód1 == "i":
    setpos(250,-200)

pendown()
circle(50)
penup()                                     # Celá procedura ještě jednou, aby to bylo 9x
print("Konec hry!")