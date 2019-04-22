class Kotatko():
    def __init__(self, jmeno):  # self musi byt vzdycky, zbytek ne
        self.jmeno = jmeno

    def zamnoukej(self):  # tady uz to neni funkce, ale je to metoda, da se volat na konkretnim objektu, volani je odlisne
        print('{}: Mnau!'.format(self.jmeno))

    def snez(self, jidlo):
        print('{}: Mnaou! {} mi chutna!'.format(self.jmeno, jidlo))


# Vytvoření konkrétního objektu
kotatko = Kotatko()
kotatko.jmeno = 'Cici'
# Volání metody na konkretnim objektu
kotatko.zamnoukej()
kotatko.snez('pizza')

mourek = Kotatko()
mourek.jmeno = 'Mourek'  # pridani atributu .jmeno (atribut = vlastnost)
mourek.zamnoukej()
mourek.snez('ryba')

micka = Kotatko()
micka.jmeno = 'Micka'
# micka.zamnoukej = 12345  # v tuto chvili prepiseme to, co tam bylo (Mnaou), a je tam cislo, cislo se neda zavolat
micka.zamnoukej()
micka.snez('mliko')

print(mourek.jmeno)
print(micka.jmeno)
