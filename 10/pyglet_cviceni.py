import pyglet
from pyglet.window import key

window = pyglet.window.Window()
image = pyglet.resource.image('had.png')

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    # def vykresli():
    window.clear()
    label.draw()
    image.blit(50, 50)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The A key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

# window.push_handlers(
#    on_draw=vykresli,
# )
pyglet.app.run()
