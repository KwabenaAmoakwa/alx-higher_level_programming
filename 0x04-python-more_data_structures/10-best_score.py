#!/usr/bin/python3

def best_score(a_dictionary):
    hs, hk = 0, ''
    if not a_dictionary None:
        for i in a_dictionary.keys():
            if a_dictionary[i] > hs:
                hs = a_dictionary[i]
                hk = i
    return hk if hs > 0 else None
