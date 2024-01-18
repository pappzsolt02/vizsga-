class Varos:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(";")
        self.varos=adatok[0]
        self.orszag=adatok[1]
        self.lakossag=int(adatok[2])

    def szok_sz(self)->int:
        db=0
        for karakter in self.varos:
            if karakter==" ":
                db+=1
        return db