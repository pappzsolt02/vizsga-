szam=float(input('Kérem adjon meg egy számot:'))

if szam >= 0:
    print(f'A szám abszolút értéke:{szam}')
else:
    #print(f'A szám abszolút értéke:{szam*-1}')
    print(f'A szám abszolút értéke:{-szam}')
    print('Ez még benne ')
print('Ez már nincs benne')
