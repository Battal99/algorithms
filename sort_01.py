# Сортировка двоичного массива за линейное время
nums = [1, 1, 1, 0, 0, 1, 0, 1, 0]


def sort_01(arr: list):
    count_one = 0
    count_null = 0

    for i in arr:
        if i == 0:
            count_null += 1
        else:
            count_one += 1
    result = [0 for _ in range(count_null)] + [1 for _ in range(count_one)]
    return result


print(sort_01(nums))


def sort_01_2(arr: list):
    zeros = arr.count(0)

    k = 0
    while zeros:
        arr[k] = 0
        zeros -= 1
        k += 1

    for i in range(k, len(arr)):
        arr[i] = 1

    return arr


print(sort_01_2(nums))

print(nums)