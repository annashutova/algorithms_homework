"""
Вводим переменную кол-ва матчей.
Пока у нас не останется 1 команда, мы выполняем действия из условия.

Сложность: O(log(n))
"""

def numberOfMatches(n: int) -> int:
    """Counts the number of matches played in the tournament until a winner is decided.
        
    Args:
        n : int - the number of the teams
        
    Returns:
        matches : int - the number of played mantches
    """
    matches = 0 # переменная подсчета кол-ва матчей
    while n > 1: # пока не останется одна команда
        if n % 2 == 0: # проверка на четность кол-ва команд
            matches += n // 2
            n //= 2
        else:
            matches += (n - 1) // 2
            n = (n - 1) // 2 + 1
    return matches
