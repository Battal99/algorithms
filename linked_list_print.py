class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, node):
        self.head = node

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def __repr__(self) -> str:
        s = ''
        tmp = self.head
        while tmp:
            s = s + str(tmp.data) +"-->"
            tmp = tmp.next

        return s



# l1 = LinkedList(Node(1))
# print(l1.head.data)
# l1.insert_at_beginning(Node(2))
# l1.insert_at_beginning(Node(3))
# # print(l1.head.next.next.data)
# l1