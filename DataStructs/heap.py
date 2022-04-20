'''
Heap Implementation
'''

from math import inf

class Heap:
    def __init__(self):
        self.l = []

    def child_left(self, idx):
        left_idx = 2 * idx + 1
        if left_idx >= len(self.l):
            return -1, (-inf, None)
        else:
            return left_idx, self.l[left_idx]

    def child_right(self, idx):
        right_idx = 2 * idx + 2
        if right_idx >= len(self.l):
            return -1, (-inf, None)
        else:
            return right_idx, self.l[right_idx]

    def parent(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx < 0:
            return -1, (+inf, None)
        else:
            return parent_idx, self.l[parent_idx]

    def add(self, value, data):
        self.l.append((value, data))
        idx = len(self.l) - 1
        while True:
            parent_idx, (parent_value, _) = self.parent(idx)
            if parent_value < value:
                self.l[parent_idx], self.l[idx] = self.l[idx], self.l[parent_idx]
            else:
                break

    def pop(self):
        if len(self.l) == 0:
            return None
        if len(self.l) == 1:
            return self.l.pop()
        retval = self.l[0]
        self.l[0] = self.l.pop()
        idx = 0
        while True:
            val = self.l[idx]
            left_idx, left_val = self.child_left(idx)
            right_idx, right_val = self.child_right(idx)
            max_idx, _ = max(
                zip((idx, left_idx, right_idx), (val, left_val, right_val)), key=lambda tup: tup[1]
            )
            if max_idx == idx:
                break
            else:
                self.l[idx], self.l[max_idx] = self.l[max_idx], self.l[idx]
                idx = max_idx
        return retval


if __name__ == "__main__":
    h = Heap()
    print(h.pop())
    h.add(10, "10")
    h.add(20, "20")
    h.add(30, "30")
    h.add(15, "15")
    print(h.pop())  # 30
    print(h.pop())  # 20
    print(h.pop())  # 15
    print(h.pop())  # 10
    print(h.pop())
