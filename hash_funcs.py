def polynomial_hash(key: any, table_size: int, base=31) -> int:
    """
    Функция генерирует хэш используя номер символа в ASCII таблице, а также константу base
    и остаток от деления на размер таблицы. При малом размере таблицы вероятны коллизии,
    при большом их шанс практически минимален.
    Из минусов - начало таблицы(~50 ячеек) зачастую будет пустыми. Можно использовать как
    небольшой резерв для коллизий.
    """
    hash_value = 0
    for char in str(key):
        hash_value = (hash_value * base + ord(char)) % table_size
    return hash_value

def support_hash(key: any, table_size: int, i: int) -> int:
    """
    Вспомогательная хэш функция, генерирует хэш как остаток от деления на размер таблицы,
    + переменная i = [0, 1, ..., table_size-1]
    """
    if key is int or str(key).isnumeric():
        return int(key) % table_size + i
    else:
        key_value = get_str_value(key)
        return key_value % table_size + i


def get_str_value(st: str) -> int:
    """
    Возвращает сумму ASCII символов в строке, чтобы использовать строку как ключ.
    Вспомогательная функция для support_hash
    """
    value = 0
    for char in st:
        value += ord(char)
    return value


def div_hash(key: int, table_size: int) -> int:
    return key % table_size