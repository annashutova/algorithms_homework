"""Сложность O(n)"""
# class TreeNode:
#      def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def trimBST(root, low: int, high: int):
    """Рекурсивно производим поиск в глубину, проверяя принадлежность узла к диапазону."""
    def trim(node):
        if not node: # если узла нет - возвращаем None
            return None
        if node.val < low: # если значение узла меньше нижней границы, все значения по левой ветви отсекаем и проходимся далее тольлко по правой
            return trim(node.right)
        elif node.val > high: # если значение узла больше верхней границы, все значения по правой ветви отсекаем и проходимся далее тольлко по девой
            return trim(node.left)
        else:
            # если же узел находится в диапазоне, идем по обеим ветвям
            node.left = trim(node.left)
            node.right = trim(node.right)
        return node
    return trim(root)
