class hegycsucs:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.nev=adatok[0]
        self.hegyseg=adatok[1]
        self.magasag=int(adatok[2])
        self.magasag_lab=self.magasag*3.2803895