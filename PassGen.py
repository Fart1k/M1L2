import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    nums = int(input('Длина пароля: '))
    password = ""
    for i in range(nums):
        password += random.choice(symbols)
    print(password)
