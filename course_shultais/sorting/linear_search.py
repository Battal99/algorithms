def linear_search(arr, target):
    result_index = []
    for index, element in enumerate(arr):
        if element == target:
            result_index.append(index)

    return result_index if result_index else -1


idx = linear_search([1, 2 ,3 , 1,4], 1)
print(idx)