## How `matrix_sudoku`function works?

`matrix_sudoku`function has three arguments: `index_row`, `index_column` and `digit`. All three are list type. 

This function initializes the sudoku matrix `mat_s` (which initially contains only zeros) with the digits corresponding to the sudoku problem we want to solve and then print the matrix. It is important to mention that the elements of `index_row` and `index_column` must be ordered and must be match the indexes of the cells where the digits of list `digit` must be placed.

Here is an example of how this function is executed

```python
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
## How `check_valid` function works?

`check_valid`function has three arguments: `row`, `column`, and `num`. All three are int type.

First, the function checks if `num` is within the `column`, and also within the submatrix, if both don't contain this `num`, the function returns `True`, but if `num` is in the `column` or the submatrix then the function returns `False`.

In particular, `square_row` and `square_column` put us in the first cell within the submatrix where is `num`.

For example, if we want to know if it is valid to put 7 in row 6 and column 7, in the previous example, we run the function:

```python
check_valid(6, 7, 7)
```
```
False
```
As we can note, is `False` because there is a 7 within the submatrix.

## How `solve_sudoku` function works?

