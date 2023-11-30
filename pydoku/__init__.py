import numpy as np
mat_sudoku = np.zeros((9, 9), dtype=int)
def matrix_sudoku(index_row, index_column, digit):
    for i in range(len(digit)):
        mat_sudoku[index_row[i]][index_column[i]] = digit[i]
    return mat_sudoku

from pydoku import pre_digits
