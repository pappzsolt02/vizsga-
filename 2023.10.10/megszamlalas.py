from random import randint

szamok=[]

for i in range(randint(10,40)):
    szamok.append(randint(-100,100))

print(szamok)

print(f'{len(szamok)} darab szám került legenerálásra.')

#Hány páros szám van a listában
db=0
for szam in szamok:
    if szam%2==0:
        db+=1
print(f'{db} páros szám van a listában.')

#Hány negatív szám van a listában
db=0
for szam in szamok:
    if szam<0:
        db+=1
print(f'{db} negatív szám van a listában.')
