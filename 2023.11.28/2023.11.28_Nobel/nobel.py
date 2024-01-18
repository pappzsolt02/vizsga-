from dijazott import *

dijazottak:list[dijazott]=[]

def beolvas(fajlnev):
    fajl=open(fajlnev, "r", encoding="utf-8")
    fajl.readline()
    for sor in fajl:
        uj_dijazott=dijazott(sor.strip())
        dijazottak.append(uj_dijazott)
    fajl.close()

def  tipus_nev_alapjan(nev:str)->str:
    for d in dijazottak:
        if nev.upper()==d.teljesnev.upper():
            return d.tipus
    return None

def dijazot_ev(ev:int,tipus:str):
    for d in dijazottak:
        if ev==d.ev and tipus==d.tipus:
            return d
    return None

def szervezetek_adott_ev_utan(ev:int):
    for d in dijazottak:
        if d.ev>=ev and d.vezeteknev=="":
            print(f"\t{d.ev}: {d.keresztnev}")

def dijazott_nev_tert(nev:str):
    for d in dijazottak:
        if nev.upper() in d.teljesnev.upper():
            print(f"\t{d.ev}: {d.teljesnev}({d.tipus})")

def nobeldij_statisztika():
    stat={}
    for d in dijazottak:
        if d.tipus in stat.keys():
            stat[d.tipus]+=1
        else:
            stat[d.tipus]=1
    for key,vaule in stat.items():
        print(f"\t{str(key).ljust(25)} {vaule:4d} db")