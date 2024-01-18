#Készítsünk programot? amely beolvassa egy diák igazolatlan hiányzásainak számát.
#készítsünk kategóriákat a hiányzások szám aalapján
#1-5 ofői figyelmeztetés
#6-10ofői intő
#11-35 iggazgatói megrovás
#35 fölött, kérjük be a tanuló születési évét 
#ha elmút 16, akkor kirúgás  
#egyébként családi pótlék megvonás.


akt_ev=2023

#be kell kérni a hiányzások számát 

hianyzas=int(input('Adja meg hogy hány nap igazolatlan  hiábnyzása van!: '))

if hianyzas==0:
    print('úgyes vagy')
elif hianyzas<=5:
    print('ofői figyelmeztetés')
elif hianyzas<=10:
    print('ofői intő')
elif hianyzas<=35:
    print('igazgatói megrovás')
elif hianyzas>35:
    eltkor=int(input('Adja meg a születési évet!: '))
    kirugasi_ev=akt_ev-eltkor
    if kirugasi_ev<=16:
        print('családi pótlék megvonás!')
    else:
        print('ki van rúgva az iskolából')