from data import*

fordulok:list[Fogadasi_forduldo]=[]

def fajl_be(fajlnev):
    with open(fajlnev, "r" , encoding="utf-8")as f:
        f.readline()
        for sor in f:
            fordulok.append(Fogadasi_forduldo(sor.strip()))

def fog_for_szam():
    return len(fordulok)

def telitalat_sz()->int:
    db=0
    for fordulo in fordulok:
        db+=fordulo.t13p1
    return db

def dontetlen_m()->bool:
    for fordulo in fordulok:
        if "X" not in fordulo.eredmenyek:
            return True
    return False