#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list2 = my_list.copy()
        my_list2[idx] = element
        return my_list2
    return my_list.copy()
