# Exercise 4: calculator step 4
# See if you can now write an option that makes it possible to use the 
# result from the previous calculation as input to the next calculation. 
# This should work as long as the user wants and with any calculation.
# The goal here is therefore to make the functions as general as possible 
# so that they can be reused.


def main():
    print("Calculator")
    result = 0
    while True:
        num1 = get_number("Enter a number (or press Enter to use the previous result): ", result)
        operation = get_operation()
        if operation == '=':
            break
        num2 = get_number("Enter another number: ", result)
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        print("The result of", num1, operation, num2,  "is:", result)
        if not continue_calculations():
            break

def get_number(prompt, previous_result):
    while True:
        user_input = input(prompt)
        if user_input == '':
            return previous_result
        elif validate_input(user_input):
            return int(user_input)
        else:
            print("Invalid input, please enter a number.")

def validate_input(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def get_operation():
    while True:
        operation = input("Enter an operation (+, -, *, /, = to quit): ")
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print("Invalid operation, please enter a valid operation (+, -, *, /, = to quit).")

def continue_calculations():
    while True:
        user_input = input("Do you want to continue? (y/n): ")
        if user_input.lower() == 'y':
            return True
        elif user_input.lower() == 'n':
            return False
        else:
            print("Invalid input, please enter 'y' for yes or 'n' for no.")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if __name__ == "__main__":
    main()

