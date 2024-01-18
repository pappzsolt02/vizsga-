from data import * 

erdemenyek:list[erdemeny]=[]

def beolv(fajlnev):
    with open(fajlnev ,"r", encoding="utf-8")as fajl:
        fajl.readline()
        for sor in fajl:
            erdemenyek.append(erdemeny(sor.strip()))

def versenyzoszam():
    return len(erdemenyek)

def noi_teljes():
    db=0
    for e in erdemenyek:
        if e.kategira=="Noi" and e.telejistett==100:
            db+=1
    return db

def leghosszab_nev():
    max_hossz=erdemenyek[0]
    for e in erdemenyek:
        if len(e.nev)>len(max_hossz.nev):
            max_hossz=e
    return max_hossz

def atlag():
    db=0
    osszeg=0
    for e in erdemenyek:
        if e.kategira=="Ferfi" and e.telejistett==100:
            db+=1
            ido_db=e.ido.split(":")
            osszeg+=int(ido_db[0])*3600+int(ido_db[1])*60+int(ido_db[2])
    return (osszeg/3600)/db