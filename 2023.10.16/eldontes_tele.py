szamok=[10,26,33,12,3]
print(szamok)

#v1
index=0
while (index<len(szamok) and (szamok[index]%13!=0)):
    index+=1
if index==len(szamok):
    print("Nincs 13-mal oszható eleme a listában!")
else:
    print("Van 13-mal oszható eleme a listában!")

#v2
#csak pythonban 
for szam in szamok:
    if szam%13==0:
        print("Van 13-mal oszható eleme a listában!")
        break
else:
    print("Nincs 13-mal oszható eleme a listában!")
