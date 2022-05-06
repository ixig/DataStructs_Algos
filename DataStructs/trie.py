'''
Trie Implementation
'''

class TrieNode:
    def __init__(self, children=None, complete=False):
        self.children = {} if children is None else children
        self.complete = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def is_valid(self, seq, node=None):
        node = self.root if node is None else node
        for element in seq:
            if element in node.children:
                node = node.children[element]
            else:
                return None
        return node if node.complete else None

    def add(self, seq):
        node = self.root
        for element in seq:
            if element not in node.children:
                node.children[element] = TrieNode()
            node = node.children[element]
        node.complete = True


if __name__ == "__main__":
    t = Trie()
    print("a", t.is_valid("a"))
    print("---")
    t.add("abc")
    t.add("abcd")
    t.add("ac")
    print("abc", t.is_valid("abc"))
    print("abce", t.is_valid("abce"))
    print("ab", t.is_valid("ab"))
    print("ac", t.is_valid("ac"))
    abc = t.is_valid("abc")
    print("abc+d", t.is_valid("d", abc))
    print("abc+e", t.is_valid("e", abc))
