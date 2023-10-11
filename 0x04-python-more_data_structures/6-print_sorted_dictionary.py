#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    li = list(a_dictionary.keys())
    li.sort()
    for i in range(len(li)):
        print("{}: {}".format(li[i], a_dictionary[li[i]]))
