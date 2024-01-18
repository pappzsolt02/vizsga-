class versenyzo:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(";")
        self.nev=adatok[0]
        self.szuletesiev=int(adatok[1])
        self.rajtszam=int(adatok[2])
        self.nem=adatok[3]
        self.kategoria=adatok[4]
        self.ido_uszas=adatok[5]
        self.ido_elsodepo=adatok[6]
        self.ido_kerekpar=adatok[7]
        self.ido_madosdikdepo=adatok[8]
        self.ido_futas=adatok[9]
        self.osszido=self.ido_konvertal(self.ido_uszas)+self.ido_konvertal(self.ido_elsodepo)+self.ido_konvertal(self.ido_kerekpar)+self.ido_konvertal(self.ido_madosdikdepo)+self.ido_konvertal(self.ido_futas)
        
    def ido_konvertal(self,ido:str)->int:
        ido_adatok=ido.split(":")
        return int(ido_adatok[0])*3600+int(ido_adatok[1])*60+int(ido_adatok[2])