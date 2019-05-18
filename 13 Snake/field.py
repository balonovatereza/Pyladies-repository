# Class creating a field


class Field():
    def __init__(self):
        self.cell_size = 64  # pixels
        self.width = 10  # no. of columns
        self.height = 10  # no. of rows

    def window_size(self):
        width = self.width * self.cell_size
        height = self.height * self.cell_size
        return (width, height)


field = Field()
