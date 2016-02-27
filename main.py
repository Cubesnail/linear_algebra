from matrix import *

matrix = Matrix()
matrix.open_matrix_file('matrix.txt')
solved_matrix = matrix.row_reduce()
solved_matrix.display_matrix()