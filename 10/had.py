import pyglet
import math
import random

SIRKA = 800
VYSKA = 600
VELIKOST_HADA = 128  # v pixelech
RYCHLOST = 300

pozice_hada = [0, 0]  # x, y souradnice pozice hada
rychlost_hada = [0, 0]  # x, y slozky rychlosti hada


window = pyglet.window.Window(width=SIRKA, height=VYSKA)


def reset():
    pozice_hada[0] = SIRKA // 2
    pozice_hada[1] = VYSKA // 2

    # x-ova rychlost - bud vpravo, nebo vlevo
    if random.randint(0, 1):
        rychlost_hada[0] = RYCHLOST
    else:
        rychlost_hada[0] = -RYCHLOST

    # y-ova rychlost - uplne nahodna
    rychlost_hada[1] = random.uniform(-1, 1) * RYCHLOST


    # nastavit vychozi stav pro start hry
reset()


def tik(t):
    # pohyb hada
    pozice_hada[0] += t * rychlost_hada[0]
    pozice_hada[1] = rychlost_hada[0] + rychlost_hada[0] * math.sin(pozice_hada[0] / 5)

    # odraz hada od vertikalnich sten
    if pozice_hada[0] < VELIKOST_HADA // 2:
        rychlost_hada[0] = abs(rychlost_hada[0])


pyglet.clock.schedule_interval(tik, 1/30)


def zpracuj_text(text):
    had.x = 150
    had.rotation = had.rotation + 10


obrazek = pyglet.image.load('had.png')
had = pyglet.sprite.Sprite(obrazek)  # sprite je obr. ktery ma navic data / pozici a rotation,
# pyglet bude rovnou vedet kde ho ma hledat


def vykresli():
    window.clear()
    had.draw()


def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y


window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,  # draw se deje sama, poprve, kdy se okno otevre, pohne se s nim, kdy se prepnete do okna..
    on_mouse_press=klik,
)

obrazek2 = pyglet.image.load('had2.png')


def zmen(t):
    had.image = obrazek2  # vymeni obrazek
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)  # naplanuje akci


def zmen_zpatky(t):
    had.image = obrazek  # vymeni obrazek
    pyglet.clock.schedule_once(zmen, 0.2)  # naplanuje akci


pyglet.clock.schedule_once(zmen, 1)


pyglet.app.run()
