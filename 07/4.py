domaci = ['pes', 'kočka', 'králík', 'had', 'slepice', 'prase', 'nosorožec']
divoka = ['slepice', 'kráva', 'pavouk', 'pes', 'kůň', 'mravenec', 'želva']


def vrat_seznamy(seznam1, seznam2):
    sjednocene = seznam1 + seznam2
    rozdil1 = list(set(seznam1) - set(seznam2))
    rozdil2 = list(set(seznam2) - set(seznam1))
    return sjednocene, rozdil1, rozdil2


print(vrat_seznamy(domaci, divoka))
