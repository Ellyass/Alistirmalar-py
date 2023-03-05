"""
Basit bir hesap makinesi
"""

print("""
**********************
Basit Hesap Makinesi 

1. Toplama İşlemi 

2. Çıkarma İşlemi 

3. Çarpma İşlemi

4. Bölme İşlemi
**********************
""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

islem = int(input("İşlem seçiniz:"))

if islem == 1:
    print("{} ile {} Sayıalarının Toplamı {}".format(a, b, a + b))
elif islem == 2:
    print("{} ile {} Sayıalarının Farkı {}".format(a, b, a - b))
elif islem == 3:
    print("{} ile {} Sayıalarının Çarpımı {}".format(a, b, a * b))
elif islem == 4:
    print("{} ile {} Sayıalarının Bölümü {}".format(a, b, a / b))
else:
    print("Geçersiz İşlem...")
