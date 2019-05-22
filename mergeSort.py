#  Bill Armstrong
#  May 2019
#  Merge Sort Algorithm
###########################################

lst = [10, 2, 4, 6, 8, 1, 3, 5, 7, 9, 34, 35, 12, 67, 98, 43, 42, 1483]

#  ab represents the full list passed to the function.
#  a  represents the left half of the list (the slpit)
#  b  represents the right hald of the list


def split (ab):
    #  splits argument list into two halfs with integer division
    return ab[:len(ab)//2], ab[len(ab)//2:]

def merge (a, b):

    #  for zero based split lists it returns the non-zero side
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    
    #  initiation for indexing on lists and building final list
    idx_a = idx_b = 0
    final_list = []
    list_len = len(a) + len(b)

    while len(final_list) < list_len:
        #  Also works with a For loop
        #  with another iterator

        #  Compares elements and appends smaller element to end of
        #  final list creating an increasing value list.
        if a[idx_a] <= b[idx_b]:
            final_list.append(a[idx_a])
            idx_a += 1
        else:
            final_list.append(b[idx_b])
            idx_b += 1

        #  When a list is fully iterated (the index value is == length)
        #  the while loop is broken.  This is not reuquired on an For 
        #  loop implementation.
        if idx_a == len(a):
            final_list += b[idx_b:]
            break
        elif idx_b == len(b):
            final_list += a[idx_a:]
            break

    return final_list

def sort (ab):

    #  If the list is a single element then it is already sorted.
    #  Else, the input number is first split and then the two elements
    #  are sent to be sorted.  The sort function is recursive and will
    #  continue to divide the list until down to a single element.  The
    #  recursive call is within the Return statement for this same
    #  function.  Ultimately, the outer call to the Merge function 
    #  returns the "final_list" which represents the sorted integer
    #  list.
    if len(ab) <= 1:
        return ab
    else:
        a, b = split(ab)
        return merge(sort(a), sort(b))

print(sort(lst))