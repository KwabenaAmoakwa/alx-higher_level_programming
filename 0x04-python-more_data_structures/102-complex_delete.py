#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    li = list(a_dictionary.keys())
    for key in li:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
