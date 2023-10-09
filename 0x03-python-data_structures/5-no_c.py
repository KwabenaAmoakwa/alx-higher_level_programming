#!/usr/bin/python3

def no_c(my_string):
    if 'c' in my_string or 'C' in my_string:
        nl = list(my_string)
        for i in nl:
            if i == "c" and i == "C":
                nl.remove(i)
        return ('').join(nl)
    return my_string
