#  Bill Armstrong
#  May 2019
#  Linear Inversion (Recursive) Algorithm
###########################################

#  Recursive Search for Counting Inversions
#
#  Roughgarden, Section 3.2.6 - 3.2.10
#
#   Sort-and-CountInv Definition
#
#   INPUT:   array A of n distinct integers
#   OUTPUT:  sorted array B with the same 
#            integers, and the number of 
#            inversions of A
#
#   if n = 0 or n = 1 then
#       return (A, 0)
#   else:
#       (C, leftInv) := Sort-and-CountInv(first half of A)
#       (D, rightInv) := Sort-and-CountInv(second half of A)
#       (B, splitInv) := Merge-and-CountSplitInv(C, D)
#       return (B, leftInv + rightInv + splitInv)
#
#
#   Merge-and-CountSplitInv Definition
#
#   INPUT:  sorted arrays C and D (length n/2 each)
#   OUTPUT: sort array B (length n) and the 
#           number of split inversions 
#   ASM:    n is even
#
#   i := 1, j := 1, splitInv := 0
#   for k := 1 to n do
#       if C[i] < D[j] then
#           B[k] := C[i], i := i + 1
#       else:
#           B[k] := D[j], j := j + 1
#           splitInv := splitInv + (n/2 - i + 1
#   return (B, splitInv)

###
#
# Week two problem - added text import script for algodata2.txt
#
###

import time

A = tuple(map(int, [line.rstrip('\n') for line in open("./algodata2.txt")]))

def sortAndCountInv(n):

    #  Recursive function to find all inversions through
    #  dividing the problem space into two parts (C & D).
    #  Each part is then iterated for inverted integers.
    #  Once the two recursive calls for the sepearte halves
    #  completes, the arrays and the inversion counts are
    #  passed to the merge function which also performs a
    #  split inversion function.  The base case if for any
    #  array of 1 item or NULL.  The mergeAndCountSplitInv
    #  function is a single call as it will merge the exiting
    #  arrays and count inversions similar to mergeSort.py.

    if len(n) <= 1:
        return (n,0)
    else:
        middle=len(n)//2
        C = n[:middle]
        D = n[middle:]
        
        leftInv  = 0
        rightInv = 0
        splitInv = 0
        
        (C,leftInv)   = sortAndCountInv(C)
        (D,rightInv)  = sortAndCountInv(D)
        (B,splitInv)  =  mergeAndCountSplitInv(C, D)      
        return (B, leftInv + rightInv + splitInv)

def mergeAndCountSplitInv(C, D):

    #  Same setup and functionality as the merge function
    #  in mergeSort.py except using enbedded while loops 
    #  instead of if, elif, else statements.  A little 
    #  clear (and easier to read) presentation.

    B = []
    splitInv = 0
    while len(C) > 0 and len(D) > 0:
        if C[0] <= D[0]:
            B.append(C[0])
            C = C[1:]
        else:
            B.append(D[0])
            D = D[1:]
            splitInv += len(C)
    while len(C)>0:
        B.append(C[0])
        C = C[1:]
    while len(D)>0:
        B.append(D[0])
        D = D[1:]
    return (B, splitInv)

# Remove comment line below for testing.
#A = (1, 3, 5, 2, 4, 6)

print("Count Inversions with Recursion")
print("...running...")
start = time.time()
print("Sorted Order, Inversions: ", sortAndCountInv(A))
end = time.time()
print ("Data file: ./algodata2.txt")
print("Total list elements: ", len(A))
print("Total run time: ", end - start)

###
#
#   Output:
#   
#   *  number of inversions:  2407905288
#   Data file: ./algodata2.txt
#   ('Total list elements: ', 100000)
#   ('Total run time: ', 16.117273092269897)
#
###