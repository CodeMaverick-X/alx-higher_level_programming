#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    new_t = []
    for i in range(2):
        new_t.append(tuple_a[i] + tuple_b[i])
    new_tuple = (new_t[0], new_t[1])

    return new_tuple
