class versenyzo:
    def __init__(self,nev:str,elso:float,masodik:float,harmadik:float) -> None:
        self.nev=nev
        self.elso=elso
        self.masodik=masodik
        self.harmadik=harmadik
    
    def legnagyobb_ugras(self):
        ugrasok=[]
        ugrasok.append(self.elso)
        ugrasok.append(self.masodik)
        ugrasok.append(self.harmadik)
        return max(ugrasok)