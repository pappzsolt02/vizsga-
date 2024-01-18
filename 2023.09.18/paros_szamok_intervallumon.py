kezd=int(input('Eleje: '))
vege=int(input('Vége: '))

if kezd%2!=0:
    kezd+=1

for i in range(kezd,vege+1,2):
    print(i,end=' ')
    