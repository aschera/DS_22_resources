# Exercise 3: calculator step 3
# Now build further functions to perform other calculations. 
# Create functions to subtract, multiply and divide two numbers.
# When these work, then let the user choose which calculation should be 
# performed.

def main():
    print("Calculator")
    num1 = get_input()
    num2 = get_input()
    operation = get_operation()
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    print("The result of", num1, operation, num2,  "is:", result)

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

def get_operation():
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:

            print("Invalid operation, please enter a valid operation (+, -, *, /).")

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
