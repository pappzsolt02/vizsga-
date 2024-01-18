from function import *

beolv("eredmenyek.txt")

print(f"3. feladat: Real Madrid: Hazai: {real_hazai('Real Madrid')}, Idegen: {real_idegen('Real Madrid')}")

if dontetlen():
    print("4. feladat Volt döntetlen? nem")

print("6. feladat:")
ossz_csap("2004-11-21")