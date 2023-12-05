"""Function that becomes a matrix full of zeros to a sudoku matrix"""

import numpy as np

mat_sudoku = np.zeros((9, 9), dtype=int)

def matrix_sudoku(index_row, index_column, digit):
    for i in range(len(digit)):
        mat_sudoku[index_row[i]][index_column[i]] = digit[i]
    return mat_sudoku

mat_sudoku_4x4 = np.zeros((4, 4), dtype=int)

def matrix_sudoku_4x4(index_row, index_column, digit):
    for i in range(len(digit)):
        mat_sudoku_4x4[index_row[i]][index_column[i]] = digit[i]
    return mat_sudoku_4x4
