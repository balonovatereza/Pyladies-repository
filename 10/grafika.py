import pyglet
window = pyglet.window.Window()


def tik(t):
    print(t)


pyglet.clock.schedule_interval(tik, 1/30)


def zpracuj_text(text):
    print(text)


window.push_handlers(on_text=zpracuj_text)

pyglet.app.run()
