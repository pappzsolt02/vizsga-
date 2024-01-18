from helyezes import *

helyezesek:list[helyez]=[]

def beolvas(fajlnev):
    fajl=open(fajlnev, "r" , encoding="utf-8")
    for sor in fajl:
        helyezesek.append(helyez(sor.strip()))
    fajl.close()

def pontszerzo_helyezesek_szama()->int:
    return len(helyezesek)

def helyezes_sz(hely:int)->int:
    db=0
    for h in helyezesek:
        if h.helyezes==hely:
            db+=1
    return db 

def pont_ossz()->int:
    osszeg=0
    for h in helyezesek:
        osszeg+=h.olimpiai_pont
    return osszeg

def ermek_szama(sportag:str)->int:
    db=0
    for h in helyezesek:
        if h.helyezes<=3 and h.sportag==sportag:
            db+=1
    return db

def mentes(fajlnev):
    fajl=open(fajlnev, "w" ,encoding="utf-8")
    for h in helyezesek:
        if h.sportag=="kajakkenu":
            fajl.write(f"{h.helyezes} {h.sprotolok_sz} {h.olimpiai_pont} kajak-kenu {h.versenyszam}\n")
        else:
            fajl.write(f"{h.helyezes} {h.sprotolok_sz} {h.olimpiai_pont} {h.sportag} {h.versenyszam}\n")
    fajl.close()