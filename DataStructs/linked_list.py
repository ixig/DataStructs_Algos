'''
Linked-List and Sorted Linked-List Implementations
'''

from math import inf

class Cell:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.sentinel = Cell(None, None)
        self.len = 0

    def insert(self, value, pos):
        if pos > self.len:
            print(f'ERROR: Invalid pos={pos} !')
            return
        cell = self.sentinel
        for _ in enumerate(range(pos)):
            cell = cell.next
        cell.next = Cell(value, cell.next)
        self.len += 1
    
    def append(self, value):
        self.insert(value, self.len)

    def remove(self, pos):
        if pos >= self.len:
            print(f'ERROR: Invalid pos={pos} !')
            return
        cell = self.sentinel
        for i in enumerate(range(pos)):
            cell = cell.next
        cell.next = cell.next.next
        self.len -= 1

    def __str__(self):
        cell = self.sentinel
        s = '['
        while cell.next:
            cell = cell.next
            s += str(cell.value) + ', '
        if len(s) > 2: 
            s = s[:-2] + ']'
        else:
            s += ']'
        return s

class SortedLinkedList:
    def __init__(self):
        self.max = inf
        self.sentinel_end = Cell(+self.max, None)
        self.sentinel_begin = Cell(-self.max, self.sentinel_end)

    def insert(self, value):
        assert (value > -self.max) and (value < +self.max)
        cell = self.sentinel_begin
        while not (cell.value < value < cell.next.value):
            cell = cell.next
        cell.next = Cell(value, cell.next)

    def remove(self, value):
        prev_cell = self.sentinel_begin
        cell = prev_cell.next
        while cell.next:
            if cell.value == value:
                break
            elif cell.value > value:
                print(f'ERROR1: Value {value} Not Found!')
                return
            prev_cell, cell = cell, cell.next
        else:
            print(f'ERROR2: Value {value} Not Found!')
            return
        prev_cell.next = cell.next

    def __str__(self):
        cell = self.sentinel_begin
        s = '['
        while cell.next:
            cell = cell.next
            if cell.value == self.max: break
            s += str(cell.value) + ', '
        if len(s) > 2: 
            s = s[:-2] + ']'
        else:
            s += ']'
        return s

def ll_check():
    l = LinkedList()
    l.insert(1, 1)
    l.insert(1, 0)
    l.insert(-1, 0)
    l.insert(2, 2)
    l.insert(3, 0)
    l.append(4)
    print(l)
    l.remove(5)
    l.remove(4)
    l.remove(0)
    print(l)

def sorted_ll_check():
    l = SortedLinkedList()
    l.insert(0)
    l.insert(-1)
    l.insert(2)
    print(l)
    l.remove(1)
    l.remove(-1)
    l.remove(2)
    l.remove(2)
    l.remove(0)
    print(l)


if __name__ == '__main__':
    ll_check()
    sorted_ll_check()
