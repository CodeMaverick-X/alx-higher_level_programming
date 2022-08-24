#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            str[i] == chr(ord(str[i]) + 32)
        print(f"{str[i]}", end="")
    print("\n")
