#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) is not 'e' or chr(i) == 'q':
        print("{}".format(chr(i)), end="")