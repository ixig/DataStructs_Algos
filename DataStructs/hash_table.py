# Optimizations
# i. Open Addressing
# ii. Double Hashing (Collisions)

class HashTable:
    def __init__(self, size=256, max_tries=3):
        self.size = size
        self.table = [None] * size
        self.removed = [False] * size
        self.max_tries = 3

    def add(self, key: str):
        assert isinstance(key, str)
        hash_pri = hash(key) % self.size
        # print(key, ':', hash_pri, end=' ')
        if self.table[hash_pri] == None or self.removed[hash_pri]:
            self.table[hash_pri] = key
        else:
            hash_sec = hash(key + '@@@') % self.size
            # print(hash_sec, '!', end=' ')
            tries = 0
            while tries < self.max_tries:
                tries += 1
                addr = (hash_pri + hash_sec * tries) % self.size
                # print(addr, end=' ')
                if self.table[addr] == None or self.removed[addr]:
                    self.table[addr] = key
                    break
            else:
                print(f'ERROR: Cannot add {key}, table full!')
                return False
        # print()
        return True
    
    def remove(self, key: str):
        hash_pri = hash(key) % self.size
        # print(key, '<', hash_pri, end=' ')
        if self.table[hash_pri] == key:
            self.removed[hash_pri] = True
        elif self.table[hash_pri] == None:
            raise ValueError(f'ERROR: Key {key} not found!')
        else:
            hash_sec = hash(key + '@@@') % self.size
            tries = 0
            while tries < self.max_tries:
                tries += 1
                addr = (hash_pri + hash_sec * tries) % self.size
                # print(addr, end=' ')
                if self.table[addr] == key:
                    self.removed[addr] = True
                    break
                elif self.table[addr] == None:
                    raise ValueError(f'ERROR: Key {key} not found!')
            else:
                raise ValueError(f'ERROR: Key {key} not found!')
        # print()
        return

    def is_in(self, key: str):
        hash_pri = hash(key) % self.size
        # print(key, '?', hash_pri, end=' ')
        if self.table[hash_pri] == None:
            # print()
            return False
        elif self.table[hash_pri] == key and not self.removed[hash_pri]:
            # print()
            return True
        else:
            hash_sec = hash(key + '@@@') % self.size
            tries = 0
            while tries < self.max_tries:
                tries += 1
                addr = (hash_pri + hash_sec * tries) % self.size
                # print(addr, end=' ')
                if self.table[addr] == None:
                    # print()
                    return False
                elif self.table[addr] == key and not self.removed[addr]:
                    # print()
                    return True
            else:
                # print()
                return False

def hash_check1():
    t = HashTable()
    t.add('A')
    print(t.is_in('A'))
    print(t.is_in('B'))
    t.remove('A')
    print(t.is_in('A'))

from random import randint, choice

def hash_check():
    for _ in range(100):
        print('.', end='')
        l = [str(randint(0, 250)) for _ in range(40)]
        t_check = set(l)
        t = HashTable()
        for key in t_check:
            assert t.add(key)
        # print(t_check)
        t_len = len(t_check)
        for _ in range(randint(t_len // 4, t_len // 3)):
            key = choice(list(t_check))
            t_check.remove(key)
            t.remove(key)
        for key in t_check:
            assert t.is_in(key), key
        for x in [randint(1000, 1250) for _ in range(len(l))]:
            assert not t.is_in(str(x))

hash_check()
