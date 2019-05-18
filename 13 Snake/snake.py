
import pyglet
from pyglet.window import key
from pyglet import gl
from random import randrange
from image_load import apple_img, snake_tiles, poisoned_apple_img
from field import field


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
        self.poisoned_food_position = [(4, 8)]
        self.poisoned_food_sprites = []
        self.info_text = None
        self.gameover_text = None
        self.gameover = False
        self.food_eaten = False
        self.lifes = 3
        self.stopped = False
        self.interval = 1/2
        self.keys_pressed = []
        pyglet.clock.schedule_interval(self.move, self.interval)

    def move(self, t):
        '''
        One-step movement of snake in set direction. Solves also situations:
        - snake eats itself
        - snake hits the wall
        - snake eats poisoned food
        - snake eats food.
        '''
        self.determine_direction()
        x, y = self.snake_position[-1]  # head position
        move_x, move_y = self.direction  # one step in set direction
        new_step = (x + move_x, y + move_y)

        # Snake eats itself
        if new_step in self.snake_position:
            self.handle_gameover()
            return

        # Snake hits the wall
        elif (x + move_x) > (field.width - 1) or (x + move_x) < 0 or \
             (y + move_y) > (field.height - 1) or (y + move_y) < 0:
            self.handle_gameover()
            return

        # Snake moves
        if new_step not in self.food_position and \
           new_step not in self.poisoned_food_position:
            del self.snake_position[0]

        # Snake eats poisoned food
        elif new_step in self.poisoned_food_position:
            if len(self.snake_position) > 3:
                del self.snake_position[0:3]
            else:
                self.handle_gameover()
                return
            del self.poisoned_food_position[0]
            self.poisoned_food_position.append(self.generate_food(new_step))
            self.food_eaten = True

        # Snake eats food
        else:
            del self.food_position[0]
            self.food_position.append(self.generate_food(new_step))
            self.food_eaten = True

        self.snake_position.append(new_step)

    def handle_gameover(self):
        pyglet.clock.unschedule(game.move)
        self.lifes -= 1
        self.stopped = True
        if self.lifes == 0:
            self.gameover = True

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
        # draw red apple
        self.create_food_sprites(self.food_sprites, self.food_position, apple_img)
        # draw golden apple
        self.create_food_sprites(self.poisoned_food_sprites, self.poisoned_food_position, poisoned_apple_img)

        # Draw line above snake field
        self.draw_rectangle([(field.window_size()[0]+1, field.window_size()[1]+1), (1, field.window_size()[1]+1)])
        self.batch.draw()

        self.draw_text('Snake lifes: {}'.format(self.lifes),
                       field.window_size()[0] - 5,
                       field.window_size()[1] + 5,
                       'right')
        self.draw_text('Snake length: {}'.format(str(len(self.snake_position))),
                       5,
                       field.window_size()[1] + 5,
                       'left')

        if self.stopped and not self.gameover:
            self.draw_text('Set right direction to continue',
                           int((field.window_size()[0])/2),
                           int(field.window_size()[1]/2),
                           'center')

        if self.gameover:
            self.draw_text('GAME OVER',
                           int((field.window_size()[0])/2),
                           int(field.window_size()[1]/2),
                           'center')
            self.draw_text('Press ENTER to restart',
                           int(field.window_size()[0]/2),
                           int(field.window_size()[1]/2 - 40),
                           'center')

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

        for snake_part in range(len(self.snake_position)):

            # Tail of the snake
            if snake_part == 0:
                x_to_dir = self.snake_position[snake_part][0] - self.snake_position[snake_part + 1][0]
                y_to_dir = self.snake_position[snake_part][1] - self.snake_position[snake_part + 1][1]
                img_name = 'tail-' + self.sprite_direction(x_to_dir, y_to_dir)

            # Body of the snake
            if snake_part > 0 and snake_part < (len(self.snake_position) - 1):
                x_to_dir = self.snake_position[snake_part][0] - self.snake_position[snake_part + 1][0]
                y_to_dir = self.snake_position[snake_part][1] - self.snake_position[snake_part + 1][1]
                x_from_dir = self.snake_position[snake_part][0] - self.snake_position[snake_part - 1][0]
                y_from_dir = self.snake_position[snake_part][1] - self.snake_position[snake_part - 1][1]
                img_name = self.sprite_direction(x_to_dir, y_to_dir) + '-' + self.sprite_direction(x_from_dir, y_from_dir)

            # Head of the snake
            if snake_part == len(self.snake_position) - 1:
                x_from_dir = self.snake_position[snake_part][0] - self.snake_position[snake_part - 1][0]
                y_from_dir = self.snake_position[snake_part][1] - self.snake_position[snake_part - 1][1]
                if self.gameover:
                    img_name = self.sprite_direction(x_from_dir, y_from_dir) + '-dead'
                elif self.food_eaten:
                    img_name = self.sprite_direction(x_from_dir, y_from_dir) + '-tongue'
                    self.food_eaten = False
                else:
                    img_name = self.sprite_direction(x_from_dir, y_from_dir) + '-head'
            x = self.snake_position[snake_part][0]
            y = self.snake_position[snake_part][1]
            self.snake_sprites.append(pyglet.sprite.Sprite(snake_tiles[img_name], x=x*field.cell_size, y=y*field.cell_size, batch=self.batch))

    def change_direction(self, direction):
        ''' Changes direction of the snake according to a key pressed. '''
        if direction == 'up':
            self.direction = (0, 1)
        elif direction == 'down':
            self.direction = (0, -1)
        elif direction == 'left':
            self.direction = (-1, 0)
        elif direction == 'right':
            self.direction = (1, 0)

    def generate_food(self, new_step):
        '''Generates a position of food. '''
        while True:
            x = randrange(field.width)
            y = randrange(field.height)
            if (x, y) not in self.snake_position and \
                (x, y) not in self.food_position and \
                (x, y) not in self.poisoned_food_position and \
                (x, y) != new_step:
                return x, y

    def create_food_sprites(self, sprite_list, food_list, image):
        '''Clears and then recreates food sprites. '''
        sprite_list.clear()
        for food_position in food_list:
            x, y = food_position
            sprite_list.append(pyglet.sprite.Sprite(image, x=x*field.cell_size, y=y*field.cell_size, batch=self.batch))

    def draw_text(self, text, x, y, anchor_x):
        ''' Draws text in the window. '''
        text = pyglet.text.Label(
            text,
            font_name='Arial',
            font_size=30,
            x=x, y=y, anchor_x=anchor_x)
        text.draw()

    def draw_rectangle(self, vertexes):
        '''Draws rectangle around game field. '''
        gl.glLineWidth(2)
        gl.glClearColor(0, 0, 0, 1)
        gl.glColor3f(1, 1, 1)
        gl.glBegin(gl.GL_LINE_LOOP)
        for point in vertexes:
            gl.glVertex2f(point[0], point[1])
        gl.glEnd()

    def determine_direction(self):
        '''According to a key pressed changes direction of the snake. '''
        if len(self.keys_pressed) == 0:
            return
        symbol = self.keys_pressed[0]
        if symbol == key.UP:
            self.change_direction('up')
        elif symbol == key.DOWN:
            self.change_direction('down')
        elif symbol == key.RIGHT:
            self.change_direction('right')
        elif symbol == key.LEFT:
            self.change_direction('left')
        del self.keys_pressed[0]


game = Game()


def on_key_press(symbol, modifiers):
    '''
    Resets a game if pressed enter.
    Solves also situation when user presses more keys at once.
    '''
    if game.stopped and not game.gameover:
        game.keys_pressed.clear()
        game.stopped = False
        game.interval /= 2
        pyglet.clock.schedule_interval(game.move, game.interval)
    if symbol == key.ENTER:
        game.reset()
    else:
        game.keys_pressed.append(symbol)


window = pyglet.window.Window(width=field.window_size()[0], height=field.window_size()[1] + 36)  # 6 pixels space between text and game field, 30 pixels font size
window.push_handlers(
    on_draw=game.draw,
    on_key_press=on_key_press,
)
pyglet.app.run()
