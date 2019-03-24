def vyhodnot(pole):
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """
    if 'xxx' in pole.lower():
        return 'x'
    elif 'ooo' in pole.lower():
        return 'o'
    elif '-' not in pole.lower():
        return '!'
    else:
        return '-'


print(vyhodnot('------xxx-oo--------'))
