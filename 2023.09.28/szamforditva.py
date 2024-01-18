#Adott szám számjegyeinek fordított sorrendjének a meghatározása. (ez bármyilyen str fordított kiírására jó lesz!)

szam=input('Kérek egy számot!: ')

print(szam) #egyben írjuk ki a str
print(len(szam))

# for i in range(len(szam)):
#     print(szam[i],end='')

forditott=''
for i in range(len(szam)-1,-1,-1):
    print(szam[i],end='')
    forditott+=szam[i]
print(f'\n{forditott}')