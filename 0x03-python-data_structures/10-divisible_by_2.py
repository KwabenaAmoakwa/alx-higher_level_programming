#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bol = []
    if len(my_list) > 0:
        for i in my_list:
           bol += [True] if i%2 == 0 else [False]
        return bol
    return None
