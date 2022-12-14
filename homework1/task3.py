"""
Вводим переменную подсчета бриллиантов.
Проходимся по каждому виду бриллианта и смотрим есть ли он в наборе камней.
Увеличиваем счетчик, если  такой камень имеется.

Сложность: O(n) * O(n) = O(n**2)
"""

def numJewelsInStones(jewels: str, stones: str) -> int:
    """Counts how many of the stones are also jewels.

    Args:
        jewels : str - possible jewels
        stones : str - given line of the stones

    Returns:
        count_jewels : int - number of the stones that are also jewels
    """
    count_jewels = 0 # переменная подсчета камней
    for i in jewels: # проход по каждому камню
        count_jewels += stones.count(i) # проверка наличие камня и увеличение счетчика
    return count_jewels