#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

rem = 0
if number > 0:
    rem = number % 10
elif number < 0:
    rem = -(-number % 10)
else:
    rem = 0

if rem < 6 and rem != 0:
    print(f"Last digit of {number:d} is {rem:d} and is less than 6 and not 0")
elif rem > 5:
    print(f"Last digit of {number:d} is {rem:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {rem:d} and is 0")
