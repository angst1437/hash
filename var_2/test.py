import hash_funcs as h
import hash_table_class
import random as r

hasht = hash_table_class.HashTable(10000)
key = r.randint(0, 100)
hasht.insert(key, "привет")