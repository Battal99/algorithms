# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#
#     def __str__(self):
#         return str(self.value)
#
#
# class List:
#
#     def __init__(self):
#         self.head = Node()
#         self.tail = None
#
#     def append_l(self, value):
#         current = self.head
#
#         while current.next is not None:
#             current = current.next
#
#         current.next = Node(value)
#
#     def append(self, value):
#         if self.tail is None:
#             self.head.next = Node(value)
#             self.tail = self.head.next
#             return
#         cur = self.tail
#         cur.next = Node(value)
#         self.tail = cur.next
#
#     def __str__(self):
#         result = '['
#         cur = self.head.next
#         while cur is not None:
#             end = ', ' if cur.next else ""
#             result += str(cur) + end
#             cur = cur.next
#         return result+']'
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next_node = None
#
#     def __str__(self):
#         return str(self.value)
#
#
# class List:
#
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#             return
#
#         current = self.head
#         while current.next_node is not None:
#             current = current.next_node
#
#         current.next_node = Node(value)
#
#     def prepend(self, value):
#         new_element = Node(value)
#         new_element.next_node = self.head
#         self.head = new_element
#
#     def __str__(self):
#         current = self.head
#         values = "["
#
#         while current is not None:
#             end = ", " if current.next_node else ""
#             values += str(current) + end
#             current = current.next_node
#
#         return values + "]"


# --------
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next_node = None
#
#     def __str__(self):
#         return self.key, self.value


# class List:
#
#     def __init__(self):
#         self.head = None
#
#     def append(self, key, value):
#         if self.head is None:
#             self.head = Node(key, value)
#             return
#
#         current = self.head
#         while current.next_node is not None:
#             current = current.next_node
#
#         current.next_node = Node(key, value)
#
#     def find(self, key):
#         cur = self.head
#         while cur is not None:
#             if cur.key == key:
#                 return cur.value
#             cur = cur.next_node

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next_node = None
#
#     def __str__(self):
#         return str(self.value)
#
#
# class List:
#
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#             return
#
#         current = self.head
#         while current.next_node is not None:
#             current = current.next_node
#
#         current.next_node = Node(value)
#
#     def length(self):
#         cur = self.head
#         total = 0
#         while cur is not None:
#             total += 1
#             cur = cur.next_node
#         return total

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.top = Node(None)

    def append(self, value):
        """
        Добавление нового элемента в конец связного списка.
        """

        # Перебираем поочереди все элементы, чтобы найти последний
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый
        current.next_node = Node(value)

    def insert(self, value, after_value):
        """
        Вставка нового элемента в середину связного списка.
        После значения after_value
        """
        new_el = Node(value)
        cur = self.top.next_node
        while cur is not None:
            if cur.value == after_value:
                new_el.next_node = cur.next_node
                cur.next_node = new_el
                return
            cur = cur.next_node

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(5)
lst.append(7)
# print(lst.__str__())
"[1, 2, 3, 5, 7]"
lst.insert(11, 7)
lst.insert(-1, 1)
print(lst.__str__())
"[1, -1, 2, 3, 5, 7]"
