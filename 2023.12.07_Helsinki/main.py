from helsinki import *

beolvas("helsinki.txt")

print(f"3. feladat:\nPontszerző helyezések száma: {pontszerzo_helyezesek_szama()}")

print(f"4. feladat\nArany: {helyezes_sz(1)}\nEzüst: {helyezes_sz(2)}\nBronz: {helyezes_sz(3)}\nÖsszesen: {helyezes_sz(1)+helyezes_sz(2)+helyezes_sz(3)}")

print(f"5. feladat:\nOlimpiai pontok száma: {pont_ossz()}")

print("6. feladat")
uszas=ermek_szama("uszas")
torna=ermek_szama("torna")
if uszas==torna:
    print("Egyenlő volt az érmek száma")
elif torna>uszas:
    print("Torna sprotágban szereztek több érmet")
else:
    print("Uszás sprotágban szereztek több érmet")

mentes("helsiniki2.txt")