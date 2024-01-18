from hegyek_mo import *

beolvas("hegyekMo.txt")

print(f"3. feladat: Hegycsúcsok száma {len(hegyek)} db")
#print(f"3. feladat: Hegycsúcsok száma {hegyek_szama()} db")

print(f"4. feladat: Hegycsúcsomk átlagos magassága: {atlag_M()} m")

print("5. feladat: A legmagasabb hegycsúcs adatai:")
legmagasabb=legmagasabb_hegy()
print(f"\tNév: {legmagasabb.nev}")
print(f"\tHegység: {legmagasabb.hegyseg}")
print(f"\tMagasság: {legmagasabb.magasag} m")

magassag=int(input("6. feladat: Kérek egy magasságot: "))
if van_magasabb(magassag)==False:
    print(f"\tNincs {magassag} m-nél magasabb hegycsúcs.")
else:
    print(f"\tVan {magassag} m-nél magasabb hegcsúcs például a(z) {van_magasabb(magassag)}")
    
print(f"7. feladat: 3000 lábnál maggassab hegycsúcsok:{ darab_magasab_mint(3000)} db")

print("8. feladat: Hegység statisztika:")
for key, value in hegy_statisztika().items():
    print(f"\t{key}: {value} db")
    
print("9. feladat: mentés")
mentes("Bükk-vidék","bukk-videk.txt")