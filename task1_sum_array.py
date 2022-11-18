# Найти пару с заданной суммой в массиве
nums = [1, 4, 7, 4, 10]
target = 8


def find_sum(arr: list, target_sum: int) -> tuple:
    arr.sort()

    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] + arr[end] == target_sum:
            return arr[start], arr[end]
        elif arr[start] + arr[end] > target_sum:
            end -= 1
        else:
            start += 1


print(find_sum(nums, target))
