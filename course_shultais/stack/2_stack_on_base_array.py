class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size
        self.right_top = size
        self.left_top = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Двойной стек на базе статического массива.
    """

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        if self.length > 0 and self.left_top:
            value = self.data[self.left_top - 1]
            self.length -= 1
            self.left_top -= 1
            return value
        else:
            return None

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        if self.length > 0:
            element = self.data[self.right_top]
            self.length -= 1
            self.right_top += 1
            return element
        else:
            return None

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        if self.length < self.size:
            self.data[self.left_top] = value
            self.length += 1
            self.left_top += 1
        else:
            raise OverflowError

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        if self.length < self.size:
            self.data[self.right_top - 1] = value
            self.length += 1
            self.right_top -= 1
        else:
            raise OverflowError

    def clear(self):
        """
        Очищает стек.
        """
        for i in range(self.length):
            self.data[i] = None
            self.length -= 1

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        Используем size, так как массив теперь заполняется с двух сторон.
        """
        return "[" + ", ".join(map(str, self.data[:self.size])) + "]"


# stack = Stack(6)
# # stack.push_left(7)
# # stack.push_left(6)
# stack.push_right(2)
# stack.push_right(1)
# # stack.push_left(11)
# stack.push_right(8)
# stack.push_right(2)
# stack.push_right(1)
# stack.push_right(2)
# stack.push_right(1)
# print(stack)
# print(stack.pop_left())
# # >>> 11
# print(stack.pop_left())
# # >>> 6
# print(stack.pop_left())
# # >>> 7
# print(stack.pop_left())
# # >>> None
# print(stack.pop_right())
# # >>> None
# print(stack.pop_right())
# # >>> None
