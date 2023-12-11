"""Function for rows"""

mat_s = np.zeros((9, 9), dtype=int)

def options_row(index_row):
    """Function to search digits that are not in a specific row"""
    global mat_s
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for digit in mat_s[index_row]:
        if digit !=0:
            options.remove(digit)
    return options

