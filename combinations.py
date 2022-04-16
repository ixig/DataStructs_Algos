# nCr: n = # objects in set; r = # objects to choose
def combinations(n, r):
    output = []
    stack = [0]
    while stack:
        entry = stack.pop()
        if len(entry) == r:
            output.append(entry)
            continue
        elif entry[-1]
            entry.append(entry[-1] + 1)
            continue
        if entry[-1] < (n - len(entry)):
            entry[-1] += 1
            stack.append(entry)

    

print(combinations(3, 2))
# print(res)