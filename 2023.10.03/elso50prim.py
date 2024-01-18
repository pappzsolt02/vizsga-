#írjuk ki az első 50db prímszámot!
from math import sqrt
db=0
szam=2

while db<50:
    for i in range(2,int(sqrt(szam))+1):
        if szam%i==0:
            break
    else:
        print(szam, end=" ")
        db+=1
    szam+=1