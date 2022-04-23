'''
Given some number of shunting tracks, sort the carriages of a train so that
carriages going to the same destination are grouped together and in sorted
order, e.g. [3, 3, 2, 1, 1, 1].
'''

from random import randint
import math

INF = math.inf

def is_sorted(l):  # Descending Sorted
    prev_x = +INF
    for x in l:
        if x > prev_x:
            return False
        prev_x = x
    return True

def train_sort(input):
    NUM_STACKS = 3  # Num of Shunting Tracks (incl'd Outgoing)

    stacks = [ [] for _ in range(NUM_STACKS) ]
    input_stack = input[:]
    len_input = len(input)

    def matching_stack(x, stacks):
        for stack in stacks:
            if stack and stack[-1] == x:
                return stack
        return None

    def max_stack(stacks):
        return max(stacks, key=lambda x: -INF if not x else x[-1])

    def best_stack(stacks, x):
        return min(stacks, key=lambda x: -INF if not x else x[-1])

    def phase1():  # Distribute Carriages over shunting stacks
        assert all([len(stack) == 0 for stack in stacks])
        while len(input_stack):
            x = input_stack.pop()
            target_stack = matching_stack(x, stacks)
            if target_stack is None:
                best_stack(stacks, x).append(x)
            else:
                target_stack.append(x)

    def phase2():  # Reassemble Carriages
        assert len(input_stack) == 0
        for _ in range(len_input):
            input_stack.append(max_stack(stacks).pop())

    rounds = 0  # [DEBUG]
    while not is_sorted(input_stack):
        print('.', end='')
        phase1()
        phase2()
        rounds += 1
    print()

    return input_stack, rounds

# input = [1, 2, 3, 4]
# input = [randint(1, 60) for _ in range(50)]
# print(train_sort(input))

total_rounds = 0
for _ in range(100):
    total_rounds += train_sort([randint(1, 60) for _ in range(50)])[1]
print(total_rounds)
