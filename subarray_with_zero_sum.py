#  Проверьте существует ли подмассив с суммой 0 или нет O(n)

nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]


def hasZeroSumSublist(arr) -> bool:
    """ Используем хеширование"""
    result = set()
    result.add(0)
    total = 0
    exist = False
    for i in arr:
        total += i

        if total in result:
            print(total, result)
            exist = True

        result.add(total)

    return exist


print(hasZeroSumSublist(nums))
