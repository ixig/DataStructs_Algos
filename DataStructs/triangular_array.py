'''
Triangular Array Implementation
'''

import numpy as np

class TriArray:
    def __init__(self, dim):
        self.dim = dim
        num_elements = dim * (dim - 1) // 2
        # self.array = np.array(num_elements)
        self.array = np.arange(1, num_elements + 1)  # [DEBUG]

    @staticmethod
    def idx(row, col):
        return row * (row - 1) // 2 + col

    def get(self, row, col):
        if row == col:
            print('ERROR: row must not equal col')
        elif row < col:
            row, col = col, row
        return self.array[self.idx(row, col)]


if __name__ == '__main__':
    a = TriArray(4)
    print(a.get(1, 1))
    print(a.get(1, 0))
    print(a.get(3, 2))
    print(a.get(2, 3))
