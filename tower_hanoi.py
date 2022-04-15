def hanoi1(stacks, src, dst):  # Iterative
    idxs = list(range(len(stacks)))
    idxs[0], idxs[src] = idxs[src], idxs[0]
    idxs[1], idxs[dst] = idxs[dst], idxs[1]
    while len(stacks[1]) != len(stacks):
        if len(stacks[1]) == 0:
            stacks[1].append(stacks[0].pop())
        else:
            for idx in idxs[2:]:
                stacks[idx].append(stacks[0].pop())
            stacks[idxs[-1]].append(stacks[1].pop())
            

stacks = [[3,2,1], [], []]
print(hanoi(stacks, 0, 1))