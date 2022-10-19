"""
Функция сортирует входной список по возрастанию.
Проходится по парам элементов и, если их разность наименьшая, добваляет их в список.

Сложность: O(nlog(n))
"""
def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    """Finds all pairs of elements with the minimum absolute difference.

    Args:
        arr : list - given array of distinct integers

    Returns:
        result : list - a list of pairs with the minimum absolute difference in ascending order
    """
    arr.sort()
    min_diff = 10000
    result = []
    for i in range(len(arr) - 1): # проходимся по парам отсортированного списку чисел
        cur_diff = abs(arr[i + 1] - arr[i])
        if cur_diff < min_diff: # если текущая разность меньше, мы перезаписываем мин. разность
            min_diff = cur_diff
            result = [[arr[i], arr[i + 1]]] # добавляем пару в результат
        elif cur_diff == min_diff: # если разность такая же добавляем пару в результат
            result.append([arr[i], arr[i + 1]])
    return result
