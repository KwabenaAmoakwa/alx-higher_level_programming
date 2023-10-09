#!/usr/bin/python3

def no_c(my_string):
    if 'c' in my_string or 'C' in my_string:
        nl = []
        for i in my_string:
            if i == "c" or i == "C":
                continue
            else:
                nl += [i]
        return ('').join(nl)
    return my_string
