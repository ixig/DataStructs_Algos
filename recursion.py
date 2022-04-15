def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_test():
    print([factorial(x) for x in [1, 2, 3, 4]])


def binary_search(x, l, offs=0):
    # print(x, l, offs)
    mid = len(l) // 2
    if not l:
        return -1
    if x == l[mid]:
        return offs + mid
    elif x > l[mid]:
        return binary_search(x, l[mid + 1:], offs + mid + 1)
    else:
        return binary_search(x, l[:mid], offs)


def binary_search_test():
    tests = [
        [-1, 0],
        [-1, 1, 2],
        [0, 1, 3, 5]
    ]
    print([binary_search(-2, l) for l in tests])
    print([binary_search(0, l) for l in tests])
    print([binary_search(3, l) for l in tests])
    print([binary_search(5, l) for l in tests])
    print([binary_search(6, l) for l in tests])


def anagram(s):
    if not s:
        return ['']
    else:
        results = []
        for word in anagram(s[1:]):
            for pos in range(len(word) + 1):
                results.append(word[:pos] + s[0] + word[pos:])
        return results


def anagram_test():
    tests = ['a', 'ab', 'abc']
    print([anagram(s) for s in tests])


if __name__ == '__main__':
    # factorial_test()
    # binary_search_test()
    anagram_test()
