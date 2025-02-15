def print_board(board):
    """
    Prints the Tic-Tac-Toe board to the console.

    Each row is displayed with cells separated by " | ", and rows
    are separated by a horizontal divider line.

    Args:
        board (List of str): The current Tic-Tac-Toe board, a 3x3 grid
            where each cell contains " ", "X", or "O".
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 10)


def check_winner(board, player):
    """
    Checks if the specified player has won the game.

    Winning conditions include:
    - A complete row filled with the player's symbol.
    - A complete column filled with the player's symbol.
    - A diagonal filled with the player's symbol.

    Args:
        board (List of str): The current Tic-Tac-Toe board, a 3x3 grid
            where each cell contains " ", "X", or "O".
        player (str): The player's symbol ("X" or "O").

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    """
    Checks if the Tic-Tac-Toe board is full.

    The board is considered full if there are no empty cells remaining.

    Args:
        board (List of str): The current Tic-Tac-Toe board, a 3x3 grid
            where each cell contains " ", "X", or "O".

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)


def get_valid_move(board, player):
    """
    Prompts the player to input a valid move for the Tic-Tac-Toe game.

    Ensures the input is within bounds (0-2) for both row and column,
    and that the selected cell is empty. Re-prompts the player in case
    of invalid input.

    Args:
        board (List of str): The current Tic-Tac-Toe board, a 3x3 grid
           where each cell contains " ", "X", or "O".
        player (str): The player's symbol ("X" or "O").

    Returns:
        tuple: A tuple (row, col) representing the valid move coordinates.
    """
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
    """
    Plays a game of Tic-Tac-Toe between two players.

    The game alternates turns between Player "X" and Player "O",
    prompting players to input their moves. The game ends when one
    of the following conditions is met:
    - A player wins by filling a row, column, or diagonal with their symbol.
    - The board is full, no winner (a draw).

    The current state of the board is printed after every move.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for t in range(9):
        player = players[t % 2]
        row, col = get_valid_move(board, player)
        board[row][col] = player
        print_board(board)
        if check_winner(board, player):
            print(f"Player {player} wins!")
            return
        if is_full(board):
            print("Draw!")
            return
    print("Draw!")


if __name__ == "__main__":
    tic_tac_toe()
