# Generáljunk egy listába elemeket!
# A generáló függvény kapjon 3 paramétert (min,max, db)

# Írjuk ki a lista elemeit egymás mellé, vesszővel elválasztva (utolsó után ne legyen vessző)

# Határozzuk meg a lista legnagyobb elemét

# Kérjünk be egy értéket, és mondjuk meg, hogy benne van-e a listában. 
# Ehhez készítsünk függvényt, amely ha benne van, akkor adja vissza az # indexét, ha nincs benne, # akkor pedig False-t. A főprogram pedig ettől függően írja ki a az indexet vagy azt,
# hogy 'A keresett elem nincs benne a listában.'

# Írjuk ki a listában szereplő negatív elemek átlagát. Ehhez készítsünk 'negativ_atlag' néven függvényt.

from fugvenyek import *

feltolt(20,-100,100)

for i in range(len(szamok)):
    print(szamok[i],end=" ")
    if i <len(szamok)-1:
        print(" , ",end="")

print(f"\nA legnagyobb elemem a lsitában a {legnagyobb_elem(szamok)}")

keresett=int(input("Keresett szám: "))
keresett_eredmeny=keresett_szam(keresett)
if keresett_eredmeny==False:
    print("A keresett elem nincs benne a listában.")
else:
    print(f"A keresett szám {keresett} és a helye  {keresett_eredmeny+1}")