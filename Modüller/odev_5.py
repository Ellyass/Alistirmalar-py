"""
Problem 1 -> Gelişmiş Hesap Makinesi

CEVAP ->
"""


import math
import time
from math import *


def toplama(a, b):
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    return a + b


def cikarma(a, b):
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    return a - b


def carpma(a, b):
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    return a * b


def bolme(a, b):
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    return a / b



def karealma():
    kare_al = float(input("Karesi Alınacak Sayı:"))
    karesi = kare_al ** 2
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    print(karesi)



def kupalma():
    kup_al = float(input("Küpü Alınacak Sayı:"))
    kupu = kup_al ** 3
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    print(kupu)



def hipotenus():
    f_dik = float(input("1. Dik Kenar:"))
    s_dik = float(input("2. Dik Kenar:"))

    hip = ((f_dik ** 2) + (s_dik ** 2)) ** 0.5
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    print(hip)



def karakok():
    karekok = float(input("Karakök'ünü Bulmak İstediğiniz Sayı:"))
    kok = math.sqrt(karekok)
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    print(kok)



def usalma():
    a = int(input("Tabanı Giriniz:"))
    b = int(input("Üssü Giriniz:"))
    x = math.pow(a, b)
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    print(x)


def logalma():
    a = int(input("Tabanı Giriniz:"))
    b = int(input("Üssü Giriniz:"))
    x = math.log(a, b)
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    print(x)


def radyan():
    a = int(input(" radyanı giriniz:"))
    x = math.radians(a)
    print("İşleminiz Yapılıyor")
    time.sleep(1)
    print(x)


def sinus():
    secim = input("Radyan için = R , Derece için = D Seçiniz")
    if secim == "R" or secim == "r":
        a = int(input("Radyanı Giriniz:"))
        x = math.sin(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Sinüs {} = {}".format(a, x))

    elif secim == "D" or secim == "d":
        a = int(input("Derece'yi Giriniz:"))
        x = math.sin(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Sinüs {} = {}".format(a, x))


def cosinus():
    secim = input("Radyan için = R , Derece için = D Seçiniz")
    if secim == "R" or secim == "r":
        a = int(input("Radyanı Giriniz:"))
        x = math.cos(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Cosinüs {} = {}".format(a, x))

    elif secim == "D" or secim == "d":
        a = int(input("Derece'yi Giriniz:"))
        x = math.cos(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Cosinüs {} = {}".format(a, x))


def tanj():
    secim = input("Radyan için = R , Derece için = D Seçiniz")
    if secim == "R" or secim == "r":
        a = int(input("Radyanı Giriniz:"))
        x = math.tan(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Tanjant {} = {}".format(a, x))

    elif secim == "D" or secim == "d":
        a = int(input("Derece'yi Giriniz:"))
        x = math.tan(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Tanjant {} = {}".format(a, x))


def cot():
    secim = input("Radyan için = R , Derece için = D Seçiniz")
    if secim == "R" or secim == "r":
        a = int(input("Radyanı Giriniz:"))
        x = math.cos(a) / math.sin(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Cotanjant {} = {}".format(a, x))

    elif secim == "D" or secim == "d":
        a = int(input("Derece'yi Giriniz:"))
        x = math.cos(a) / math.sin(a)
        print("İşleminiz Yapılıyor")
        time.sleep(1)
        print("Cotanjant {} = {}".format(a, x))


print(
    "**********************\n"
    "HESAP MAKİNESİ PROGRAMI\n"
    "LÜTFEN İŞLEM SEÇİN\n"
    "1. İşlem = Toplama\n"
    "2. İşlem = Çıkarma\n"
    "3. İşlem = Çarpma \n"
    "4. İşlem = Bölme\n"
    "5. İşlem = Kare Alma\n"
    "6. İşlem = Küp Alma\n"
    "7. İşlem = Hipotenüs\n"
    "8. İşlem = KareKök\n"
    "9. İşlem = Faktoriyel\n"
    "10. İşlem = Üs Alma\n"
    "11. İşlem = Logaritma\n"
    "12. İşlem = Radyanı Dereceye Çevirme\n"
    "13. İşlem = Sinüs'ü Bulma\n"
    "14. İşlem = Cosinüs'ü Bulma\n"
    "15. İşlem = Tanjant'ı Bulma\n"
    "16. İşlem = Cotanjant'ı Bulma"
)


while True:
    islem = input("İşlem Seçiniz:")
    if islem == "q":
        time.sleep(1)
        print("Çıkış Yaptınız İyi Günler....")
        break
    elif islem == "1":
        a = int(input("Birinci Sayı:"))
        b = int(input("İkinci Sayı:"))
        print(toplama(a, b))
    elif islem == "2":
        a = int(input("Birinci Sayı:"))
        b = int(input("İkinci Sayı:"))
        print(cikarma(a, b))
    elif islem == "3":
        a = float(input("Bİrici Sayı:"))
        b = float(input("İkinci Sayı:"))
        print(carpma(a, b))
    elif islem == "4":
        a = float(input("Bİrici Sayı:"))
        b = float(input("İkinci Sayı:"))
        print(bolme(a, b))
    elif islem == "5":
        karealma()
    elif islem == "6":
        kupalma()
    elif islem == "7":
        hipotenus()
    elif islem == "8":
        karakok()
    elif islem == "9":
        faktoriyel = int(input("Faktöriyel'i Alınacak SAyıyı Giriniz:"))
        faktoriyel_sonuc = factorial(faktoriyel)
        time.sleep(1)
        print(faktoriyel_sonuc)
    elif islem == "10":
        usalma()
    elif islem == "11":
        logalma()
    elif islem == "12":
        radyan()
    elif islem == "13":
        sinus()
    elif islem == "14":
        cosinus()
    elif islem == "15":
        tanj()
    elif islem == "16":
        cot()

    else:
        print("Geçersiz İşlem")
        time.sleep(1)
        break

