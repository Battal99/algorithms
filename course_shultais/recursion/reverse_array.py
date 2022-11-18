def list_reverse(seq):
    """Итеративная функция для разворота массива"""
    for i in range(len(seq) // 2):
        el = seq[i]
        seq[i] = seq[len(seq) - 1 - i]
        seq[len(seq) - 1 - i] = el


def rec_list_reverse(seq, i=0):
    """Рекурсивная функция для разворота массива"""
    el = seq[i]
    seq[i] = seq[len(seq) - 1 - i]
    seq[len(seq) - 1 - i] = el

    if i < (len(seq) - 1) // 2:
        rec_list_reverse(seq, i+1)
    else:
        return


langs = ["python", "js", "html", "sql"]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

reverse = rec_list_reverse

reverse(langs)
print(langs)

reverse(digits)
print(digits)
