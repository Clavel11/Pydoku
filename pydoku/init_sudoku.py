import numpy as np
matrix_sudoku = np.zeros((9, 9), dtype=int)

def pre_digits(matrix_sudoku, index_row, index_column, digit):
    for i in range(len(digit)):
        matrix_sudoku[index_row[i]][index_row[i]] = digit[i]
    return matrix_sudoku
