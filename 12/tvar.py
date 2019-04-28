from math import pi
from itertools import combinations


class Tvar:
    def obvod(self):  # nadefinovano pro pripad napr. primky
        return

    def obsah(self):  # nadefinovano pro pripad napr. primky
        return

    def rozdil_obsahu(self, jiny_tvar):
        return abs(self.obsah() - jiny_tvar.obsah())


class Primka(Tvar):
    def __init__(self, delka):
        self.delka = delka


class Ctverec(Tvar):
    def __init__(self, strana):
        self.strana = strana

    def obvod(self):
        return 4 * self.strana

    def obsah(self):
        return self.strana ** 2


class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer

    def obvod(self):
        return 2 * pi * self.polomer

    def obsah(self):
        return pi * self.polomer ** 2


class Obdelnik(Tvar):
    def __init__(self, strana_a, strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b

    def obvod(self):
        return 2 * self.strana_a + 2 * self.strana_b

    def obsah(self):
        return self.strana_a * self.strana_b


p1 = Primka(4)
print('Obvod primky je:', p1.obvod())

seznam_tvaru = [Ctverec(2), Ctverec(4), Kruh(2), Kruh(4), Obdelnik(2, 4), Obdelnik(4, 6)]
seznam_kombinaci = list(combinations(seznam_tvaru, 2))

# for tvar in seznam_tvaru:
#    for tvar_odcitany in seznam_tvaru:
#        print(tvar.rozdil_obsahu(tvar_odcitany))

for cislo, kombinace_tvaru in enumerate(seznam_kombinaci, 1):
    print('Rozdil obsahu {}. kombinace'.format(cislo))
    print(kombinace_tvaru[0].rozdil_obsahu(kombinace_tvaru[1]))
