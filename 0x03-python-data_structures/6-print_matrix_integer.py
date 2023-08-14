#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 0
        for j in i:
            if count < 2:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
            count = count + 1
        if len(matrix[0]) > 0:
            print('')
