def max_combination(selection, max_choices, target):

    def find_solution(choices):
        nonlocal iter_count; iter_count += 1
        choices_sum = sum(choices)
        if choices_sum == target:
            # return True
            solutions.append(choices[:]); return False
        if choices_sum > target or len(choices) == max_choices:
            return False

        if choices:
            max_idx = max([selection.index(choice) for choice in choices])
        else:
            max_idx = -1

        # For each *Legal Move* from *Current Position*
        for choice in selection[max_idx + 1:]:
            if find_solution(choices + [choice]):
                return True

        return False

    # return find_solution([])

    # Optimization (Warnsdorff's Heuristic):
    # Start with the move that most reduces subsequent possible moves 
    selection = sorted(selection, reverse=True)

    iter_count = 0
    solutions = []; find_solution([]); print(iter_count); return solutions

# selection = [11, 6, 9, 4, 5, 2, 1, 3]
selection = [1, 6, 9, 4, 5, 2, 11, 3]
# print(max_combination(selection, 2, 10))
# print(max_combination(selection, 3, 10))
print(max_combination(selection, 4, 10))
