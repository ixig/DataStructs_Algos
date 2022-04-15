from sort_check import sort_check, sort_check1

def pivot_sort(l, begin, end):

    def get_pivot_idx():
        '''Use middle-value of three samples (left/center/right)'''
        middle = (begin + end) // 2
        sample_values = (l[begin], l[middle], l[end])
        if sample_values[0] <= sample_values[1]:
            if sample_values[1] <= sample_values[2]:   # b < m < e
                return middle
            elif sample_values[2] <= sample_values[0]: # e < b < m 
                return begin
            else:
                return end
        else:
            if sample_values[1] >= sample_values[2]:   # b > m > e
                return middle
            elif sample_values[2] >= sample_values[0]: # e > b > m
                return begin
            else:
                return end
    
    pivot_idx = get_pivot_idx()
    pivot_value = l[pivot_idx]
    l[pivot_idx] = l[begin]
    left = begin + 1
    right = end
    hole = begin
    hole_on_left = True
    while left <= right:
        if hole_on_left:
            if l[right] < pivot_value:
                l[hole] = l[right]
                hole = right
                hole_on_left = False
            right -= 1
        else:
            if l[left] > pivot_value:
                l[hole] = l[left]
                hole = left
                hole_on_left = True
            left += 1
    l[hole] = pivot_value
    return hole

def quick_sort(l, begin, end):
    if begin == end:
        return
    pivot_idx = pivot_sort(l, begin, end)
    if pivot_idx > begin:
        quick_sort(l, begin, pivot_idx - 1)
    if pivot_idx < end:
        quick_sort(l, pivot_idx + 1, end)

def quick_sort_wrap(l):
    quick_sort(l, 0, len(l) - 1)

sort_check1(quick_sort_wrap, 0b111)
sort_check(quick_sort_wrap)
