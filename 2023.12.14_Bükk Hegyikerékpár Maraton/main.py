from versenytavok import *

beolv("bukkm2019.txt")

print(f"4. feladat: Versenytávot nem teljestytők: {nem_ert()}%")

print(f"5. feladat: Női vesenyzők száma a rövid távú versenyen: {n_vers_szama('Rövid','Nő')}fő")

if v_tobb_mint(6*60*60):
    print("6. feladat: Volt ilyen versenyző")
else:    
    print("6. feladat: Nem volt ilyen versenyző")

print(f"7. feladat: A felnőtt férfi (ff) kategória győztese rövid távon\n\tRajtszám: {gyoztes('Rövid','ff').rajtszam}\n\tNév: {gyoztes('Rövid','ff').nev}\n\tEgyesület: {gyoztes('Rövid','ff').egyesulet}\n\tIdő: {gyoztes('Rövid','ff').ido}")