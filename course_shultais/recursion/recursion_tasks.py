
number = 5


def digits_sum(digit):
    if digit == 0:
        return digit
    return digits_sum(digit//10) + digit % 10

# print(digits_sum(number))


def sum_num(digit):
    if digit == 0:
        return digit
    return sum_num(digit-1) + digit

# print(sum_num(number))


def count_2(digit):
    while digit > 0:
        num = digit % 2
        print(num)
        digit //= 2
# print(count_2(10))


def count_1(digit):
    """ Напишите рекурсивную функцию count_1,
     которая принимает целое число, а затем возвращает
    количество единиц в двоичном представлении этого числа."""
    if digit == 0:
        return digit
    return count_1(digit//2) + digit % 2


print(count_1(7145))
