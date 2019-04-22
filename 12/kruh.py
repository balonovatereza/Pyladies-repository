from math import pi


class Kruh:
    def __init__(self, polomer):
        self.polomer = polomer

    def obvod(self):
        return 2 * pi * self.polomer

    def obsah(self):
        return pi * self.polomer ** 2


kolecko = Kruh(5)
print(kolecko.obvod())
print(kolecko.obsah())
