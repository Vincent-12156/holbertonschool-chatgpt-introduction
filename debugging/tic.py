#!/usr/bin/python3

import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    clear_screen()
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_draw(board):
    """Checks if the board is full with no winner."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input loop for valid row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid position. Use numbers between 0 and 2.")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            break  # Valid input

        # Place the move
        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
