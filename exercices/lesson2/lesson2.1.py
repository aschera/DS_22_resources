# Exercise 1
# use variables of the different basic types. (int, float, str, bool).
# Do some arithmetic with them, mix a little and see what works, read what error messages you get when it doesn't work.
# for example add an int with a str and see what happens. for example add an int with a float and see what happens. 
# for example add a float with a str and see what happens. for example add a float with a bool and see what happens. etc.
# with other operations such as multiplication, subtraction and division.



# arithmetic with (int, float, str, bool)

# DO: pip install prettytable 

from prettytable import PrettyTable

#------------------------------INT-------------------------------------------------#
# Specify the Column Names while initializing the Table
myArithmeticTableInt = PrettyTable(["Basic Type 1", "Basic Type 2", "Arithmetic", "Result"])
 
# Add rows: +
myArithmeticTableInt.add_row(["Int", "Int", "Add", "Int"])
myArithmeticTableInt.add_row(["Int", "Float", "Add", "Float"])
myArithmeticTableInt.add_row(["Int", "Str", "Add", "TypeError"])
myArithmeticTableInt.add_row(["Str", "Int", "Add", "TypeError"])
myArithmeticTableInt.add_row(["Int", "Bool", "Add", "Int"])

# Add rows: -
myArithmeticTableInt.add_row(["Int", "Int", "Subtract", "Int"])
myArithmeticTableInt.add_row(["Int", "Float", "Subtract", "Float"])
myArithmeticTableInt.add_row(["Int", "Str", "Subtract", "TypeError"])
myArithmeticTableInt.add_row(["Str", "Int", "Subtract", "TypeError"])
myArithmeticTableInt.add_row(["Int", "Bool", "Subtract", "Int"])

# Add rows: *
myArithmeticTableInt.add_row(["Int", "Int", "Multiply", "Int"])
myArithmeticTableInt.add_row(["Int", "Float", "Multiply", "Float"])
myArithmeticTableInt.add_row(["Int", "Str", "Multiply", "Str with the string printed twice"])
myArithmeticTableInt.add_row(["Str", "Int", "Multiply", "Str with the string printed twice"])
myArithmeticTableInt.add_row(["Int", "Bool", "Multiply", "Int"])

# Add rows: /
myArithmeticTableInt.add_row(["Int", "Int", "Divide", "Int"])
myArithmeticTableInt.add_row(["Int", "Float", "Divide", "Float"])
myArithmeticTableInt.add_row(["Int", "Str", "Divide", "TypeError"])
myArithmeticTableInt.add_row(["Str", "Int", "Divide", "TypeError"])
myArithmeticTableInt.add_row(["Int", "Bool", "Divide", "ZeroDivisionError"])
myArithmeticTableInt.add_row(["Bool", "Int", "Divide", "Float"]) # Interesting!

#-------------------------------------------------------------------------------#

print(myArithmeticTableInt)