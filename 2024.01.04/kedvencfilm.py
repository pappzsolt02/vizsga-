def oraperc():
    ora=0
    perc=0
    
    return str(ora) +"óra" + str(perc)+"perc"

nev=input("Adja meg a film cimét! ")
film_hosz=int(input("Hány perces a film ?"))
print(f"A(z) {nev} című film {oraperc()} hósszú")

