# Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
class erdemeny:
    def __init__(self,sor) -> None:
        adatok=sor.split(";")
        self.nev=adatok[0]
        self.rajtszam=int(adatok[1])
        self.kategira=adatok[2]
        self.ido=adatok[3]
        self.telejistett=int(adatok[4])