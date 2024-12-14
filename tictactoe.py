PLAYER_ONE = "Player 1"
PLAYER_TWO = "Player 2"


def display_board(board):
    """Displays the board in a grid format."""
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[7]}|{board[8]}|{board[9]}")


def player_input():
    """Handles player input for selecting a marker and returns markers for both players."""
    marker = ""
    while marker not in ["X", "O"]:
        marker = input(f"{PLAYER_ONE}, enter your marker (X or O): ").upper()
    player_one_marker = marker
    player_two_marker = "O" if marker == "X" else "X"
    return player_one_marker, player_two_marker


def is_winner(board, marker):
    """Checks if the given marker is a winner on the board."""
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
        [1, 5, 9], [3, 5, 7]  # Diagonal
    ]
    return any(all(board[pos] == marker for pos in condition) for condition in win_conditions)


def get_player_position(player_name):
    """Prompts the player for a board position and returns the valid position."""
    while True:
        try:
            position = int(input(f"{player_name}, choose a position (1-9): "))
            if 1 <= position <= 9:
                return position
            else:
                print("Invalid input. Position must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def place_marker(board, player_one_marker, player_two_marker):
    """Alternates turns for each player to place their markers on the board."""
    for turn in range(1, 10):
        current_player = PLAYER_ONE if turn % 2 != 0 else PLAYER_TWO
        current_marker = player_one_marker if current_player == PLAYER_ONE else player_two_marker
        position = get_player_position(current_player)

        # Place marker and display board
        if board[position] == " ":
            board[position] = current_marker
            display_board(board)

            # Check for a winner
            if is_winner(board, current_marker):
                print(f"{current_player} wins!")
                return
        else:
            print("Position is already taken. Try again.")
            continue
    print("It's a tie!")


# Initialize game
test_board = [" "] * 10
display_board(test_board)
player_1_marker, player_2_marker = player_input()
place_marker(test_board, player_1_marker, player_2_marker)
