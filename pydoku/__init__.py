import numpy as np

def matrix_sudoku(index_row, index_column, digit):
    mat_sudoku = np.zeros((9, 9), dtype=int)
    for i in range(len(digit)):
        mat_sudoku[index_row[i]][index_column[i]] = digit[i]
    return mat_sudoku
