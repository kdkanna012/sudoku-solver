board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
    if not find_empty(board):
        return True
    else:
        i, j = find_empty(board)

    for num in range(1, 10):

        if valid(board, num, i, j):
            board[i][j] = num

            if solve(board):
                return True

            board[i][j] = 0

    return False


def valid(board, num, i, j):
    for x in range(len(board)):
        if board[i][x] == num and x != j:
            return False

    for x in range(len(board[0])):
        if board[x][j] == num and x != i:
            return False

    box_x = i // 3
    box_y = j // 3

    for x in range(box_x*3, box_x*3 + 3):
        for y in range(box_y*3, box_y*3 + 3):
            if board[x][y] == num and x != box_x and y != box_y:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, column

    return None


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            if j == 8:
                print(str(board[i][j]))
            else:
                print(board[i][j], end=" ")


print_board(board)
solve(board)
print('\n')
print_board(board)
