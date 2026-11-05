import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
password = ""

length = int(input("Введите длину пароля: "))

for i in range(length):
    password += random.choice(chars)

print("Твой готовый пароль:",password)
