def osszead(a:float,b:float) -> float:
    #print(a+b) nem kiírni szeretnénk, hanem visszaadni
    return a+b
    #ami a return után van az nem fut le!
    print("Ezt soha nem látjuk!")

print(f'Összeg: {osszead(2,3)}')


x=float(input("Első szám: "))
y=float(input("Második szám: "))
print(f"{x}+{y}={osszead(x,y)}")