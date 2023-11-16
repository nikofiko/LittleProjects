import random

wybory = ['papier', 'kamien', 'nozyce']

print('Witamy w grze w papier kamien nozyce!')
wygrane = 0
ilosc_gier = 0

while True:
    komputer = random.choice(wybory)
    czlowiek = input('Wybierz papier/kamien/nozyce a jezeli chcesz zakonczyc gre napisz \"q\"')

    if czlowiek == 'q':
        print('Wygrales ', wygrane, 'z', ilosc_gier, 'gier')
        break
    
    ilosc_gier += 1

    print('Komputer wybral: ', komputer)

    if czlowiek == 'kamien' and komputer == 'nozyce':
        print('Wygrales!')
        wygrane += 1
    elif czlowiek == 'papier' and komputer == 'kamien':
        print('Wygrales!')
        wygrane += 1
    elif czlowiek == 'nozyce' and komputer == 'papier':
        print('Wygrales!')
        wygrane += 1

    