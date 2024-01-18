a1=int(input('Adja meg a számtani srozozat első számát(a1)!: '))
d=int(input('Adja meg a differencijáját(d)!: '))
n=int(input('Adja meg a elemszámát(n)!: '))

# for i in range(n):
#     an=a1+i*d
#     print(an,end=', ')

for i in range(n):
    an=a1+i*d
    if i==n-1:
        print(an,end=' ')
    else:
        print(an,end=', ')