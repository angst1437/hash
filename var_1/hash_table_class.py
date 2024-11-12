class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None

    def set_next(self, nxt):
        self.nxt = nxt

    def get_next(self):
        return self.nxt


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = list()

    def insert(self, key, value):
        hsh = polynomial_hash(key, self.table_size)
        if hsh not in self.table:
            self.table[hsh] = Node(key, value)
        else:
            el = self.table[hsh]
            while el.get_next() is not None:
                el = el.get_next()
            el.set_next(Node(key, value))

    def get(self, key):

        hsh = polynomial_hash(key, self.table_size)

        if hsh in self.table:
            if self.table[hsh].key == key:
                return self.table[hsh].value
            else:
                el = self.table[hsh]
                while el.key != key:
                    el = el.get_next()
                return el.value

        else:
            return None

    def delete(self, key):
        pass





def polynomial_hash(key: any, table_size: int, base=31) -> int:
    hash_value = 0
    for char in str(key):
        hash_value = (hash_value * base + ord(char)) % table_size
    return hash_value



