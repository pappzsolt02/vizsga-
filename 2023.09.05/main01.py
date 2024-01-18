#Ez egy 1 soros komment
"""
Ez
egy
több soros komment
"""
print("Helló 'szöveg' Világ!!")
szam=20.5 #változó létrehozása, értékadás
print(szam) #változó tartalmának kiírása
print(type(szam)) #változó típusának kiírása
a="alma"
b="fa"
print(a+b) #összefűzés
a=5
b=10
print(a+b) #összeadás
print("összeg=" + str(a+b)) #str-->string konverzió
print(f"összeg={a+b}")
print(f"{a} + {b} = {a+b}") #f-string

#-------------------------------------------------
#Változónevekkel kapcsolatos szabályok:

#1péter - nem kezdődhet számmal
#péter neve - nem lehet benne szóköz
#peters'name - nem lehet benne speciális karakter, csak
                #0-9 vagy A-Z vagy a-z vagy _

#péter_neve - ez jó!  
#péter1 - ez jó!

# case sensitive - kis és nagy betűk különbözőek!
A=2
a=3 # a nem ugyanaz mint A
    #alma nem Alma
#-----------------------------------------------
#olyan változónevet válasszunk, ami utal annak tartalmára
#asd=12 TILOS!!!

#pl ezek nem jók:

#a=1 --> helyette: a_oldal=1
#d="körte"

#Péda jó megoldásra:
#Autó: típus, tulajdonos
auto_tipus='Opel'
auto_tulajdonos='Gipsz Jakab'

#megadási típusok:
auto_tipus='Opel' #snake case
autoTipus='Opel'  #camel case
AutoTipus='Opel'  #Pascal case

print('Tantárgyak:')
print('\n\tMatek') #\n egy soremelés \t egy tabulátor
print('\tTöri') #\t egy tabulátor
print('alma','körte','narancs','banán','barack',sep='-',end=' ')
print('szilva') #sep='-' elválasztó karakter megváltoztatása
                #end=' ' zárókarakter megváltoztatása
 

