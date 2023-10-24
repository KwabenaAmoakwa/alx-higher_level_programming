#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    try:
        for i in range(list_length):
            try:
                nl += [my_list_1[i] / my_list_2[i]]
            except ZeroDivisionError:
                nl += [0]
                print("division by 0")
            except TypeError:
                nl += [0]
                print("wrong type")
    except IndexError:
        nl += [0]
        print("out of range")
    finally:
        return nl
