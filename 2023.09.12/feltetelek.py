ma_ev=2023
ma_honap=9
ma_nap=12

szul_ev=int(input('Adja meg a születési évét: '))

if ma_ev-szul_ev<18:
    print('Még nem 18 éves. Nem vehet alkoholt!')
elif ma_ev-szul_ev>18:
    print('Vehet már alkoholt')
else:
    szul_honap=int(input('Adja meg a születési honapját:'))
    if ma_honap<szul_honap:
        print('Még nem 18 éves. Nem vehet alkoholt!')
    elif ma_honap>szul_honap:
        print('Vehet már alkoholt')
    else:
        szul_nap=int(input('Adja meg a születési napját:'))
        if ma_nap<szul_nap:
            print('Még nem 18 éves. Nem vehet alkoholt!')
        elif ma_nap>szul_nap:
            print('Vehet már alkoholt')
        else:
            print('Boldog születésnapot! Igyon egy pezsgőt')