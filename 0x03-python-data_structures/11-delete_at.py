#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    c = 0
    if 0 <= idx < len(my_list):
        for i in my_list:
            if c == idx:
                my_list.remove(i)
            c+=1
        return my_list
    return my_list
