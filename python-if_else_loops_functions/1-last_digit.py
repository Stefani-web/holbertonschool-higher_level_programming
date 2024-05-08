#!/usr/bin/python3
import random
numb = random.randint(-10000, 10000)
last_digit = abs(numb) % 10

print("The string Last digit of", numb, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
