'''
Selection Sort
'''

from math import inf
from sort_check import sort_check, sort_check1

INF = inf

def selection_sort(l):

    def argmin(start, stop):
        min = +INF
        min_idx = None
        while start != stop:
            if l[start] < min:
                min = l[start]
                min_idx = start
            start += 1
        return min_idx

    stop = len(l)
    for start in range(stop - 1):
        min_idx = argmin(start, stop)
        l[start], l[min_idx] = l[min_idx], l[start]

sort_check1(selection_sort, 0b111)
sort_check(selection_sort)
