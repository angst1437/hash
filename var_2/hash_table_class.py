class HashTable(dict):
    def __init__(self, size=None):
        super().__init__()
        self.table = {}
        self.size = size

    def insert(self, key, value):
        hsh = polynomial_hash(key, self.size)
        if hsh not in self.table:
            self.table[hsh] = value



def polynomial_hash(key: any, table_size: int, base=31) -> int:
    """
    Функция генерирует хэш используя номер символа в ASCII таблице, а также константу base
    и остаток от деления на размер таблицы. При малом размере таблицы вероятны коллизии,
    при большом их шанс практически минимален
    """
    hash_value = 0
    for char in str(key):
        hash_value = (hash_value * base + ord(char)) % table_size
    return hash_value



