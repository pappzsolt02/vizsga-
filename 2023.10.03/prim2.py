# Egy pozitív egész számot prímszámnak nevezünk, ha a számnak csak 1 és
# önmaga az osztója. Az 1 definíció szerint nem prím. A legkisebb prímszám
# így a 2, hiszen csak 1-gyel és önmagával osztható.
# Írj programot, mely bekér egy pozitív egész számot, majd megállapítja,
# hogy az prímszám-e vagy sem! 

# A program várt működése pl. a következő:
# Írj be egy pozitív egész számot: 6
# Nem prím.
# Írj be egy pozitív egész számot: 13
# Prím.
from math import sqrt

szam=int(input("Írj be egy pozitív egész számot: "))

for i in range(2,int(sqrt(szam))+1):
    if szam%i==0:
       print("nem prím!")
       break 
else:
    print("Prím")