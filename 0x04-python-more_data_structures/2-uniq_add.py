#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    val = 0

    for i in new:
        val += i
    return val
