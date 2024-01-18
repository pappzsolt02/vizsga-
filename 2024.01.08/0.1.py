#kérjünk be ellenőrzöttrn 3 érttéket (a,b,c)
#a: 20-40
#b: 30-80
#c: 20-60
# Mennyi a háromszög kerülete?

print("Adja meg a hárómszög oldalait!")

a=0
while a<20 or a>40:
    a=int(input("a (20-40)= "))
b=0
while b<30 or b>80:
    b=int(input("b (30-80)= "))
c=0
while c<20 or c>60:
    c=int(input("a (20-60)= "))

print(f"Kerület = {a+b+c}")    

print(f"{a}:{str(b).zfill(2)}:{c}")