string = "abcde((abcd)(abcd"
# print(string[:string.find('(')])
string2 = "abcde((abc"
string3 = "abcde"


def clear_brackets(string: str):
    open_bracket: int = -1
    closed_bracket: int = -1
    for i in range(len(string)):
        if string[i] == '(':
            open_bracket = i
        elif string[i] == ')':
            closed_bracket = i
    if open_bracket and closed_bracket and closed_bracket < open_bracket:
        return clear_brackets(string[:open_bracket])
    elif closed_bracket < 0 and open_bracket >= 0:
        return clear_brackets(string[:open_bracket])
    return string


# print(clear_brackets("(abc"))


def clear_brackets_optimal(s):
    """
    Функция для удаления из строки незакрытых скобок вместе с их содержимым,
    если после них нет закрытых блоков.
    Решение с помощью rfind и рекурсии.
    """

    right = s.rfind("(")
    left = s.rfind(")")

    if right != -1 and right > left:
        s = clear_brackets(s[:right])
    return s


# Альтернативный вариант с помощью регулярных выражений (без рекурсии)
import re

bad_block_pattern = re.compile(r'((\([^)]*)$)')


def clear_brackets_re(s):
    """
    Функция для удаления из строки незакрытых скобок вместе с их содержимым,
    если после них нет закрытых блоков.
    """
    return re.sub(bad_block_pattern, '', s)
