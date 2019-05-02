snake_position = [(0, 0), (1, 0), (2, 0)]


def direction(x, y):
    '''Sets a direction according to an input  '''
    if (x, y) == (-1, 0):
        return 'right'
    if (x, y) == (1, 0):
        return 'left'
    if (x, y) == (0, 1):
        return 'bottom'
    if (x, y) == (0, -1):
        return 'top'


for i in range(len(snake_position)):

    # Tail of the snake
    if i == 0:
        x_to_dir = snake_position[i][0] - snake_position[i + 1][0]
        y_to_dir = snake_position[i][1] - snake_position[i + 1][1]
        img_name = 'tail-' + direction(x_to_dir, y_to_dir)

    # Body of the snake
    if i > 0 and i < (len(snake_position) - 1):
        x_to_dir = snake_position[i][0] - snake_position[i + 1][0]
        y_to_dir = snake_position[i][1] - snake_position[i + 1][1]
        x_from_dir = snake_position[i - 1][0] - snake_position[i][0]
        y_from_dir = snake_position[i - 1][1] - snake_position[i][1]
        img_name = direction(x_to_dir, y_to_dir) + '-' + direction(x_from_dir, y_from_dir)

    # Head of the snake
    if i == len(snake_position) - 1:
        x_from_dir = snake_position[i - 1][0] - snake_position[i][0]
        y_from_dir = snake_position[i - 1][1] - snake_position[i][1]
        img_name = direction(x_from_dir, y_from_dir) + '-head'
