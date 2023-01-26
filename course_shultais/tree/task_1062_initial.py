"""
Создайте функцию find, которая будет искать значение в дереве с произвольным количеством потомков.
Функция должна принимать корневой элемент дерева, а также ключ поиска.
По результату функция должна возвращать значение,связанное с этим ключом.
"""


class Node:

    def __init__(self, key, value):
        # Ключ.
        self.key = key
        # Значение.
        self.value = value
        # Потомки.
        self.children = []


def find(node: Node, key):
    result = None
    if node.key == key:
        return node.value
    if node.children:
        for n in node.children:
            result = find(n, key)
            if result:
                break
    if result:
        return result
    else:
        return


def find_result(node, key):
    """
    Поиск по дереву произвольного размера.
    """
    # Финальный результат, по умолчанию None.
    result = None

    # Если нашли, то сразу возвращаем значение.
    if node.key == key:
        return node.value

    # Перебираем всех детей.
    for child in node.children:
        # Если нашли, то прерываем рекурсивные вызовы и возвращаем значение.
        result = find(child, key)
        if result is not None:
            break

    return result


root = Node('a', "A")
element1 = Node('b', 'B')
element2 = Node('c', 'C')
element3 = Node('g', 'G')
root.children.append(element1)
root.children.append(element2)
element2.children.append(element3)
# print(root.children)

result = find(root, "g")
print(result)
# A


