"""
Tam Bölenleri liste şeklinde bulma
"""

def tambolenlerbulma(sayi):
    tam_bolenler = []

    for i in range(2, sayi):
        if sayi % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler


while True:
    sayi = input("Sayi Giriniz : ")

    if sayi == "q":
        break

    else:
        sayi = int(sayi)
        print("Tam Bölenler : ", tambolenlerbulma(sayi))
