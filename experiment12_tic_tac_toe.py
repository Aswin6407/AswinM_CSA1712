def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")


def check_winner(board, player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def play_game():
    board = [" "] * 9
    player = "X"

    while True:
        print_board(board)
        try:
            position = int(input(
                f"Player {player}, choose a position (1-9): "
            )) - 1
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position. Try again.")
            continue

        board[position] = player

        if check_winner(board, player):
            print_board(board)
            print("Player", player, "wins!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


play_game()