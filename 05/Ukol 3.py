from turtle import shape, left, forward, exitonclick
from math import sqrt
from math import degrees, atan


shape('turtle')


def vykresli_domecek(sirka, vyska):
    'Vykresli domecek o sirce a vysce, kterou zada uzivatel.'
    uhel = degrees(atan(vyska / sirka))
    delka_prepony = sqrt(vyska**2 + sirka**2)
    for i in range(2):  # nakresli ctverec
        forward(sirka)
        left(90)
        forward(vyska)
        left(90)
    left(uhel)
    forward(delka_prepony)  # nakresli sikmou caru v domecku
    left((90 - uhel) * 2)
    forward(delka_prepony/2)  # nakresli strisku
    left(uhel * 2)
    forward(delka_prepony/2)  # nakresli strisku
    left((90 - uhel) * 2)
    forward(delka_prepony)  # nakresli sikmou caru v domecku


sirka = int(input('Zadej sirku domecku: '))
vyska = int(input('Zadej vysku domecku: '))
vykresli_domecek(sirka, vyska)

exitonclick()
