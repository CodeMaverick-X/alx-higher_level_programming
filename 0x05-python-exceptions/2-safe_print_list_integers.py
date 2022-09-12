#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        for n in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            except (ValueError, TypeError):
                pass
            i = i + 1

        print()
    except IndexError:
        print()

    return (count)
