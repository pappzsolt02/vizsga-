from random import randint

N=int(input('Hány alkalommal legyen feldobás? '))
anni_nyert=0
panni_nyert=0
for i in range(N):
    kocka_dobas1=randint(1,6)
    kocka_dobas2=randint(1,6)
    kocka_dobas3=randint(1,6)
    ossz=kocka_dobas1+kocka_dobas2+kocka_dobas3
    if ossz < 10:
        nyert='Anni'
        anni_nyert+=1
    else:
        nyert='Panni'
        panni_nyert+=1
    print(f'Dobás: {kocka_dobas1} + {kocka_dobas2} + {kocka_dobas3} = {ossz} \tnyert={nyert}')
print(f'A játék során {anni_nyert} alkalommal Anni, {panni_nyert} alakaolmmal Pannyi nyert')
