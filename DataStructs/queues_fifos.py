class Cell:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f'{self.value}'

class Queue():
    def __init__(self):
        self.sentinel_start = Cell(None, None, None)
        self.sentinel_stop = Cell(None, self.sentinel_start, None)
        self.sentinel_start.next = self.sentinel_stop
        self.len = 0
    
    def enqueue(self, value):
        new_cell = Cell(value, self.sentinel_start, self.sentinel_start.next)
        self.sentinel_start.next.prev = new_cell
        self.sentinel_start.next = new_cell
        self.len += 1
    
    def dequeue(self):
        if self.len == 0:
            print('ERROR: Queue is Empty!')
            return None
        last_cell = self.sentinel_stop.prev
        last_cell.prev.next = self.sentinel_stop
        self.sentinel_stop.prev = last_cell.prev
        self.len -= 1
        return last_cell.value

    def __str__(self):
        s = '['
        next_cell = self.sentinel_start
        while next_cell.next.next:
            next_cell = next_cell.next
            s += str(next_cell.value) + ', '
        if len(s) > 2:
            return s[:-2] + ']'
        else:
            return '[]'

class CircularQueue():
    def __init__(self, size=3):
        self.size = size
        self.queue = [None] * self.size
        self.head = self.tail = 0

    def enqueue(self, value):
        head_next = (self.head + 1) % self.size
        if head_next == self.tail:
            print('ERROR: Queue is Full!')
            return
        self.queue[self.head] = value
        self.head = head_next

    def dequeue(self):
        if self.head == self.tail:
            print('ERROR: Queue is Empty!')
            return None
        retval = self.queue[self.tail]
        self.tail = (self.tail + 1) % self.size
        return retval

    def __str__(self):
        s = '['
        idx = self.tail
        while idx != self.head:
            s += str(self.queue[idx]) + ', '
            idx = (idx + 1) % self.size
        if len(s) > 2:
            return s[:-2] + ']'
        else:
            return '[]'

q = Queue()
# q = CircularQueue()
q.enqueue(1)
q.enqueue(2); print(q)
print(q.dequeue()); print(q)
q.enqueue(3); print(q)
print(q.dequeue()); print(q)
print(q.dequeue()); print(q)
print(q.dequeue())
q.enqueue(4)
q.enqueue(5); print(q)
print(q.dequeue())
print(q.dequeue())
