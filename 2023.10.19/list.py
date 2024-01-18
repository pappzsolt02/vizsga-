from random import randint

szamok=[]

def feltolt(n: int,min:int, max:int) -> None:
    for i in range(n):
        szamok.append(randint(min,max))
def osszegzes() ->int:
    osszeg=0
    for szam in szamok:
        osszeg+=szam
    return osszeg