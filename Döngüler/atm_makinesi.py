print("""
**********************

Atm Makinesine Hoşgeldiniz 

İşlemler;

1. İşlem -> Bakiye Sorgulama
2. İşlem -> Para Yatırma
3. İşlem -> Para Çekme

Programdan Çıkmak için 'q' ya basınız....

**********************
""")

bakiye = 1000

while True:
    islem = input("İşlem Seçiniz :")

    if islem == "q":
        print("Yine bekleriz")
        break

    elif islem == "1":
        print("Bakiyeniz {} ₺".format(bakiye))

    elif islem == "2":
        miktar = int(input("Miktar Giriniz :"))
        bakiye += miktar
        print("Bakiyeniz {} ₺".format(bakiye))

    elif islem == "3":
        cekme = int(input("Miktar Giriniz :"))

        if cekme > bakiye:
            print("Hesabınızda Çekmek istediğiniz miktarda Para Bulunmamaktadır")
            continue
        bakiye -= cekme
        print("Bakiyeniz {} ₺".format(bakiye))

    else:
        print("Geçersiz İşlem....")