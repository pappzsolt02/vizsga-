from random import randint

szamok=[]

def feltolt(n:int,min:int,max:int) -> None:
    for i in range(n):
        szamok.append(randint(min,max))

def legnagyobb_elem() ->int:
    legnagyobb=szamok[0]
    for szam in szamok[1:]:
        if legnagyobb<szam:
            legnagyobb=szam
    return legnagyobb

def keresett_szam(mit:int)->int|bool:
    for i in range(len(szamok)):
        if mit==szamok[i]:
            return i
    return False

def neg_atlag()->float:
    ossz=0
    negszam=0
    atlag=0
    for szam in szamok:
        if szam<0:
            negszam+=szam
            ossz+=1
    atlag=negszam/ossz
    return atlag