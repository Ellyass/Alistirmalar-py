print("""
**********************

Faktoriyel Programı 

Programdan Çıkmak için 'q' ya basınız....

**********************
""")

while True:

    sayi = input("Sayı : ")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for a in range(2, sayi + 1):
            faktoriyel *= a
        print("Faktoriyel :", faktoriyel)