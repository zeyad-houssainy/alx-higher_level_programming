#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_key = sorted([x for x in a_dictionary.keys() ])
    for i in list_key:
        print("{}: {}".format(i , a_dictionary[i]))
