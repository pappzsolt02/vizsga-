from random import randint

szamok=[]

def feltolt(n:int,min:int,max:int) -> None:
    for i in range(n):
        szamok.append(randint(min,max))

def legnagyobb_elem(szamok:list) ->int:
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

def negativ_atlag()