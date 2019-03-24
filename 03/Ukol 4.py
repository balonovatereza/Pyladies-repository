from turtle import shape, left, right, forward, exitonclick
from math import sqrt


shape('turtle')

for i in range(4):  # nakresli ctverec
    forward(50)
    left(90)
left(45)
forward(sqrt(2)*50)  # nakresli sikmou caru v domecku
left(90)
forward(sqrt(2)*50/2)  # nakresli strisku
left(90)
forward(sqrt(2)*50/2)  # nakresli strisku
left(90)
forward(sqrt(2)*50)  # nakresli sikmou caru v domecku
exitonclick()
