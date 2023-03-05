print("""
**********************

Kullanıcı Giriş Programı

**********************
""")

sys_kullanici_girisi = "elyas"
sys_parola = "112233"

giris_hakki = 3

while True:
    kullanici_girisi = input("Kullanıcı Girişi : ")
    parola = input("Parola : ")

    if (sys_kullanici_girisi == kullanici_girisi and sys_parola != parola):
        print("Parolanızı Hatalı Girdiniz....")
        giris_hakki -=1
    elif (sys_kullanici_girisi != kullanici_girisi and sys_parola == parola):
        print("Kullanıcı Adınızı Hatalı Girdiniz....")
        giris_hakki -= 1
    elif (sys_kullanici_girisi != kullanici_girisi and sys_parola != parola):
        print("Kullanıcı Adınızı ve Şifrenizi Hatalı Girdiniz....")
        giris_hakki -= 1
    else:
        print("Sisteme Başarılı Bir Şekilde Giriş Yaptınız....")
        break

    if(giris_hakki == 0):
        print("Giriş Hakkınız Kalmamıştır....")
        break