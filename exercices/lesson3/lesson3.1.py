# Exercise 1: calculator step 1

# create a main function. Make a print that just says, for example, "Calculator" or "calculator". Then call the function when the program is running.
# To practice functions, printing to the terminal (other than the input printing) must not take place anywhere else than in the main() function.
# Create a function that can add two numbers together and return the result. Print the result in the main function.
# When this works, continue to take input from the user to add two numbers together. However, input from the user must be retrieved in another function.


def main():
    print("Calculator")
    num1 = get_input()
    num2 = get_input()
    result = add(num1, num2)
    print("The result is:", result)

def get_input():
    return int(input("Enter a number: "))

def add(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    main()