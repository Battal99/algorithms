# arr = [1,1,2,0,1,-2,2,1,0,0,1]

#
# def countingsort(arr, max_value):
#     counts = [0] * (max_value + 1)
#
#     for digit in arr:
#         counts[digit] += 1
#
#     index = 0
#     for i in range(max_value + 1):
#         for j in range(counts[i]):
#             arr[index] = i
#             index += 1

#
# print(countingsort(arr, 2))
# print(arr)


def countingsort(values):
    """
    Сортировка подсчетом.
    """

    # Вычисляем max_value.
    max_value = values[0]
    for value in values[1:]:
        if value > max_value:
            max_value = value
    min_value = values[0]
    for value in values[1:]:
        if value < min_value:
            min_value = value

    # Создаем массив-счетчик.
    counts_max = [0] * (max_value + 1)
    counts_min = [0] * (abs(min_value) + 1)

    # Считаем количество значений основного массива.
    for value in values:
        if value >= 0:
            counts_max[value] += 1
        else:
            counts_min[abs(value)] += 1

    index = 0
    for i in range(max_value + 1):
        for j in range(counts_max[i]):
            values[index] = i
            index += 1
            
    for i in range(abs(min_value) + 1):
        for j in range(counts_min[i]):
            values.insert(0, -i)
            values.pop()

#
# print(countingsort_v2(arr))
# print(arr)