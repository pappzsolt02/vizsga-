ma_ev=2023
ma_honap=9
ma_nap=12

szul_datum=input('Születési dátum (éééé.hh.nn): ')
(szul_ev,szul_honap,szul_nap)=szul_datum.split('.')
szul_ev=int(szul_ev)
szul_honap=int(szul_honap)
szul_nap=int(szul_nap)
elmult_18=False

if ma_ev-szul_ev>18:
    elmult_18=True
elif ma_ev-szul_ev==18:
    if ma_honap>szul_honap:
        elmult_18=True
    elif ma_honap==szul_honap:
        if ma_nap>=szul_nap:
            elmult_18=True
        
if elmult_18==True:
    print('Vehet már alkoholt')
else:
    print('Nem múlt el még 18. Nem vehet még alkoholt')