from pathlib import Path
import pyglet

#background_img = pyglet.image.load('SpaceShooterRedux/Backgrounds/blue.png')
ship_img = pyglet.image.load('SpaceShooterRedux/PNG/playerShip1_blue.png')
ship_img.anchor_x = ship_img.width // 2
ship_img.anchor_y = ship_img.height // 2


# TILES_DIRECTORY = Path('SpaceShooterRedux/Backgrounds')

# img_dict = {}
# for path in TILES_DIRECTORY.glob('*.png'):
#    img_dict[path.stem] = pyglet.image.load(path)
