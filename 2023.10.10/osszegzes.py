# Mennyi egy megadott feltételt teljesitő számok összege, átlaga...)
from random import randint

# szamok=[randint(-100,100) for i in range(20)]

szamok=[]

for i in range(20):
    szamok.append(randint(-100,100))
print(szamok)

#Mennyi a pozítiv számok összege 

osszeg=0

for szam in szamok:
    if szam>0:
        osszeg+=szam
print(f'A pozítiv számok összege: {osszeg}')

#Mennyi a páros számok átlaga
osszeg=0
db=0

for szam in szamok:
    if szam%2==0:
        osszeg+=szam
        db+=1
print(f'A páros számok átlaga: {osszeg/db}.')

