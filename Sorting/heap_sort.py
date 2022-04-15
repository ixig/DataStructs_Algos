import math
from sort_check import sort_check, sort_check1

INF = math.inf

def heap_sort(heap):

    def heap_add(length, value):

        def parent(idx):
            if idx == 0:
                return None, +INF
            else:
                parent_idx = (idx - 1) // 2
                return parent_idx, heap[parent_idx]

        heap[length] = value
        test_idx = length
        
        while True:
            parent_idx, parent_value = parent(test_idx)
            if value > parent_value:
                heap[parent_idx], heap[test_idx] = heap[test_idx], heap[parent_idx]
                test_idx = parent_idx
            else:
                break
        return

    def child_left(idx):
        child_idx = 2 * idx + 1
        nonlocal length
        if child_idx < length:
            return child_idx, heap[child_idx]
        else:
            return None, -INF

    def child_right(idx):
        child_idx = 2 * idx + 2
        nonlocal length
        if child_idx < length:
            return child_idx, heap[child_idx]
        else:
            return None, -INF

    def fix_heap():
        idx = 0
        while True:
            max_idx, _ = max(
                ((idx, heap[idx]), child_left(idx), child_right(idx)),
                key=lambda x: x[1])
            if max_idx == idx:
                return
            heap[max_idx], heap[idx] = heap[idx], heap[max_idx]
            idx = max_idx

    for i in range(1, len(heap)):
        heap_add(i, heap[i])
    
    for length in range(len(heap) - 1, 0, -1):
        heap[length], heap[0] = heap[0], heap[length]
        fix_heap()

sort_check1(heap_sort, 0b111)
sort_check(heap_sort)
