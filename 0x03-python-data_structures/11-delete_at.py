#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    ln = len(my_list)
    if idx < 0 or idx > (ln - 1):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            del my_list[i]
