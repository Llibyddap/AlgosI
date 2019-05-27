#  Bill Armstrong
#  May 2019
#  Matrix Multiplication (Recursive) Algorithm
################################################

#  Recursive (8 matrix products) for matrix
#  multiplication.
#
#    INPUT:  n x n integer matrices X and Y
#    OUTPUT: Z = X . Y
#    ASM:    n is a power of 2
#
#    if n = 1 then
#         return the 1 x 1 matrix with \
#              entry X[1][1] . Y[1][1]
#    else
#         A, B, C, D := submatrices of X as in \
#              matrixMult-bruteForce.py
#         E, F, G, H := submatrices of Y as in \
#              matrixMult-bruteForce.py
#         recursively compute teh eight matrix products
#         return the result
#   

X = [[1, 2, 3],
     [4 ,5, 6],
     [7 ,8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

Z = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           Z[i][j] = Z[i][j] + X[i][k] * Y[k][j]

for r in Z:
   print(r)