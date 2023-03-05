class Dosya:

    def __init__(self):

        with open("metin.txt", "r", encoding="utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()

            self.sade_kelimeler = list()

            for kelime in kelimeler:
                kelime = kelime.strip()
                kelime = kelime.strip(".")
                kelime = kelime.strip("\n")

                self.sade_kelimeler.append(kelime)

    def kelime_bul(self, aranan):

        konumlar = list()
        say = 1
        for kelime in self.sade_kelimeler:
            if kelime == aranan:
                konumlar.append(say)

            say += 1

        if len(konumlar) != 0:
            print("{} kelimesi dosyada şuralarda geçiyor. \n{}".format(aranan, konumlar))
        else:

            print("Dosyada böyle bir kelime bulunmuyor...")

    def kelime_histogrami(self):

        kelime_frekansi = dict()
        kelime_kumesi = set()

        for kelime in self.sade_kelimeler:
            kelime_kumesi.add(kelime)
            if kelime in kelime_frekansi:
                kelime_frekansi[kelime] += 1
            else:
                kelime_frekansi[kelime] = 1
        print("Kelimelerin Frekansı........................")
        for i, j in kelime_frekansi.items():
            print("{} kelimesi metinde {} defa geçiyor.".format(i, j))

        print("Tüm Kelimeler")
        for i in kelime_kumesi:
            print(i)
            print("*************************************")


dosya = Dosya()
print("""****************

Dosya İşlemleri 

1. Tüm kelime frekansını öğren
2. Kelime Ara
Çıkmak için 'q' ya basın.
""")
while True:
    islem = input("İşlem:")

    if islem == "q":
        print("Programdan Çıkılıyor....")
        break
    elif islem == "1":
        dosya.kelime_histogrami()
    elif islem == "2":
        kelime = input("Hangi kelimeyi arıyorsunuz ?")
        dosya.kelime_bul(kelime)
    else:
        print("Geçersiz İşlem...")
