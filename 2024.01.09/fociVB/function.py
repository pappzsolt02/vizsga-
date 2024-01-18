from data import *

eredmenyek:list[focivb]=[]

def beolv(fnev):
    with open(fnev, "r" , encoding="utf-8")as f:
        f.readline()
        for sor in f:
            eredmenyek.append(focivb(sor.strip()))

def ossz():
    return len(eredmenyek)

def vb_2018():
    resztvetek=[]
    for e in eredmenyek:
        if e.elso_reszvetel==2018 or e.legutobbi_reszvetel==2018:
            resztvetek.append(e.csapat)
    return resztvetek
    
def BeNeLux():
    db=0
    for e in eredmenyek:
        if e.csapat=="Belgium" or e.csapat=="Hollandia" or e.csapat=="Luxemburg":
            db+=e.reszvetelek_szama
    return db

def vilagbajnok():
    db=0
    for e in eredmenyek:
        if "Világbajnok" in e.legjobb_eredmeny:
            db+=1
    return db