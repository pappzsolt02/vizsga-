#Egy szám osztói

#Kérjunk be egy számot, majd írjuk ki az osztóit
#az osztók egy sorban, pontosveszővel jelenjenek meg (szóközökkel elválasztva)

#várt működés: 
#Kérem adjon meg egy egész számot!: 15
#15 osztói 1 3 5 15 

bekert_szam=int(input("adjon meg egy számot: "))
print(f'{bekert_szam} osztói: ',end='')
for i in range(1,int(bekert_szam/2)+1):
    if bekert_szam%i==0:
        print(i, end=' ')
print(bekert_szam)