#  Bill Armstrong
#  June 2019
#  QuickSort (First Element Pivot) Algorithm
############################################

#  QuickSort Algorithm for Sorting an Array
#
#  Roughgarden, Section 5.2.4
#
#   Partition Psudocode
#
#   INPUT:   array A of n distinct integers, left and right 
#            endpoints l, r == {1, 2, ..., n} with l<= r.
#   POSTCONDITION:  elements of teh subarray A[l], A[l+1], 
#            ..., A[r] are partitioned around A[l].
#   OUTPUT:  final position of the pivot element.
#
#   p := A[l]
#   i := l + 1
#   for j := l + 1 to r do
#       if A[j] < p then
#           swap A[j] and A[i]
#           i := i + 1
#   swap A[l] and A[i - 1]
#   return i - 1

###
#
# Week three problem - added text import script for algodata3.txt
#
###

import time

A = tuple(map(int, [line.rstrip('\n') for line in open("./algodata3.txt")]))

def partition(A, l, r):
    p = A[l]
	i = l + 1

	for j in range(l, r): 
		if A[j] < p:
            A[i], A[j] = A[j], A[i]
			i = i+1
    A[l], A[i - 1] = A[i - 1], A[l]
	return (i - 1) 

#   quickSort Psudocode
#
#   INPUT:  array A of n distinct integers, left and right 
#           endpoints l, r == {1, 2, ..., n}.
#   POSTCONDITION:  elemetns of the subsarray A[l], A[l+1], 
#           ..., A[r] are sorted from smallest to largest.
#
#   if l >= r then
#       return
#   i := ChoosePivot(A, l, r)
#   swap A[l] and A[i]
#   j := Partition(A, l, r)
#   quickSort(A, l, j-1)
#   quickSort(A, j+1, r)
#

def quickSort(A, l, r): 
	if l >= r: 
		i = choosePivot(A, l, r) 
        A[l], A[i] = A[i], A[l]
        j = partition(A, l, r)
        quickSort(A, l, j-1)
        quickSort(A, j+1, r)


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


# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 

# This code is contributed by Mohit Kumra 
