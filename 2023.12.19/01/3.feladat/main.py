from fug import *

beolv("ub2017egyeni.txt")

print(f"3.2 feladat: Futók száma: {versenyzoszam()}")

print(f"3.3 feladat: Célba érkező nói sportolók: {noi_teljes()} fő")

legh_n=leghosszab_nev()
print(f"3.4 feladat: A leghósszab nevű futó\n\tNév: {legh_n.nev}\n\tRajtszám: {legh_n.rajtszam}\n\tEredmény: {legh_n.ido}")

print(f"3.5 :Férfi sportolok átlagos ideje: {atlag()} óra")