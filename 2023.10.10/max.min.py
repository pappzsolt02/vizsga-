from random import randint
import math

szamok=[]

for i in range(20):
    szamok.append(randint(-100,100))
print(szamok)

#Melyik a legnagyobb szám?

legnagyobb=szamok[0]

for szam in szamok[1:]:
    if szam>legnagyobb:
        legnagyobb=szam
print(f'A legnagyobb szám: {legnagyobb}')

print(f'A legnagyobb szám a {max(szamok)}')
# Hányadik a legnagyobb szám?

legnagyobb_indexe=0

for i in range(1,len(szamok)):
    if szamok[i]>szamok[legnagyobb_indexe]:
        legnagyobb_indexe=i
print(f'A legnagyobb szám: {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe+1}')


# Hányadik a legnagyobb páratlan szám?

legnagyobb_indexe=len(szamok) # olyan elemet kell belerakni, amit biztosan felül fogunk írni
#szamok[legnagyobb_indexe] #list index out of range 
for i in range(len(szamok)):
    if szamok[i]%2==1:
        if legnagyobb_indexe==len(szamok) or szamok[i]>szamok[legnagyobb_indexe]:
            legnagyobb_indexe=i
if legnagyobb_indexe==len(szamok):
    print("Nincs páratlan szám a listában!")
else:
    print(f'A legnagyobb páratlan szám: {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe+1}')

#v2
legnagyobb_indexe=False # hamis 
legnagyobb_erteke=-math.inf # végtelen
for i in range(len(szamok)):
    if szamok[i]%2 and szamok[i]>legnagyobb_erteke:
        legnagyobb_erteke=szamok[i]
        legnagyobb_indexe=i
if legnagyobb_indexe!=False:
    print(f'A legnagyobb páratlan szám: {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe+1}')
else:
    print("Nincs páratlan szám a listában")