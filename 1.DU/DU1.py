from turtle import forward, left, right, penup, pendown, setpos, speed, exitonclick, circle
a = 100
speed(0)
for _ in range(2):
    for _ in range(3):
        for _ in range(4):
            forward(a)
            left(90)
        forward(a)
    left(180)
    penup()
    forward(3*a)
    left(90)
    forward(a)
    left(90)
    pendown()

for _ in range(3):
        for _ in range(4):
            forward(a)
            left(90)
        forward(a)
penup()

x = int(input("Zadej souřadnici x:"))
y = int(input("Zadej souřadnici y:"))

setpos(x,y)
pendown()
circle(50)





exitonclick()



