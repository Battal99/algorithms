import math
nums = [6, -4, -3, 2, 3]

def partition(nums):
    total_sum = sum(nums)

    sum_so_far = 0

    for i in range(len(nums)):

        if sum_so_far == total_sum - sum_so_far:
            return i

        sum_so_far += nums[i]

i = partition(nums)

# print(nums[:i])
# print(nums[i:])

def reverse(x: int) -> int:
    invert = 0
    i = 0
    len_digit = find_len(x)
    if x > 0:
        while i < x:
            digit = x % 10
            invert += digit*(10**(len_digit-1))
            len_digit -= 1
            x = x // 10
    if x < 0:
        x = abs(x)
        while i < x:
            digit = x % 10
            invert += digit*(10**(len_digit-1))
            len_digit -= 1
            x = x // 10
        invert = int("-" + str(invert))
    return invert


def find_len(x):
    result = 0
    if x > 0:
        result = len(str(x))
    elif x < 0:
        result = len(str(x)) - 1
    return result


# print(reverse(-53213))


nums = [1, 5, 2, 1, 4, 5, 1]
nums2 = [1, 5, 2, 13, 4, 53, 133]

# def find_duplicates(nums):
#
#     s = set()
#     d = {x for x in nums if x in s or s.add(x)}
#     return d
#
# print(find_duplicates(nums2))

# имеем список слов:
words = ['ate', 'owl', 'tea', 'sing', 'eat', 'low']

# хотим получить его сгруппированным по анаграммам
# [['ate', 'tea', 'eat'], ['owl', 'low'], ['sing']]

def annogram(words: list):
    result = []
    ctn = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in ctn:
            ctn[sorted_word] = []
        ctn[sorted_word].append(word)

    for items in ctn.values():
        result.append(items)
    return result

print(annogram(words))