from turtle import shape, left, forward, exitonclick
from math import sqrt


shape('turtle')


def vykresli_domecek(sirka_domecku):
    'Vykresli domecek velikosti, kterou zada uzivatel.'
    delka_prepony = sqrt(2)*sirka_domecku
    for i in range(4):  # nakresli ctverec
        forward(sirka_domecku)
        left(90)
    left(45)
    forward(delka_prepony)  # nakresli sikmou caru v domecku
    left(90)
    forward(delka_prepony/2)  # nakresli strisku
    left(90)
    forward(delka_prepony/2)  # nakresli strisku
    left(90)
    forward(delka_prepony)  # nakresli sikmou caru v domecku


sirka = int(input('Zadej sirku domecku: '))

vykresli_domecek(sirka)

exitonclick()
