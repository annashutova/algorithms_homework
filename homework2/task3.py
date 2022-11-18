from typing import List
"""Сложность O(mn)."""


def uniquePathsWithObstacles(grid: List[List[int]]) -> int:
    if grid[0][0] == 1: # если начальная точка имеет препятствие сражу возвращаем 0
        return 0
    """Cоздаем матрицу такой же размерности как и grid.
    Каждая ячейка dp[m][n] это кол-во путей до этой ячейки.
    """
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    dp[0][0] = 1
    for m in range(len(grid)): # проходимся по матрице
        for n in range(len(grid[0])):
            if m == 0 and n == 0: # эта ячейка заполнена, ее пропускаем
                continue
            if grid[m][n] == 1: # если в ячейкм препятствие, в нее не идем
                dp[m][n] = 0
            else:
                if m == 0: # если передвигаемся по первой строке, ячеек всерху еще не было
                    dp[m][n] = dp[m][n - 1]
                elif n == 0: # если передвигаемся по первому столбцу, ячеек слева еще не было
                    dp[m][n] = dp[m - 1][n]
                else:
                    dp[m][n] = dp[m - 1][n] + dp[m][n - 1]
    return dp[-1][-1] # возвращаем значение финишной ячейки с кол-вом путей до нее
