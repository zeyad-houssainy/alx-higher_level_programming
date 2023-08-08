#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if x == 9 and i == 9:
            print("{}{}".format(i, x), end="")
            continue
        print("{}{}, ".format(i, x), end="")
