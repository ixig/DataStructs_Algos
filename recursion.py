'''
Find all Word Anagrams
'''

def anagram(s):
    if not s:
        return ['']
    else:
        results = []
        for word in anagram(s[1:]):
            for pos in range(len(word) + 1):
                results.append(word[:pos] + s[0] + word[pos:])
        return results

tests = ['a', 'ab', 'abc']
print([anagram(s) for s in tests])
