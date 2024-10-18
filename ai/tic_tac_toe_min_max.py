import math

player, opponent = "x", "o"


def movesLeft(board):

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return True

    return False


def evaluate(board):

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == player:
                return 10
            else:
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10
            else:
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        else:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        else:
            return -10

    return 0


def minmax(board, depth, isMax):

    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    if not movesLeft(board):
        return 0

    if isMax:

        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = player
                    best = max(best, minmax(board, depth + 1, not isMax))
                    board[i][j] = "_"
        return best

    else:

        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = opponent
                    best = min(best, minmax(board, depth + 1, not isMax))
                    board[i][j] = "_"
        return best


def findBestMove(board):
    bestVal = -math.inf
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = player
                moveVal = minmax(board, 0, False)
                board[i][j] = "_"
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove


board = [["x", "o", "x"], ["o", "x", "x"], ["_", "o", "_"]]
print("Current Board:")
for row in board:
    print(row)

bestMove = findBestMove(board)
board[bestMove[0]][bestMove[1]] = player
print("\nBoard after the best move:")
for row in board:
    print(row)
