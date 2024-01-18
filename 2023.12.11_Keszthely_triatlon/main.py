from vesenyzok import *

fajl_be_olvas("Eredmenyek.txt")

print(f"2. feladat: A versenyt {versenyzok_szama()} versenyző fejzet be.")

print(f"3. feladat: Versenyzők száma az 'elit junior' kategóriában: {kat_letszam('elit junior')} fő")

print(f"4. feladat: Átlagéletkor: {atlag_eletkor():.1f} év.")

kategoria=input('5. feladat: kérek egy kategóriát: ')
if len(kategoria_keres(kategoria))==0:
    print("\tRajtszáma(ok): Nincs ilyen kategória",end="")
else:
    print(f"\tRajtszáma(ok):",end=" ")
    for rajtszam in kategoria_keres(kategoria):
        print(rajtszam,end=" ")
    
print(f"\n6. feladat: A legobb {gyoztes('n').nev} időt érte el.")

print(f"7. feladat: fájlba írás")
mentes("mentes.txt",1970,"f")