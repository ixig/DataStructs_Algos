def max_combination(choices, selection, max_choices, max_sum):
    if sum(choices) == max_sum:
        # return choices
        print(choices)
        return []
    elif sum(choices) > max_sum or len(choices) == max_choices or not selection:
        return []
    for choice in selection:
        choices.append(choice)
        new_selection = selection.copy()
        new_selection.remove(choice)
        if max_combination(choices, new_selection, max_choices, max_sum):
            return choices
        choices.pop()
    return []

selection = [1, 6, 9, 4, 3, 2, 0, 0]
print(max_combination([], selection, 3, 10))
