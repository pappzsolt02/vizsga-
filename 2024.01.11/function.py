from data import *

valtozasok:list[valtozas]=[]

def beolv(fnev):
    with open(fnev, "r" ,encoding="utf-8")as f:
        for sor in f:
            valtozasok.append(valtozas(sor.strip()))

def ossz():
    return len(valtozasok)