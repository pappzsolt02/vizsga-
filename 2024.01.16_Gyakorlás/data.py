class kosar:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(";")
        self.hazai=adatok[0]
        self.idegen=adatok[1]
        self.hazai_pont=int(adatok[2])
        self.idegen_pont=int(adatok[3])
        self.helyszín=adatok[4]
        self.időpont=adatok[5]