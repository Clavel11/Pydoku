"""Functions for columns"""

def options_column(matrix_s, index_column):
    """Function that determines the options within a column"""
    options = [1,2,3,4]
    for digit in matrix_s[:,index_column]:
        if digit !=0:
            options.remove(digit)
    return options
