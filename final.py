import random

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('Amount of passwords to generate:')
number = int(number)

length = input('Input length of password:')
length = int(length)

print("These are your passwords. Make sure to remember them!")

def generate_password(length, count):
    passwords = []
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print (passwords)
