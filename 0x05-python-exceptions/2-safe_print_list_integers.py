#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        for n in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                i = i + 1
            except ValueError:
                pass
        print()
    except IndexError:
        print()

    return (i)
