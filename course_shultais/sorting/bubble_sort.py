arr = [13, 7, 8, 2, 11, 5]

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# print(bubble_sort(arr))
# print(arr)

def bubblesort(array):
    """
    Алгоритм пузырьковой сортировки массива в прямом порядке.
    """

    # Модифицируйте алгоритм.
    is_sorted = False
    while not is_sorted:

        is_sorted = True
        n = 1

        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        n += 1
print(arr)
print(bubblesort(arr))
print(arr)
