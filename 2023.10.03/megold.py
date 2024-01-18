from random import randint
a=int(input("a= "))
b=int(input("b= "))
db=0
for i in range(10):
    szam=randint(a,b)
    print(szam,end=' ')
    if szam%3==0:
        db+=1
print(f'\n{db} db 3-mal oszahtó szám van a generáltak között.')

legidosebb=''
legidosebb_kora=0

for i in range(3):
    kor=0
    nev=input("Név: ")
    while kor<18 or kor>99:
        kor=int(input("Kor: "))     
    if kor>legidosebb_kora:
        legidosebb_kora=kor
        legidosebb=nev
print(f'{legidosebb} a legidősebb ({legidosebb_kora} éves)')