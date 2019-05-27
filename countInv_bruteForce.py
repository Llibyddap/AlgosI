#  Bill Armstrong
#  May 2019
#  Linear Inversion (Brute Force) Algorithm
###########################################

#  Brute-Force Search for Counting Inversions
#
#  Roughgarden, Section 3.2.4
#
#   INPUT:   array A of n distinct integers
#   OUTPUT:  the number of inversions of A
#
#   numInv := 0
#   for i := 1 to n - 1 do
#       for j := i + 1 to n do
#           if A[i] > A[j] then
#               numInv := numInv + 1
#   return numInv


def brute_count(A):
    numInv=0
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                numInv += 1
    return numInv

#A = (1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 12)
A = (1, 3, 5, 2, 4, 6)

print("Brute Force Count: ", brute_count(A))
