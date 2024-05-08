import random

length = int(input("Enter character amount: "))

def passw(length):
    password = ""
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*();:<>'
    for i in range(length):
        password += random.choice(char)
    return password

password = passw(length)

print('Your password is: ',password)