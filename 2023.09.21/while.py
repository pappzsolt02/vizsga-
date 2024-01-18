#Ellenőrözz adatbekérés 10 és 100 között fogadunk el számokat


szam=-1 # olyan kezdőrtéket kell, ami teljesíti a feltételt

while szam<10 or szam>100:
    #szam=int(input('Adjon meg egy számot 10 és 100 között!: '))
    input_txt=input('Adjon meg egy számot 10 és 100 között!: ')
    if input_txt.isnumeric(): #csak számjegy , tizedes pont,- előjel nem
        szam=int(input_txt)
    else:
        print('Kérem pozitív egyész számot adjon meg!')
#később:
#saját fgv. float_input() -->valós szám ellenőrzötten
#saját fgv. int_input() -->valós szám ellenőrzötten(negatív is akár )