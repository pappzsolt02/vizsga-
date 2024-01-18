#Kérjünk be egy kúp alpajának sugarát és magasságát
#Írjuk ki a kúp felszínét és térfogatát
from math import sqrt, pow, pi
#sqrt - négyzetgyök
#pow - hatányozás

r=float(input("Adja meg a kúp alapjának sugatárt!: "))
m=float(input("Adja meg a kúp magaságát!: "))

#a=sqrt(r**2+m**2)
a=sqrt(pow(r,2)+pow(m,2)) # pow(mit, hányadik hatványra)

A=round(r**2*pi+pi*r*a,2) # teljes felszín (alap+palást)

print(f'A kúp felszíne: {A}')

V=pi*r**2*m/3
#V=(pi*r**2*m)/3

print(f'A kúp térfogata: {V:.2f}')