#!/usr/bin/python3

def no_c(my_string):
    if not my_list:
        return
    nl = list(my_string)
    if 'c' in nl:
        for i in nl:
            if i == "c" or i == "C":
                nl.remove(i)
    else:
        return my_string
    return ('').join(nl)
