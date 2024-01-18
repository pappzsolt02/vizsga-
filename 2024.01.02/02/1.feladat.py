print("1. feladat: Kisebb-nagyobb meghatározása")
a=int(input("Kérem az első számot: "))
b=int(input("Kérem az második számot: "))
if a>b:
    print(f"A nagyob szám {a}, a kisebb {b}.")
elif a==b:
    print("A két szám egyenlő")
else:
    print(f"A nagyob szám {b}, a kisebb {a}.")