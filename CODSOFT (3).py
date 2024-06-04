import math
import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the game is over
def game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    # Check if the board is full (tie)
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# Function to evaluate the score of the current board
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return 1
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return -1
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return 1
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return -1
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        return -1
    return 0

# Function to perform the AI's move using Minimax algorithm
def minimax(board, depth, is_maximizing):
    if game_over(board):
        return evaluate(board)
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI
def best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function for human player's move
def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] != " ":
                print("Cell already occupied. Try again.")
            else:
                board[row][col] = "O"
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        player_move(board)
        print_board(board)
        if game_over(board):
            break
        
        print("AI's turn...")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print_board(board)

    result = evaluate(board)
    if result == 1:
        print("You lose!")
    elif result == -1:
        print("You win!")
    else:
        print("It's a tie!")

# Start the game
play_game()
