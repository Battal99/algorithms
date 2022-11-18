""" Расширьте класс Queue дополнительными методами:

peek() — должен возвращать значение первого элемента в очереди без его удаления.
Если очередь пустая, то peek должен вернуть None.
count() — должен возвращать количество элементов в очереди.
clear() — должен очищать очередь.
Также добавьте в очередь контроль размера.
Если очередь полностью заполнена, то очередной вызов enqueue должен вернуть исключение OverflowError."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self, size):
        self.top = Node(None)
        self.first = None
        self.size = size
        self.length = 0

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        new_node = Node(value)

        # Вставялем элемент в начало.
        if self.length < self.size:
            # Связываем последний элемент в очереди с новым.
            if self.top.next_node:
                self.top.next_node.prev_node = new_node

            # Связываем новый элемент со следующим (последним) и с top.
            new_node.next_node = self.top.next_node
            new_node.prev_node = self.top

            # Связываем top с новым.
            self.top.next_node = new_node
            self.length += 1
            # Устанавливаем first, если это первая вставка.
            if not self.first:
                self.first = new_node
        else:
            raise OverflowError

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """

        # Если элемент есть, то получаем его значение.
        if self.first:
            value = self.first.value

            # Смещаем указатель.
            self.first = self.first.prev_node

            # Удаляем последний элемент.
            self.first.next_node = None
            self.length -= 1
            # Проверяем, не ссылается ли first на top.
            # Если ссылается, то сбрасываем first.
            if self.first.value is None:
                self.first = None

            return value

        return None

    def count(self):
        """
        Возвращает количество элементов в очереди.
        """
        return self.length

    def peek(self):
        """
        Возвращает значение первого элемента очереди без его извлечения.
        """
        return self.first.value if self.first else None

    def clear(self):
        """
        Очищает очередь.
        """
        # Добавьте ваш код тут.
        self.top.next_node = None
        self.first = None
        self.length = 0


queue = Queue(3)
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
# queue.enqueue(6)
# ...
# OverflowError
print(queue.dequeue())
# # 12
print(queue.count())
# 2
queue.clear()
print(queue.count())
# 0
print(queue.peek())
# None