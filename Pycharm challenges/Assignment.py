def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 10)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def get_valid_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, row col (0-2): ").split())
            if 0 <= row < 3 and 0 <= col < 3:  # Check if input is within bounds
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Nope. Spot taken. Try again.")
            else:
                print("Out of bounds. Enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two numbers between 0 and 2.")


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for t in range(9):
        player = players[t % 2]
        row, col = get_valid_move(board,player)
        board[row][col] = player
        print_board(board)
        if check_winner(board, player):
            print(f"P {player} wins!")
            return
        if is_full(board):
            print("Draw!")
            return
    print("Draw!")


if __name__ == "__main__":
    tic_tac_toe()
