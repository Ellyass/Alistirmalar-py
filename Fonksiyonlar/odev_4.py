"""
Problem 1 -> Mükkemmel sayı

CEVAP ->

def mukkemmel(sayi):
    toplam = 0

    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi


for i in range(1, 1001):
    if mukkemmel(i):
        print("Mükkemmel sayi : ", i)
"""


"""
Problem 2-> Ebob 

CEVAP ->

def ebob_bulma(sayi1, sayi2):

    i = 1
    ebob = 1

    while i <= sayi1 and i <= sayi2:

        if not (sayi1 % i) and not (sayi2 % i):
            ebob = i
        i += 1
    return ebob


sayi_1 = int(input("1.ci Sayıyı giriniz :"))
sayi_2 = int(input("2.ci Sayıyı giriniz :"))

print("Ebob", ebob_bulma(sayi_1, sayi_2))
"""


"""
Problem 3->Ekok 

CEVAP ->

def ekok_bulma(sayi1, sayi2):

    ekok = 1
    i = 2

    while True:
        if sayi1 % i == 0 and sayi2 % i == 0:
            ekok *= i

            sayi1 //= i
            sayi2 //= i

        elif sayi1 % i == 0 and sayi2 % i != 0:
            ekok *= i

            sayi1 //= i

        elif sayi1 % i != 0 and sayi2 % i == 0:
            ekok *= i

            sayi2 //= i
        else:
            i += 1
        if sayi1 == 1 and sayi2 == 1:
            break
    return ekok


sayi_1 = int(input("1.ci Sayıyı giriniz:"))
sayi_2 = int(input("2.ci Sayıyı giriniz:"))

print("Ekok :", ekok_bulma(sayi_1, sayi_2))
"""

"""
Problem 4 -> Sayıyı yazıya döndürme

CEVAP ->

Birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
Onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10

    return Onlar[ikinci]+" "+Birler[birinci]


sayi = int(input("Sayi Giriniz:"))
print("Sayınız ->", okunus(sayi))
"""


"""
Problem 5 -> Pisagor Üçgenleri

CEVAP ->

def pisagor_bulma():
    pisagor_listesi = list()

    for a in range(1, 101):
        for b in range(1, 101):
            c = (a ** 2 + b ** 2) ** 0.5
            if c == int(c):
                pisagor_listesi.append((a, b, int(c)))
    return pisagor_listesi


for i in pisagor_bulma():
    print(i)
"""