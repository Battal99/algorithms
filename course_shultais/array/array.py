class Array:
    """
    Линейный ститический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполнненого массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        try:
            self.data[self.length] = value
            self.length += 1
        except IndexError:
            raise OverflowError

    def insert(self, index, value):
        """
        Добавление нового элемента со значением value на позицию index.
        """
        # [20, 40, 10, 30]
        self.append(value)
        i = self.length - 1
        while index < i:
            self.data[i], self.data[i-1] = self.data[i-1],  self.data[i]
            i -= 1

    # def remove(self, value):
    #     count = False
    #     for i in range(self.length - 1):
    #         if self.data[i] == value:
    #             count = True
    #             for j in range(i, self.length - 1):
    #                 self.data[j] = self.data[j+1]
    #         if count:
    #             break
    #     self.data[self.length - 1] = None
    #     self.length -= 1

    def remove(self, value):
        """
        Удаляет все элементы со значением value.
        """
        count = 0
        for i in range(self.length):  # Проходим циклом по списку
            if self.data[i] == value:  # Находим элемент, который совпадает с искомым
                self.data[i] = None
                count += 1

        for i in range(self.length - 1):
            if self.data[i] is None:
                for z in range(i, self.length):
                    if self.data[z] is None:
                        continue
                    else:
                        self.data[i], self.data[z] = self.data[z], self.data[i]
                        break
        while count > 0:
            self.length -= 1
            count -= 1

    def reverse(self):
        """
        Разворачивает массив.
        """
        start = 0
        end = self.length - 1

        while start < end:
            self.data[start], self.data[end] = self.data[end], self.data[start]
            start += 1
            end -= 1

    def min(self):
        """
        Минимальное значение в массиве.
        """
        min_result = float("inf")
        for digit in self.data:
            if digit:
                if digit < min_result:
                    min_result = digit

        return min_result

    def max(self):
        """
        Максимальное значение в массиве.
        """
        max_result = float("-inf")
        for digit in self.data:
            if digit:
                if digit > max_result:
                    max_result = digit
        return max_result

    def avg(self):
        """
        Среднее значение в массиве.
        """
        if self.length != 0:
            summ = 0
            for digit in self.data:
                if digit:
                    summ += digit
            return summ / self.length
        else:
            raise ZeroDivisionError

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


# array = Array(5)
# print(array.__str__())
# print(array.size)
# print(array.length)
# array.append(7)
# array.append(7)
# array.append(5)
# array.append(5)
# array.append(7)
# array.remove(7)
# print(array.__str__())