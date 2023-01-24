# The challenge: Tic Tac Toe / Tramp Chess
# A small note about games as exercises: I like to use games as exercises and challenges in my programming courses, not because they are the most useful,
#  but because they are very clearly defined problems to solve. 
# It is clear what is the end and it is quite easy to plan the increments there.
# Take this game and the steps can be.
# Print the game plan.
# Take input from the user.
# Change the game plan with user input.
# Validate the input so nothing can be overwritten.
# Check if someone has won. 5.1 check per row 5.2 check per column 5.3 check diagonally
# This is a challenge that is a bit more advanced. It will require some work with lists, strings and loops.
# A few tips to get you started. Solve the task step by step. Some functions that might be good to create are: print_board() - prints the board get_input() - 
# takes input from the user validate_input() - validates input from the user, remember that it must both be a valid input and that 
# it must an empty box update_board() - updates the board with the user's input check_winner() - checks if someone has won
# It is easiest to start by creating a function that can print the game board. How you solve this is up to you, but I can recommend a list of lists.
# My suggestion for characters to represent empty squares is # and for players 1 and 2 it is X and O respectively.
# If you manage to solve the task very easily, you can try expanding it into a game against the computer. Then you can use the random module to randomly 
# choose which box the computer should choose.
# If you want to make it even bigger, you can then build on to a four in a row game instead. Then there are more winning combinations and more rules.

# ------------------------------------------------------------------#
# My steps:
# 1 Create a function that prints the game board, using a list of lists to represent the squares. 
# Use "#" to represent empty squares, "X" for player 1, and "O" for player 2.
# 2 Create a function that takes input from the user, and validates that the input is a valid move 
# (e.g. the square is empty and within the boundaries of the board).
# Create a function that updates the board with the user's input, by replacing the "#" character with the player's symbol ("X" or "O").
# Create a function that checks if someone has won, by checking for winning combinations of symbols in rows, columns, and diagonals.
# Create a main loop that repeatedly calls the input, validation, update, and win-check functions, until the game is over.
# If you want to make it more advanced, you can try adding a feature to play against the computer, using the random module to randomly choose the computer's moves.
# If you want to make it even bigger, you can try building a four-in-a-row game, with more winning combinations and more rules.

# ----------------------------------------------------------------------#

# cross-platform library that supports ANSI escape codes
# to color the board
from colorama import Fore, Style

board = [['#', '#', '#'],
         ['#', '#', '#'],
         ['#', '#', '#']]

n = 3
board = [['#' for _ in range(n)] for _ in range(n)]


def print_board(board):
    from colorama import Fore, Style
    print(Fore.YELLOW + " ---"*len(board))
    for i, row in enumerate(board):
        print(Fore.YELLOW + "| ", end="")
        for j, square in enumerate(row):
            if square == 'X':
                print(Fore.RED + square, end="")
            elif square == 'O':
                print(Fore.GREEN + square, end="")
            else:
                print(square, end="")
            print(" | ", end="")
        print("")
        print(Fore.YELLOW + " ---"*len(board))
    print(Style.RESET_ALL)


def get_input(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and col (e.g: 1 2): ").split())
            row -= 1
            col -= 1
            if row not in range(len(board)) or col not in range(len(board)) or board[row][col] != "#":
                print("Invalid input: row, col or cell already filled")
            else:
                return row, col
        except ValueError:
            print("Invalid input: enter two integers separated by a space")


def update_board(board, player, row, col):
    board[row][col] = "X" if player == 1 else "O"


def check_winner(board, symbol):
    # check rows
    for row in board:
        if row.count(symbol) == len(row):
            return True

    # check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False



player = 1

while True:
    print_board(board)
    row, col = get_input(board, player)
    update_board(board, player, row , col )
    symbol = "X" if player == 1 else "O"
    if check_winner(board, symbol):
        print_board(board)
        print(f'Player {player} wins!')
        break
    player = 1 if player == 2 else 2



print_board(board)
