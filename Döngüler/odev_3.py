"""
Problem 1 ;

CEVAP ->

sayi = int(input("Sayı Giriniz :"))

i = 1
toplam = 0

while i < sayi:
    if sayi % i == 0:
        toplam += i
    i += 1
if toplam == sayi:
    print(sayi, "Mükkemmel bir sayıdır")
else:
    print(sayi, "Mükkemmel bir sayı değlidir")
"""

"""
Problem 2 ;

CEVAP ->

sayi = input("Sayı Giriniz :")
basamak_sayisi = len(sayi)
sayi = int(sayi)
toplam = 0
basamak = 0
gecici_sayi = sayi

while gecici_sayi > 0:
    basamak = gecici_sayi % 10
    toplam += basamak ** basamak_sayisi
    gecici_sayi //= 10

if toplam == sayi:
    print(sayi, "Armstrong Sayısıdır")
else: 
    print(sayi, "Armstrong Sayısı Değildir")
"""

"""
Problem 3 ;

CEVAP ->

for i in range(1, 11):
    print("*************************************************")
    for k in range(1, 11):
        print("{} x {} = {}".format(i, k, i*k))
"""

"""
Problem 4;

CEVAP ->

toplam = 0

while True:

    sayi = input("Sayı Giriniz :")

    if sayi == "q":
        break
    sayi = int(sayi)
    toplam += sayi
print("Girmiş olduğunuz sayıların toplamı : {}".format(toplam))
"""

"""
Problem 5;

CEVAP ->

for i in range(1, 101):
    if(i % 3 !=0):
        continue
    print(i)
"""

"""
Problem 6;

CEVAP ->

liste = [x for x in range(1, 101) if x % 2 == 0]
print(liste)
"""