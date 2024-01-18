from auto import auto
"""
az_en_autom=auto

az_en_autom.rendszama="AA-AA-001"
az_en_autom.szine="kék"
az_en_autom.tipus="Skoda Octavia"
az_en_autom.teljesitmeny=140

"""

autok:list[auto]=[]

egy_auto=auto("Skoda","AA-AA-001","kék",140,8.8)
autok.append(egy_auto)
egy_auto=auto("Audi","RRT-768","piros",230)
autok.append(egy_auto)
egy_auto=auto("Lada","AAB-768","barna",45)
autok.append(egy_auto)
egy_auto=auto("KIA","AA-BB-768","zöld",125)
autok.append(egy_auto)

#print(autok[0].szin)
#print(autok)
for egy_auto in autok:
    # print(egy_auto.tipus,egy_auto.rendszam,egy_auto.szin,egy_auto.teljesitmeny,egy_auto.gyorsulas)
    print(f"{egy_auto.tipus.ljust(10,' ')}{egy_auto.rendszam.ljust(12,' ')}{egy_auto.teljesitmeny} LE")

# legnagyobb teljesítményű autó
legnagyobbb_teljesitmenyu_auto=autok[0]
for egy_auto in autok:
    if egy_auto.teljesitmeny>legnagyobbb_teljesitmenyu_auto.teljesitmeny:
        legnagyobbb_teljesitmenyu_auto=egy_auto
print("A legnagyobb teljesítméníű autó:")
print(f"\tTípusa: {legnagyobbb_teljesitmenyu_auto.tipus}")
print(f"\tRendszama: {legnagyobbb_teljesitmenyu_auto.rendszam}")
print(f"\tSzíne: {legnagyobbb_teljesitmenyu_auto.szin}")
print(f"\tTeljesítménye: {legnagyobbb_teljesitmenyu_auto.teljesitmeny}")

#keresünk egy adott rendszámot 
bekert_rendszam=input("\n\nKeresett rendszám: ")
for egy_auto in autok:
    if egy_auto.rendszam.upper()==bekert_rendszam.upper():
        print(f"\tA kerestt autó tipusa: {egy_auto.tipus}")
        print(f"\tA kerestt autó szíje: {egy_auto.szin}")
        break
else:
    print("\tNinsc ilyen autó")