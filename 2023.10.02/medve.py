elojovetelek_szama=0
for i in range(7):
    print(f"{i+1}. nap:")
    reggel=float(input('Reggel: '))
    delben=float(input('Délben:'))
    este=float(input('Este: '))
    atlag=(reggel+delben+este/3)
    
    if atlag>10:
        print("Ma előjött a medve!")
        elojovetelek_szama+=1
    else:
        print("Ma nem jött elő a medve")
print(f"A héten {elojovetelek_szama} nap volt látható a medve.")