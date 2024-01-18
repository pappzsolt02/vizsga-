#kérjuk be egy másofokú egyenlet együtthatóit (a,b,c)
#és írjuk ki a gyökeit (megoldásait): x1,x2

from math import sqrt

a=float(input('Adja meg az "a" elemét!: '))
b=float(input('Adja meg a "b" elemét!: '))
c=float(input('Adja meg a "c" elemét!: '))

d=b**2-4*a*c
if d>=0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print(f'x1={x1}')    
    print(f'x2={x2}')    
else:
    print('nincs megoldás a valós számok halmazán')