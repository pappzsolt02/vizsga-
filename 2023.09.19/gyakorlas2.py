# Dobjunk 1 hagyományos dobókockával, és számoljuk meg hány 6-os volt 

from random import randint

n=int(input('Hányszor szeretne dobni a kockával?: '))
# ennél lessz job megoldásunk később
egyes_szam=0
kettes_szam=0
harom_szam=0
negy_szam=0
ot_szam=0
hatos_szam=0

for i in range(n):
    dobas=randint(1,6)
    print(dobas, end=' ')
    # if dobas==6:
    #     hatos_szam+=1
    # elif dobas==5:
    #     ot_szam+=1
    # elif dobas==4:
    #     negy_szam+=1
    # elif dobas==3:
    #     harom_szam+=1
    # elif dobas==2:
    #     kettes_szam+=1
    # else:
    #     egyes_szam+=1
    match dobas:
        case 1: egyes_szam+=1
        case 2: kettes_szam+=1
        case 3: harom_szam+=1
        case 4: negy_szam+=1
        case 5: ot_szam+=1
        case 6: hatos_szam+=1
        #case _: # akkor fut le, ha a fenti esetek egyik sem teljesül
print(f'\n\nEgyesek dobások száma:{egyes_szam}')
print(f'Kettesek dobások száma:{kettes_szam}')
print(f'Hármas dobások száma:{harom_szam}')
print(f'Négyes dobások száma:{negy_szam}')
print(f'Ötös dobások száma:{ot_szam}')
print(f'Hatosok dobások száma:{hatos_szam}')