from mukorcsolya import *

for i in range(10):
    print(f"{i+1}. versenyző: ")
    versenyzo_pontszamai=versenyzo_osszes_pontszama()
    print(f"\t A versenyző pontszamai:,{versenyzo_pontszamai}")
    print(f"\t A legnagyob pontszám: {legjobb_pontszam(versenyzo_pontszamai)}")
    print(f"\t A legkisebb pontszám: {legroszabb_pontszam(versenyzo_pontszamai)}")
    print(f"\t Átlagpontszám: {atlag(versenyzo_pontszamai)}")

print(f"\n A győztes versenyző rajtszáma: {gyoztes()+1}. versenyző")