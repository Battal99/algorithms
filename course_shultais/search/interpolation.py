import sys

val = int(sys.argv[1])
values = list(map(int, sys.argv[2:]))


def interpolation_search(array, value):
    """
    Возвращает индекс значения value в массиве array.
    Возвращает -1 если элемент не найден.
    """
    min_index = 0
    max_index = len(array) - 1
    while min_index <= max_index:
        # TODO: Проверить равенство индексов, а также наличие элемента.
        if min_index == max_index:
            if array[max_index] == value:
                return min_index
            else:
                return -1
        # Поиск среднего элемента.
        middle_index = min_index + (max_index - min_index) * \
                       (value - array[min_index]) // (array[max_index] - array[min_index])

        if (middle_index < min_index) or (middle_index > max_index):
            return -1

        # Продолжаем поиск или возвращаем найденный индекс.
        if array[middle_index] < value:
            min_index = middle_index + 1
        elif array[middle_index] > value:
            max_index = middle_index - 1
        else:
            return middle_index

    # Если к этому шагу ничего не нашли, то возвращаем -1.
    return -1

print(interpolation_search(values, val))