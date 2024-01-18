# ido=input("Kérem az aktuális időt [hh:mm:ss]: ")
# idok=ido.split(":")
# masodperc=int(idok[0])*3600+int(idok[1])*60+int(idok[2])
# print(f"Másodpercben: {masodperc}")


ido=int(input("Kérem az időt [másodperc]: "))
ora=ido//3600
perc=ido%3600//60
masodperc=ido%60
print(f"{str(ora).zfill(2)}:{str(perc).zfill(2)}:{str(masodperc).zfill(2)}")
