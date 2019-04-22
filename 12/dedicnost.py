class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def udelej_zvuk(self):
        print("{}: Mňau!".format(self.jmeno))

    def snez(self, jidlo):
        print("({} na {} chvíli fascinovaně kouká)".format(self.jmeno, jidlo))
        super().snez(jidlo)


class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print("{}: Haf!".format(self.jmeno))


class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)


standa = Hadatko('Stanislav')
standa.snez('myš')
micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.udelej_zvuk()
azorek.udelej_zvuk()
micka.snez('myš')
micka.snez('granule')
azorek.snez('kost')

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.snez('flákota')
    zviratko.udelej_zvuk()
