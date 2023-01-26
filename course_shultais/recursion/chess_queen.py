ROWS = COLS = QUEENS = 8

chess_board = [[False for col in range(COLS)] for row in range(ROWS)]

chess_board_attacks = [[0 for _ in range(COLS)] for _ in range(ROWS)]


def eight_queens(chess_board, queens, next_row=0):
    """
    Рассчитывает и выводит все возможные правильные комбинации размещения ферзей.
    chess_board - доска.
    queens - число размещенных ферзей.
    next_row - следующая строка.
    """

    # Проверяем верное ли текущее размещение.
    if not check_placement(chess_board):
        return

    # Смотрим, если все ферзи на столе, то выводим результата и выходим из рекурсии.
    if queens == QUEENS:
        show_board(chess_board)
        return

    # Перебираем строки и столбцы.
    # Пробуем разместить следующую фигуру.
    for row in range(ROWS)[next_row:]:
        for col in range(COLS):
            if not chess_board[row][col] and chess_board_attacks[row][col] == 0:
                chess_board[row][col] = True
                mark(chess_board_attacks, row, col, 1)

                eight_queens(chess_board, queens + 1, row + 1)

                chess_board[row][col] = False
                mark(chess_board_attacks, row, col, -1)


def check_placement(chess_board):
    """
    Возвращает True если данная расстановка возможна.
    """

    for row in range(ROWS):
        for col in range(COLS):
            if chess_board[row][col]:
                # Проверяем строки.
                for c in chess_board[row][col + 1:]:
                    if c:
                        return False

                # Проверяем столбцы.
                for r in chess_board[row + 1:]:
                    if r[col]:
                        return False

                #
                # Проверяем диагонали.
                #

                # Смотрим влево вниз.
                r, c = row, col
                while r < ROWS - 1 and c > 0:
                    r, c = r + 1, c - 1
                    if chess_board[r][c]:
                        return False

                # Идем вправо вниз.
                r, c = row, col
                while r < ROWS - 1 and c < COLS - 1:
                    r, c = r + 1, c + 1
                    if chess_board[r][c]:
                        return False
    return True


def mark(chess_board, row, col, inc):
    """
    Маркирует ячейки, которые находятся по контролем ферзя на позиции row, col.
    """

    # Перебираем строки.
    for i in range(ROWS):
        if i != row:
            chess_board[i][col] += inc

    # Перебираем столбцы.
    for j in range(COLS):
        if j != col:
            chess_board[row][j] += inc

    # Идем вверх и влево.
    i, j = row, col
    while i > 0 and j > 0:
        i, j = i - 1, j - 1
        chess_board[i][j] += inc

    # Идем вверх и вправо.
    i, j = row, col
    while i > 0 and j < COLS - 1:
        i, j = i - 1, j + 1
        chess_board[i][j] += inc

    # Идем вниз и влево.
    i, j = row, col
    while i < ROWS - 1 and j > 0:
        i, j = i + 1, j - 1
        chess_board[i][j] += inc

    # Идем вниз и вправо.
    i, j = row, col
    while i < ROWS - 1 and j < COLS - 1:
        i, j = i + 1, j + 1
        chess_board[i][j] += inc


def show_board(chess_board):
    """
    Выводит текущее расположение фигур на доске.
    """

    for row in chess_board:
        for col in row:
            print({False: ".", True: "Q"}[col], end=" ")
        print()
    print()


eight_queens(chess_board, 0)

