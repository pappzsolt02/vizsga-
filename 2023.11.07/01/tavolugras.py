#12 versenyző
#Minden versenyző 6-ot ugrik
#Szimuláljuk le a versenyt
# UGrások 7 és 8.50 között legyenek, 30% esély, gogy érvénytelen  

#1. versenyző ugrásai: 7.80 8.10 érvénytelen 7.56 érvénytelen 8.34 
#1. versenyző legjobb ugrása: 8.34 

from random import randint

def ugrasok_generalasa()->list:
    ugarsok=[]
    for i in range(6):
        egy_ugras=randint(700,850)/100
        if randint(1,10)<=3:
            egy_ugras=0
        ugarsok.append(egy_ugras)
    return ugarsok

def print_egy_versenyzo(rajtszam:int,ugrasok:list,)-> None:
    print(f"{rajtszam}. versenyző ugrásai:",end=" ")
    for ugras in ugrasok:
        if ugras==0:
            print("érvénytelen",end=" ")
        else:
            print(ugras, end=" ")
    print(f"\n{rajtszam}. versenyző legjobb ugrása: {versenyzo_legjobb_ugrasa(ugrasok)} ") #legjobb ugrás 

def versenyzo_legjobb_ugrasa(ugrasok:list)->float:
    legjobb=ugrasok[0]
    for ugras in ugrasok[1:]:
        if ugras>legjobb:
            legjobb=ugras
    return legjobb

def gyoztes(eredmenyek:list)->int:
    """
    Megkeresei és visszaadja a győztes versenyző rajtszámát.
    """
    legjobb=0
    for i in range(len(eredmenyek)):
        if eredmenyek[i]>eredmenyek[legjobb]:
            legjobb=i
        return legjobb+1

def ervenytelen_ugrasok_szama(ugrasok:list)->int:
    darab=0
    for ugras in ugrasok:
        if ugras==0:
            darab+=1
    return darab