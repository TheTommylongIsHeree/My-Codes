import random



while True:
    password_length = int(input("Password length: "))
    try:
        password_length -= 1
        password_length += 1
        break
    except ValueError:
        print("Invalid number!")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

for i in range 100:
	word = list(characters)
	random.shuffle(word)
print(word)

password = ""   

for _ in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))
