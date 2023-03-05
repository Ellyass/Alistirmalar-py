"""
Problem 1

CEVAP ->

print("Beden Kitle İndeksi Gİrmek İstediğiniz Kişinin Lütfen Ad Soyad Boy ve Kilosunu Giriniz")
ad = input("Adınız:")
soyad = input("Soyadınız:")
kilo = int(input("Kilonuz:"))
boy = float(input("Boyunuz:"))
bki = kilo / (boy ** 2)
print("sayın {} {}\n".format(ad,soyad))
if (bki < 18.5):
    print("Zayıfsınız")
elif (bki >= 18.5 and bki < 25):
    print("İdeal Kilodasınız")
elif (bki >= 25 and bki < 30):
    print("Fazla Kilolusunuz")
else:
    print("Obezsiniz")
"""


"""
Problem 2

CEVAP ->

print("Aralarındaki 3 sayıyı bulalım")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a > b and a > c:
    print("en büyük sayı {}".format(a))
elif b > a and b > c:
    print("en büyük sayı {}".format(b))
else:
    print("en büyük sayı {}".format(c))
  
"""


"""
Problem 3

CEVAP ->

print("Harf Notunuzu Bulalım Bulalım")

vize = int(input("vize notu:"))
final = int(input("final notu:"))

ort = (vize * 2 / 5) + (final * 3 / 5)

if ort >= 90:
    print("Harf Notunuz AA")
elif ort >= 85:
    print("Harf Notunuz BA")
elif ort >= 80:
    print("Harf Notunuz BB")
elif ort >= 75:
    print("Harf Notunuz CB")
elif ort >= 70 :
    print("Harf Notunuz CC")
elif ort >= 65:
    print("Harf Notunuz DC")
elif ort >= 60:
    print("Harf Notunuz DD")
elif ort >= 55:
    print("Harf Notunuz FD")
elif ort < 55:
    print("Harf Notunuz FF")
"""


"""
Problem 4

CEVAP ->

sekil = input("Hangi Şeklin Tipini Öğrenmek İsteriniz ?\n")

if (sekil == "Dörtgen" or sekil == "dörtgen"):
    print("Lütfen Kenarları Sırasıyla Giriniz.")
    a = int(input("Kenar 1:"))
    b = int(input("Kenar 2:"))
    c = int(input("Kenar 3:"))
    d = int(input("Kenar 4:"))

    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif (sekil == "Üçgen" or sekil == "üçgen"):
    a = int(input("Kenar 1:"))
    b = int(input("Kenar 2:"))
    c = int(input("Kenar 3:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...") 
"""
