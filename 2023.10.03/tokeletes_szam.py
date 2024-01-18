#Tökéletes számok

#Akkor nevezünk egy pozitíc egész számot tökéletes számnak,ha a szám önmagánál kisevv osztóinak összege megegyezik a számmal.
#Kérjünk be egy számot és mondjuk meg,hogy tökéletes szám-e!

szam=int(input("Szám: "))
osszeg=0
for i in range(1,int(szam/2)+1):
    if szam%i==0:
        osszeg+=i
if osszeg==szam:
    print("tökéletes szám!")
else:
    print("nem tökéletes szám")