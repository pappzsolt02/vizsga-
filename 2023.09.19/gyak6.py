# Dobjunk fel egy pénzérmét 100-szor, és mondjuk meg, hogy fej vagy írás volt többször!

#0-fej
#1-írás

from random import randint
fej=0
iras=0
for i in range(100):
    dob=randint(0,1)
    # print(dob)
    if dob==0:
        fej+=1
    else:
        iras+=1
print(f'fej={fej}')
print(f'írás={iras}')
