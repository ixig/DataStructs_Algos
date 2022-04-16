def hanoi1(stacks, src, dst, tmp):  # Recursive

    def print_stacks():  # [DEBUG]
        for i, stack in enumerate(stacks):
            print(f'{i}:{stack}', end=' ')
        print()

    def move_disks(num_discs, src, dst, tmp):
        if num_discs == 1:
            stacks[dst].append(stacks[src].pop())
            # assert sorted(stacks[dst], reverse=True) == stacks[dst]
            print(f'{src} => {dst}', end=' | '); print_stacks()
            return

        move_disks(num_discs - 1, src, tmp, dst)
        move_disks(1, src, dst, None)
        move_disks(num_discs - 1, tmp, dst, src)
    
    move_disks(len(stacks[src]), src, dst, tmp)

def hanoi2(stacks, src, dst, tmp):  # Iterative

    def print_stacks():  # [DEBUG]
        for i, stack in enumerate(stacks):
            print(f'{i}:{stack}', end=' ')
        print()

    def move_disks(num_discs, src, dst, tmp):
        params = [(num_discs, src, dst, tmp)]
        while params:
            num_discs, src, dst, tmp = params.pop()

            if num_discs == 1:
                stacks[dst].append(stacks[src].pop())
                # assert sorted(stacks[dst], reverse=True) == stacks[dst]
                print(f'{src} => {dst}', end=' | '); print_stacks()
                continue

            params.append((num_discs - 1, tmp, dst, src))
            params.append((1, src, dst, None))
            params.append((num_discs - 1, src, tmp, dst))
    
    move_disks(len(stacks[src]), src, dst, tmp)

# stacks0 = [[3,2,1], [], []]; hanoi1(stacks0, 0, 1, 2); print(stacks0)
stacks0 = [[3,2,1], [], []]; hanoi2(stacks0, 0, 1, 2); print(stacks0)
# stacks0 = [[4,3,2,1], [], []]; hanoi1(stacks0, 0, 2, 1); print(stacks0)
# stacks0 = [[4,3,2,1], [], []]; hanoi2(stacks0, 0, 2, 1); print(stacks0)
