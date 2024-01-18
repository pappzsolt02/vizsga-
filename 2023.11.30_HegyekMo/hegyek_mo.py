from hegycsucs import *

hegyek:list[hegycsucs]=[]

def beolvas(fajlnev):
    fajl=open(fajlnev, "r", encoding="utf-8")
    fajl.readline()
    for sor in fajl:
        hegyek.append(hegycsucs(sor.strip()))
    fajl.close()

def hegyek_szama():
    return len(hegyek)

def atlag_M():
    osszeg=0
    for h in hegyek:
        osszeg+=h.magasag
    return osszeg/hegyek_szama()

def legmagasabb_hegy() ->hegycsucs:
    legmagasabb=hegyek[0]
    for h in hegyek[1:]:
        if h.magasag>legmagasabb.magasag:
            legmagasabb=h
    return legmagasabb

def van_magasabb(magassag)->bool|str:
    for h in hegyek:
        if h.magasag > magassag:
            return h.nev
    return False

def darab_magasab_mint(magassag)->int:
    db=0
    for h in hegyek:
        if h.magasag_lab>magassag:
            db+=1
    return db 

def hegy_statisztika()->dict[str,int]:
    stat:dict[str,int]={}
    for h in hegyek:
        if h.hegyseg in stat.keys():
            stat[h.hegyseg]+=1
        else:
            stat[h.hegyseg]=1
    return stat

def mentes(hegyseg,fajlnev):
    fajl=open(fajlnev, "w" , encoding="utf-8")
    fajl.write("Hegycsúcs;Magasság lábban\n")
    for h in hegyek:
        if h.hegyseg==hegyseg:
            fajl.write(f"{h.nev};{h.magasag_lab:.1f}\n")
    fajl.close()