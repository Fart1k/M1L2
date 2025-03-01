import random
engSymbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ruSymbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890+-/*!&$#?=@"
password = ""
while True:
    password = ""
    nums = int(input('Длина пароля: '))
    type = input("Русский, Английский, всё вместе? (1/2/3): ") 
    if type == "1":
        for i in range(nums):
            password += random.choice(ruSymbols)
        print(password)
    elif type == "2":
        for i in range(nums):
            password += random.choice(engSymbols)
        print(password)
    elif type == "3":
        for i in range(nums):
            password += random.choice(engSymbols + ruSymbols)
        print(password)
    else:
        print("Неверный ввод")

    
