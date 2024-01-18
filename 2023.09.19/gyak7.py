#Készítsen programot, amely mezőgazdasági jóslást végez!
#Kérje be az elvetett búza mennyiségét tonnában!
#Ez alapján számolja ki egy véletlenszerűen generált szorzóval (5-15) a hozamot és írja ki a mennyiséget!
#A szorzó alapján hazározza meg és írja ki, hogy milyen volt az adott év:
#5-8 -->átlag alatti
#9-12 -->átlagos
#13-15 --> átlag feletti

from random import randint
takarmany=int(input('Adja meg a betakaritot takarmány mennyiségét tonnában!: '))
szorzo=randint(5,15)
print(f'várható mennyiség: {takarmany*szorzo}')

if szorzo<=8:
     print('átlag alatti')
elif szorzo<=12:
     print('átlag')
else:
     print('átlag feletti')
    