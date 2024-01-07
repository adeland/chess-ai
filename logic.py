def print_board(board):

    for row in board:
        print(" | ".join(row))
        print("-" * 5)

    return None

def check_win(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    if all(cell != "" for row in board for cell in row):
        return "Draw"

    return None

def player_move(board, player):

    while True:
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "":
            board[row][col] = player
            break
        else:
            print("Invalid move, try again.")

    return None

def minimax(board, depth, is_maximizing):

    winner = check_win(board)

    if winner == 'X':
        return -10
    elif winner == 'O':
        return 10
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score

    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)

        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
current_player = "X"

while True:
    print_board(board)
    if current_player == "X":
        player_move(board, current_player)
    else:
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = current_player

    winner = check_win(board)
    if winner:
        print_board(board)
        if winner == "Draw":
            print("Draw")
        else:
            print(f"Player {winner} is the victor.")
        break
    current_player = "O" if current_player == "X" else "X"



