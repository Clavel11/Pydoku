"""Functions for columns"""

def search_in_column(M, index_column):
    """Function that determines which values within a column are non-zero"""
    op_column = []
    for i in range(9):
        if M[i][index_column] != 0:
            op_column.append(M[i][index_column])
    return op_column
