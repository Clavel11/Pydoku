## How `matrix_sudoku`function works?

`matrix_sudoku`function has three arguments: `index_row`, `index_column` and `digit`. All three are list type. 

This function initializes the sudoku matrix `mat_s` (which initially contains only zeros) with the digits corresponding to the sudoku problem we want to solve and then print the matrix. It is important to mention that the elements of `index_row` and `index_column` must be ordered and must be match the indexes of the cells where the digits of list `digit` must be placed.

Here is an example of how this function is executed

```python
import numpy as np
import itertools

def printMatrix():
    global mat_s
    for row in mat_s:
        print(row)

def matrix_sudoku(index_row, index_column, digit):
    global mat_s
    print("Here is the Sudoku Problem :")
    for i in range(len(digit)):
        mat_s[index_row[i]][index_column[i]] = digit[i]
    printMatrix()

mat_s = np.zeros((9, 9), dtype=int)
index_row = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8]
index_column = [4, 7, 0, 2, 3, 7, 1, 2, 4, 7, 1, 2, 5, 0, 4, 1, 3, 5, 8, 0, 4, 6, 6, 8]
digit = [9, 2, 4, 2, 5 , 6, 5, 3, 7, 4, 7, 8, 1, 9, 5, 4, 6, 7, 2, 5, 4, 7, 1, 6]
matrix_sudoku(index_row, index_column, digit)
```
```
Here is the Sudoku Problem :
[0 0 0 0 9 0 0 2 0]
[4 0 2 5 0 0 0 6 0]
[0 5 3 0 7 0 0 4 0]
[0 7 8 0 0 1 0 0 0]
[9 0 0 0 5 0 0 0 0]
[0 4 0 6 0 0 0 0 0]
[0 0 0 0 0 7 0 0 2]
[5 0 0 0 4 0 7 0 0]
[0 0 0 0 0 0 1 0 6]
```
