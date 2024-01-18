from function import *

beolv("uzemanyag.txt")

print(f"3. feldadat: Változások száma: {ossz()}")


print(f"{valtozasok[0].datum.year}")
print(f"{valtozasok[0].datum-valtozasok[1].datum}")