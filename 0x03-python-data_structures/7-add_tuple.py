#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    [tuple_a1, tuple_b1] = [[], []]

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        [tuple_a1, tuple_b1] = [list(tuple_a), list(tuple_b)]
    elif len(tuple_a) >= 2 and len(tuple_b) != 2:
        tuple_a1 = list(tuple_a)
        tuple_b1 = [tuple_b[0], 0] if len(tuple_b) > 0 else [0, 0]
    elif len(tuple_b) >= 2 and len(tuple_a) != 2:
        tuple_b1 = list(tuple_b)
        tuple_a1 = [tuple_a[0], 0] if len(tuple_a) > 0 else [0, 0]
    else:
        tuple_a1 = [tuple_a[0], 0] if len(tuple_a) > 0 else [0, 0]
        tuple_b1 = [tuple_b[0], 0] if len(tuple_b) > 0 else [0, 0]
    return tuple_a1[0] + tuple_b1[0], tuple_a1[1] + tuple_b1[1]
