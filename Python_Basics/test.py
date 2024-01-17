import random

print("Think of a number...")

l = [1,2,3,4,5,6,7,8,9,10]

print(f'Is this the number you guessed {random.choice(l)}')
u = input('Yes / No?')

while u != 'y':
    print(f'Is this the number you guessed {random.choice(l)}')
    u = input('Yes / No?')

print('I did it')