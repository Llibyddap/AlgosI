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

###
#
# Week two problem - added text import script for algodata2.txt
#
###

import time

A = tuple(map(int, [line.rstrip('\n') for line in open("./algodata2.txt")]))

def brute_count(A):
    numInv=0
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                numInv += 1
    return numInv

#A = (1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 12)
#A = (1, 3, 5, 2, 4, 6)

start = time.time()
print("Inversions: ", brute_count(A))
end = time.time()
print ("Data file: ./algodata2.txt")
print("Total list elements: ", len(A))
print("Total run time: ", end - start)

###
#
#   Output:
#
#   ('Inversions: ', 2407905288)
#   Data file: ./algodata2.txt
#   ('Total list elements: ', 100000)
#   ('Total run time: ', 293.84303402900696)
#
###