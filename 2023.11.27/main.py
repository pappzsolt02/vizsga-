from fug import *
from os import system

autok_betolt()


while True:
    system("cls") #képernyő törlése 
    print("0 - kilép")
    print("1 - Új autó adatainak megadása")
    print("2 - Adatok litázása")
    print("3 - A legerősebb autó")
    print("4 - Adott színű autók listázása")
    valasztas=input("Választás: ")
    
    match valasztas:
        case '0':
            break
        case '1':
            system('cls')
            auto_beker()
        case '2':
            system('cls')
            print("A nyilvántartásban lévő autók:")
            autok_kiir(autok)
            input("Tovább...")
        case '3':
            system('cls')
            legerosebb_auto=legerosebb()
            print("A legerősebb autó adatai:")
            print(f"\tRendszám: {legerosebb_auto.rendszam}")
            print(f"\tMárka. {legerosebb_auto.marka}")
            print(f"\tTipus: {legerosebb_auto.tipus}")
            print(f"\tSzín: {legerosebb_auto.szin}")
            print(f"\tTeljesítmény: {legerosebb_auto.teljesitmeny}")
            input("Tovább...")
        case '4':
            system('cls')
            szin=input("Milyen színű autókat listázzunk? ")
            print(f"{szin} színű autók:")
            autok_kiir(kereset_szin(szin))
            input("Tovább...")
