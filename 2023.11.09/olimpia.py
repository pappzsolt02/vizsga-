versenyzok=['BASTIEN Steven', 'dos SANTOS Felipe', 'DUBLER Cedric', 'ERM Johannes', 'HELCELET Adam Sebastian', 'KAZMIREK Kai', 'LEPAGE Pierce', 'MAYER Kevin', 'MOLONEY Ashley', 'ROE Martin', 'SCANTLING Garrett', 'SHKURENYOV Ilya', 'SYKORA Jiri', 'TILGA Karel', 'UIBO Maicel', 'URENA Jorge', 'VICTOR Lindon', 'WARNER Damian', 'WIESIOLEK Pawel', 'ZHUK Vitaliy', 'ZIEMEK Zachery']
eredmenyek=[8236, 7880, 7008, 8213, 8004, 8126, 8604, 8726, 8649, 7863, 8611, 8413, 7943, 7018, 8037, 8322, 8414, 9018, 8176, 8131, 8435]

def versenyzok_szama()->int:
    ossz=len(versenyzok)
    return ossz
    
def tobb_pont_mint_8600()->int:
    db=0
    for erdmeny in eredmenyek:
        if erdmeny>8600:
            db+=1
    return db

def atlag()->float:
    osszeg=0
    for eredmeny in eredmenyek:
        osszeg+=eredmeny
    return osszeg/len(eredmenyek)

def max_pont()->int:
    legnagyobb=eredmenyek[0]
    for eredmeny in eredmenyek[1:]:
        if legnagyobb<eredmeny:
            legnagyobb=eredmeny
    return legnagyobb

