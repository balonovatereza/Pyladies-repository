class Ctverec():
    def __init__(self, strana):
        self.strana = strana

    def obvod(self):
        return 4*self.strana

    def obsah(self):
        return self.strana ** 2

    def rozdil_obsahu(self, druhy_ctverec):
        return abs(self.obsah() - druhy_ctverec.obsah())


c1 = Ctverec(5)
c2 = Ctverec(10)
seznam_ctvercu = [c1, c2]

for cislo, ctverec in enumerate(seznam_ctvercu, 1):
    print("Strana ctverce {0}: {1} m.\n"
          "Obvod ctverce {0}: {2} m.\n"
          "Obsah ctverece {0}: {3} m2.\n".format(cislo,
                                                 ctverec.strana,
                                                 ctverec.obvod(),
                                                 ctverec.obsah(),
                                                 )
          )


print(c1.rozdil_obsahu(c2))
