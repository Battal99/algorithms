def merge(array1, array2):
    """
    Функция слияния двух отсортированных массивов в один.
    array1 и array2 - массивы представленные python-списками.
    """
    result = []
    index_ar1 = 0
    index_ar2 = 0
    while index_ar1 < len(array1) and index_ar2 < len(array2):
        if array1[index_ar1] < array2[index_ar2]:
            result.append(array1[index_ar1])
            index_ar1 += 1
        else:
            result.append(array2[index_ar2])
            index_ar2 += 1

    for i in range(index_ar1, len(array1)):
        result.append(array1[i])

    for i in range(index_ar2, len(array2)):
        result.append(array2[i])

    return result



# a = [5,5,5]
# b = [5,5]
# # 1,3,4,6,10,20
# print(merge([1, 3, 5], [2, 4, 6]))
#
# i, j = 0, 0
# res = []
# while i < len(array1) and j < len(array2):
#     if array1[i] < array2[j]:
#         res.append(array1[i])
#         i += 1
#     else:
#         res.append(array2[j])
#         j += 1
# res += array1[i:]
# res += array2[j:]
# # один из list1[i:] и list2[j:] будет уже пустой, поэтому добавится только нужный остаток
# return res