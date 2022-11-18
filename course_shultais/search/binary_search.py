import sys

val = int(sys.argv[1])
values = list(map(int, sys.argv[2:]))


def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    x = None
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            x = mid
            start = mid + 1
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
    if x is not None:
        return x
    else:
        return -1



# print(binary_search([1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8], 2))
print(binary_search(values, val))
