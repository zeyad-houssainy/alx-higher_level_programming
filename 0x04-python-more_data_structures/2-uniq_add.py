#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    for i in set(my_list):
        x = x + i
    return (x)
