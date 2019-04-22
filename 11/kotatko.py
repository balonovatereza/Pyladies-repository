class Kotatko:
    # init se vola automaticky pokazde kdyz vznika trida
    def __init__(self, jmeno):  # self musi byt vzdycky, zbytek ne
        self.jmeno = jmeno

    def __str__(self):
        return '<Kotatko jmenem {}>'.format(self.jmeno)

    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

# nize je zkratka techto dvou radku kodu:
# mourek = Kotatko()
# mourek.jmeno = 'Mourek'
mourek = Kotatko('Mourek')  # co jsme dali jako atributy metody init, tady musime pridat
mourek.zamnoukej()
