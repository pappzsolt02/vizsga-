#A bekérést addig ismételjük, amíg a név helyére üres karakterláncot nem ad meg a felhasználó(csak ENTERt üt)

nev='na'
while nev !='':
    nev=input("Név (ENTER = kilépés): ")
    if nev!='':
        osztaly=input("Osztály: ")
        kategoria=int(input("Kategória: "))
        koltseg=int(int(input("Kötlség: ")))
        
        limit=kategoria*10000
        
        if koltseg>limit:
            print(f"{nev}: {koltseg-limit} FT")
        else:
            print(f"{nev}: nincs önköltség.")