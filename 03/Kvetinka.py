from turtle import speed, forward, left, right, exitonclick, circle

speed(10)

# květ
for x in range(18):
    for y in range(4):
        forward(50)
        left(90)
    left(20)

# stonek
right(90)
forward(400)
left(180)

# listy
for size in range(200, 80, -20):
    forward(25)
    left(45)
    for x in range(2):
        circle(size, 45)
        left(135)
    right(45)

    forward(25)
    right(45)
    for x in range(2):
        circle(-1*size, 45)
        right(135)
    left(45)

exitonclick()
