mondat = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam necessitatibus fugiat iure dolorum dicta, delectus distinctio aperiam beatae eveniet fuga ab iusto minima sit labore asperiores eum placeat, praesentium tempora?'
rovid_mondat = 'Lorem ipsum dolor sit amet consectetur adipisicing.'

# Milyen hosszú a mondat? (Karakterek száma.)
print(f'A mondat {len(mondat)} karakterből áll.')

# Hány szóból áll a mondat? (Szóközök száma + 1)
darab=0 # kezdetben még nincs szóköz
#for i in range(len(mondat)):
for karakter in mondat:
    if karakter==' ':
        darab+=1
print(f'A mondat {darab+1} szóból áll.')

# Hány olyan szó van a mondatban, amely legalább 10 karakter hosszú?
# v1:
darab=0
szo_hossza=0
for karakter in rovid_mondat:
    if karakter!=' ':
        szo_hossza+=1
    else:
        if szo_hossza>=10:
            darab+=1
        szo_hossza=0
if szo_hossza>=10: # az utolsó szó hosszát is meg kell néznünk, aminek nincs szóköz a végén, de a ciklus már végigment a teljes szövegen
            darab+=1        
print(f'A mondatban {darab} darab legalább 10 karakter hosszú szó van.')

# v2:
szavak=rovid_mondat.split() # szétdaraboljuk a szöveget és egy listába tesszük a darabokat (szavakat). split() paraméter nélkül a szóköz mentén darabol.
darab=0
for szo in szavak:
     if len(szo)>=10:
          darab+=1
print(f'A mondatban {darab} darab legalább 10 karakter hosszú szó van.')        

# Kérjünk be egy karaktert, és mondjuk meg, hogy hány darab van belőle a mondatban! (Ne számítson, hogy kicsi vagy nagy betű!)
darab=0
bekert_karakter=input('Karakter: ')
for karakter in mondat:
     if karakter.lower()==bekert_karakter.lower(): # .lower() kisbetűssé konvertál, .upper() nagybetűssé konvertál
        darab+=1
print(f'"{bekert_karakter}" karakterek száma a mondatban: {darab}.')

# Melyik karakterből mennyi van? (Karakter statisztika.)

lehetseges_karakterek='qwertzuiopőúöüóasdfghjkléáűíyxcvbnm'
karakterek_szama=[]

for lehetseges_karakter in lehetseges_karakterek:
    darab=0
    for karakter in mondat:
        if karakter.lower()==lehetseges_karakter:
             darab+=1
    karakterek_szama.append(darab)
#print(karakterek_szama)
print('Karakter statisztika:')
for i in range(len(lehetseges_karakterek)):
     print(f'{lehetseges_karakterek[i]}: {karakterek_szama[i]}')
         
max_index=0
for i in range(1,len(karakterek_szama)):
     if karakterek_szama[i]>karakterek_szama[max_index]:
          max_index==i
print(f'{lehetseges_karakter[max_index]} karakterből van a legtöbb: {karakterek_szama[max_index]} db')


        

