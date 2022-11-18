""" Создайте очередь на базе двунаправленного связного списка.
Класс для управления очередью должен называться Queue и содержать два метода:
enqueue для добавления новых значений и dequeue для извлечения элемента.
dequeue должен вернуть значение элемента.
В случае если в очереди не осталось элементов, то dequeue должен вернуть None.
Считаем, что очередь на базе связного списка не ограничена по количеству элементов."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return str(self.value)


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = Node(None)
        self.first = self.top.next_node

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """

        new_node = Node(value)
        flag = True
        current = self.top
        while current.next_node:
            flag = False
            current = current.next_node
        current.next_node = new_node
        new_node.prev_node = current
        if flag:
            self.first = current.next_node

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        answer = self.top.next_node
        current = self.top
        if answer is None:
            return None
        if self.top.next_node.next_node:
            current.next_node = current.next_node.next_node
            current.next_node.prev_node = current
        else:
            self.top.next_node = None

        return answer.value


queue = Queue()
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(2)
print(queue.dequeue())
# 7
print(queue.dequeue())
# 6
print(queue.dequeue())
# 2
print(queue.dequeue())
# None
