"""Сложность O(n)"""
from typing import List

def averageOfLevels(root) -> List[float]:
        if root == None: # если корень = None, сразу возвращаем None
            return None
        """В queue хранятся вершины, по которым мы пойдем в первую очередь.
        В temp хранятся дочерние узлы вершины, на которой мы находимся.
        В summary добавляется значение текущей вершины.
        Count считает кол-во вершин на одном уровне.
        В res добавляется конечный результат уровня.
        """
        queue = [root]
        temp = []
        summary = 0
        count = 0
        res = []
        while queue: # пока в очереди есть вершины, мы проходимся по ним
            cur_node = queue.pop() # берем последний узел
            summary += cur_node.val # добавляем ее значение
            count += 1
            # если у узла есть дочерние узлы, добавляем их во временную очередь 
            if cur_node.left:
                temp.insert(0, cur_node.left)
            if cur_node.right:
                temp.insert(0, cur_node.right)
            if not queue: # когда узлы в queue заканчиваются, 
                res.append(summary / count) # добавляем их среденее арифм. в res
                queue, temp = temp, [] # обновляем queue в соответствии с temp, а temp обнуляем 
                summary, count = 0, 0 # обнуляем sum и count для того, чтобы перейти на следующий уровень
        return res
