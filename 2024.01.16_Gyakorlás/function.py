from data import *

kosarak:list[kosar]=[]

def beolv(fajlnev):
    with open(fajlnev ,"r" , encoding="utf-8")as f:
        f.readline()
        for sor in f:
            kosarak.append(kosar(sor.strip()))

def real_hazai(csapatnev):
    hazai=0
    for k in kosarak:
        if k.hazai == csapatnev:
            hazai+=1
    return hazai

def real_idegen(csapatnev):
    idegen=0
    for k in kosarak:
         if k.idegen ==csapatnev:
            idegen +=1
    return idegen

def dontetlen():
    for k in kosarak:
        if k.hazai_pont == k.hazai_pont:
            return True
    return False   

def ossz_csap(nap):
    for k in kosarak:
        if k.időpont==nap:
            print(f"\t{k.hazai}-{k.idegen} ({k.hazai_pont}:{k.idegen_pont})")

def stad():

