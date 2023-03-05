import random
import time

print("""
**************************************
Sayı Tahmin Oyunu 
1 - 100 arasındaki bir sayı tahmin etmeye çalışın 
İyi Şanslar 
**************************************
""")

rasgele_sayi = random.randint(1, 100)
tahmin_hakki = 5

while True:
    time.sleep(1)
    tahmin = int(input("Tahmininiz:"))

    if tahmin < rasgele_sayi:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(2)

        print("Daha Büyük bir sayı tahmin etmelisiniz....")
        tahmin_hakki -= 1


    elif tahmin > rasgele_sayi:
        print("Bİlgiler Sorgulanıyor....")
        time.sleep(2)

        print("Daha Küçük bir sayı tahmin etmelisiniz....")
        tahmin_hakki -= 1

    else:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(2)

        print("Tebrikler Doğru Tahmin Ettiniz Sayımız:", rasgele_sayi)

        break

    if tahmin_hakki == 0:
        print("Tahmin Hakkınız Bitmiştir Bir Daha ki Sefere Bol Şans....")
        print("Sayımız:", rasgele_sayi)
        break
