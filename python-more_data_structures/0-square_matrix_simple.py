#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Ensure the input matrix is not modified
    new_matrix = []
    for row in matrix:
        # Compute the square of each element in the row
        squared_row = [x**2 for x in row]
        new_matrix.append(squared_row)
    return new_matrix
