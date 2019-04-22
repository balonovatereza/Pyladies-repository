class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return '<Kotatko jmenem {}>'.format(self.jmeno)

    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

mourek = Kotatko('Mourek')
print(mourek)
mourek.zamnoukej()
mourek.snez('ryba')
