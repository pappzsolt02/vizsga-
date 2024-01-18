#Kérjük be egy sokszöge oldalinak számát 
#Kérjuk be az oldalak hoszzát
#Írjuk ki a sokszög kerlületét!

old_szam=int(input('Adja meg az oldalak számát!: '))
kerulet=0
for i in range(old_szam):
    old_hossz=int(input('Adja meg az oldal hosszát!: '))
    # kerulet=kerulet+old_hossz 
    kerulet+=old_hossz
print(f'Kerület: {kerulet}')