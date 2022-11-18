# Учитывая целочисленный массив, содержащий дубликаты, вернуть элемент большинства, если он присутствует.
# Элемент большинства появляется больше, чем n/2 раз, где n это размер массива.

nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]


def findMajorityElementNaive(arr):
    d = {}

    for i in arr:
        d[i] = d.get(i, 0) + 1

    for i, j in d.items():
        if j > len(arr) // 2:
            return i


print(findMajorityElementNaive(nums))
