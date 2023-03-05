"""
Kullanıcı Kaydetme
"""

print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı : ")
soyad = input ("Oyuncunun Soyadı : ")
takim = input ("Oyuncunun Takımı : ")

bilgiler = [ad,soyad,takim]

print("Bilgiler Kaydediliyor")

print("Oyuncunun adı : {}\nOyunucunun Soyadı : {}\nOyuncunun Takımı : {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi....")
