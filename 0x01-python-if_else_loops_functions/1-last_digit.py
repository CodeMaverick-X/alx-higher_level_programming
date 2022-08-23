#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num1 = number % 10
else:
    num1 = ((number * -1) % 10) * -1
if num1 > 5:
    print(f"Last digit of {number} is {num1} and is greater than 5")
elif num1 == 0:
    print(f"Last digit of {number} is {num1} and is 0")
elif num1 < 6 and num1 != 0:
    print(f"Last digit of {number} is {num1} and is less than 6 and not 0")
