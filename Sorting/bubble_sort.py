from sort_check import sort_check, sort_check1

# Optimizations: 
# i. Alternating directions
# ii. Sorted Boundaries
def bubble_sort(l):
    start = 0
    stop = len(l) - 1
    sorted_left, sorted_right = start, stop
    incr = +1
    last_swap = -1

    while last_swap:
        while start != stop:
            if ( incr * (l[start] - l[start + incr]) ) > 0:
                l[start], l[start + incr] = l[start + incr], l[start]
                last_swap = start
            start += incr
        if last_swap == -1:
            return
        elif incr == 1:
            sorted_right = last_swap
            start, stop = sorted_right, sorted_left
            incr = -1
        else: 
            sorted_left = last_swap
            start, stop = sorted_left, sorted_right
            incr = + 1
        last_swap = -1

sort_check1(bubble_sort, 0b111)
sort_check(bubble_sort)
