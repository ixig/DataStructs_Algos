from sort_check import sort_check, sort_check1

def insertion_sort(l):

    def shift_insert(value, pos, end):
        idx_dst = end
        while idx_dst != pos:
            l[idx_dst] = l[idx_dst - 1]
            idx_dst -= 1
        l[pos] = value
        return l

    def find_pos(value, length):
        for pos in range(length):
            if l[pos] > value:
                break
        else:
            return pos + 1
        return pos
    
    for pos in range(1, len(l)):
        value = l[pos]
        shift_insert(value, find_pos(value, pos), pos)

sort_check1(insertion_sort, 0b111)
sort_check(insertion_sort)
