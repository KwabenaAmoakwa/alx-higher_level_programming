#!/usr/bin/python3

def fizzbuzz():
    temp = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            temp += "Fizz "
        elif i % 3 != 0 and i % 5 == 0:
            temp += "Buzz "
        elif i % 3 == 0 and i % 5 == 0:
            temp += "FizzBuzz "
        else:
            temp += str(i) + " "
    print(temp, end="")
