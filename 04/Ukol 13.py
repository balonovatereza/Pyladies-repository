# Ukol 13

print('Ukol 13')

sirka_ctverce = int(input('Zadej sirku ctverce: '))

for osa_X in range(sirka_ctverce):
    for osa_Y in range(sirka_ctverce):
        znak = ' '
        konec = ' '
        if osa_X == 0 or osa_X == (sirka_ctverce - 1) or osa_Y == 0 or \
                osa_Y == (sirka_ctverce - 1):
            znak = 'X'
        if osa_Y == (sirka_ctverce - 1):
            konec = '\n'
        print(znak, end=konec)
