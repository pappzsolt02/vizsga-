from random import randint

darab=int(input("Hány elemeű legyen a lista? "))
szamok=[]

for i in range(darab):
    szamok.append(randint(10,99))
print(szamok)

# szamok.clear() # lista kiürítése 
# print(szamok)

szamok.insert(1,40) # a első paraméterben megadott helyre beszúrja a második paraméterben megadott értéket 
print(szamok)

szam=szamok.pop()
print(szam)
print(szamok)
szam=szamok.pop(2)
print(szam)
print(szamok)


torlendo=int(input("mit szeretne törölni: "))
szamok.remove(torlendo)
print(szamok)

szamok.sort()
print(szamok)

szamok.sort(reverse=True)
print(szamok)


masik_szamok=[1,2,3,4]
szamok.extend(masik_szamok)
print(szamok)

meg_szamok=[5,6,7,8,9]
eredmeny_lista=masik_szamok+meg_szamok
print(eredmeny_lista)