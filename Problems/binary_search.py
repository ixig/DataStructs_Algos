'''
Perform Binary Search on a Sorted List, returning (position, value)
'''

def binary_search1(l, target, offs=0):  # Recursive
    if not l:
        return None, None
    middle = len(l) // 2
    mid_value = l[middle]
    if target == mid_value:
        return offs + middle,  mid_value
    elif target < mid_value:
        return binary_search1(l[:middle], target, offs)
    else:
        return binary_search1(l[middle + 1:], target, offs + middle + 1)
    # Tail-Recursion ... which can be easily removed

def binary_search2(l, target):  # Iterative
    left = 0
    right = len(l) - 1
    while left <= right:
        middle = (left + right) // 2
        mid_value = l[middle]
        if target == mid_value:
            return middle, mid_value
        elif target < mid_value:
            right = middle - 1
        else:
            left = middle + 1
    print(f'ERROR: {target} not found in {l}!')
    return None, None

# l = [1, 2, 3, 4, 5]; print(binary_search(l, 3))
# l = [1, 2, 3, 4, 5]; print(binary_search(l, 1))
# l = [1, 2, 3, 4, 5]; print(binary_search(l, 5))
# l = [1, 2, 3, 4]; print(binary_search(l, 2))
# l = [1, 2, 3, 4]; print(binary_search(l, 3))
# l = [1, 2, 3, 4]; print(binary_search(l, 1))
# l = [1, 2, 3, 4]; print(binary_search(l, 4))

from random import randint

def search_check(search):
    for _ in range(100):
        print('.', end='')
        l = sorted([randint(0, 80) for _ in range(50)])
        tgt_pos = randint(0, len(l) - 1)
        tgt_val = l[tgt_pos]
        pos, val = search(l, tgt_val)
        assert val == tgt_val
        assert l[pos] == tgt_val
    print()

search_check(binary_search1)
search_check(binary_search2)
