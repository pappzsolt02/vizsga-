#Írjuk ki a prímszámol egy tartományon!
#Kérjük be a taromány határait.
#Figyeljünk arra, hogy a kezdete pozitív szám legyen(>1). #Figyljünk arra,hogy a vége nagyobb legyen, mint a kezdete.
from math import sqrt
kezdete=-1
while kezdete<2:
    kezdete=int(input("kezdete: "))
    
vege=-1
while vege<=kezdete:
    vege=int(input("vége: "))

for szam in range(kezdete,vege+1):
    for i in range(2,int(sqrt(szam))+1):
        if szam%i==0:
            break
    else:
        print(szam, end=" ")
    