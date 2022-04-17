'''
Sparse Array Implementation [TODO]
'''

class Cell():
    def __init__(self, idx, value, next):
        self.idx = idx
        self.value = value
        self.next = next

class AxisLinkedList():
    def __init__(self, name):
        self.name = name
        self.max = 9999
        self.sentinel_stop = Cell(+self.max, None, None)
        self.sentinel_start = Cell(-self.max, None, self.sentinel_stop)

    def get(self, idx):
        cell = self.sentinel_start
        while cell.next:
            if cell.idx == idx:
                break
            cell = cell.next
        else:
            raise ValueError(f'ERROR: {self.name}-LList, idx={idx} not found!')
        return cell.value
    
    def get_cell(self, idx):
        cell = self.sentinel_start
        while cell.next:
            if (cell.idx < idx < cell.next.idx):
                break
        else:
            raise ValueError(f'ERROR: {self.name}-LList, idx={idx} too large!')
        if cell.idx == idx:
            return cell
        else:
            cell.value = Cell(idx, AxisLinkedList(f'Row{idx}'))
            return cell

class SparseArray():
    def __init__(self):
        self.rows = AxisLinkedList('ROWS')

    def get(self, row, col):
        row_ll = self.rows.get(row)
        return row_ll.get(col)

    def set(self, row, col, value):
        row_ll = self.rows.set_get(row)
        row_ll.set

    
if __name__ == '__main__':
    ll = AxisLinkedList('Row')
    ll.set(1, [])
    ll.set(3, [])
    # ll.get(0)
    print(ll.get(1))
    # sa = SparseArray()
