#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    chr(i)
    print("{:c}".format(i), end="")
