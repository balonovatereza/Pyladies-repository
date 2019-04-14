import pyglet

VYSKA = 600
SIRKA = 800
VELIKOST_HADA = 128  # v pixelech
rychlost_hada = [0, 0]  # x, y slozky rychlosti hada

window = pyglet.window.Window(width=SIRKA, height=VYSKA)

rychlost_hada[0] = 500
rychlost_hada[1] = 500


def tik(t):

    # pohyb hada
    had.x += rychlost_hada[0] * t
    had.y += rychlost_hada[1] * t

    # Odraz hada od sten
    if had.x < 0:
        rychlost_hada[0] = abs(rychlost_hada[0])
    if had.x > SIRKA - VELIKOST_HADA:
        rychlost_hada[0] = -abs(rychlost_hada[0])
    if had.y < 0:
        rychlost_hada[1] = abs(rychlost_hada[1])
    if had.y > VYSKA - VELIKOST_HADA:
        rychlost_hada[1] = -abs(rychlost_hada[1])


pyglet.clock.schedule_interval(tik, 1/30)


def zpracuj_text(text):
    had.x = 150


obrazek = pyglet.image.load('had.png')
had = pyglet.sprite.Sprite(obrazek, x=10, y=10)


def vykresli():
    window.clear()
    had.draw()


def klik(x, y, tlacitko, mod):
    print(tlacitko, mod)
    had.x = x
    had.y = y


window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik,
)

obrazek2 = pyglet.image.load('had2.png')


def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)


def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)


pyglet.clock.schedule_once(zmen, 0.2)

pyglet.app.run()
