from szamok_modul import *

feltolt(10,1,100)
#print(szamok) 
# for szam in szamok:
#     print(szam,end=" ")

for i in range(len(szamok)):
    print(szamok[i],end="")
    if i < len(szamok)-1:
        print(", ", end="")


oszto=int(input("\nMilyen osztót kerersünk?: "))
if van_e_oszhato(oszto):
    print(f"Van olyan szám a listában, amely oszható ezzel: {oszto}")
else:
       print(f"Nincs olyan szám a listában, amely oszható ezzel: {oszto}")

# szamok_atlaga=atlag()
# print(f"A lista elemeinek átlaga: {szamok_atlaga}")
# Ha később nem kell az átlag értéke sehol, akkor nem kell eltárolni
print(f"A lista elemeinek átlaga: {atlag()}")

keresett_szam=int(input("keresett szám: "))
kereses_eredemeny=keres(keresett_szam)
if kereses_eredemeny==False:
    print("A keresett szám nincs a listában.")
else:
     print(f"A keresett szám első előfordulásának sorszáma: {kereses_eredemeny+1}")

print(f'A számok között {darab_ha_tobb(50)} darab 50-nél nagyobb (vagy eyenlő) szám van.  ')