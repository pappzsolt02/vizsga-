# 3. feladat: 
# Generáljunk egy 4 jegyű PIN kódot. 
# Kérjük be a felhasználótól a PIN kódot. Maximum 3 próbálkozása lehet. Ha nem találja el, akkor írjuk ki, hogy HIBÁS, és hogy hány próbálkozása maradt még. Három sikertelen próbálkozás után írjuk ki hogy "ZÁROLÁS", egyébként "Sikeres azonosítás".
# Ha a PIN kód helyett egy mesterkódot ad meg (legyen: 123456) akkor írja ki a PIN kódot!

from random import randint

#v1
#pin=randint(1000,9999) #itt a pin az int típusú
#ha 1000-nél kisebb számot generánlánk, akkor nem lenne 4 jegyű a pin!!

#v2
# pin=''# a pin string típusú
# for i in range(4):
#     szamjegy=randint(0,9)
#     pin+=str(szamjegy)
    
# print(pin)

#v3
pin=str(randint(0,9999))
# jo_pin=pin.zfill(4)#balról vezető 0-val tölti fel megadott hosszúságra (itt összesen 4 számjegyű lesz)
jo_pin=pin.rjust(4,'0')#balról tölti fel a stringet megadott hosszra, megadott karakterrel 
#ljust jobbról tölti fel a stringet megadott hosszra, megadott karakterrel 
#print(jo_pin)

mesterkod='123456'
megadott_pin=''
probal_szama=3
while jo_pin!=megadott_pin and probal_szama>0:
    megadott_pin=input('Adja meg a PIN kódját!: ')
    probal_szama-=1
    if megadott_pin==mesterkod:
        #v1:print(f'Mesterkódot adott meg. PIN: {jo_pin}')
        #v2:
        print(f'Mesterkódot adott meg. PIN: {jo_pin}')
        uj_pin=input('Adja meg új PIN kódját: ')
        uj_pin2=input('Adja meg új PIN kódját mégegyszer: ')
        if uj_pin==uj_pin2:
            jo_pin=uj_pin
            print('PIN kódját sikeresen megválzoztatta')
            porbal_szama=3
        else:
            print('A megadott két PIN nem egyezik meg. PIN kódja nem változott!')
    elif jo_pin!=megadott_pin:
        print(f'Hibás PIN kód. Hátralvévő probálkozások száma:{probal_szama}')

if jo_pin!=megadott_pin:
    print('Kártyákát zároltuk!')
else:
    print('Sikeres azonosítás!')
    
    