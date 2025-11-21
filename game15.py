import random

size = 4 #размер поля

def new_board(): #создание поля
    nums = list(range(1, size * size)) 
    nums.append(0)
    while True:
        random.shuffle(nums)
        board = [nums[i:i + size] for i in range(0, size * size, size)]
        if if_solvable(nums):
            return board

def if_solvable(nums): #проверка на решаемость
    inv_count = 0
    for i in range(len(nums)):
        for d in range(i + 1, len(nums)):
            if nums[i] and nums[d] and nums[i] > nums[d]:
                inv_count += 1

    empty = size - (nums.index(0) // size)
    return (empty % 2 == 0) == (inv_count % 2 == 1)

def print_board(board): #вывод поля
    for row in board:
        for num in row:
            print(f"{num:2}" if num != 0 else "  ", end = "  ")
        print()
    print()

def empty_pos(board): #поиск координат пустой плитки
    for i in range(size):
        for d in range(size):
            if board[i][d] == 0:
                return i, d

def empty_move(board, direction): #передвижение пустой плитки
    x, y = empty_pos(board)

    if direction == "up" and x > 0:
        board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
    elif direction == "down" and x < size - 1:
        board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
    elif direction == "left" and y > 0:
        board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]
    elif direction == "right" and y < size - 1:
        board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
    else:
        print("Неверный ход")

def if_solved(board): #проверка упорядоченности поля
    nums = [board[i][d] for i in range(size) for d in range(size)]
    return nums == list(range(1, size * size)) + [0]

def main():
    board = new_board()
    print("Вы запустили игру 'Пятнашки'\n Команды для управления плиткой: up, down, left, right, exit\n")
    print_board(board)

    while True:
        move = input("Следующий ход: ").strip().lower()
        if move == "exit":
            print("Завершение игры")
            break

        if move in ["up", "down", "left", "right"]:
            empty_move(board, move)
            print_board(board)
            if if_solved(board):
                print("Вы решили головоломку")
                break
        else:
            print("Неверная команда")

if __name__ == "__main__":
    main()
