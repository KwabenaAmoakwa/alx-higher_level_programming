#!/usr/bin/python3

def no_c(my_string):
    if 'cC' not in my_string:
        return my_string
    nl = list(my_string)
    for i in nl:
        if i == "c" or i == "C":
            nl.remove(i)
    else:
        return my_string
    return ('').join(nl)
