import random
import string

length = int(input("Enter password length: "))
count = int(input("How many passwords? "))

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = ""

    for j in range(length):
        password += random.choice(characters)

    print(f"Password {i+1}: {password}")