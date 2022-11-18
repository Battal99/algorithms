"""
Создайте функцию direct для прямого обхода дерева с произвольным
 количеством потомков. Функция должна принимать корневой элемент дерева
 и возвращать значения узлов разделенные пробелом.
 Обратите внимание, что функция должна именно возвращать строку со значениями, а не выводить их.
Класс с узлом и функцию заглушку вы можете скачать ниже. Обратите внимание, что узел
 дерева может принимать как строки, так и числа.
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def direct(node, res=None):
    # Напишите ваш код здесь.
    if res is None:
        res = []
    res.append(str(node.value))
    for child in node.children:
        direct(child, res)
    return " ".join(res)
