"""Functions for rows"""

def search_in_row(M, index_row):
    """Function that determines which values within a row are non-zero"""
    op_row = []
    for i in range(9):
        if M[index_row][i] != 0:
            op_row.append(M[index_row][i])
    return op_row

def options_row(matrix_s, num_row):
    options = [1,2,3,4,5,6,7,8,9]
    for digit in matrix_s[num_row]:
        if digit !=0:
            options.remove(digit)
    return options

def options_row_4x4(matrix_s, num_row):
    options = [1,2,3,4]
    for digit in matrix_s[num_row]:
        if digit !=0:
            options.remove(digit)
    return options
