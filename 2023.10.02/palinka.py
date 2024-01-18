from random import randint

osszesen=0
ivott=False

for i in range(1,31):
    if ivott==False:
        mai_fozet=randint(1,5)
        osszesen+=mai_fozet
        if randint(1,5)==5:
            ivott=True
            osszesen-=1
        print(f'{i}. nap: {mai_fozet} liter. Eddigi termés összesen: {osszesen} liter. ',end='')
        if ivott:
            print("\nMa ivott Pista bácsi a haverokkal.",end='')
        print()
    else:
        print(f'{i}. nap: Pista bácsi nem főz, mert másnapos')
        ivott=False

print(f"\nA 30. map végére Pista bácsinak {osszesen} liter pálinkája lett")