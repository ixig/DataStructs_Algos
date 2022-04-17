'''
Find all Word Anagrams
'''

def anagrams(s):
    if not s:
        return ['']
    else:
        results = []
        for word in anagrams(s[1:]):
            for pos in range(len(word) + 1):
                results.append(word[:pos] + s[0] + word[pos:])
        return results

tests = ['a', 'ab', 'abc']
print([anagrams(s) for s in tests])
