"""Сложность O(n)"""

from typing import List

def binaryTreePaths(root) -> List[str]:
    if root == None: # если корень пустой сразу возвращаем None
        return None
    queue = [(root, str(root.val))] # определяем очередь и сразу в нее добавляет узел и путь до этого узла
    res = [] # список, в который добавляется результат
    while queue: # пока в очререди есть узлы
        cur_node, node_path = queue.pop() # делаем pop последнего узла из очереди
        if not cur_node.left and not cur_node.right: # если узел является листом
            res.append(node_path) # добавляем его путь в res
        
        else:
            if cur_node.left: # если есть левый узел, добавляем его и его путь в queue
                queue.append((cur_node.left, '{0}->{1}'.format(node_path, cur_node.left.val)))
            if cur_node.right: # если есть правый узел, добавляем его и его путь в queue
                queue.append((cur_node.right, '{0}->{1}'.format(node_path, cur_node.right.val)))
    return res
