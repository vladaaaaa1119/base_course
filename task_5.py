a = int(input("введите число"))
b = int(input("введите число"))

if b != 0 and a % b == 0:
    print(f"делится нацело Частное: {a / b}")
elif b != 0 and a % b != 0:
    print(f"не делится нацело Частное: {a / b} остаток{a % b}")
else:
    print("Ошибка")
