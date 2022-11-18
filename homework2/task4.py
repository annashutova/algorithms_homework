from typing import List
"""Упростим немного формулу: values[i] + i + values[j] - j.
Для того, чтобы максимизировать эту формулу нужно максимизировать (values[i] + i) и (values[j] - j)
Сложность: O(n).
"""


def maxScoreSightseeingPair(values: List[int]) -> int:
    res = 0 # переменная, в которой записывается результат формулы
    cur_max = values[0] + 0 # текущим максимальным значением суммы принимаем первое значение, т.к. пары у него пока нет
    for i in range(1, len(values)): # проходимся по списку
        res = max(res, cur_max + values[i] - i) # общий максимум - это сумма текущего максимума и максимальной разности
        cur_max = max(cur_max, values[i] + i) # текущий максимум суммы (values[i] + i)
        """Так как мы переопределяем res перед cur_max, это нам гарантирует выполнение условия пары (i < j)."""
    return res
