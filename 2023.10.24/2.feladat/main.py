from nevsor import *


print(f"Az osztályban {osztalyletszam()} fő van.")


print(f"A leghosszab nevű diák: {legh_nev()}")

print(f"Az osztályban a nevek áltagos hossza: {atlag_h()}")

#Van-e az osztályban 'keresett' nevű tanuló?
#Ha van, akkor mennyi?
#Ha van, akkor hányadik a névsorban?

keresett=input("keresett tanuló neve: ")
if vane(keresett):
    print(f" van {keresett} az osztályban, {tanulo_szamol(keresett)} fő.")
    print(f"A névsorban az első {keresett} sorszáma:{keres(keresett)+1}")
else:
    print(f"Nincs {keresett} nevú tanuló az osztályban")