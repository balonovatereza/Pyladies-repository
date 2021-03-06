domaci_zvirata = ['pes', 'kočka', 'králík', 'had']


def vrat_kratka_zvirata(seznam):
    '''
    Vrati jmena domacich zvirat kratsi nez 5 pismen.
    '''
    kratka_zvirata = []
    for zvire in seznam:
        if len(zvire) < 5:
            kratka_zvirata.append(zvire)
    return kratka_zvirata


print(vrat_kratka_zvirata(domaci_zvirata))


def vrat_zvirata_k(seznam):
    '''
    Vrati jmena domacich zvirat zacinajicich na k.
    '''
    zvirata = []
    for zvire in seznam:
        if zvire[0] == 'k':
            zvirata.append(zvire)
    return zvirata


print(vrat_zvirata_k(domaci_zvirata))


def potvrd_pritomnost_v_seznamu(seznam):
    '''
    Vrati true pokud zadane zvire najde v seznamu zvirat.
    '''
    slovo = input('Zadej zvire k provereni pritomnosti v seznamu: ')
    return slovo in seznam


print(potvrd_pritomnost_v_seznamu(domaci_zvirata))


def serad(seznam):
    '''
    Vrati seznam zvirat serazenych podle abecedy.
    '''
    seznam.sort()
    return seznam


print(serad(domaci_zvirata))


def serad2(seznam):
    '''
    Vrati seznam zvirat serazenych podle abecedy.
    '''
    return sorted(seznam)


print(serad2(domaci_zvirata))

domaci_zvirata2 = ['pes', 'kočka', 'králík', 'had', 'andulka']


domaci = ['pes', 'kočka', 'králík', 'had', 'slepice', 'prase', 'nosorožec']
divoka = ['slepice', 'kráva', 'pavouk', 'pes', 'kůň', 'mravenec', 'želva']


def vrat_seznamy(seznam1, seznam2):
    '''
    Vrati tri seznamy zvirat:
    zvířata, která jsou v obou seznamech (sjednocení),
    zvířata, která jsou jen v prvním seznamu (rozdíl množin: první - druhá),
    zvířata, která jsou jen ve druhém seznamu (rozdíl množin: druhá - první).
    '''
    sjednocene = seznam1 + seznam2
    rozdil1 = list(set(seznam1) - set(seznam2))
    rozdil2 = list(set(seznam2) - set(seznam1))
    return sjednocene, rozdil1, rozdil2


print(vrat_seznamy(domaci, divoka))


def serad_podle_2_pismena(seznam):
    '''
    Vytvori seznam dvojic (klíč = druhe pismeno, hodnota=zvire), seradi ho podle klice (druhe
    pismeno hodnoty) a vrati takto serazeny seznam zvirat.

    '''
    seznam_dvojic = []
    serazeny_seznam = []
    for zvire in seznam:
        seznam_dvojic.append((zvire[1:], zvire))
    seznam_dvojic.sort()
    for klic, zvire in seznam_dvojic:
        serazeny_seznam.append(zvire)
    return serazeny_seznam


print(serad_podle_2_pismena(domaci_zvirata2))
