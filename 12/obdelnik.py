class Obdelnik:
    def __init__(self, strana):
        self.strana = strana

    def obvod(self):
        return 4 * self.strana

    def obsah(self):
        return self.strana ** 2
