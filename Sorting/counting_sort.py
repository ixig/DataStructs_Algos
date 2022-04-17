'''
Counting Sort
Faster than O(NLogN)!
'''

import numpy as np
from sort_check import sort_check, sort_check1

def count_sort(l, min_val=0, max_val=100):
    counts = np.zeros(max_val - min_val + 1, dtype=np.int32)

    for value in l:
        counts[value - min_val] += 1

    idx = 0
    for i, count in enumerate(counts):
        while count:
            l[idx] = i + min_val
            idx += 1
            count -= 1

sort_check1(count_sort, 0b111)
sort_check(count_sort)
