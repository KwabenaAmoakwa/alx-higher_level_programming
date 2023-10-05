#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{} argument{}".format(len(argv) - 1, "s."))
    elif len(argv) == 2:
        print("{} argument{}".format(len(argv) - 1, ":"))
        print("{}: {}".format(len(argv) - 1, argv[1]))
    else:
        print("{} argument{}".format(len(argv) - 1, "s:"))
        c = 0
        for i in argv:
            if i != argv[0]:
                c += 1
                print("{}: {}".format(c, i))
