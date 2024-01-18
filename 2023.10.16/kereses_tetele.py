from random import randint
szamok=[]
for i in range(100):
    szamok.append(randint(-100,100))
print(szamok)

kertszam=int(input("Keresett szám: "))

#v1 
index=0
while index<len(szamok) and szamok[index]!=kertszam:
    index+=1
if index==len(szamok):
    print("A keresett szám nincs benne a listában")
else:
    print(f'A keresett szám a {index+1}. a listában')