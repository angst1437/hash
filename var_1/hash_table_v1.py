import hash_funcs as h

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def set_next(self, node):
        self.next = node

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]
        self.keys = []

    def insert(self, key, value):
        hsh = h.div_hash(key, self.size)
        if self.table[hsh] is None:
            self.table[hsh] = Node(key, value)
            self.keys.append(key)
        else:
            node = self.table[hsh]
            while node.next is not None:
                node = node.next
            node.next = Node(key, value)
            self.keys.append(key)

    def find(self, key):
        if key not in self.keys:
            print("Такого ключа нет")
            return None

        hsh = h.div_hash(key, self.size)
        if self.table[hsh].next is None and self.table[hsh].key == key:
            return self.table[hsh].value
        else:
            node = self.table[hsh]
            while node.key != key:
                node = node.next
            return node.value

    def delete(self, key):
        hsh = h.div_hash(key, self.size)
        node = self.table[hsh]
        if node is None:
            print("Такого ключа нет")
            return None
        elif node.next is None:
            self.keys.remove(key)
            node = None

        elif node.next.next is None:
            if node.key == key:
                self.keys.remove(key)
                self.table[hsh] = node.next
            else:
                self.keys.remove(key)
                self.table[hsh].next = None
        else:
            while node.key != key:
                last_node = node
                node = node.next
            last_node.next = node.next
