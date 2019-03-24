zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']


def vyber_chybne(zaznamy):
    chybne = []
    for zaznam in zaznamy:
        jmeno_prijmeni = zaznam.split()
        jmeno = jmeno_prijmeni[0]
        prijmeni = jmeno_prijmeni[1]
        if jmeno.islower() or prijmeni.islower():
            chybne.append(zaznam)
    return chybne


chybne_zaznamy = vyber_chybne(zaznamy)
print(chybne_zaznamy)  # → ['pepa novák', 'Ivo navrátil', 'jan Poledník']


def vyber_spravne(zaznamy):
    spravne = []
    for zaznam in zaznamy:
        jmeno_prijmeni = zaznam.split()
        jmeno = jmeno_prijmeni[0]
        prijmeni = jmeno_prijmeni[1]
        if not jmeno.islower() and not prijmeni.islower():
            spravne.append(zaznam)
    return spravne


spravne_zaznamy = vyber_spravne(zaznamy)
print(spravne_zaznamy)  # → ['Jiří Sládek']


def oprav_zaznamy(zaznamy):
    opravene = []
    for zaznam in zaznamy:
        jmeno_prijmeni = zaznam.split()
        jmeno = jmeno_prijmeni[0]
        prijmeni = jmeno_prijmeni[1]
        opravene.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())
    return opravene


opravene_zaznamy = oprav_zaznamy(zaznamy)
print(opravene_zaznamy)  # → ['Pepa Novák', 'Jiří Sládek', 'Ivo Navrátil', 'Jan Poledník']
