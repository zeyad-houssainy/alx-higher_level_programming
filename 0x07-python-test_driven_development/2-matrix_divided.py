#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    #check matrix is list
    if not (type(matrix) is list) or not (all(type(i) is list for i in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    #check if list lenght are equal:
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    #check if div is integer or float
    if not (type(div) is int or type(div) is float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    for i in range(len(matrix)):
        new_matrix.append([])
        for k in range(len(matrix[i])):
            # x = 
            new_matrix[i][k] = (new_matrix[i]).append(round((matrix[i][k] / 3)), div)
            # new_matrix[i][k] = round(x, 2)
    print(f"new matrix is: {new_matrix}")
    print(f"Original matrix is: {matrix}")
    print(id(matrix))
    print(id(new_matrix))
    print(matrix is new_matrix)
    return (new_matrix)
    
    
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
# print(matrix_divided(matrix, 3))
# print(matrix)
matrix_divided(matrix, 3)
