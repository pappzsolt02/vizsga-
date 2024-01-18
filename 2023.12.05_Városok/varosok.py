from Varos import *

varosok:list[Varos]=[]

def beolvas(fajlnev:str):
    fajl=open(fajlnev, "r" , encoding="utf-8")
    fajl.readline()
    for sor in fajl:
        varosok.append(Varos(sor.strip()))
    fajl.close()
    
def orszag_lakossaga(orszag:str)->int:
    osszeg=0
    for v in varosok:
        if v.orszag==orszag:
            osszeg+=v.lakossag
    return osszeg*1000

def legnagyobb_varos()->Varos:
    legnaygyobb=varosok[0]
    for v in varosok[1:]:
        if v.lakossag>legnaygyobb.lakossag:
            legnaygyobb=v
    return legnaygyobb

def legnagyobb_varos_orszagban(orszag:str)->Varos:
    for varos in varosok:
        if varos.orszag==orszag:
            legnaygyobb=varos
            for v in varosok[1:]:
                if v.lakossag>legnaygyobb.lakossag and v.orszag==orszag:
                    legnaygyobb=v
            return legnaygyobb

def legnagyobb_varos_orszagban2(orszag:str)->Varos|bool:
    #ha nem biztos, hogy az toszág benne van a listában
    for varos in varosok:
        if varos.orszag==orszag:
            legnaygyobb=varos
            for v in varosok[1:]:
                if v.lakossag>legnaygyobb.lakossag and v.orszag==orszag:
                    legnaygyobb=v
            return legnaygyobb
    return False

def van_e(orszag:str)->bool:
    for v in varosok:
        if v.orszag==orszag:
            return True
    return False

def szokozos_varosok(szokozok_szama:int)->int:
    db=0
    for v in varosok:
        if v.szok_sz()==szokozok_szama:
            db+=1
    return db

def orsz_stat()->dict[str,int]:
    stat:dict[str,int]={}
    for v in varosok:
        if v.orszag in stat.keys():
            stat[v.orszag]+=1
        else:
            stat[v.orszag]=1
    return stat

def orszag_mentes(fajlnev:str,orszag:str):
    fajl=open(fajlnev, "w" ,encoding="utf-8")
    for v in varosok:
        if v.orszag==orszag:
            fajl.write(f"{v.varos};{v.lakossag}\n")
    fajl.close()
    
