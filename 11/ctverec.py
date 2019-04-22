class Ctverec:
    def __init__(self, strana):
        self.strana = strana

    def obvod(self):
        return 4 * self.strana

    def obsah(self):
        return self.strana ** 2

    def rozdil_obsahu(self, jiny_ctverec):
        return self.obsah() - druhy_ctverec.obsah()


prvni_ctverec = Ctverec(2)
druhy_ctverec = Ctverec(4)

print(prvni_ctverec.obvod())
print(prvni_ctverec.obsah())
print(prvni_ctverec.rozdil_obsahu(druhy_ctverec))
