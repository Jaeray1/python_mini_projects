import random, string
length = int(input("Enter length: "))
chars = string.ascii_letters + string.digits + "!@#$%^&*"
print("Password:", "".join(random.choice(chars) for _ in range(length)))
