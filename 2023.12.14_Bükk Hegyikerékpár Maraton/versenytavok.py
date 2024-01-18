from versenytav import *
import math

Versenytavok:list[Versenytav]=[]

def beolv(fajlnev:str):
    f=open(fajlnev, "r" , encoding="utf-8")
    f.readline()
    for sor in f:
        Versenytavok.append(Versenytav(sor.strip()))
    f.close()

def nem_ert()->float:
    return (1-len(Versenytavok)/691)*100

def n_vers_szama(tav:str,nem:str)->int:
    db=0
    for v in Versenytavok:
        if v.Tav()==tav and v.Nem() == nem:
            db+=1
    return db

def v_tobb_mint(masodpercek:int):
    for v in Versenytavok:
        if v.masodpercek > masodpercek:
            return True
    return False

def gyoztes(tav:str,kategotia:str):
    min=math.inf
    gyozetsv=None
    for v in Versenytavok:
        if v.Tav()==tav and v.kategoria==kategotia and v.masodpercek<min:
            min=v.masodpercek
            gyozetsv=v
    return gyozetsv

def stat():
    stat={}
    for v in Versenytavok:
        if v.Nem()=="Férfi":
            if v.kategoria in stat.keys():