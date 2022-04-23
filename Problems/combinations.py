'''
Find all possible subsets of given size (sampling without replacement), where
order does not matter
'''

# n(C)r: n = # objects in set; r = # objects to choose
def combinations1(n, r):

    def find_solution(choices):
        if len(choices) == r:
            solutions.append(choices)
            return

        start_idx = choices[-1] if choices else -1
        for choice in range(start_idx + 1, n):
            find_solution(choices + [choice])
        
    solutions = []; find_solution([]); return solutions
    
# Select <r> objects from <selection>
def combinations2(selection, r):

    def find_solution(choices):
        if len(choices) == r:
            solutions.append(choices)
            return

        start_idx = selection.index(choices[-1]) if choices else -1
        for choice in selection[start_idx + 1:]:
            find_solution(choices + [choice])
        return False
        
    solutions = []; find_solution([]); return solutions
    

print(combinations1(3, 2))
print(combinations2(['a', 'b', 'c'], 2))
