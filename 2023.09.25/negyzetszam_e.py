# Készítsünk programot, amely bekér egy számot, 
# majd meghatározza, hogy az a szám négyzetszám-e!

from math import sqrt

szam=int(input('Kérek egy számot: '))
gyok=sqrt(szam)  # a szám négyzetgyöke

if gyok==round(gyok):  # a kerekített == az eredetivel --> CSAK ha egész
    print('Négyzetszám!')
else:
    print('NEM négyzetszám!')
