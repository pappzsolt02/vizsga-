from versenyzo import versenyzo

versenyzok:list[versenyzo]=[]

versenyzok.append(versenyzo('Kovács Béla',7.56,8.12,6.45))
versenyzok.append(versenyzo('Gipsz Jakab',6.66,7.12,6.98))
versenyzok.append(versenyzo('Makk Márton',8.01,8.87,7.32))
versenyzok.append(versenyzo('Kiss Albert',6.87,5.65,6.74))

print("    Név            1.     2.     3.   Legnyagyobb")
print("-------------------------------------------------")
for egy_versenyzo in versenyzok:
    print(f"{egy_versenyzo.nev.ljust(15,' ')} | {egy_versenyzo.elso} | {egy_versenyzo.masodik} | {egy_versenyzo.harmadik}|    {egy_versenyzo.legnagyobb_ugras()}   |")
    print("-------------------------------------------------")

# Hány olyan veresenyző van, akinek mindhárom ugrása 6.5 méter feletti
mind_hatesfel_feletti=0
for egy_versenyzo in versenyzok:
    if egy_versenyzo.elso>6.5 and egy_versenyzo.masodik>6.5 and egy_versenyzo.harmadik>6.5:
        mind_hatesfel_feletti+=1
print(f"\n{mind_hatesfel_feletti} versenyzőnek nagyobb mindhárom ugársa mint 6.5 méter")        

# Ki nyerete a versenyt, és mekkora ugrással?
gyoztes_indexe=0
for i in range(1,len(versenyzok)):
    if versenyzok[i].legnagyobb_ugras()>versenyzok[gyoztes_indexe].legnagyobb_ugras():
        gyoztes_indexe=i
print(f"Győzet: {versenyzok[gyoztes_indexe].nev} ({versenyzok[gyoztes_indexe].legnagyobb_ugras()} m)")

bekert_nev=input("\nKeresett versenyző: ")
for egy_versenyzo in versenyzok:
    if egy_versenyzo == bekert_nev.upper():
        print(f"{egy_versenyzo.nev} legnagyobb ugársa:{egy_versenyzo.legnagyobb_ugras()}")
        break
else:
    print("Nincs ilyen versenyző")