#!/usr/bin/python3

def search_replace(my_list, search, replace):
    nl = [i if i != search else replace for i in my_list]
    return nl
