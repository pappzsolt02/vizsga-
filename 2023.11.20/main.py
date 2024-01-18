from tanulok import *

tanulok_feltolt(10)
tanulok_kiir()

legjobb_tanulo=legjobb()
print(f"A legjobb tanuló: {legjobb_tanulo.vezeteknev} {legjobb_tanulo.keresztnev}, Átlag: {legjobb_tanulo.atlag()}")
print(f"Az osztály átlaga: {osztaly_atlag()}")
print(f"{atlag_felett()} tanuló van az osztály átlag felett.")