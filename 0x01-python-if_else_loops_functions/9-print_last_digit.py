#!/usr/bin/python3

def print_last_digit(number):
    rem = 0
    if number > 0:
        rem = number % 10
    elif number < 0:
        rem = (-number % 10)
    else:
        rem = 0
    print(rem, end="")
    return rem
