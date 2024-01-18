print("1. feladat: A háromszög szerkethetősége\nkérem a háromszög oldalait!")
a=float(input("a ="))
b=float(input("b ="))
c=float(input("c ="))
if c < a+b and c+c>b and b+c>a: 
    print("A háromszög megszerkeszhető!")
else:
    print("A háromszög nem megszerkeszhető a megadott adatokkal!")