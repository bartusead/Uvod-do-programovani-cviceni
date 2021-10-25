from turtle import forward, left, right, penup, pendown, exitonclick

for _ in range(6):
    for _ in range(6):
        forward(100)
        left(60)
    forward(100)
    right(60)

exitonclick()