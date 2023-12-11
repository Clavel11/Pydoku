import numpy as np
import itertools

mat_s = np.zeros((9, 9), dtype=int)

def matrix_sudoku(index_row, index_column, digit):
    """Function to fill the predefined cells of a 9x9 matrix to a sudoku problem""""
    global mat_s
    print("Here is the Sudoku Problem :")
    for i in range(len(digit)):
        mat_s[index_row[i]][index_column[i]] = digit[i]
    printMatrix()

def printMatrix():
    """Function to print a matrix by row"""
    global mat_s
    for row in mat_s:
        print(row)

