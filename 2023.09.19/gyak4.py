#Írjun programot, amely bekéri két pont koedinátáit
#majd kiszámolja azok távolságát
#P1(5,-3) - P1(x1,y1)
#P2(2,2) - P2(x2,y2)

from math import sqrt

p1x=int(input('Adja meg a P1 x koordinátálját: '))
p1y=int(input('Adja meg a P1 y koordinátálját: '))
p2x=int(input('Adja meg a p2 x koordinátálját: '))
p2y=int(input('Adja meg a p2 y koordinátálját: '))

d=sqrt((p2x-p1x)**2+(p2y-p1y)**2)
print(d)