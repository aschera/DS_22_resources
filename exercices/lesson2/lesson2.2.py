# Exercise 2
# Play with strings. Create a string then try to extract part of that string into a new string. 
# For example, if you have a string called s = "Hello World" then you can extract 
# "Hello" by typing s[:5] and "World" by typing s[6:].
# Play around with a few different strings and see what happens.

# ------------------------------------Using brackets-----------------------------------#
print("# ------------------------------------Using brackets-----------------------------------#")
myString = "Mississippi"
print(myString[:]) # Line 1
print(myString[4 : ]) # Line 2
print(myString[ : 8]) # Line 3
print(myString[2 : 7]) # Line 4
print(myString[4 : -1]) # Line 5
print(myString[-6 : -1]) # Line 6

print("# ------------------------------------Using slice-----------------------------------#")
# ------------------------------------Using slice-----------------------------------#
myString = "Mississippi"
slice1 = slice(3)
slice2 = slice(4)
slice3 = slice(0, 8)
slice4 = slice(2, 7)
slice5 = slice(4, -1)
slice6 = slice(-6, -1)
print(myString[slice1])
print(myString[slice2])
print(myString[slice3])
print(myString[slice4])
print(myString[slice5])
print(myString[slice6])

print("# ------------------------------------Using re.search-----------------------------------#")
# For regular expression, we’ll use Python’s in-built package re
# https://docs.python.org/3/library/re.html#module-re
import re

string = "123AAAMississippiZZZ123"
try:
    found = re.search('AAA(.+?)ZZZ', string).group(1)
    print(found)
except AttributeError:
    pass

print("# ------------------------------------Using re.findall-----------------------------------#")

subject = "123AAAMississippiZZZ123"
a = re.findall(r"[\d\-.]+AAA(.+?)ZZZ", subject) # d: Integer 
print (a)