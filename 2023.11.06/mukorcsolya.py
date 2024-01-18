from random import randint

veresenyzok_osszpontszama=[]

def random_pontszam() ->float:
    """ Visszaad egy random pontszámor 0 és 10 között? 0,25-ös lépésközzel"""
    return randint(0,9)+randint(0,4)/4

def versenyzo_osszes_pontszama()->list[float]:
    pontszamok=[]
    for i in range(7):
        pontszamok.append(random_pontszam())
    return pontszamok

def legjobb_pontszam(pontszamok: list[float])->float:
    legnagyobb=pontszamok[0]    
    for pont in pontszamok[1:]: 
        if pont>legnagyobb:
            legnagyobb=pont
    return legnagyobb

def legroszabb_pontszam(pontszamok: list[float])->float:
    legkisebb=pontszamok[0]    
    for pont in pontszamok[1:]: 
        if pont<legkisebb:
            legkisebb=pont
    return legkisebb

def atlag(pontszamok: list[float])->float:
    """ 
    A legrosszab és a legjobb pontszám kiesik, és a többinek az átlagát adja vissza
    """
    osszeg=0
    for pont in pontszamok:
        osszeg+=pont
    osszeg-=legjobb_pontszam(pontszamok)-legroszabb_pontszam(pontszamok)
    veresenyzok_osszpontszama.append(osszeg)
    return osszeg/(len(pontszamok)-2)

def gyoztes()->int:
    """ 
    Visszaadja a győztes versenyző sorszámát.
    """
    gyoztes_indexe=0
    for i in range(len(veresenyzok_osszpontszama)):
        if veresenyzok_osszpontszama[i]>veresenyzok_osszpontszama[gyoztes_indexe]:
            gyoztes_indexe=i
    return gyoztes_indexe