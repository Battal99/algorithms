# Сортировка выбором O(n^2)
arr = [7,8,2,5,3,6]
arr1 = [1,2,3,4,55,6]
print(arr)


def selection_sort(arr: list):
    for i in range(len(arr)-1):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        if i != min_ind:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]


print(selection_sort(arr))
print(arr)


