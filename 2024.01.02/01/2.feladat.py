from random import randint
def halmaz_e(lista:list)->str:
    if len(set(lista))==len(lista):
        return "Halmaznak tekinthető!"
    return "Halmaznak nem tekinthető!"

print("2. feladat: Halmaz-e?")
for i in range(1,9):
    lista:list[int]=[]
    for j in range(5):
        lista.append(randint(0,10))
    print(F"{i}. {lista} -> {halmaz_e(lista)}")