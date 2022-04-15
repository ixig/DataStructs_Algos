from random import randint

def sort_check(sort):
    for _ in range(100):
        l = [randint(0, 80) for _ in range(50)]
        l_check = sorted(l)
        sort(l); print('.', end='')
        assert l == l_check, l

def sort_check1(sort, which):
    if which & 0b001:
        l = [3, 2, 1, 4, 8, 7, 9]
        sort(l); print(l)
    if which & 0b010:
        l = [4, 2, 1, 3, 8, 7, 9]
        sort(l); print(l)
    if which & 0b100:
        l = [48, 45, 67, 22, 38, 64, 61, 63, 33, 58]
        sort(l); print(l)
