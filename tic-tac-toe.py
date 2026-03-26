# Tic Tac Toe

# Create the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board():
    for row in board:
        print('|'.join(row))

# Function to check for a win
def check_win(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                game_over = True
            elif ' ' not in [cell for row in board for cell in row]:
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

# Start the game
play_game()