from turtle import penup, dot, forward, exitonclick, backward, left, right
from turtle import pencolor, home, setposition, heading, circle, speed, pendown

speed(0)

vzdalenost_tecek = 30  # vzdalenost tecek od sebe
sirka = 10  # pocet tecek na radku/sloupci
pencolor('red')
penup()

for i in range(sirka):
    for j in range(sirka):
        dot()
        forward(vzdalenost_tecek)
    backward(vzdalenost_tecek * sirka)
    right(90)
    forward(vzdalenost_tecek)
    left(90)

home()
pendown()
pencolor('green')
for k in range(50):
    forward(100)
    left(123)
pencolor('blue')
for l in range(70):
    forward(80)
    left(100)
penup()

exitonclick()
