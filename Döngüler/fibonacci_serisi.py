a = 1
b = 1
sayi = int(input("Sayi Giriniz :"))
fibonacci = [a, b]

for i in range(sayi):
    a, b = b, a + b

    fibonacci.append(b)

print(fibonacci)
