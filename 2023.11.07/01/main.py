from tavolugras import * 

eredmenyek=[]

volt_legalabb_3_ervenytelen=False

for i in range(12):
    ugrasok=ugrasok_generalasa()
    print_egy_versenyzo(i+1,ugrasok)
    eredmenyek.append(versenyzo_legjobb_ugrasa(ugrasok))
    if ervenytelen_ugrasok_szama(ugrasok)>=3:
        volt_legalabb_3_ervenytelen=True

print(f"A győztes versenyző rajtszáma: {gyoztes(eredmenyek)}")

#Van-e olyan versenyző, akinek legalább 3 érvénytelen egrása volt? 
if volt_legalabb_3_ervenytelen:
    print("Van olyan versenyző, akinek legalánn 3 érvénytelen ugrása volt.")
else:
    print("Nincs olyan versenyző, akinek legalánn 3 érvénytelen ugrása volt.")