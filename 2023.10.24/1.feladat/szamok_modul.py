from random import randint

szamok=[]

def feltolt(n:int,min:int,max:int) -> None:
    for i in range(n):
        szamok.append(randint(min,max))

def van_e_oszhato(oszto:int)->bool:
    for szam in szamok:
        if szam%oszto==0:
            return True
    return False

def atlag()->float:
    oszzeg=0
    for szam in szamok:
        oszzeg+=szam
    return oszzeg/len(szamok)   

def keres(mit:int)->int|bool:
    for i in range(len(szamok)):
        if mit==szamok[i]:
            return i 
    return False

def darab_ha_tobb(limit:int)->int:
    darab=0
    for szam in szamok:
        if szam>=limit:
            darab+=1
    return darab