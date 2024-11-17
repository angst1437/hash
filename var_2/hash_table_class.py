import hash_funcs as h


class HashTable:
    def __init__(self, size):
        self.table = [[None] for _ in range(size)] # задается список с парами [ключ, значение]
        self.size = size

    def insert(self, key, value) -> None:
        if key in self.get_keys():
            print(f"ключ {key} уже существует!")
            return None

        hsh = h.polynomial_hash(key, self.size) # создаем хэш
        if self.table[hsh] == [None]: # если коллизии нет, то добавляем пару в таблицу
            self.table[hsh] = [key, value]
        else: # если коллизия найдена, используем открытую индексацию
            index = h.support_hash(key, self.size, 0) # задаем начало обхода
            while self.table[index] is not [None]: # пока не  найдем доступную ячейку
                index = h.support_hash(key, self.size, index) # увеличиваем индекс
                if index >= self.size:
                    print("Свободных ячеек не осталось")
                    return None
            self.table[index] = [key, value]

    def find(self, key, return_value=True) -> any:
        """
        Находит значение в таблице.
        Если флаг return_value стоит True, то возвращает толькозначение по ключу.
        Если он стоит False, то возвращает только индекс(нужно для работы ф-ии удаления)
        """
        if key in self.get_keys():
            hsh = h.polynomial_hash(key, self.size)
            if self.table[hsh][0] == key:
                return self.table[hsh][1]
            else:
                index = h.support_hash(key, self.size, 0)  # задаем начало обхода
                while self.table[index][0] != key:  # пока не  найдем доступную ячейку
                    index = h.support_hash(key, self.size, index)  # увеличиваем индекс
                return self.table[index][1] if return_value else index
        else:
            print("такого ключа нету в таблице!")
            return None


    def get_keys(self) -> list:
        """
        Возвращает список ключей(может замедлять программу)
        """
        keys = []
        for pair in self.table:
            keys.append(pair[0])
        return keys

    def del_e(self, key):
        """
        Удаляет элемент по индексу, полученному из функции find
        """
        index = self.find(key, return_value=False)
        self.table[index] = [None]