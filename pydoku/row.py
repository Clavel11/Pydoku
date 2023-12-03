"""Function that determines which values within a row are non-zero"""

def search_in_row(M, index_row):
    op_row = []
    for i in range(9):
        if M[index_row][i] != 0:
            op_row.append(M[index_row][i])
    return op_row
