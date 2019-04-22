import pyglet

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
    print('A key was pressed.')

# window.push_handlers(
#    on_draw=vykresli,
# )
pyglet.app.run()
