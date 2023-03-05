"""
Problem 1(Girilen 3 SAyıyı Çarpma)

CEVAP ->

print("Lütfen Çarpmak İstediğiniz 3 Tane Sayıyı Sırayla Giriniz....")
x = int(input("Sayı 1 : "))
y = int(input("Sayı 2 : "))
z = int(input("Sayı 3 : "))
print("Girmiş Olduğunuz Sayılar Çarpılıyor....")
carp = x * y * z
print("Girmiş olduğunuz Sayıların Çarpımı : {}\n".format(carp))
"""


"""
Problem 2(Vucit Kitle Endeksini bulma)

CEVAP ->

print("Beden Kitle İndeksi Gİrmek İstediğiniz Kişinin Lütfen Ad Soyad Boy ve Kilosunu Giriniz")
ad = input("Adınız : ")
soyad = input("Soyadınız : ")
kilo = int(input("Kilonuz : "))
boy = int(input("Boyunuz : "))
vki = kilo / (boy * boy)
print("sayın\n{} {}\n".format(ad,soyad))
print("Vucüt Kitle Endeksiniz Hesaplanmıştır : {}\n".format(vki))
"""


"""
Problem 3 (Ne kadar yakıt Alması gerekiyor)

CEVAP ->

print("Gideceğiniz Yolda Ne kadar Yakıt Lazım Bırakın Biz Hesaplayalım.... ")

arac = input("Aracınızın Markası : ")
model = input("Aracınızın Modeli : ")
yakma = float(input("100 km 'de kaç Lt Yakıt Yakıyor : "))
km = float(input("Gideceğiniz Yol Kaç Kilometre : "))
yakit = float(input("Güncel Yakıt Fiyatı :  "))

hesap = (km * yakma) / 100
odeme = hesap * yakit

print("{} {} Model Aracanıza Gideceğiniz Yolda '{} LT' Yakıt Lazım\n".format(arac,model,hesap))
print("Alacağınız Yakıt Tutarı :{}₺\n ".format(odeme))
"""


"""
Problem 4 (Hipotenüs Bulma)

CEVAP ->

import math

print("Dik olan 2 kenarın uzunluklarını giriniz...")
a = float(input("Dik olan 1. Kenar : "))
b = float(input("Dik olan 2. Kenar : "))

hipotenus = a ** 2  + b ** 2
print("Girilen Kenarların Hipotenüsü : {}\n".format(math.sqrt(hipotenus)))
"""






