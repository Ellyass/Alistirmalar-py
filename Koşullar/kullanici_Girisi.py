"""
Basit bir kullanıcı girişi
"""

print("""
**********************

Kullanıcı Girişi

**********************
""")

sys_kullanici_adi = "elyas"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adınızı Giriniz:")
parola = input("Parolanızı Giriniz:")

if(sys_kullanici_adi == kullanici_adi and sys_parola != parola):
    print("Şifrenizi Yanlış Girdiniz...")
elif (sys_kullanici_adi != kullanici_adi and sys_parola == parola):
    print("Kullanıcı Adınızı Yanlış Girdiniz...")
elif (sys_kullanici_adi != kullanici_adi and sys_kullanici_adi != parola):
    print("Kullanıcı Adınızı ve Şifrenizi Yanlış Girdiniz...")
else:
    print("Başarılı Bir şekilde Giriş Yaptınız.")