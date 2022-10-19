from heapq import nsmallest


"""
Функция count_power считает power переданного ей числа.

В функции getKth создается список по данному диапазону [lo, hi].
Далее он сортируется при помощи функции nsmallest из модуля heapq.
Ключом сортировки выступает функция count_power.
В итоге мы получаем отсортированный список из первый k элементов.
В конце функция возвращает последний, k-ый, элемент очереди.
"""


def count_power(x: int) -> int:
    """Counts the power of a given number.

    Args:
        x : int - given number

    Returns:
        power : int - counted power of the number
    """
    power = 0
    while x != 1: # пока число не будет равняться 1, мы его преобразуем по условию
        if x % 2 == 0:
            x /= 2
            power += 1
        else:
            x = 3 * x + 1
            power += 1
    return power


def getKth(lo: int, hi: int, k: int) -> int:
    """Returns the kth integer in the range [lo, hi] sorted by the power value.

    Args:
        lo : int - the beginning of the interval
        hi : int - th end of the interval

    Returns: 
        int - the kth integer in the range [lo, hi]
    """
    all_nums = [num for num in range(lo, hi+1)]
    k_smallest = nsmallest(k, all_nums, key=lambda x: count_power(x))
    return k_smallest[-1]
