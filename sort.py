lst = [10, 2, 4, 6, 8, 1, 3, 5, 7, 9, 34, 35, 12, 67, 98, 43, 42, 1483]

def split (ab):   #split step 1
    ab_len = len(ab)
    midpoint = ab_len//2
    return ab[:midpoint], ab[midpoint:]

def merge (a, b):  #merge_sorted_lists step 2

    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    
    idx_a = idx_b = 0
    final_list = []
    list_len = len(a) + len(b)
    while len(final_list) < list_len:
        if a[idx_a] <= b[idx_b]:
            final_list.append(a[idx_a])
            idx_a += 1
        else:
            final_list.append(b[idx_b])
            idx_b += 1

        if idx_b == len(b):
            final_list += a[idx_a:]
            break
        elif idx_a == len(a):
            final_list += b[idx_b:]
            break

    return final_list

def sort (ab):   #merge_sort step 3
    if len(ab) <= 1:
        return ab
    else:
        a, b = split(ab)
        return merge(sort(a), sort(b))


print(sort(lst))
