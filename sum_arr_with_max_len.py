# Найдите подмассив максималньой длины, имеющий заданную сумму

nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8


def findMaxLenSublist(arr, s):
    d = {0: -1}
    total = 0
    lenght = 0
    end_index = -1

    for i in range(len(arr)):
        total += arr[i]

        if total not in d:
            d[total] = i
        if total - s in d and lenght < i - d[total - s]:
            lenght = i - d[total - s]
            end_index = i

    print((end_index - lenght + 1, end_index))


print(nums)
findMaxLenSublist(nums, target)
