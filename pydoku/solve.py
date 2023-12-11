"""Functions to solve a sudoku"""

def checkValidFunc(row, column, num):
  """Auxiliary function to check if the digit to be assigned is not repeated in the column and in the 3x3 submatrix"""
    global mat_s
    for i in range(0, 9):
        if mat_s[row][i] == num:
            return False
    for i in range(0, 9):
        if mat_s[i][column] == num:
            return False
    square_row = (row // 3) * 3
    square_col = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if mat_s[square_row + i][square_col + j] == num:
                return False
    return True
