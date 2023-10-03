#!/usr/bin/python3

def uppercase(str):
    temp = ""
    for i in str:
        if 97 <= ord(i) <= 122 and i != " " and '0':
            temp += chr((ord(i)-97)+65)
        else:
            temp += i
    print("{}".format(temp))
