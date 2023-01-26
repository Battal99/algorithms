
def parentheses(arr:str):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == '[':
            new_arr.append(arr[i])
        if arr[i] == ']':
            if not new_arr:
                return False
            else:
                new_arr.pop()
    if not new_arr:
        return True
    else:
        return False

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False



print(parentheses('[][][]'))

class Queue:
    def __init__(self):
        self.people = []
    def add(self, person):
        self.people.insert(0, person)
    def remove(self):
        return self.people.pop()
    def __len__(self):
        return len(self.people)
    def __str__(self):
        return str(self.people)
    def __getitem__(self, key):
        return self.people[key]

a = Queue()

a.add('[')
a.add('[')
a.add(']')
a.add(']')

print(parentheses(a))

class Stack:
    """
    This is an implementation of a Stack.
    The "right" or "top" of this stack the end of the list.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def valid_parentheses(symbol_string):
    """
    This is a practice problem.
    It checks to see if parenthesis's are balanced
    :param symbol_string: String
    :return Bool:
    """

    stack = Stack()
    for char in symbol_string:
        if char == "(":
            stack.push("(")
        elif char == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()

    if not stack.is_empty():
        return False
    else:
        return True