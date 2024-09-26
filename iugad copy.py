def printboard(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]            # Diagonals

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_tie(board):
    return all([spot != " " for spot in board])


def play_game():
    board = [" " for _ in range(9)]  # Initialize board with empty spaces
    current_player = "X"

    while True:
        printboard(board)
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Choose a position between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        # Validate move
        if board[move] == " ":
            board[move] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        # Check for a win or a tie
        if check_win(board, current_player):
            printboard(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            printboard(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Game loop control
while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break
else:
    exit()
