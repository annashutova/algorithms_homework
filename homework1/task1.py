"""
Вводим переменную, которая будет считать шаги. 
Пока изначальное число не равно 0,
выполняем его преобразование, проверяя четность.

Сложность: O(log(n))
"""

def numberOfSteps(num: int) -> int:
    """Counts the number of steps to reduce a number to zero.

    Args:
        num : int - given number

    Returns:
        steps : int - required number of steps to reduce number to zero
    """
    steps = 0 # переменная, которая будет считать шаги
    while num != 0: # пока изначальное число не будет равно 0, мы выполняем его преобразование
        if num % 2 == 0: # проверка четности числа
            num /= 2 
        else:
            num -= 1
        steps += 1 # в обоих случаях увеличиваем шаг на 1
    return steps
