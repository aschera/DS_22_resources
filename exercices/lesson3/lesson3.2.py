# Exercise 2: calculator step 2
# Create a function to validate user input. The function should take in 
# a string and return True if the string is an integer otherwise False. 
# Use the function to validate input from the user. If the input is invalid, 
# the user will receive an error message and must try again.

def main():
    print("Calculator")
    num1 = get_input()
    num2 = get_input()
    result = add(num1, num2)
    print("The result is:", result)

def get_input():
    while True:
        user_input = input("Enter a number: ")
        if validate_input(user_input):
            return int(user_input)
        else:
            print("Invalid input, please enter a number.")

def validate_input(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def add(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    main()