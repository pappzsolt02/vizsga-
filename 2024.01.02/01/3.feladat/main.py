from function import *

fajl_be("toto.txt")
print("3. feladat: Toto\n3.1 feladat: Adatok beolvasása ás tárolása")

print(f"3.2 feladat: Fogadási fordulók száma: {fog_for_szam()}")

print(f"3.3 feladat: Telitalálatos szelvények száma: {telitalat_sz()} darab")

if dontetlen_m():
    print("3.4 feladat: Volt döntetlen mentes forduló")
else:
    print("3.4 feladat: Nem volt döntetlen mentes forduló")