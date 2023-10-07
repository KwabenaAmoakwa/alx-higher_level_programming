#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for i in matrix:
            if len(i) > 0:
                print("{:d}".format(i[0]), end="")
                for x in range(1, len(i)):
                    print(" {:d}".format(i[x]), end="")
            print("{}".format(''))
    else:
        print("{}".format(''))
