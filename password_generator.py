import random

def generate_password(length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password())
