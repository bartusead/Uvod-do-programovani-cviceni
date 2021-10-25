from turtle import forward, left, right, penup, pendown, exitonclick, speed
x = int(input("Zadej délku x"))
y = int(input("Zadej délku y"))


for _ in range(8):
    for _ in range(2):
        forward(x)
        left(90)
        forward(y)
        left(90)
    forward(x)

penup()
right(180)
forward(8*x)
left(90)
forward(y)
left(90)
pendown()

for _ in range(8):
    for _ in range(2):
        forward(x)
        left(90)
        forward(y)
        left(90)
    forward(x)

penup()
right(180)
forward(8*x)
left(90)
forward(y)
left(90)
pendown()

for _ in range(8):
    for _ in range(2):
        forward(x)
        left(90)
        forward(y)
        left(90)
    forward(x)

penup()
right(180)
forward(8*x)
left(90)
forward(y)
left(90)
pendown()

for _ in range(8):
    for _ in range(2):
        forward(x)
        left(90)
        forward(y)
        left(90)
    forward(x)
        
    



exitonclick()