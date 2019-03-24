domaci = ['pes', 'kočka', 'králík', 'had', 'slepice', 'prase', 'nosorožec']
divoka = ['slepice', 'kráva', 'pavouk', 'pes', 'kůň', 'mravenec', 'želva']


def vrat_seznamy(seznam1, seznam2):
    '''
    Vrati tri seznamy zvirat:
    zvířata, která jsou v obou seznamech (sjednocení),
    zvířata, která jsou jen v prvním seznamu (rozdíl množin: první - druhá),
    zvířata, která jsou jen ve druhém seznamu (rozdíl množin: druhá - první).
    '''
    sjednocene = []
    for zvire in seznam2 and seznam1:
        if zvire not in sjednocene:
            sjednocene.append(zvire)
    rozdil1 = list(set(seznam1) - set(seznam2))
    rozdil2 = list(set(seznam2) - set(seznam1))
    return sjednocene, rozdil1, rozdil2


print(vrat_seznamy(domaci, divoka))
