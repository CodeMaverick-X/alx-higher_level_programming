#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    av_len = len(argv) - 1
    if av_len == 1:
        print("{} argument:".format(av_len))
    elif av_len > 1:
        print("{} arguments:".format(av_len))

    if av_len >= 2:
        j = 0
        for i in argv:
            j = j + 1
            if j > 1:
                print("{}: {}".format(j - 1, i))
    if av_len == 0:
        print(".")
