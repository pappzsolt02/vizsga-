from versenyzo import versenyzo
import math

versenyzok_lista:list[versenyzo]=[]

def fajl_be_olvas(fajlnev:str):
    fajl=open(fajlnev, "r" ,encoding="utf-8")
    for sor in fajl:
        versenyzok_lista.append(versenyzo(sor.strip()))
    fajl.close
    
def versenyzok_szama()->int:
    return len(versenyzok_lista)

def kat_letszam(kategoria:str)->int:
    db=0
    for v in versenyzok_lista:
        if v.kategoria==kategoria:
            db+=1
    return db

def atlag_eletkor()->float:
    osszeg=0
    for v in versenyzok_lista:
        eletkor=2014-v.szuletesiev
        osszeg+=eletkor
    return osszeg/len(versenyzok_lista)

def kategoria_keres(kategoria:str)->list:
    kategoria_lista=[]
    for v in versenyzok_lista:
        if v.kategoria==kategoria:
            kategoria_lista.append(v.rajtszam)
    return kategoria_lista

def gyoztes(nem:str)->versenyzo:
    gyoztes_ideje=math.inf
    gyoztes_versenyzo=None
    for v in versenyzok_lista:
        if v.nem==nem and v.osszido<gyoztes_ideje:
            gyoztes_versenyzo=v
            gyoztes_ideje=v.osszido
    return gyoztes_versenyzo

def mentes(fajlnev,ev:int,nem:str):
    fajl=open(fajlnev, "w", encoding="utf-8")
    for v in versenyzok_lista:
        if v.szuletesiev<=ev and v.nem == nem:
            fajl.write(f"{v.nev} - {v.rajtszam}\n")
    fajl.close()