## How `matrix_sudoku`function works?
`matrix_sudoku`function have three arguments: `index_row`, `index_column` and `digit`. All three are list type. 
This function initialize the sudoku matrix `mat_s` (which initially contains only zeros) with the digits corresponding to the sudoku problem we want to solve. 

```
mat_s = np.zeros((9, 9), dtype=int)
index_row = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8]
index_column = [4, 7, 0, 2, 3, 7, 1, 2, 4, 7, 1, 2, 5, 0, 4, 1, 3, 5, 8, 0, 4, 6, 6, 8]
digit = [9, 2, 4, 2, 5 , 6, 5, 3, 7, 4, 7, 8, 1, 9, 5, 4, 6, 7, 2, 5, 4, 7, 1, 6]
matrix_sudoku(index_row, index_column, digit)

```
