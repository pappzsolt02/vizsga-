"""
class auto:
    tipus=""
    rendszama=""
    szine=""
    teljesitmeny=""
"""

class auto:
    def __init__(self,tipus:str,rendszam:str,szin:str,teljesitmeny:float,gyorsulas:float=0) -> None:
        self.tipus=tipus
        self.rendszam=rendszam
        self.szin=szin
        self.teljesitmeny=teljesitmeny
        self.gyorsulas=gyorsulas
        pass