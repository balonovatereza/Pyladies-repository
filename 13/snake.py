import pyglet
from pyglet.window import key
from random import randrange
from image_load import apple_img, snake_tiles


CELL_SIZE = 64  # pixels
WIDTH = 10  # no. of columns
HEIGHT = 10  # no. of rows


class Game:
    '''
    Basic game info, snake position, food position, creation of sprites,
    snake moves.
    '''
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake_position = [(0, 0), (1, 0), (2, 0)]
        self.direction = (1, 0)
        self.batch = pyglet.graphics.Batch()
        self.snake_sprites = []
        self.food_position = [(4, 7)]
        self.food_sprites = []
        self.poisoned_food_position = []
        self.poisoned_food_sprites = []
        pyglet.clock.schedule_interval(self.next_step, 1/4)

    def move(self):
        '''
        One-step movement of snake in set direction. Solves also situations:
        - snake eats itself
        - snake hits the wall
        - snake eats food.
        '''
        x, y = self.snake_position[-1]  # head position
        move_x, move_y = self.direction  # one step in set direction
        new_step = (x + move_x, y + move_y)

        # Snake eats itself
        if new_step in self.snake_position:
            pyglet.clock.unschedule(game.next_step)

        # Snake hits the wall
        elif (x + move_x) > (WIDTH - 1) or (x + move_x) < 0 or (y + move_y) > (HEIGHT - 1) or (y + move_y) < 0:
            pyglet.clock.unschedule(game.next_step)

        # Snake moves
        if new_step not in self.food_position:
            del self.snake_position[0]

        # Snake eats food
        else:
            del self.food_position[0]
            self.generate_food()

        self.snake_position.append(new_step)

    def sprite_direction(self, x, y):
        '''
        Returns a direction (right, left, bottom, top), which is needed to set
        a right name of image.
        '''
        if (x, y) == (-1, 0):
            return 'right'
        if (x, y) == (1, 0):
            return 'left'
        if (x, y) == (0, 1):
            return 'bottom'
        if (x, y) == (0, -1):
            return 'top'

    def draw(self):
        '''
        Clears the window, recreates snake and food sprites and draws them
        into the window.
        '''
        window.clear()
        self.create_snake_sprites()
        self.create_food_sprites()
        self.batch.draw()

    def create_snake_sprites(self):
        '''
        Clears and then recreates snake sprites.
        Also sets a name of the image to be picked to particular snake parts.
        Names of the x, y coordinates:
        - 'x_to_dir' and 'y_to_dir' - difference between value of x, y and
            value of x, y of the next snake part
        - 'x_from_dir' and 'y_from_dir' - difference between value of x, y and
            value of x, y of the preceding snake part
        '''
        self.snake_sprites.clear()

        for i in range(len(self.snake_position)):

            # Tail of the snake
            if i == 0:
                x_to_dir = self.snake_position[i][0] - self.snake_position[i + 1][0]
                y_to_dir = self.snake_position[i][1] - self.snake_position[i + 1][1]
                img_name = 'tail-' + self.sprite_direction(x_to_dir, y_to_dir)

            # Body of the snake
            if i > 0 and i < (len(self.snake_position) - 1):
                x_to_dir = self.snake_position[i][0] - self.snake_position[i + 1][0]
                y_to_dir = self.snake_position[i][1] - self.snake_position[i + 1][1]
                x_from_dir = self.snake_position[i][0] - self.snake_position[i - 1][0]
                y_from_dir = self.snake_position[i][1] - self.snake_position[i - 1][1]
                img_name = self.sprite_direction(x_to_dir, y_to_dir) + '-' + self.sprite_direction(x_from_dir, y_from_dir)

            # Head of the snake
            if i == len(self.snake_position) - 1:
                x_from_dir = self.snake_position[i][0] - self.snake_position[i - 1][0]
                y_from_dir = self.snake_position[i][1] - self.snake_position[i - 1][1]
                img_name = self.sprite_direction(x_from_dir, y_from_dir) + '-head'
            x = self.snake_position[i][0]
            y = self.snake_position[i][1]
            self.snake_sprites.append(pyglet.sprite.Sprite(snake_tiles[img_name], x=x*CELL_SIZE, y=y*CELL_SIZE, batch=self.batch))

    def next_step(self, t):
        '''
        Calls funkction move() and then draws it into the window.
        '''
        self.move()
        self.draw()

    def change_direction(self, direction):
        '''
        Changes direction of the snake according to a key pressed.
        '''
        if direction == 'up':
            self.direction = (0, 1)
        elif direction == 'down':
            self.direction = (0, -1)
        elif direction == 'left':
            self.direction = (-1, 0)
        elif direction == 'right':
            self.direction = (1, 0)

    def generate_food(self):
        '''
        Generates a position of food.
        '''
        while True:
            x = randrange(WIDTH)
            y = randrange(HEIGHT)
            if (x, y) not in self.snake_position and (x, y) not in self.food_position and (x, y) not in self.poisoned_food_position:
                self.food_position.append((x, y))
                break

    def create_food_sprites(self):
        '''Clears and then recreates food sprites. '''
        self.food_sprites.clear()
        for food_position in self.food_position:
            x, y = food_position
            self.food_sprites.append(pyglet.sprite.Sprite(apple_img, x=x*CELL_SIZE, y=y*CELL_SIZE, batch=self.batch))

    def generate_poisoned_food(self):
        while True:
            x = randrange(WIDTH)
            y = randrange(HEIGHT)
            if (x, y) not in self.snake_position and (x, y) not in self.food_position and (x, y) not in self.poisoned_food_position:
                self.poisoned_food_position.append((x, y))
                break


game = Game()


def on_key_press(symbol, modifiers):
    '''
    According to a pressed key calls a function that changes direction of
    the snake.
    '''
    if symbol == key.UP:
        game.change_direction('up')
    elif symbol == key.DOWN:
        game.change_direction('down')
    elif symbol == key.RIGHT:
        game.change_direction('right')
    elif symbol == key.LEFT:
        game.change_direction('left')
    elif symbol == key.ENTER:
        game.reset()


window = pyglet.window.Window(width=WIDTH*CELL_SIZE, height=HEIGHT*CELL_SIZE)
obrazek = pyglet.image.load('green.png')
had = pyglet.sprite.Sprite(obrazek)
window.push_handlers(
    on_draw=game.draw,
    on_key_press=on_key_press,
)
pyglet.app.run()
