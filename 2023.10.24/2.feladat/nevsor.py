nevek = ['Nikovits Ádám','Palkovics Marcell','Papp Zsolt','Rákóczy Tamás','Rózsavölgyi Simon','Szabó Benjámin','Száva Levente Imre','Veiger Kevin','Zagyva Tamás','Zalavári Marcell']

def osztalyletszam()->int:
    return len(nevek)

def legh_nev()->str:
    legh=nevek[0]
    for nev in nevek[1:]:
        if len(nev)>len(legh):
            legh=nev
    return legh

def atlag_h()->float:
    osszeg=0
    for nev in nevek:
        osszeg+=len(nev)
    return osszeg/osztalyletszam()

def vane(keresett_nev:str)->bool:
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            return True
    return False

def tanulo_szamol(keresett_nev:str)-> int:
    darab=0
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            darab+=1
    return darab

def keres(keresett_nev:str)->int|bool:
    for i in range(osztalyletszam()):
        if keresett_nev.lower() in nevek[i].lower():
            return i
    return False