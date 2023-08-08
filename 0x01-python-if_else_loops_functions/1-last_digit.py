#!/usr/bin/python3
import random
number = -667
if number < 0:
    digit = number % -10
elif number > 0:
    digit = number % 10
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number} and is 0")
elif digit < 6 and number != 0:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
