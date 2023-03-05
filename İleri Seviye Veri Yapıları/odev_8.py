"""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.


CEVAP ->

s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for karakter in s:
    if karakter in frekans:
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i, j in frekans.items():
    print(i, ":", j)
"""


"""
Problem 2
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.


CEVAP ->

bas_harfler = ""
with open("şiir.txt", "r", encoding = "utf-8") as file:
    for satir in file:
        bas_harfler += satir[0]
print(bas_harfler)
"""


"""
Problem 3
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.


CEVAP ->             

with open("mailler.txt", "r", encoding="utf-8") as file:
    for satir in file:
        satir = satir[:-1]
        if (satir.endswith(".com") and satir.find("@") != -1):
            print(satir)
"""


"""
Problem 4
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri *isimlere* göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]


CEVAP ->

isim = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisim = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

liste = list(zip(isim, soyisim))
liste.sort()
for i, j in liste:
    print(i, j)
"""