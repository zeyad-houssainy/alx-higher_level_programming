#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 0
        for j in i:
            if count < 2:
                print(j, end=" ")
            else:
                print(j, end="")
            count = count + 1
        print('')
