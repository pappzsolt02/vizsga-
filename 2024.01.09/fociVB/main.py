from function import *

beolv("fociVBK.csv")

print(f"1. feladat: csapatok száma: {ossz()}")

print("2. feladat: 2018-as VB csapatai:")
reszvet:list[str]=vb_2018()
for i in range(len(reszvet)):
    if i%4==0 and i!=0:
        print("")
        print(f"\t{reszvet[i].ljust(14)}",end="") 
    else:
        print(f"\t{reszvet[i].ljust(14)}",end="")
    
print(f"\n\n3. feladat: A BeNelux országok összesen {BeNeLux()} alkalommal vettek részt a VB-n")

print(f"5. feladat: Eddig {vilagbajnok()} ország bolt világbajnok")
