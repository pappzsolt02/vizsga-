# Készítsünk programot, amely ki fogja kérdezni a matematikát 
# (két szám összeadását, kivonását és szorzását az <1,10> intervallumból).
# A két számot és a műveletet a számítógép véletlenszerűen válassza ki.
# A program akkor fejeződjön be, ha a felhasználó 5 példát kiszámolt helyesen. 
# Rossz válasz esetén kérdezze újra ugyanazt a példát.
# A program végén írjuk ki az eredményességet százalékokban.

from random import randint

kerdesek_szama=5 #csak itt kell átírni, ha többet/kevesebbet szeretnénk

rossz_valaszok_szama=0
for i in range(kerdesek_szama):
    szam1=randint(1,10)
    szam2=randint(1,10)
    muvelet=randint(0,2) # 0='+'  1='-'  2='*'
    helyes_valasz=False  #kezdőértéka while ciklushoz
    
    while helyes_valasz==False:
        match muvelet:
            case 0: # '+'
                valasz=int(input(f'{szam1} + {szam2} = '))
                if szam1+szam2==valasz:
                    print('Jó válasz!')
                    helyes_valasz=True
                else:
                    print('Rossz válasz!')
                    rossz_valaszok_szama+=1
            case 1: # '-'
                valasz=int(input(f'{szam1} - {szam2} = '))
                if szam1-szam2==valasz:
                    print('Jó válasz!')
                    helyes_valasz=True
                else:
                    print('Rossz válasz!')
                    rossz_valaszok_szama+=1
            case 2: # '*'
                valasz=int(input(f'{szam1} * {szam2} = '))
                if szam1*szam2==valasz:
                    print('Jó válasz!')
                    helyes_valasz=True
                else:
                    print('Rossz válasz!')
                    rossz_valaszok_szama+=1
print(f'Eredményesség: {kerdesek_szama/(kerdesek_szama+rossz_valaszok_szama)*100:.2f}%')                   

#KÉSŐBB függvény használata, mert kb. ugyanazt csináltuk 3-szor (3 műveletnél)


