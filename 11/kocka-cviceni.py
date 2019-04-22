class Kocka:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pocet_zivotu = 9

    def zamnoukej(self):
        print('{}: Mniau'.format(self.jmeno))

    def je_ziva(self):
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if not self.je_ziva():
            print('{} uz je mrtva'.format(self.jmeno))
        else:
            self.pocet_zivotu -= 1
            print('{} ma {} zivotu'.format(self.jmeno, self. pocet_zivotu))

    def snez(self, jidlo):
        if not self.je_ziva():
            print('Je mrtva, neni mozne krmit.')
        if jidlo == 'ryba' and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print('{} ma {} zivotu.'.format(self.jmeno, self.pocet_zivotu))
        else:
            print('Kocka se krmi.')


cici = Kocka('Cici')
cici.zamnoukej()
cici.je_ziva()
cici.uber_zivot()
cici.snez('mouka')
cici.uber_zivot()
cici.snez('ryba')
for i in range(8):
    cici.uber_zivot()
cici.snez('mouka')
