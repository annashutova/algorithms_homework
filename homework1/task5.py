from heapq import nlargest


"""
Модуль heapq содержит готовые функции для работы с приоритетной очередью.
В данном модуле я использовала функцию nlargest(n, iterable),
которая возвращает n наибольших элементов очереди.
Далее я просто обращаюсь к последнему элементу полученного списка,
он и является k наибольшим элементом из изначального списка.

Сложность: O(n)
"""


def findKthLargest(nums: list, k: int) -> int:
    """Finds the kth largest element in the array.

    Args:
        nums : list - given integer array of numbers
        k : int - order of the largest element

    Returns:
        int - the kth largest element in the array
    """
    return nlargest(k, nums)[-1]
