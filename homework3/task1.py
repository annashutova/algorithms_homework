"""Сложность O(m*n)"""

def numEnclaves(grid) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    """Обход в глубину каждого острова"""
    def dfs(r: int, c: int, plus: int=0):
        count = 0 # счетчик для каждого острова
        count += plus
        # stack - ячейки, по которым мы будем проходиться, если они == 1
        stack = [(r, c)]
        while stack:
            r, c = stack.pop()
            # проверка ячейки сверху
            if (r - 1 >= 0) and (grid[r-1][c] == 1) and ((r - 1, c) not in visited):
                stack.append((r-1, c))
                visited.add((r-1, c))
                count += plus
            # проверка ячейки слева
            if (c - 1 >= 0) and (grid[r][c-1] == 1) and ((r, c - 1) not in visited):
                stack.append((r, c-1))
                visited.add((r, c-1))
                count += plus
            # проверка ячейки снизу
            if (r + 1 < rows) and (grid[r+1][c] == 1) and ((r + 1, c) not in visited):
                stack.append((r+1, c))
                visited.add((r+1, c))
                count += plus
            # проверка ячейки справа
            if (c + 1 < cols) and (grid[r][c+1] == 1) and ((r, c + 1) not in visited):
                stack.append((r, c+1))
                visited.add((r, c+1))
                count += plus
        return count

    # counter - счетчик ячеек == 1 и не касающихся границ,
    # visited - ячейки, которые мы уже посетили.
    visited = set()
    counter = 0

    """Проходимся по всем крайним и прилегающим к ним ячейкам.
    Добавляем их в visited, чтобы при подсчете островов, не посчитать эти ячейки.
    """
    for row in range(rows):
        if grid[row][0] == 1:
            dfs(row, 0)
        if grid[row][cols-1] == 1:
            dfs(row, cols-1)

    for col in range(cols):
        if grid[0][col] == 1:
            dfs(0, col)
        if grid[rows-1][col] == 1:
            dfs(rows-1, col)

    """Проходимся по оставшейся матрице"""
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if (row, col) not in visited: # если мы еще не посещали эту ячейку
                visited.add((row, col))
                if grid[row][col] == 1:
                    counter += dfs(row, col, 1)
    return counter
