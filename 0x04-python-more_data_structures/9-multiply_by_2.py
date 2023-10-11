#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    nd = dict()
    for i in a_dictionary.keys():
        nd[i] = a_dictionary[i]*2
    return nd
