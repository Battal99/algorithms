class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Стек на базе статического массива.
    """

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        if self.length > 0:
            element = self.data[self.length - 1]
            self.length -= 1
        else:
            return None

        return element

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        if self.length < self.size:
            self.data[self.length] = value
            self.length += 1
        else:
            raise OverflowError

    def clear(self):
        """
        Очищает стек.
        """
        for i in range(self.length):
            self.data[i] = None
            self.length -= 1

    def peek(self):
        """
        Возвращает значение верхнего элемента без его извлечения из стека.
        """
        value = self.data[self.length - 1]
        return value

    def count(self):
        """
        Возвращает количество элементов в стеке.
        """
        return self.length


# stack = Stack(3)
# stack.push(12)
# stack.push(7)
# stack.push(6)
# print(stack.peek())
# # 6
# print(stack.count())
# # 3
# stack.clear()
# print(stack.count())
# # 0
# print(stack.peek())
# # None