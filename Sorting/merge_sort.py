'''
Merge Sort
'''

from sort_check import sort_check, sort_check1
import numpy as np

# Merging cannot be performed in-place
def merge(l1, l2):
    l1_idx, l2_idx = 0, 0
    l1_len, l2_len = len(l1), len(l2)
    total_len = l1_len + l2_len
    new_l = np.empty(total_len, np.int32)
    idx = 0
    while idx < total_len:
        if l1_idx == l1_len:
            new_l[idx] = l2[l2_idx]
            l2_idx += 1
        elif l2_idx == l2_len:
            new_l[idx] = l1[l1_idx]
            l1_idx += 1
        elif l1[l1_idx] <= l2[l2_idx]:
            new_l[idx] = l1[l1_idx]
            l1_idx += 1
        else:
            new_l[idx] = l2[l2_idx]
            l2_idx += 1
        idx += 1
    return new_l.tolist()

# Not in-place, returns a new sorted list
def merge_sort(l):
    if len(l) == 1:
        return l
    mid_idx = len(l) // 2
    l1, l2 = merge_sort(l[:mid_idx]), merge_sort(l[mid_idx:])
    return merge(l1, l2)

# Wrappper to mimic in-place sorting
def merge_sort_inplace(l):
    new_l = merge_sort(l)
    l.clear()
    l.extend(new_l)

sort_check1(merge_sort_inplace, 0b111)
sort_check(merge_sort_inplace)
