import pyglet
import math
from pyglet.window import key
from image_load import ship_img

OBJECTS = []
batch = pyglet.graphics.Batch()
pressed_keys = set()
ROTATION_SPEED = 4  # radians per second
ACCELERATION = 100

def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        pressed_keys.add('up')
    elif symbol == key.LEFT:
        pressed_keys.add('left')
    elif symbol == key.RIGHT:
        pressed_keys.add('right')

def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        pressed_keys.discard('up')
    elif symbol == key.LEFT:
        pressed_keys.discard('left')
    elif symbol == key.RIGHT:
        pressed_keys.discard('right')

class Spaceship:
    def __init__(self):
        self.x
        self.y
        self.x_speed
        self.y_speed
        self.rotation
        self.sprite = pyglet.sprite.Sprite(ship_img, x=self.x, y=self.y, batch=batch)

    def tick(self, dt):
        # move of the spaceobject
        self.x = self.x + dt * self.x_speed
        self.y = self.y + dt * self.y_speed

        # rotation of the spaceobject
        self.rotation = self.rotation + dt * ROTATION_SPEED

        # acceleration of the spaceobject
        self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
        self.y_speed += dt * ACCELERATION * math.sin(self.rotation)

        #
        self.sprite.rotation = 90 - math.degrees(self.rotation)
        self.sprite.x = self.x
        self.sprite.y = self.y


spaceship = Spaceship()
