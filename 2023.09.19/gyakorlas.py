# 0 1 1 2 3 5 8 13 21 34 ....stb
#A nulladik eleme a 0 az első eleme az 1
#további elemeket az alőző 2 elem összegéből kapjuk 
#a(n)=a(n-1)+a(n-2)-aktuális=előző+előző elötti

n=int(input("Adja meg , hogy meddig mennyen a sorozat!: "))
elozo_elt=0
elozo=1

if n>=2:
    print('0 1 ',end ='')
elif n==1:
    print('0')

for i in range(n-2):
    akt=elozo_elt+elozo
    elozo_elt=elozo
    elozo=akt
    print(akt,end=' ')