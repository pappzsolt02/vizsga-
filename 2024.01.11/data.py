from datetime import datetime

class valtozas:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(";")
        self.datum=datetime.strptime(adatok[0],"%Y.%m.%d")
        self.benzin=int(adatok[1])
        self.gazolaj=int(adatok[2])

    # def ev_ho_nap(self,datum:str):
    #     dat=datum.split(".")
    #     ev=dat[0]
    #     honap=dat[1]
    #     nap=dat[2]