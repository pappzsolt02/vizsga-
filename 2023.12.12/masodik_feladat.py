def mgh_szam(szo:str)->int:
    db=0
    for b in szo:
        if b in mgh:
            db+=1
    return db

napok=['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
mgh='aáeéoóöőiíúuűü'
legtobb=napok[0]
for nap in napok[1:]:
    if mgh_szam(nap)>mgh_szam(legtobb):
        legtobb=nap
print(f"A legtöbb magánhangzó a {legtobb}-ben van!") 