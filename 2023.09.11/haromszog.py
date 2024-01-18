import math
a_oldal=int(input('Adja meg "a" háromszög a oldalát'))
b_oldal=int(input('Adja meg "b" háromszög a oldalát'))
c_oldal=int(input('Adja meg "c" háromszög a oldalát'))

if ((a_oldal+b_oldal)>c_oldal) and ((b_oldal+c_oldal)>a_oldal) and ((a_oldal+c_oldal)>b_oldal):
    kerulet=a_oldal+b_oldal+c_oldal
    print(f"A háromszög kerülete: {kerulet}")
    s=kerulet/2
    terulet=math.sqrt(s*(s-a_oldal)*(s-b_oldal)*(s-c_oldal))
    print(f"A háromszög területe: {terulet:.3f}")# itt nem .:f2 hanem :.2f
    print(f"A háromszög területe: {round(terulet,3)}")   
else:
    print('A háromszög nem megszerkeszthető!')

