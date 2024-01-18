n=int(input('Adjon meg egy számot!: '))
faktor=1
print(f'{n}! = 1',end='')

for i in range(2,n+1):
    faktor*=i
    print(f'*{i}',end='')
    
print(f'={faktor}')