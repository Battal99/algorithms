class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class Stack:
    """
    Стек на базе связного списка.
    """

    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Получаем верхний элемент
        top = self.top.next_node

        # Перестраиваем связи и возвращаем значение
        if top:
            self.top.next_node = top.next_node
            return top.value

    def push(self, value):
        """
        Извлекает элемент со значением value в стек.
        """
        # Добавляем элемент в начало связного списка
        new_node = Node(value)

        new_node.next_node = self.top.next_node
        self.top.next_node = new_node

    def clear(self):
        """
        Очищает стек.
        """
        self.top.next_node = None

    def peek(self):
        """
        Возвращает значение верхнего элемента без его извлечения из стека.
        """
        return None if not self.top.next_node else self.top.next_node.value

    def count(self):
        """
        Возвращает количество элементов в стеке.
        """
        total = 0
        cur = self.top.next_node
        while cur is not None:
            cur = cur.next_node
            total += 1
        return total


    def __str__(self):
        result = '['
        cur = self.top.next_node
        while cur is not None:
            end = ", " if cur.next_node else ""
            result += str(cur) + end
            cur = cur.next_node

        return result + "]"

# #
# stack = Stack()
# # stack.push(7)
# # stack.push(6)
# # stack.push(2)
# stack.push(8)
# print(stack.count())
#
# print(stack.peek())

