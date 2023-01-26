
num = 13456


def digital_root(number, result=0):
    if number < 10:
        if result + number < 10:
            return result + number
        return digital_root(number+result, result=0)

    result += number % 10
    number //= 10
    return digital_root(number, result)


def digital_root_2(number):
    """
    Рекурсивно вычисляем цифровой корень.
    """

    if number < 10:
        # База рекурсии - возвращаем число, если они меньше 10.
        return number

    # Шаг рекурсии - отсекаем по одной цифре с конца.
    # На данном этапе мы получаем только сумму цифр числа, она может быть и двузначной.
    root = digital_root(int(number / 10)) + number % 10

    # Если число не однозначное, то еще раз запускаем функцию.
    if root >= 10:
        root = digital_root(root)

    return root


print(digital_root(num))
print(digital_root_2(num))
