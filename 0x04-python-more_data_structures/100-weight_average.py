#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0
    det = sum([ i[1] for i in my_list])
    av = sum([i[0] * i[1] for i in my_list]) / det
    return av   
