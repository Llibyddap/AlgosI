#  Bill Armstrong
#  May 2019
#  Matrix Multiplication (Brute Force) Algorithm
################################################

#  Brute Force (nested for loops) for matrix
#  multiplication.
#
#   INPUT:  n x n integer matrices X and Y
#   OUTPUT: Z = X . Y
#
#   for i := 1 to n do
#       for j := 1 to n do
#           Z[i][j] := 0
#           for k := 1 to n do
#               Z[i][j] := Z[i][j] + X[i][k] . Y[k][j]
#   return Z

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