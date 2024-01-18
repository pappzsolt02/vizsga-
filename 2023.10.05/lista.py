# a=123
# b=34
# c=87
# d=66

szamok=[123,34,87,66]
szinek=['piros','kék','zöld','fehér']
print(szamok)
print(*szinek,sep=' - ')#szinek lista összes eleme

print(szamok[0])
print(szamok[-1])

print(f'{len(szamok)} elem van a listában.')
print(f'A lista utolsó eleme: {szamok[len(szamok)-1]}.')


for i in range(0,len(szamok)):
    print(f'A lista {i+1}. eleme: {szamok[i]}')

db=0
for szam in szamok:
    print(szam, end=' ')
    if szam%3==0:
        db+=1
print(f'\n{db} db 3-mal oszható szám van a "szamok listában.')