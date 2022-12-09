"""Сложность большая..., зато по памяти 99.91% на leetcode :)"""

# находим максимальную длину ветви
def max_depth(node):
        if not node:
            return 0
        stack = [(node, 1)] # вершины, по которым нужно пройтись
        max_depth = 0 # максимальная глубина из этой вершины
        while stack:
            cur_node, dist = stack.pop() # dist - длина до этой вершины
            if not cur_node.left and not cur_node.right: # если у вершины нет ветвей
                max_depth = max(max_depth, dist) # находим максимальную длину
            # каждую следующую вершины добавляем в стек и увеличиваем длину
            if cur_node.left:
                stack.append((cur_node.left, dist + 1))
            if cur_node.right:
                stack.append((cur_node.right, dist + 1))
        return max_depth

# ищет максимальный диаметер через каждую вершину
def diameterOfBinaryTree(root):
    if not root:
        return 0
    stack = [root] 
    max_diameter = 0
    while stack:
        node = stack.pop()
        # если у вершины есть ветви, добавляем их в стек, чтобы потом проверить их диаметры
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        # диаметер каждой вершины - макс длина левой ветви + макс длина правой ветви
        dist = max_depth(node.left) + max_depth(node.right)
        # после каждого прохода по вершине, проверяем не больше ли ее диаметер текущего максимума
        max_diameter = max(max_diameter, dist)
    return max_diameter
