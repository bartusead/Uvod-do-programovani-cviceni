from turtle import exitonclick, left, right, forward, penup, pendown

for _ in range(int(input("Zadej počet řádků:"))):
    for _ in range(int(input("Zadej počet sloupců:"))):
        for _ in range(4):
            forward(50)
            left(90)
        forward(50)
    penup()
    left(180)
    forward(300)
    left(90)
    forward(50)
    left(90)
    pendown()
exitonclick()