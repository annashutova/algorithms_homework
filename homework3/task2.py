"""Сложность o(m*n)"""

def closedIsland(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    """Функция обходит нулевые острова и заменяет их на 1, чтобы не произошло повторного обхода."""
    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
            grid[r][c] = 1 # замена 0 на 1
            dfs(r+1, c) # проверка клетки снизу
            dfs(r, c+1) # проверка клетки справа
            dfs(r-1, c) # проверка клетки сверху
            dfs(r, c-1) # проверка клетки слева

    """Проходимся по всем крайним и прилегающим к ним ячейкам.
    Они не будут являться островами, так как не окружены 1.
    """
    for row in range(rows):
        if grid[row][0] == 0:
            dfs(row, 0)
        if grid[row][cols-1] == 0:
            dfs(row, cols-1)

    for col in range(cols):
        if grid[0][col] == 0:
            dfs(0, col)
        if grid[rows-1][col] == 0:
            dfs(rows-1, col)
    
    count = 0
    """Проходимся по оставшейся матрице"""
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid[row][col] == 0:
                dfs(row, col)
                count += 1 # после полного обхода одного острова увеличиваем счетчик на 1
    return count
