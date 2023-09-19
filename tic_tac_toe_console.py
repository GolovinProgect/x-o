def draw_board(board):
    for row in board:
        for col in row:
            print(col, end="|")
        print()


def player_win(board, player):
    # проверка по горизонтали
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            print(f"Победил игрок {player}!")
            return True


    # Проверка по вертикали
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != "-":
            print(f"Победил игрок {player}!")
            return True

    # Проверка по диагонали
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        print(f"Победил игрок {player}!")
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        print(f"Победил игрок {player}!")
        return True

    return False


def game_step(my_board, player):
    print(f"Ходит {player}!")
    x = int(input("Введите номер строки: ")) - 1
    y = int(input("Введите номер столбца: ")) - 1

    if player == player_1:
        sign = "X"
    else:
        sign = "O"

    curr = my_board[x][y]
    if curr == "-":
        my_board[x][y] = sign
        return
    else:
        print("Ячейка занята! Выберите другую ячейку.")
        game_step(my_board, player)



print("Добро пожаловать в tic-tac-toe my first console-version!")
print('-' * 56)

player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")
print('-' * 56)

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print(f"Начало игры!")
draw_board(board)

print('-' * 56)

curr_player = player_2
while not player_win(board, curr_player):

    if curr_player == player_1:
        curr_player = player_2
    else:
        curr_player = player_1

    game_step(board, curr_player)
    draw_board(board)

print(f"{curr_player} выиграл!")
quit()
