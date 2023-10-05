#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    c = 0
    for i in argv:
        if i != argv[0]:
            c += int(i)
    print("{}".format(c))
