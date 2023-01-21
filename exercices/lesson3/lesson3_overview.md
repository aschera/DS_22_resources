#Exercises lesson 3#
All exercises except the challenge are connected.

# Exercise 1: calculator step 1
create a main function. Make a print that just says, for example, "Calculator" or "calculator". Then call the function when the program is running.

To practice functions, printing to the terminal (other than the input printing) must not take place anywhere else than in the main() function.

Create a function that can add two numbers together and return the result. Print the result in the main function.

When this works, continue to take input from the user to add two numbers together. However, input from the user must be retrieved in another function.

Exercise 2: calculator step 2
Create a function to validate user input. The function should take in a string and return True if the string is an integer otherwise False. Use the function to validate input from the user. If the input is invalid, the user will receive an error message and must try again.

Exercise 3: calculator step 3
Now build further functions to perform other calculations. Create functions to subtract, multiply and divide two numbers.

When these work, then let the user choose which calculation should be performed.

Exercise 4: calculator step 4
See if you can now write an option that makes it possible to use the result from the previous calculation as input to the next calculation. This should work as long as the user wants and with any calculation.

The goal here is therefore to make the functions as general as possible so that they can be reused.

The challenge: Tic Tac Toe / Tramp Chess
A small note about games as exercises: I like to use games as exercises and challenges in my programming courses, not because they are the most useful, but because they are very clearly defined problems to solve. It is clear what is the end and it is quite easy to plan the increments there.

Take this game and the steps can be.

Print the game plan.
Take input from the user.
Change the game plan with user input.
Validate the input so nothing can be overwritten.
Check if someone has won. 5.1 check per row 5.2 check per column 5.3 check diagonally
!!! See tic_tac_toe_hint.py for more hints.

This is a challenge that is a bit more advanced. It will require some work with lists, strings and loops.

A few tips to get you started. Solve the task step by step. Some functions that might be good to create are: print_board() - prints the board get_input() - takes input from the user validate_input() - validates input from the user, remember that it must both be a valid input and that it must an empty box update_board() - updates the board with the user's input check_winner() - checks if someone has won

It is easiest to start by creating a function that can print the game board. How you solve this is up to you, but I can recommend a list of lists.

My suggestion for characters to represent empty squares is # and for players 1 and 2 it is X and O respectively.

If you manage to solve the task very easily, you can try expanding it into a game against the computer. Then you can use the random module to randomly choose which box the computer should choose.

If you want to make it even bigger, you can then build on to a four in a row game instead. Then there are more winning combinations and more rules.