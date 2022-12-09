"""Сложность O(n)"""

def getDecimalValue(head) -> int:
        res = 0 # объявляем переменную результата
        while head: # пока в списке есть элементы
            res = res * 2 + head.val # умножаем текущее значение на 2 и добавляем к ниму значение узла
            head = head.next # берем следующий элемент списка
        return res