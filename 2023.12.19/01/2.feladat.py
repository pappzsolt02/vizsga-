def tokeltes_e(szam:int)->bool:
    osszeg=0
    for oszto in range(1,szam//2+1):
        if szam%oszto==0:
            osszeg+=oszto
    if szam==osszeg:
        return True
    return False

print("2. feladat: Tökéletes számok\nKérek két természetes számot:")
tol=int(input("Tól = "))
ig=int(input("ig = "))
print(f"Tökéketes számok {tol} és {ig} között:")

db=0
for szam in range(tol,ig+1):
    if tokeltes_e(szam):
        if db>0:
            print('; ',end="")
        print(szam,end="")
        db+=1    
if db==0:
    print("A megadott tartományon nincsen tökéletes szám!")