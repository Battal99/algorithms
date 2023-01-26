import sys

data = sys.argv[1:]

matrix = [data[:3], data[3:6], data[6:]]


def winner(data):
    if data[0] == data[1] == data[2] == 'X':
        return 'X'
    elif data[0] == data[1] == data[2] == '0':
        return '0'
    return '-'


def tic_tac_toe(matrix):
    for row in matrix:
        win = winner(row)
        if win == 'X':
            return win
        elif win == '0':
            return win
    matrix_transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for row in matrix_transpose:
        win = winner(row)
        if win == 'X':
            return win
        elif win == '0':
            return win
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'X' or matrix[0][2] == matrix[1][1] == matrix[2][0] == 'X':
        return 'X'
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == '0' or matrix[0][2] == matrix[1][1] == matrix[2][0] == '0':
        return '0'

    return '-'


print(tic_tac_toe(matrix))
