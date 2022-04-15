def binary_search(l, target):
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

search_check(binary_search)
