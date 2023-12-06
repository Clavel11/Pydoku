"""Functions for rows"""

def options_row_4x4(matrix_s, index_row):
    """Function that determines which values within a row are non-zero"""
    options = [1,2,3,4]
    for digit in matrix_s[index_row]:
        if digit !=0:
            options.remove(digit)
    return options
