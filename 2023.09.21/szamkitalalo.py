#Generáljunk egy és 100 közé eső számot!
# A játékos feladata az, hogy kitalálja.
#segítség: a tipp kisebb vagy nagyobb a keresett számnál

import random

titkos_szam=random.randint(1,100)
#print(titkos_szam)

tipp=-214
tippek_szama=0
while tipp!=titkos_szam:
    tipp_txt=input('Tipp(1-100): ') 
    tippek_szama+=1
    if tipp_txt.isnumeric():
        tipp=int(tipp_txt)
        if tipp>titkos_szam:
            print('Kisebb!')
        elif tipp<titkos_szam:
            print('Nagyobb!')

print(f'Talál, {tippek_szama} tippre volt szükésg.')