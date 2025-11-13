import random

#азмер поля
SIZE = 4

def create_board():
    #создание случайного поля 4х4
    nums = list(range(1, SIZE * SIZE))
    nums.append(0)  # 0 — пустая клетка
    while True:
        random.shuffle(nums)
        board = [nums[i:i + SIZE] for i in range(0, SIZE * SIZE, SIZE)]
        if is_solvable(nums):
            return board

def is_solvable(nums):
    #проверка решаемости головоломки
    inv_count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] and nums[j] and nums[i] > nums[j]:
                inv_count += 1
    #нахождение строки с пустой клеткой
    zero_row = SIZE - (nums.index(0) // SIZE)
    #для поля 4x4:
    #если строка пустой клетки чётная — инверсий должно быть нечётное число
    #если нечётная — чётное
    return (zero_row % 2 == 0) == (inv_count % 2 == 1)

def print_board(board):
    #вывод игрового поля
    for row in board:
        for num in row:
            print(f"{num:2}" if num != 0 else "  ", end="  ")
        print()
    print()

def find_empty(board):
    #находит позицию пустой клетки (0)
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                return i, j

def move_tile(board, direction):
    #перемещение плитки
    x, y = find_empty(board)
    if direction == "down" and x < SIZE - 1:
        board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
    elif direction == "up" and x > 0:
        board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
    elif direction == "right" and y < SIZE - 1:
        board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
    elif direction == "left" and y > 0:
        board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]
    else:
        print("Невозможный ход")

def is_solved(board):
    #проверка упорядоченности поля
    nums = [board[i][j] for i in range(SIZE) for j in range(SIZE)]
    return nums == list(range(1, SIZE * SIZE)) + [0]

def main():
    board = create_board()
    print("Команды: up, down, left, right, exit\n")
    print_board(board)

    while True:
        move = input("Следующий ход: ").strip().lower()
        if move == "exit":
            print("Выход из игры")
            break
        if move in ["up", "down", "left", "right"]:
            move_tile(board, move)
            print_board(board)
            if is_solved(board):
                print("Вы собрали головоломку")
                break
        else:
            print("Неверная команда!")

if __name__ == "__main__":
    main()